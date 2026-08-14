import sys, json, requests, jwt
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image
import io

sys.stdout.reconfigure(encoding="utf-8")

env = {}
with open(".env") as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()

GHOST_URL       = env["GHOST_URL"]
GHOST_ADMIN_KEY = env["GHOST_ADMIN_KEY"]

HTML_FILE = Path("SKILLS/Master-social-design-system/clients/intus-hub/newsletter-ghost/artigo_content.html")
TITULO    = "A nova máfia do Vale do Silício: OpenAI e Anthropic estão produzindo os concorrentes de amanhã"
SUBTITULO = "Os maiores talentos da OpenAI e da Anthropic estão saindo para construir o que as duas empresas não conseguem controlar."

IMG_DIR = Path("SKILLS/Master-social-design-system/clients/intus-hub/newsletter-ghost/imagens-publicacao/12-08")

IMAGENS = {
    1: IMG_DIR / "img01.png",
    2: IMG_DIR / "img02.png",
    3: IMG_DIR / "img03.png",
    4: IMG_DIR / "img04.png",
    5: IMG_DIR / "img05.png",
}

QUALITY   = 82
MAX_WIDTH = 1200

def ghost_token():
    key_id, secret = GHOST_ADMIN_KEY.split(":")
    iat = int(datetime.now(timezone.utc).timestamp())
    payload = {"iat": iat, "exp": iat + 300, "aud": "/admin/"}
    return jwt.encode(payload, bytes.fromhex(secret), algorithm="HS256",
                      headers={"kid": key_id})

def compress(path: Path) -> bytes:
    img = Image.open(path).convert("RGB")
    if img.width > MAX_WIDTH:
        ratio = MAX_WIDTH / img.width
        img = img.resize((MAX_WIDTH, int(img.height * ratio)), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=QUALITY, optimize=True)
    buf.seek(0)
    size_kb = len(buf.getvalue()) // 1024
    print(f"  comprimido: {path.name}  ->  {size_kb} KB")
    return buf.getvalue()

def upload(i: int, data: bytes) -> str:
    token = ghost_token()
    files = {
        "file": (f"aimafia-artigo-img{i}.jpg", data, "image/jpeg"),
        "purpose": (None, "image"),
    }
    r = requests.post(
        f"{GHOST_URL}/ghost/api/admin/images/upload/",
        headers={"Authorization": f"Ghost {token}"},
        files=files,
        timeout=40,
    )
    if r.status_code == 201:
        url = r.json()["images"][0]["url"]
        print(f"  upload OK img{i}: {url}")
        return url
    else:
        print(f"  ERRO upload img{i}: {r.status_code} {r.text[:200]}")
        return None

print("\n=== DEPLOY ARTIGO — AI MAFIA ===\n")

img_urls = {}
for i, path in IMAGENS.items():
    if not path.exists():
        print(f"  ARQUIVO NAO ENCONTRADO: {path}")
        continue
    print(f"\n[img{i}] {path.name}")
    data = compress(path)
    url  = upload(i, data)
    if url:
        img_urls[i] = url

print(f"\n{len(img_urls)}/5 imagens enviadas.")

html = HTML_FILE.read_text(encoding="utf-8")

IMG_TAG = '<div style="padding:20px 0;"><img src="{url}" style="width:100%;max-width:680px;display:block;margin:0 auto;border-radius:6px;" alt="Intus Hub AI News"/></div>'

for i, url in img_urls.items():
    placeholder = f"[IMAGEM_{i}]"
    tag = IMG_TAG.format(url=url)
    if placeholder in html:
        html = html.replace(placeholder, tag)
        print(f"  substituido {placeholder}")
    else:
        print(f"  AVISO: {placeholder} nao encontrado no HTML")

lexical = json.dumps({
    "root": {
        "children": [{"type": "html", "version": 1, "html": html}],
        "direction": None,
        "format": "",
        "indent": 0,
        "type": "root",
        "version": 1,
    }
})

print("\nCriando draft no Ghost...")
token = ghost_token()
payload = {
    "posts": [{
        "title": TITULO,
        "custom_excerpt": SUBTITULO,
        "lexical": lexical,
        "status": "draft",
        "tags": [{"name": "IA"}, {"name": "Startups"}, {"name": "OpenAI"}, {"name": "Anthropic"}],
    }]
}
r = requests.post(
    f"{GHOST_URL}/ghost/api/admin/posts/",
    headers={"Authorization": f"Ghost {token}", "Content-Type": "application/json"},
    json=payload,
    timeout=40,
)

if r.status_code == 201:
    post = r.json()["posts"][0]
    post_id = post["id"]
    draft_url = f"{GHOST_URL}/ghost/#/editor/post/{post_id}"
    print(f"\n DRAFT CRIADO COM SUCESSO")
    print(f"   ID:  {post_id}")
    print(f"   URL: {draft_url}")
else:
    print(f"\n ERRO ao criar draft: {r.status_code}")
    print(r.text[:500])
