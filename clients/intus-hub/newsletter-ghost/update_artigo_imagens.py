#!/usr/bin/env python3
"""
Gera imagens via Freepik Mystic API e atualiza o draft existente no Ghost.
"""
import os, sys, json, requests, time
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

from dotenv import load_dotenv
load_dotenv()

GHOST_URL       = os.getenv("GHOST_URL")
GHOST_ADMIN_KEY = os.getenv("GHOST_ADMIN_KEY")
FREEPIK_API_KEY = os.getenv("FREEPIK_API_KEY")
DRAFT_ID        = "6a2d6575eeed600001bf3c6e"

TITULO    = "NOT YOUR CLAUDE, NOT YOUR WORKFLOW"
SUBTITULO = ("A mesma lição que cripto ensinou sobre custódia acaba de chegar "
             "para quem usa IA como ferramenta de trabalho. E o professor foi o governo americano.")


# ── GHOST ──────────────────────────────────────────────────────────────────

def ghost_token():
    import jwt
    key_id, secret = GHOST_ADMIN_KEY.split(":")
    iat = int(datetime.now(timezone.utc).timestamp())
    payload = {"iat": iat, "exp": iat + 300, "aud": "/admin/"}
    return jwt.encode(payload, bytes.fromhex(secret), algorithm="HS256", headers={"kid": key_id})


def upload_ghost_image(image_bytes: bytes, nome: str) -> str | None:
    try:
        token = ghost_token()
        headers = {"Authorization": f"Ghost {token}"}
        files = {"file": (f"{nome}.jpg", image_bytes, "image/jpeg"), "purpose": (None, "image")}
        r = requests.post(f"{GHOST_URL}/ghost/api/admin/images/upload",
                          headers=headers, files=files, timeout=30)
        r.raise_for_status()
        return r.json()["images"][0]["url"]
    except Exception as e:
        print(f"  ERRO upload Ghost: {e}")
        return None


def update_ghost_draft(draft_id: str, titulo: str, subtitulo: str, html: str):
    token = ghost_token()
    headers = {"Authorization": f"Ghost {token}", "Content-Type": "application/json"}

    r = requests.get(f"{GHOST_URL}/ghost/api/admin/posts/{draft_id}/",
                     headers={"Authorization": f"Ghost {token}"}, timeout=15)
    r.raise_for_status()
    updated_at = r.json()["posts"][0]["updated_at"]

    lexical = json.dumps({
        "root": {
            "children": [{"type": "html", "version": 1, "html": html}],
            "direction": None, "format": "", "indent": 0,
            "type": "root", "version": 1
        }
    })
    body = {"posts": [{
        "title": titulo,
        "custom_excerpt": subtitulo,
        "lexical": lexical,
        "status": "draft",
        "updated_at": updated_at
    }]}
    r = requests.put(f"{GHOST_URL}/ghost/api/admin/posts/{draft_id}/",
                     headers=headers, json=body, timeout=30)
    r.raise_for_status()
    return r.json()


# ── FREEPIK MYSTIC ─────────────────────────────────────────────────────────

def gerar_freepik_mystic(prompt: str, idx: int) -> bytes | None:
    headers = {
        "x-freepik-api-key": FREEPIK_API_KEY,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    body = {
        "prompt": prompt,
        "image": {"size": "landscape_16_9"},
        "styling": {"style": "photo"},
    }

    try:
        print(f"  [{idx}] Iniciando Freepik Mystic...")
        r = requests.post("https://api.freepik.com/v1/ai/mystic",
                          headers=headers, json=body, timeout=60)

        if r.status_code == 200 and r.headers.get("Content-Type", "").startswith("image/"):
            print(f"  [{idx}] Resposta síncrona recebida ({len(r.content):,} bytes)")
            return r.content

        r.raise_for_status()
        data = r.json()

        # Resposta assíncrona com task_id
        task_id = (data.get("data", {}).get("task_id")
                   or data.get("task_id")
                   or data.get("id"))

        if not task_id:
            # Pode ter retornado URL diretamente
            generated = (data.get("data", {}).get("generated")
                         or data.get("generated")
                         or [])
            if generated:
                img_url = generated[0].get("url") or generated[0]
                img_bytes = requests.get(img_url, timeout=30).content
                print(f"  [{idx}] OK — {len(img_bytes):,} bytes")
                return img_bytes
            print(f"  [{idx}] Resposta inesperada: {json.dumps(data)[:200]}")
            return None

        print(f"  [{idx}] Task ID: {task_id} — aguardando conclusão...")
        for tentativa in range(25):
            time.sleep(8)
            poll = requests.get(
                f"https://api.freepik.com/v1/ai/mystic/{task_id}",
                headers={"x-freepik-api-key": FREEPIK_API_KEY},
                timeout=30,
            )
            poll.raise_for_status()
            result = poll.json()
            status = (result.get("data", {}).get("status")
                      or result.get("status", "UNKNOWN"))
            print(f"  [{idx}] Status: {status} ({tentativa + 1}/25)")

            if status == "COMPLETED":
                generated = (result.get("data", {}).get("generated")
                             or result.get("generated", []))
                img_url = generated[0].get("url") or generated[0]
                img_bytes = requests.get(img_url, timeout=30).content
                print(f"  [{idx}] OK — {len(img_bytes):,} bytes")
                return img_bytes

            if status in ("FAILED", "ERROR", "CANCELLED"):
                print(f"  [{idx}] FALHOU (status={status})")
                return None

        print(f"  [{idx}] Timeout após 25 tentativas")
        return None

    except Exception as e:
        print(f"  [{idx}] ERRO Freepik: {e}")
        return None


# ── WORKER PARALELO ────────────────────────────────────────────────────────

def _worker(idx: int, topico: dict, data_hoje: str) -> tuple[int, str | None]:
    prompt = topico.get("prompt", "")
    time.sleep((idx - 1) * 3)  # stagger

    img_bytes = gerar_freepik_mystic(prompt, idx)
    if not img_bytes:
        return idx, None

    nome = f"intus-artigo-{data_hoje}-img{idx}"
    ghost_url = upload_ghost_image(img_bytes, nome)
    if ghost_url:
        print(f"  [{idx}] Upload Ghost OK: {ghost_url.split('/')[-1]}")
    return idx, ghost_url


# ── MAIN ───────────────────────────────────────────────────────────────────

def main():
    print(f"\n{'='*55}")
    print("  Intus — Atualizar Imagens do Artigo no Ghost")
    print(f"{'='*55}")
    print(f"  Draft ID : {DRAFT_ID}")
    print(f"  Imagens  : 4 (paralelo, Freepik Mystic)")
    print(f"{'='*55}\n")

    html     = Path("artigo_content.html").read_text(encoding="utf-8")
    topicos  = json.loads(Path("artigo_topicos.json").read_text(encoding="utf-8"))
    data_hoje = datetime.now().strftime("%Y%m%d")

    tarefas = [(i, t) for i, t in enumerate(topicos, 1)]
    resultados: dict[int, str | None] = {}

    print(f"Gerando {len(tarefas)} imagens em paralelo...\n")
    with ThreadPoolExecutor(max_workers=len(tarefas)) as ex:
        futures = {ex.submit(_worker, i, t, data_hoje): i for i, t in tarefas}
        for fut in as_completed(futures):
            i, url = fut.result()
            resultados[i] = url

    # Substituir placeholders
    img_tag = ('<div style="padding:20px 0;">'
               '<img src="{url}" alt="Imagem {i}" '
               'style="width:100%;max-width:680px;display:block;margin:0 auto;border-radius:6px;"/>'
               '</div>')

    for i in sorted(resultados):
        url = resultados[i]
        tag = img_tag.format(url=url, i=i) if url else ""
        html = html.replace(f"[IMAGEM_{i}]", tag)

    ok     = [i for i, u in resultados.items() if u]
    falhou = [i for i, u in resultados.items() if not u]
    print(f"\nImagens: {len(ok)}/{len(resultados)} OK" + (f"  ({len(falhou)} falhou)" if falhou else ""))

    print(f"\nAtualizando draft no Ghost (ID: {DRAFT_ID})...")
    result = update_ghost_draft(DRAFT_ID, TITULO, SUBTITULO, html)
    post   = result["posts"][0]

    print(f"\n{'='*55}")
    for i in sorted(resultados):
        status = "OK " if resultados[i] else "ERR"
        secao  = topicos[i-1].get("secao", f"imagem_{i}")[:45]
        print(f"  [{i:02d}] {status}  {secao}")
    print(f"{'─'*55}")
    print(f"  Draft ID : {post['id']}")
    print(f"  Revisar  : {GHOST_URL}/ghost/")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    main()
