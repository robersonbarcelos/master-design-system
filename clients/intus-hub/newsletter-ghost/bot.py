#!/usr/bin/env python3
"""
Intus Cripto Newsletter Bot
-----------------------------
Fluxo:
  1. Claude gera o HTML da newsletter e salva em newsletter_content.html
  2. Este script gera as imagens em PARALELO (Freepik Mystic API)
  3. Compõe logos reais sobre cada imagem via Pillow
  4. Faz upload das imagens direto no Ghost
  5. Substitui os placeholders [IMAGEM_N], [BTC_PRECO], [GAUGE_URL] etc.
  6. Posta tudo como DRAFT no Ghost

Uso mínimo (tudo automático):
  python bot.py --titulo "Intus Cripto News - 27/03/2026" --topicos topicos.json

Overrides opcionais:
  --fng 33          Força valor do F&G em vez de buscar da API
  --no-market       Desativa auto-fetch de mercado (CoinGecko)
"""

import os
import sys
import json
import argparse
import time
import warnings
import subprocess
import threading
import requests
import io
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed
from PIL import Image, ImageDraw

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

warnings.filterwarnings("ignore")

from dotenv import load_dotenv
load_dotenv()

GHOST_URL       = os.getenv("GHOST_URL")
GHOST_ADMIN_KEY = os.getenv("GHOST_ADMIN_KEY")
FREEPIK_API_KEY = os.getenv("FREEPIK_API_KEY")

import urllib.parse as _urlparse

# Lock para output thread-safe
_log_lock = threading.Lock()

def log(msg: str):
    with _log_lock:
        print(msg, flush=True)


# ─────────────────────────────────────────────────────────────────────────────
# GHOST — JWT + UPLOAD + DRAFT
# ─────────────────────────────────────────────────────────────────────────────

def ghost_token() -> str:
    import jwt
    key_id, secret = GHOST_ADMIN_KEY.split(":")
    iat = int(datetime.now(timezone.utc).timestamp())
    payload = {"iat": iat, "exp": iat + 300, "aud": "/admin/"}
    return jwt.encode(payload, bytes.fromhex(secret), algorithm="HS256", headers={"kid": key_id})


def upload_ghost_image(image_bytes: bytes, nome: str) -> str | None:
    """Faz upload da imagem direto no Ghost e retorna URL pública permanente."""
    try:
        token = ghost_token()
        headers = {"Authorization": f"Ghost {token}"}
        files = {"file": (f"{nome}.png", image_bytes, "image/png"), "purpose": (None, "image")}
        r = requests.post(
            f"{GHOST_URL}/ghost/api/admin/images/upload",
            headers=headers, files=files, timeout=30
        )
        r.raise_for_status()
        return r.json()["images"][0]["url"]
    except Exception as e:
        log(f"  ERRO upload Ghost: {e}")
        return None


def postar_ghost_draft(titulo: str, subtitulo: str, html: str, feature_image: str | None = None) -> dict:
    """Cria post como DRAFT no Ghost usando HTML card."""
    lexical = json.dumps({
        "root": {
            "children": [{"type": "html", "version": 1, "html": html}],
            "direction": None, "format": "", "indent": 0,
            "type": "root", "version": 1
        }
    })
    headers = {
        "Authorization": f"Ghost {ghost_token()}",
        "Content-Type": "application/json",
    }
    post_data = {
        "title": titulo,
        "custom_excerpt": subtitulo,
        "lexical": lexical,
        "status": "draft",
    }
    if feature_image:
        post_data["feature_image"] = feature_image
    body = {"posts": [post_data]}
    r = requests.post(f"{GHOST_URL}/ghost/api/admin/posts/", headers=headers, json=body, timeout=30)
    return r.json()


# ─────────────────────────────────────────────────────────────────────────────
# FEAR & GREED — auto-fetch + geração automática do gauge
# ─────────────────────────────────────────────────────────────────────────────

def buscar_fng() -> int | None:
    """Busca o valor atual do Fear & Greed Index via API pública (alternative.me)."""
    try:
        r = requests.get("https://api.alternative.me/fng/?limit=1", timeout=10)
        r.raise_for_status()
        valor = int(r.json()["data"][0]["value"])
        return valor
    except Exception as e:
        log(f"  AVISO F&G API: {e}")
        return None


def gerar_e_subir_gauge(valor_fng: int, html: str) -> str:
    """Gera o gauge, sobe pro Ghost e substitui [GAUGE_URL] no HTML."""
    if "[GAUGE_URL]" not in html:
        return html

    gauge_path = Path(__file__).parent / "fear_greed_gauge.png"
    script_path = Path(__file__).parent / "gerar_gauge.py"

    log(f"\nFear & Greed: gerando gauge (valor={valor_fng})...")
    try:
        subprocess.run(
            [sys.executable, str(script_path),
             "--valor", str(valor_fng),
             "--output", str(gauge_path)],
            check=True, capture_output=True
        )
        img_bytes = gauge_path.read_bytes()
        url = upload_ghost_image(img_bytes, f"fear-greed-{datetime.now().strftime('%Y%m%d')}")
        if url:
            html = html.replace("[GAUGE_URL]", url)
            log(f"  Gauge OK: {url}")
        else:
            log("  ERRO: upload do gauge falhou")
    except Exception as e:
        log(f"  ERRO gauge: {e}")

    return html


# ─────────────────────────────────────────────────────────────────────────────
# MARKET DATA — auto-fetch CoinGecko
# ─────────────────────────────────────────────────────────────────────────────

def buscar_dados_mercado() -> dict:
    """Busca dados de mercado ao vivo do CoinGecko. Retorna dict com os valores."""
    dados = {}
    try:
        r1 = requests.get(
            "https://api.coingecko.com/api/v3/simple/price"
            "?ids=bitcoin,ethereum&vs_currencies=usd"
            "&include_market_cap=true&include_24hr_change=true",
            timeout=10
        )
        r1.raise_for_status()
        d = r1.json()
        btc = d.get("bitcoin", {})
        eth = d.get("ethereum", {})

        def fmt_preco(v):
            return f"${v:,.0f}".replace(",", ".")

        def fmt_var(v):
            sinal = "▲" if v >= 0 else "▼"
            cor   = "#27ae60" if v >= 0 else "#e74c3c"
            return sinal, f"{abs(v):.2f}%", cor

        dados["BTC_PRECO"]    = fmt_preco(btc.get("usd", 0))
        btc_s, btc_p, btc_c  = fmt_var(btc.get("usd_24h_change", 0))
        dados["BTC_SINAL"]   = btc_s
        dados["BTC_VAR"]     = btc_p
        dados["BTC_COR"]     = btc_c

        dados["ETH_PRECO"]   = fmt_preco(eth.get("usd", 0))
        eth_s, eth_p, eth_c  = fmt_var(eth.get("usd_24h_change", 0))
        dados["ETH_SINAL"]   = eth_s
        dados["ETH_VAR"]     = eth_p
        dados["ETH_COR"]     = eth_c

    except Exception as e:
        log(f"  AVISO BTC/ETH: {e}")

    try:
        r2 = requests.get("https://api.coingecko.com/api/v3/global", timeout=10)
        r2.raise_for_status()
        g = r2.json().get("data", {})

        mc = g.get("total_market_cap", {}).get("usd", 0)
        vol = g.get("total_volume", {}).get("usd", 0)
        dom = g.get("market_cap_percentage", {}).get("btc", 0)

        def fmt_bilhoes(v):
            if v >= 1e12: return f"${v/1e12:.2f}T"
            return f"${v/1e9:.1f}B"

        dados["MARKET_CAP"] = fmt_bilhoes(mc)
        dados["VOLUME_24H"] = fmt_bilhoes(vol)
        dados["BTC_DOM"]    = f"{dom:.2f}%"

    except Exception as e:
        log(f"  AVISO Global: {e}")

    return dados


def aplicar_dados_mercado(html: str, dados: dict) -> str:
    """Substitui placeholders de mercado no HTML."""
    for chave, valor in dados.items():
        html = html.replace(f"[{chave}]", valor)
    return html


# ─────────────────────────────────────────────────────────────────────────────
# LOGOS — carregamento local + fallback online
# ─────────────────────────────────────────────────────────────────────────────

LOGO_DIR = Path(__file__).parent / "logos"

LOGO_MAP = {
    "robinhood.com":         "robinhood.png",
    "aave.com":              "aave.png",
    "circle.com":            "circle.png",
    "franklintempleton.com": "franklin_templeton.png",
    "ondo.finance":          "ondo.png",
    "chain.link":            "chainlink.png",
    "glassnode.com":         "glassnode.png",
}

def _baixar_logo(dominio: str, *args, **_) -> bytes | None:
    """Carrega logo do disco (logos/) ou fallback online."""
    nome_arquivo = LOGO_MAP.get(dominio)
    if nome_arquivo:
        caminho = LOGO_DIR / nome_arquivo
        if caminho.exists():
            return caminho.read_bytes()

    headers = {"User-Agent": "Mozilla/5.0"}
    for url in [
        f"https://icons.duckduckgo.com/ip3/{dominio}.ico",
        f"https://www.google.com/s2/favicons?domain={dominio}&sz=256",
    ]:
        try:
            r = requests.get(url, timeout=10, headers=headers)
            if r.status_code == 200 and len(r.content) > 500:
                img = Image.open(io.BytesIO(r.content))
                if img.width >= 32:
                    return r.content
        except Exception:
            continue
    return None


def adicionar_logos(img_bytes: bytes, topico: dict) -> bytes:
    """Compõe logos reais sobre a imagem com painel navy + borda gold (paleta Intus)."""
    dominios     = topico.get("logos", [])
    fonte        = topico.get("logo_source", "ddg")
    coingecko_id = topico.get("coingecko_id", "")

    if not dominios:
        return img_bytes

    try:
        base_img = Image.open(io.BytesIO(img_bytes)).convert("RGBA")
        base_w, base_h = base_img.size

        logos = []
        for dominio in dominios:
            raw = _baixar_logo(dominio, fonte, coingecko_id)
            if raw:
                logo = Image.open(io.BytesIO(raw)).convert("RGBA")
                logos.append((dominio, logo))
            else:
                log(f"    Logo falhou: {dominio}")

        if not logos:
            return img_bytes

        LOGO_H  = max(130, int(base_h * 0.15))
        PADDING = int(LOGO_H * 0.28)
        GAP     = int(LOGO_H * 0.18)
        RADIUS  = int(LOGO_H * 0.22)

        logos_r = []
        for dominio, logo in logos:
            ratio   = LOGO_H / logo.height
            lw      = max(1, int(logo.width * ratio))
            resized = logo.resize((lw, LOGO_H), Image.LANCZOS)

            # Fundo branco para logos com elementos escuros
            pixels    = list(resized.getdata())
            escuros   = sum(1 for p in pixels if len(p) == 4 and p[3] > 50 and sum(p[:3]) < 200)
            total_vis = sum(1 for p in pixels if len(p) == 4 and p[3] > 50)
            if total_vis > 0 and escuros / total_vis > 0.4:
                fundo = Image.new("RGBA", resized.size, (255, 255, 255, 255))
                fundo.paste(resized, mask=resized.split()[3])
                resized = fundo

            logos_r.append(resized)
            log(f"    Logo OK: {dominio} {logo.size}")

        total_w = sum(l.width for l in logos_r) + GAP * (len(logos_r) - 1)
        panel_w = total_w + PADDING * 2
        panel_h = LOGO_H + PADDING * 2

        panel = Image.new("RGBA", (panel_w, panel_h), (0, 0, 0, 0))
        draw  = ImageDraw.Draw(panel)
        draw.rounded_rectangle([(0, 0), (panel_w-1, panel_h-1)],
                               radius=RADIUS, fill=(10, 22, 40, 210))
        draw.rounded_rectangle([(1, 1), (panel_w-2, panel_h-2)],
                               radius=RADIUS, outline=(201, 160, 32, 180), width=2)

        x = PADDING
        for logo in logos_r:
            panel.paste(logo, (x, PADDING), logo)
            x += logo.width + GAP

        MARGIN = int(base_w * 0.02)
        base_img.paste(panel, (MARGIN, base_h - panel_h - MARGIN), panel)

        out = io.BytesIO()
        base_img.convert("RGB").save(out, format="PNG", optimize=True)
        return out.getvalue()

    except Exception as e:
        log(f"  AVISO compositing: {e}")
        return img_bytes


# ─────────────────────────────────────────────────────────────────────────────
# POLLINATIONS.AI — geração de imagem via FLUX (gratuito, sem API key)
# ─────────────────────────────────────────────────────────────────────────────

def gerar_imagem_freepik(prompt: str, idx: int) -> bytes | None:
    """Gera imagem via Pollinations.ai (FLUX). Gratuito, sem API key."""
    import random
    seed = random.randint(1, 99999)
    encoded = _urlparse.quote(prompt)
    url = (
        f"https://image.pollinations.ai/prompt/{encoded}"
        f"?width=1344&height=768&model=flux&nologo=true&seed={seed}"
    )
    try:
        log(f"  [{idx:02d}] Gerando via Pollinations.ai (FLUX)…")
        r = requests.get(url, timeout=90)
        r.raise_for_status()
        if len(r.content) < 5000:
            log(f"  [{idx:02d}] Resposta suspeita ({len(r.content)} bytes)")
            return None
        log(f"  [{idx:02d}] OK — {len(r.content):,} bytes")
        return r.content
    except Exception as e:
        log(f"  [{idx:02d}] ERRO Pollinations: {e}")
        return None


# ─────────────────────────────────────────────────────────────────────────────
# PROCESSAMENTO PARALELO DE IMAGENS
# ─────────────────────────────────────────────────────────────────────────────

def _worker(i: int, topico: dict, data_hoje: str) -> tuple[int, str | None]:
    """Worker por imagem: gera → logo → upload Ghost. Roda em thread separada."""
    descricao = topico.get("descricao", f"noticia_{i}")
    prompt    = topico.get("prompt", descricao)

    # Stagger leve entre threads (Pollinations não tem rate limit rígido)
    time.sleep((i - 1) * 2)

    img_bytes = gerar_imagem_freepik(prompt, i)

    # 1 retry automático em caso de falha (429, timeout, FAILED)
    if not img_bytes:
        log(f"  [{i:02d}] Retry em 60s...")
        time.sleep(60)
        img_bytes = gerar_imagem_freepik(prompt, i)

    if not img_bytes:
        return i, None

    if topico.get("logos"):
        log(f"  [{i:02d}] Compositing: {topico['logos']}")
        img_bytes = adicionar_logos(img_bytes, topico)

    img_url = upload_ghost_image(img_bytes, f"intus-{data_hoje}-img{i}")
    if img_url:
        log(f"  [{i:02d}] Upload OK → {img_url.split('/')[-1]}")
    return i, img_url


def processar_imagens_paralelo(html: str, topicos: list) -> tuple[str, dict]:
    """Gera TODAS as imagens em paralelo e substitui os placeholders.
    Retorna (html_final, {i: url_ou_None})."""
    data_hoje = datetime.now().strftime("%Y%m%d")

    # Apenas tópicos cujo placeholder existe no HTML
    tarefas = [
        (i, topico)
        for i, topico in enumerate(topicos, 1)
        if f"[IMAGEM_{i}]" in html
    ]

    total = len(tarefas)
    log(f"\nIniciando {total} imagens em paralelo…")
    t_inicio = time.time()

    resultados: dict[int, str | None] = {}
    concluidos = 0

    with ThreadPoolExecutor(max_workers=total) as ex:
        futures = {
            ex.submit(_worker, i, topico, data_hoje): i
            for i, topico in tarefas
        }
        for future in as_completed(futures):
            i, url = future.result()
            resultados[i] = url
            concluidos += 1
            log(f"  ✓ [{i:02d}] concluída ({concluidos}/{total})")

    elapsed = time.time() - t_inicio
    log(f"\nTodas as imagens prontas em {elapsed:.0f}s  "
        f"(sequencial seria ~{total * 20}s)")

    # Substituir placeholders
    img_tag_tpl = (
        '<div style="padding:20px 0;">'
        '<img src="{url}" alt="{alt}" '
        'style="width:100%;max-width:670px;display:block;margin:0 auto;border-radius:6px;"/>'
        '</div>'
    )
    for i in sorted(resultados):
        placeholder = f"[IMAGEM_{i}]"
        url = resultados[i]
        tag = img_tag_tpl.format(url=url, alt=f"Imagem {i}") if url else ""
        html = html.replace(placeholder, tag)

    return html, resultados


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def verificar_env():
    faltando = [v for v in ["GHOST_URL", "GHOST_ADMIN_KEY", "FREEPIK_API_KEY"] if not os.getenv(v)]
    if faltando:
        for v in faltando:
            print(f"ERRO: variavel nao definida no .env: {v}")
        sys.exit(1)


def preflight_check(html: str, topicos: list):
    """Valida que o nº de [IMAGEM_N] no HTML bate com o nº de tópicos."""
    placeholders = [f"[IMAGEM_{i}]" for i in range(1, len(topicos) + 1)]
    faltando  = [p for p in placeholders if p not in html]
    sobrando  = []
    n = len(topicos) + 1
    while f"[IMAGEM_{n}]" in html:
        sobrando.append(f"[IMAGEM_{n}]")
        n += 1

    erros = []
    if faltando:
        erros.append(f"  Placeholders ausentes no HTML : {', '.join(faltando)}")
    if sobrando:
        erros.append(f"  Placeholders sem tópico       : {', '.join(sobrando)}")

    if erros:
        print(f"\n{'='*55}")
        print("  PRÉ-FLIGHT FALHOU ⚠️")
        for e in erros:
            print(e)
        print(f"  HTML tem {n - 1 + len(faltando)} placeholders, topicos.json tem {len(topicos)} entradas.")
        print(f"{'='*55}")
        sys.exit(1)

    print(f"  Pré-flight OK — {len(topicos)} notícias / {len(topicos)} imagens ✓")


def main():
    parser = argparse.ArgumentParser(description="Intus Cripto Newsletter Bot")
    parser.add_argument("--html",        default="newsletter_content.html")
    parser.add_argument("--titulo",      required=True)
    parser.add_argument("--subtitulo",   default="Seu resumo semanal do mercado cripto!")
    parser.add_argument("--topicos",     required=True)
    parser.add_argument("--fng",       type=int, default=None,
                        help="Força valor do Fear & Greed (0-100). Padrão: auto-fetch da API.")
    parser.add_argument("--no-market", action="store_true",
                        help="Desativa auto-fetch de mercado (CoinGecko). Padrão: sempre ativo.")
    args = parser.parse_args()

    verificar_env()

    html_path = Path(args.html)
    if not html_path.exists():
        print(f"ERRO: HTML nao encontrado: {args.html}")
        sys.exit(1)
    html = html_path.read_text(encoding="utf-8")

    topicos_path = Path(args.topicos)
    if not topicos_path.exists():
        print(f"ERRO: topicos nao encontrado: {args.topicos}")
        sys.exit(1)
    topicos = json.loads(topicos_path.read_text(encoding="utf-8"))

    print(f"\n{'='*55}")
    print(f"  Intus Cripto Newsletter Bot  v2.1")
    print(f"{'='*55}")
    print(f"  Edição   : {args.titulo}")
    print(f"  Imagens  : {len(topicos)} (paralelo)")
    print(f"  F&G      : {'manual override: ' + str(args.fng) if args.fng else 'auto (alternative.me)'}")
    print(f"  Mercado  : {'DESATIVADO (--no-market)' if args.no_market else 'auto CoinGecko'}")
    print(f"{'='*55}")

    # ── Pré-flight: valida placeholders ──────────────────────────────────────
    preflight_check(html, topicos)

    # ── Gauge Fear & Greed (auto ou override manual) ──────────────────────────
    if "[GAUGE_URL]" in html:
        valor_fng = args.fng
        if valor_fng is None:
            log("\nFear & Greed: buscando valor atual (alternative.me)...")
            valor_fng = buscar_fng()
            if valor_fng is not None:
                log(f"  F&G atual: {valor_fng}")
            else:
                log("  AVISO: não foi possível buscar F&G, gauge será ignorado")
        if valor_fng is not None:
            html = gerar_e_subir_gauge(valor_fng, html)

    # ── Dados de mercado (sempre ativo, salvo --no-market) ────────────────────
    if not args.no_market:
        log("\nBuscando dados de mercado (CoinGecko)...")
        dados = buscar_dados_mercado()
        if dados:
            html = aplicar_dados_mercado(html, dados)
            log(f"  BTC={dados.get('BTC_PRECO','?')}  ETH={dados.get('ETH_PRECO','?')}  "
                f"MCap={dados.get('MARKET_CAP','?')}  Dom={dados.get('BTC_DOM','?')}")

    # ── Imagens em PARALELO ───────────────────────────────────────────────────
    print("\nPASSO 1 — Gerando imagens em paralelo (Freepik Mystic)...")
    html_final, resultados_imgs = processar_imagens_paralelo(html, topicos)

    # Versionamento: salva com data para arquivo histórico
    data_slug = datetime.now().strftime("%Y-%m-%d")
    html_final_path = Path(args.html).parent / f"newsletter_{data_slug}.final.html"
    html_final_path.write_text(html_final, encoding="utf-8")
    log(f"\nHTML final salvo: {html_final_path.name}")

    # ── Draft no Ghost ────────────────────────────────────────────────────────
    log("\nPASSO 2 — Postando DRAFT no Ghost...")
    primeira_img = resultados_imgs.get(1) or next((u for u in resultados_imgs.values() if u), None)
    resultado = postar_ghost_draft(args.titulo, args.subtitulo, html_final, feature_image=primeira_img)

    posts = resultado.get("posts", [])
    if posts:
        post = posts[0]

        # ── Sumário final ─────────────────────────────────────────────────────
        ok      = [(i, u) for i, u in sorted(resultados_imgs.items()) if u]
        falhou  = [(i, u) for i, u in sorted(resultados_imgs.items()) if not u]
        print(f"\n{'='*55}")
        print(f"  SUMÁRIO DA EXECUÇÃO")
        print(f"{'='*55}")
        for i, url in ok:
            desc = topicos[i-1].get("descricao", "")[:40]
            print(f"  [{i:02d}] ✅  {desc}")
        for i, _ in falhou:
            desc = topicos[i-1].get("descricao", "")[:40]
            print(f"  [{i:02d}] ❌  {desc}")
        print(f"{'─'*55}")
        print(f"  Imagens   : {len(ok)}/{len(resultados_imgs)} OK"
              + (f"  ({len(falhou)} falhou)" if falhou else ""))
        print(f"  Arquivo   : {html_final_path.name}")
        print(f"  Draft ID  : {post['id']}")
        print(f"{'='*55}")
        print(f"\n  Revisar em: {GHOST_URL}/ghost/")
    else:
        print(f"\nERRO ao criar draft no Ghost:")
        print(json.dumps(resultado, indent=2, ensure_ascii=False))
        sys.exit(1)


if __name__ == "__main__":
    main()
