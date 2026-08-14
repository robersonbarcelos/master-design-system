import sys, json, requests, jwt
from datetime import datetime, timezone
from pathlib import Path

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
POST_ID         = "6a7a07c16d82ee000163bdea"

HTML_FILE = Path("SKILLS/Master-social-design-system/clients/intus-hub/newsletter-ghost/artigo_content.html")

IMG_URLS = {
    1: "https://storage.ghost.io/c/bd/ee/bdee7c20-de79-40b5-bf13-57c55bb9256c/content/images/2026/08/aimafia-artigo-img1.jpg",
    2: "https://storage.ghost.io/c/bd/ee/bdee7c20-de79-40b5-bf13-57c55bb9256c/content/images/2026/08/aimafia-artigo-img2.jpg",
    3: "https://storage.ghost.io/c/bd/ee/bdee7c20-de79-40b5-bf13-57c55bb9256c/content/images/2026/08/aimafia-artigo-img3.jpg",
    4: "https://storage.ghost.io/c/bd/ee/bdee7c20-de79-40b5-bf13-57c55bb9256c/content/images/2026/08/aimafia-artigo-img4.jpg",
    5: "https://storage.ghost.io/c/bd/ee/bdee7c20-de79-40b5-bf13-57c55bb9256c/content/images/2026/08/aimafia-artigo-img5.jpg",
}

IMG_TAG = '<div style="padding:20px 0;"><img src="{url}" style="width:100%;max-width:680px;display:block;margin:0 auto;border-radius:6px;" alt="Intus Hub AI News"/></div>'

def ghost_token():
    key_id, secret = GHOST_ADMIN_KEY.split(":")
    iat = int(datetime.now(timezone.utc).timestamp())
    payload = {"iat": iat, "exp": iat + 300, "aud": "/admin/"}
    return jwt.encode(payload, bytes.fromhex(secret), algorithm="HS256",
                      headers={"kid": key_id})

print("\n=== ATUALIZANDO DRAFT — PADDING MOBILE ===\n")

html = HTML_FILE.read_text(encoding="utf-8")

for i, url in IMG_URLS.items():
    html = html.replace(f"[IMAGEM_{i}]", IMG_TAG.format(url=url))
    print(f"  substituido [IMAGEM_{i}]")

lexical = json.dumps({
    "root": {
        "children": [{"type": "html", "version": 1, "html": html}],
        "direction": None, "format": "", "indent": 0,
        "type": "root", "version": 1,
    }
})

token = ghost_token()
r = requests.get(f"{GHOST_URL}/ghost/api/admin/posts/{POST_ID}/",
                 headers={"Authorization": f"Ghost {token}"})
updated_at = r.json()["posts"][0]["updated_at"]

token = ghost_token()
r = requests.put(
    f"{GHOST_URL}/ghost/api/admin/posts/{POST_ID}/",
    headers={"Authorization": f"Ghost {token}", "Content-Type": "application/json"},
    json={"posts": [{
        "title": "A nova máfia do Vale do Silício: OpenAI e Anthropic estão produzindo os concorrentes de amanhã",
        "lexical": lexical,
        "status": "draft",
        "updated_at": updated_at,
    }]},
    timeout=40,
)

if r.status_code == 200:
    print(f"\n DRAFT ATUALIZADO")
    print(f"   URL: {GHOST_URL}/ghost/#/editor/post/{POST_ID}")
else:
    print(f"\n ERRO: {r.status_code} {r.text[:300]}")
