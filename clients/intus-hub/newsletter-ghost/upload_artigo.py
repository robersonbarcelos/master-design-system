#!/usr/bin/env python3
"""Upload manual de imagens locais + post draft Ghost (artigo)."""
import sys, os, json, requests
from datetime import datetime, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from dotenv import load_dotenv
load_dotenv()

GHOST_URL       = os.getenv("GHOST_URL")
GHOST_ADMIN_KEY = os.getenv("GHOST_ADMIN_KEY")
TITULO          = "O Bitcoin subiu — mas a guerra não acabou"
SUBTITULO       = "O cessar-fogo entre EUA e Irã foi estendido indefinidamente, o BTC rompeu $77k, e o Estreito de Ormuz continua fechado. O mercado confundiu pausa com resolução."
IMG_INICIO      = 0   # img0 = screenshot Truth Social
N_IMAGENS       = 4   # img1 a img4 = imagens Freepik


def ghost_token():
    import jwt
    key_id, secret = GHOST_ADMIN_KEY.split(":")
    iat = int(datetime.now(timezone.utc).timestamp())
    payload = {"iat": iat, "exp": iat + 300, "aud": "/admin/"}
    return jwt.encode(payload, bytes.fromhex(secret), algorithm="HS256", headers={"kid": key_id})


def upload_image(path: Path, nome: str) -> str | None:
    token = ghost_token()
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    with open(path, "rb") as f:
        files = {"file": (f"{nome}.jpg", f, mime), "purpose": (None, "image")}
        r = requests.post(
            f"{GHOST_URL}/ghost/api/admin/images/upload/",
            headers={"Authorization": f"Ghost {token}"},
            files=files, timeout=30
        )
    if r.status_code == 201:
        return r.json()["images"][0]["url"]
    print(f"  ERRO upload {path.name}: {r.status_code} {r.text[:200]}")
    return None


def main():
    pasta = Path(__file__).parent
    html_path = pasta / "artigo_content.html"
    html = html_path.read_text(encoding="utf-8")

    # ── Upload das imagens (img0 a imgN) ─────────────────────────────────────
    total = N_IMAGENS + 1  # img0 + img1..img4
    print(f"Upload de {total} imagens (img{IMG_INICIO} a img{N_IMAGENS})...")

    img_tag = (
        '<div style="padding:20px 0;">'
        '<img src="{url}" alt="Imagem {i}" '
        'style="width:100%;max-width:680px;display:block;margin:0 auto;border-radius:6px;"/>'
        '</div>'
    )

    ok, falhou = 0, 0
    feature_url = None

    for i in range(IMG_INICIO, N_IMAGENS + 1):
        path = None
        for ext in [f"img{i}.png", f"img{i}.jpeg", f"img{i}.jpg", f"img{i}.jpg.jpeg", f"img{i}.jfif"]:
            p = pasta / ext
            if p.exists():
                path = p
                break
        if not path:
            print(f"  [{i}] ❌ arquivo não encontrado (img{i}.jpeg)")
            falhou += 1
            html = html.replace(f"[IMAGEM_{i}]", "")
            continue
        url = upload_image(path, f"intus-iran-artigo-img{i}")
        if url:
            html = html.replace(f"[IMAGEM_{i}]", img_tag.format(url=url, i=i))
            if i == 1:
                feature_url = url  # img1 = feature image do post
            print(f"  [{i}] ✅ {path.name}")
            ok += 1
        else:
            html = html.replace(f"[IMAGEM_{i}]", "")
            falhou += 1

    print(f"\n  {ok}/{total} imagens OK" + (f"  ({falhou} falhou)" if falhou else ""))

    # ── Salva HTML final ──────────────────────────────────────────────────────
    final_path = pasta / "artigo_iran_2026-04-22.final.html"
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
