import os, sys, json, requests, jwt
from datetime import datetime, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

from dotenv import load_dotenv
load_dotenv()

GHOST_URL = os.getenv("GHOST_URL")
GHOST_ADMIN_KEY = os.getenv("GHOST_ADMIN_KEY")
POST_ID = "6a317d4a3ad08d000187803c"

def ghost_token():
    key_id, secret = GHOST_ADMIN_KEY.split(":")
    iat = int(datetime.now(timezone.utc).timestamp())
    payload = {"iat": iat, "exp": iat + 300, "aud": "/admin/"}
    return jwt.encode(payload, bytes.fromhex(secret), algorithm="HS256", headers={"kid": key_id})

def upload_img(path, nome):
    token = ghost_token()
    with open(path, "rb") as f:
        files = {"file": (f"{nome}.jpg", f, "image/jpeg"), "purpose": (None, "image")}
        r = requests.post(f"{GHOST_URL}/ghost/api/admin/images/upload/",
                           headers={"Authorization": f"Ghost {token}"}, files=files, timeout=30)
    r.raise_for_status()
    return r.json()["images"][0]["url"]

html = Path("artigo_content.html").read_text(encoding="utf-8")

resultados = {}
for i in range(1, 6):
    p = Path(f"img{i}.jpg")
    if not p.exists():
        print(f"  [{i}] ARQUIVO NAO ENCONTRADO: {p}")
        continue
    url = upload_img(p, f"intus-rio35-img{i}")
    resultados[i] = url
    print(f"  [{i}] upload OK -> {url}")

img_tag_tpl = ('<div style="padding:20px 0;">'
               '<img src="{url}" alt="{alt}" '
               'style="width:100%;max-width:670px;display:block;margin:0 auto;border-radius:6px;"/>'
               '</div>')

for i in range(1, 6):
    placeholder = f"[IMAGEM_{i}]"
    tag = img_tag_tpl.format(url=resultados[i], alt=f"Imagem {i}") if i in resultados else ""
    html = html.replace(placeholder, tag)

Path("artigo_content.final.html").write_text(html, encoding="utf-8")
print("\nHTML final salvo: artigo_content.final.html")
print("Imagens OK:", sorted(resultados.keys()))

if len(resultados) < 5:
    print("\nAVISO: nem todas as 5 imagens foram enviadas. Abortando atualizacao do draft.")
    sys.exit(1)

TITULO = "A IA de R$500 mil da Prefeitura do Rio era um clone de R$25 mil"
SUBTITULO = 'A Prefeitura do Rio lançou um modelo "próprio" de IA. Uma startup chinesa provou, ponto por ponto, que era um clone.'

lexical = json.dumps({
    "root": {
        "children": [{"type": "html", "version": 1, "html": html}],
        "direction": None, "format": "", "indent": 0,
        "type": "root", "version": 1
    }
})

token = ghost_token()
r_get = requests.get(f"{GHOST_URL}/ghost/api/admin/posts/{POST_ID}/",
                      headers={"Authorization": f"Ghost {token}"}, timeout=30)
r_get.raise_for_status()
updated_at = r_get.json()["posts"][0]["updated_at"]

token = ghost_token()
r = requests.put(
    f"{GHOST_URL}/ghost/api/admin/posts/{POST_ID}/",
    headers={"Authorization": f"Ghost {token}", "Content-Type": "application/json"},
    json={"posts": [{"title": TITULO, "custom_excerpt": SUBTITULO, "lexical": lexical,
                      "status": "draft", "updated_at": updated_at}]},
    timeout=30
)
print("\nStatus update:", r.status_code)
if r.status_code == 200:
    print(f"Draft atualizado: {GHOST_URL}/ghost/#/editor/post/{POST_ID}")
else:
    print(r.text[:1000])
