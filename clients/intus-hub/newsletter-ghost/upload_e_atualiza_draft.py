#!/usr/bin/env python3
"""Faz upload das imagens salvas localmente e atualiza o draft existente no Ghost."""
import os, sys, json, requests
from pathlib import Path
from datetime import datetime, timezone

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

from dotenv import load_dotenv
load_dotenv()

GHOST_URL       = os.getenv("GHOST_URL")
GHOST_ADMIN_KEY = os.getenv("GHOST_ADMIN_KEY")
DRAFT_ID        = "6a2d6575eeed600001bf3c6e"
TITULO          = "NOT YOUR CLAUDE, NOT YOUR WORKFLOW"
SUBTITULO       = ("A mesma lição que cripto ensinou sobre custódia acaba de chegar "
                   "para quem usa IA como ferramenta de trabalho. E o professor foi o governo americano.")


def ghost_token():
    import jwt
    key_id, secret = GHOST_ADMIN_KEY.split(":")
    iat = int(datetime.now(timezone.utc).timestamp())
    payload = {"iat": iat, "exp": iat + 300, "aud": "/admin/"}
    return jwt.encode(payload, bytes.fromhex(secret), algorithm="HS256", headers={"kid": key_id})


def upload_image(path: Path, nome: str) -> str | None:
    try:
        token = ghost_token()
        ext = path.suffix.lower().replace(".", "")
        mime = "image/jpeg" if ext in ("jpg", "jpeg") else f"image/{ext}"
        with open(path, "rb") as f:
            files = {"file": (f"{nome}.{ext}", f, mime), "purpose": (None, "image")}
            r = requests.post(f"{GHOST_URL}/ghost/api/admin/images/upload",
                              headers={"Authorization": f"Ghost {token}"},
                              files=files, timeout=30)
        r.raise_for_status()
        return r.json()["images"][0]["url"]
    except Exception as e:
        print(f"  ERRO upload {path.name}: {e}")
        return None


def update_draft(html: str, feature_image: str | None):
    token = ghost_token()
    headers = {"Authorization": f"Ghost {token}", "Content-Type": "application/json"}

    r = requests.get(f"{GHOST_URL}/ghost/api/admin/posts/{DRAFT_ID}/",
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
        "title": TITULO,
        "custom_excerpt": SUBTITULO,
        "lexical": lexical,
        "status": "draft",
        "updated_at": updated_at,
        **({"feature_image": feature_image} if feature_image else {}),
    }]}
    r = requests.put(f"{GHOST_URL}/ghost/api/admin/posts/{DRAFT_ID}/",
                     headers=headers, json=body, timeout=30)
    r.raise_for_status()
    return r.json()


def main():
    base = Path(__file__).parent
    html = (base / "artigo_content.html").read_text(encoding="utf-8")
    data = datetime.now().strftime("%Y%m%d")

    img_tag = ('<div style="padding:20px 0;">'
               '<img src="{url}" '
               'style="width:100%;max-width:680px;display:block;margin:0 auto;border-radius:6px;"/>'
               '</div>')

    print(f"\n{'='*55}")
    print("  Upload de imagens + atualização do draft Ghost")
    print(f"{'='*55}\n")

    resultados: dict[int, str | None] = {}
    feature_image = None

    for i in range(1, 6):
        placeholder = f"[IMAGEM_{i}]"
        if placeholder not in html:
            print(f"  [{i}] Placeholder não encontrado no HTML, pulando")
            continue

        # Aceita jpg, jpeg, png
        img_path = None
        for ext in ("jpg", "jpeg", "png"):
            p = base / f"img{i}.{ext}"
            if p.exists():
                img_path = p
                break
            p2 = base / f"img{i}.jpg.{ext}"
            if p2.exists():
                img_path = p2
                break

        if not img_path:
            print(f"  [{i}] ARQUIVO NÃO ENCONTRADO (img{i}.jpg) — placeholder removido")
            html = html.replace(placeholder, "")
            resultados[i] = None
            continue

        print(f"  [{i}] Enviando {img_path.name}...")
        url = upload_image(img_path, f"intus-artigo-{data}-img{i}")
        if url:
            html = html.replace(placeholder, img_tag.format(url=url))
            print(f"       OK: {url.split('/')[-1]}")
            resultados[i] = url
            if i == 1:
                feature_image = url
        else:
            html = html.replace(placeholder, "")
            resultados[i] = None

    print(f"\nAtualizando draft {DRAFT_ID}...")
    result   = update_draft(html, feature_image)
    post     = result["posts"][0]
    post_url = f"{GHOST_URL}/ghost/#/editor/post/{DRAFT_ID}/"

    ok     = [i for i, u in resultados.items() if u]
    falhou = [i for i, u in resultados.items() if not u]

    print(f"\n{'='*55}")
    print(f"  Imagens OK  : {ok}")
    if falhou:
        print(f"  Imagens ERR : {falhou}")
    print(f"  Draft ID    : {post['id']}")
    print(f"\n  Rascunho: {post_url}")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    main()
