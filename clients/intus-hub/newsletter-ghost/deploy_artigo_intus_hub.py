import sys, json, requests, jwt
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image
import io

sys.stdout.reconfigure(encoding="utf-8")

# ── Config ──────────────────────────────────────────────────────
env = {}
with open(".env") as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()

GHOST_URL       = env["GHOST_URL"]
GHOST_ADMIN_KEY = env["GHOST_ADMIN_KEY"]

HTML_FILE  = Path("SKILLS/Master-social-design-system/clients/intus-hub/runs/2026-07-14/artigo-internet-court-agentes.html")
TITULO     = "⚖️ Agentes de IA vão processar um ao outro, quem é o tribunal?"
SUBTITULO  = "A infraestrutura de arbitragem entre agentes já existe: e revela o quanto o mercado ainda subestima o que está vindo."

# Mapeamento: placeholder → arquivo de origem
IMAGENS = {
    1: "imagen01.png",
    2: "imagen02.png",
    3: "imagem03.png",
    4: "imagen04.png",
}
QUALITY    = 82   # qualidade JPEG
MAX_WIDTH  = 1200 # px

# ── JWT ──────────────────────────────────────────────────────────
def ghost_token():
    key_id, secret = GHOST_ADMIN_KEY.split(":")
    iat = int(datetime.now(timezone.utc).timestamp())
    payload = {"iat": iat, "exp": iat + 300, "aud": "/admin/"}
    return jwt.encode(payload, bytes.fromhex(secret), algorithm="HS256",
                      headers={"kid": key_id})

# ── Comprimir PNG → JPEG em memória ──────────────────────────────
def compress(path: Path) -> bytes:
    img = Image.open(path).convert("RGB")
    if img.width > MAX_WIDTH:
        ratio = MAX_WIDTH / img.width
        img = img.resize((MAX_WIDTH, int(img.height * ratio)), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=QUALITY, optimize=True)
    buf.seek(0)
    size_kb = len(buf.getvalue()) // 1024
    print(f"  comprimido: {path.name}  →  {size_kb} KB")
    return buf.getvalue()

# ── Upload Ghost ─────────────────────────────────────────────────
def upload(i: int, data: bytes) -> str:
    token = ghost_token()
    files = {
        "file": (f"intus-hub-img{i}.jpg", data, "image/jpeg"),
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

# ── Main ─────────────────────────────────────────────────────────
print("\n=== DEPLOY ARTIGO INTUS HUB ===\n")

# 1. Comprimir e fazer upload
img_urls = {}
for i, fname in IMAGENS.items():
    p = Path(fname)
    if not p.exists():
        print(f"  ARQUIVO NAO ENCONTRADO: {fname}")
        continue
    print(f"\n[img{i}] {fname}")
    data = compress(p)
    url  = upload(i, data)
    if url:
        img_urls[i] = url

print(f"\n{len(img_urls)}/4 imagens enviadas.")

# 2. Ler HTML e substituir placeholders
html = HTML_FILE.read_text(encoding="utf-8")

IMG_TAG = '<div style="padding:20px 0;"><img src="{url}" style="width:100%;max-width:680px;display:block;margin:0 auto;border-radius:6px;" alt="Intus Hub"/></div>'

for i, url in img_urls.items():
    placeholder = f"[IMAGEM_{i}]"
    tag = IMG_TAG.format(url=url)
    html = html.replace(placeholder, tag)
    print(f"  substituído {placeholder}")

# 3. Montar lexical
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

# 4. Criar draft no Ghost
print("\nCriando draft no Ghost...")
token = ghost_token()
payload = {
    "posts": [{
        "title": TITULO,
        "custom_excerpt": SUBTITULO,
        "lexical": lexical,
        "status": "draft",
        "tags": [{"name": "IA"}, {"name": "Agentes"}, {"name": "Blockchain"}],
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
    print(f"\n✅ DRAFT CRIADO COM SUCESSO")
    print(f"   ID:  {post_id}")
    print(f"   URL: {draft_url}")
else:
    print(f"\n❌ ERRO ao criar draft: {r.status_code}")
    print(r.text[:500])
