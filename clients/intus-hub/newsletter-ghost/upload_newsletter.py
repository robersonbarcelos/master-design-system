#!/usr/bin/env python3
"""Upload manual de imagens locais + post draft Ghost (newsletter)."""
import sys, os, json, requests, subprocess
from datetime import datetime, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from dotenv import load_dotenv
load_dotenv()

GHOST_URL       = os.getenv("GHOST_URL")
GHOST_ADMIN_KEY = os.getenv("GHOST_ADMIN_KEY")
TITULO          = "Intus Cripto News - 20/04/2026"
SUBTITULO       = "Exploits, inflows recordes e o pivô dos mineradores para IA"
N_IMAGENS       = 12


def ghost_token():
    import jwt
    key_id, secret = GHOST_ADMIN_KEY.split(":")
    iat = int(datetime.now(timezone.utc).timestamp())
    payload = {"iat": iat, "exp": iat + 300, "aud": "/admin/"}
    return jwt.encode(payload, bytes.fromhex(secret), algorithm="HS256", headers={"kid": key_id})


def upload_image(path: Path, nome: str) -> str | None:
    token = ghost_token()
    with open(path, "rb") as f:
        files = {"file": (f"{nome}.jpg", f, "image/jpeg"), "purpose": (None, "image")}
        r = requests.post(
            f"{GHOST_URL}/ghost/api/admin/images/upload/",
            headers={"Authorization": f"Ghost {token}"},
            files=files, timeout=30
        )
    if r.status_code == 201:
        return r.json()["images"][0]["url"]
    print(f"  ERRO upload {path.name}: {r.status_code} {r.text[:200]}")
    return None


def buscar_mercado() -> dict:
    dados = {}
    try:
        r = requests.get(
            "https://api.coingecko.com/api/v3/simple/price"
            "?ids=bitcoin,ethereum&vs_currencies=usd"
            "&include_market_cap=true&include_24hr_change=true",
            timeout=10
        )
        d = r.json()
        btc = d.get("bitcoin", {})
        eth = d.get("ethereum", {})
        def fp(v): return f"${v:,.0f}".replace(",", ".")
        def fv(v):
            s = "▲" if v >= 0 else "▼"
            c = "#27ae60" if v >= 0 else "#e74c3c"
            return s, f"{abs(v):.2f}%", c
        dados["BTC_PRECO"] = fp(btc.get("usd", 0))
        s, p, c = fv(btc.get("usd_24h_change", 0))
        dados["BTC_SINAL"], dados["BTC_VAR"], dados["BTC_COR"] = s, p, c
        dados["ETH_PRECO"] = fp(eth.get("usd", 0))
        s, p, c = fv(eth.get("usd_24h_change", 0))
        dados["ETH_SINAL"], dados["ETH_VAR"], dados["ETH_COR"] = s, p, c
    except Exception as e:
        print(f"  AVISO BTC/ETH: {e}")
    try:
        r2 = requests.get("https://api.coingecko.com/api/v3/global", timeout=10)
        g = r2.json().get("data", {})
        mc = g.get("total_market_cap", {}).get("usd", 0)
        vol = g.get("total_volume", {}).get("usd", 0)
        dom = g.get("market_cap_percentage", {}).get("btc", 0)
        def fb(v): return f"${v/1e12:.2f}T" if v >= 1e12 else f"${v/1e9:.1f}B"
        dados["MARKET_CAP"] = fb(mc)
        dados["VOLUME_24H"] = fb(vol)
        dados["BTC_DOM"]    = f"{dom:.2f}%"
    except Exception as e:
        print(f"  AVISO Global: {e}")
    return dados


def buscar_fng() -> int | None:
    try:
        r = requests.get("https://api.alternative.me/fng/?limit=1", timeout=10)
        return int(r.json()["data"][0]["value"])
    except:
        return None


def gerar_gauge(valor: int, output: Path):
    script = Path(__file__).parent / "gerar_gauge.py"
    subprocess.run([sys.executable, str(script), "--valor", str(valor), "--output", str(output)],
                   check=True, capture_output=True)


def main():
    pasta = Path(__file__).parent
    html_path = pasta / "newsletter_content.html"
    html = html_path.read_text(encoding="utf-8")

    # ── Mercado ──────────────────────────────────────────────────────────────
    print("Buscando dados de mercado...")
    dados = buscar_mercado()
    for k, v in dados.items():
        html = html.replace(f"[{k}]", v)
    print(f"  BTC={dados.get('BTC_PRECO','?')}  ETH={dados.get('ETH_PRECO','?')}  "
          f"MCap={dados.get('MARKET_CAP','?')}  Dom={dados.get('BTC_DOM','?')}")

    # ── Gauge F&G ─────────────────────────────────────────────────────────────
    if "[GAUGE_URL]" in html:
        print("Buscando Fear & Greed...")
        fng = buscar_fng()
        if fng is not None:
            print(f"  F&G = {fng}")
            gauge_path = pasta / "fear_greed_gauge.png"
            gerar_gauge(fng, gauge_path)
            gauge_url = upload_image(gauge_path, f"fear-greed-{datetime.now().strftime('%Y%m%d')}")
            if gauge_url:
                html = html.replace("[GAUGE_URL]", gauge_url)
                print(f"  Gauge OK")
        else:
            print("  AVISO: F&G indisponível")

    # ── Upload das imagens ────────────────────────────────────────────────────
    print(f"\nUpload de {N_IMAGENS} imagens...")
    img_tag = (
        '<div style="padding:20px 0;">'
        '<img src="{url}" alt="Imagem {i}" '
        'style="width:100%;max-width:670px;display:block;margin:0 auto;border-radius:6px;"/>'
        '</div>'
    )
    ok, falhou = 0, 0
    feature_url = None
    for i in range(1, N_IMAGENS + 1):
        # aceita .jpeg, .jpg, .jpg.jpeg
        path = None
        for ext in [f"img{i}.jpeg", f"img{i}.jpg", f"img{i}.jpg.jpeg"]:
            p = pasta / ext
            if p.exists():
                path = p
                break
        if not path:
            print(f"  [{i:02d}] ❌ arquivo não encontrado (img{i}.jpeg)")
            falhou += 1
            html = html.replace(f"[IMAGEM_{i}]", "")
            continue
        url = upload_image(path, f"intus-20260420-img{i}")
        if url:
            html = html.replace(f"[IMAGEM_{i}]", img_tag.format(url=url, i=i))
            if i == 1:
                feature_url = url
            print(f"  [{i:02d}] ✅ {path.name}")
            ok += 1
        else:
            html = html.replace(f"[IMAGEM_{i}]", "")
            falhou += 1

    print(f"\n  {ok}/{N_IMAGENS} imagens OK" + (f"  ({falhou} falhou)" if falhou else ""))

    # ── Salva HTML final ──────────────────────────────────────────────────────
    final_path = pasta / "newsletter_2026-04-20.final.html"
    final_path.write_text(html, encoding="utf-8")
    print(f"  HTML final: {final_path.name}")

    # ── Post draft Ghost ──────────────────────────────────────────────────────
    print("\nPostando DRAFT no Ghost...")
    lexical = json.dumps({
        "root": {
            "children": [{"type": "html", "version": 1, "html": html}],
            "direction": None, "format": "", "indent": 0,
            "type": "root", "version": 1
        }
    })
    post_body = {"posts": [{
        "title": TITULO,
        "custom_excerpt": SUBTITULO,
        "lexical": lexical,
        "status": "draft",
        **({"feature_image": feature_url} if feature_url else {})
    }]}
    r = requests.post(
        f"{GHOST_URL}/ghost/api/admin/posts/",
        headers={"Authorization": f"Ghost {ghost_token()}", "Content-Type": "application/json"},
        json=post_body, timeout=30
    )
    posts = r.json().get("posts", [])
    if posts:
        post = posts[0]
        print(f"\n{'='*55}")
        print(f"  DRAFT criado com sucesso!")
        print(f"  ID   : {post['id']}")
        print(f"  Editar: {GHOST_URL}/ghost/#/editor/post/{post['id']}")
        print(f"{'='*55}")
    else:
        print(f"ERRO Ghost: {r.status_code}")
        print(r.text[:500])


if __name__ == "__main__":
    main()
