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
POST_ID         = "6a5637d0014562000107d8bd"
HTML_FILE       = Path("SKILLS/Master-social-design-system/clients/intus-hub/runs/2026-07-14/artigo-internet-court-agentes.html")

# URLs já no Ghost CDN (corpo do artigo)
IMG_URLS = {
    1: "https://storage.ghost.io/c/bd/ee/bdee7c20-de79-40b5-bf13-57c55bb9256c/content/images/2026/07/intus-hub-img1.jpg",
    2: "https://storage.ghost.io/c/bd/ee/bdee7c20-de79-40b5-bf13-57c55bb9256c/content/images/2026/07/intus-hub-img2.jpg",
    3: "https://storage.ghost.io/c/bd/ee/bdee7c20-de79-40b5-bf13-57c55bb9256c/content/images/2026/07/intus-hub-img3.jpg",
    4: "https://storage.ghost.io/c/bd/ee/bdee7c20-de79-40b5-bf13-57c55bb9256c/content/images/2026/07/intus-hub-img4.jpg",
}

def ghost_token():
    key_id, secret = GHOST_ADMIN_KEY.split(":")
    iat = int(datetime.now(timezone.utc).timestamp())
    payload = {"iat": iat, "exp": iat + 300, "aud": "/admin/"}
    return jwt.encode(payload, bytes.fromhex(secret), algorithm="HS256",
                      headers={"kid": key_id})

def compress_and_upload(path: Path, name: str) -> str:
    img = Image.open(path).convert("RGB")
    if img.width > 1200:
        ratio = 1200 / img.width
        img = img.resize((1200, int(img.height * ratio)), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=85, optimize=True)
    buf.seek(0)
    print(f"  comprimido: {path.name} → {len(buf.getvalue())//1024} KB")
    token = ghost_token()
    files = {"file": (name, buf.getvalue(), "image/jpeg"), "purpose": (None, "image")}
    r = requests.post(f"{GHOST_URL}/ghost/api/admin/images/upload/",
                      headers={"Authorization": f"Ghost {token}"},
                      files=files, timeout=40)
    if r.status_code == 201:
        url = r.json()["images"][0]["url"]
        print(f"  upload OK: {url}")
        return url
    else:
        print(f"  ERRO: {r.status_code} {r.text[:200]}")
        return None

# 1. Upload da img4.jpg (banner CTA)
print("\n[CTA] Fazendo upload de img4.jpg...")
cta_img_url = compress_and_upload(Path("img4.jpg"), "intus-hub-cta.jpg")

# 2. Montar bloco CTA conectado ao tema do artigo
CTA_BLOCK = f"""
<!-- CTA SUPER AGENTE -->
<div style="margin:48px 0 0 0;">

  <div style="border-radius:12px;overflow:hidden;margin:0 0 0 0;">
    <img src="{cta_img_url}" style="width:100%;max-width:680px;display:block;margin:0 auto;" alt="Super Agente de IA"/>
  </div>

  <div style="background:#0a0a0a;border-radius:0 0 12px 12px;padding:32px 28px;text-align:center;">
    <p style="font-family:'Trebuchet MS',Arial,sans-serif;font-size:11px;font-weight:700;letter-spacing:3px;color:#E84000;text-transform:uppercase;margin:0 0 14px 0;">SUPER AGENTE DE IA</p>
    <p style="font-family:'Trebuchet MS',Arial,sans-serif;font-size:22px;font-weight:900;color:#F0F4FF;line-height:1.3;margin:0 0 8px 0;">Quando o agente errar, quem resolve é você.</p>
    <p style="font-family:'Georgia',serif;font-size:16px;font-style:italic;color:#aaaaaa;margin:0 0 20px 0;">Mas primeiro você precisa ter um agente.</p>
    <p style="font-family:'Trebuchet MS',Arial,sans-serif;font-size:15px;color:#cccccc;line-height:1.6;margin:0 0 6px 0;">Comenta nos posts do Instagram: <strong style="color:#E84000;">AGENTE</strong></p>
    <p style="font-family:'Trebuchet MS',Arial,sans-serif;font-size:15px;color:#cccccc;line-height:1.6;margin:0 0 24px 0;">Que eu te envio o Super Agente de IA.</p>
    <table cellpadding="0" cellspacing="0" border="0" style="margin:0 auto;">
      <tr>
        <td bgcolor="#E84000" style="background:#E84000;border-radius:6px;padding:14px 32px;">
          <a href="https://super-agente-v2.vercel.app" style="font-family:'Trebuchet MS',Arial,sans-serif;font-size:15px;font-weight:800;color:#ffffff;text-decoration:none;letter-spacing:1px;white-space:nowrap;">QUERO MEU SUPER AGENTE &rarr; R$ 87,90</a>
        </td>
      </tr>
    </table>
    <p style="font-family:'Trebuchet MS',Arial,sans-serif;font-size:11px;color:#666666;margin:16px 0 0 0;letter-spacing:1px;">Garantia de 7 dias &middot; Acesso imediato &middot; Sem saber programar</p>
  </div>

</div>
"""

# 3. Ler HTML local e reconstruir do zero com imagens + CTA
html = HTML_FILE.read_text(encoding="utf-8")

# Garantir placeholders substituídos (caso ainda restem)
IMG_TAG = '<div style="padding:16px 0;"><img src="{url}" style="width:100%;max-width:680px;display:block;margin:0 auto;border-radius:6px;" alt=""/></div>'
for i, url in IMG_URLS.items():
    html = html.replace(f"[IMAGEM_{i}]", IMG_TAG.format(url=url))

# Remover CTA antigo se existir e inserir novo antes do fechamento do container
if "<!-- CTA SUPER AGENTE -->" in html:
    start = html.index("<!-- CTA SUPER AGENTE -->")
    end   = html.index("<!-- DISCLAIMER -->")
    html  = html[:start] + html[end:]

# Inserir CTA antes do DISCLAIMER
html = html.replace("<!-- DISCLAIMER -->", CTA_BLOCK + "\n  <!-- DISCLAIMER -->")

# Salvar HTML local
HTML_FILE.write_text(html, encoding="utf-8")
print("\n  HTML local salvo com CTA")

# 4. Atualizar Ghost
token = ghost_token()
r = requests.get(f"{GHOST_URL}/ghost/api/admin/posts/{POST_ID}/",
                 headers={"Authorization": f"Ghost {token}"})
updated_at = r.json()["posts"][0]["updated_at"]

lexical = json.dumps({
    "root": {
        "children": [{"type": "html", "version": 1, "html": html}],
        "direction": None, "format": "", "indent": 0,
        "type": "root", "version": 1
    }
})

token = ghost_token()
r = requests.put(
    f"{GHOST_URL}/ghost/api/admin/posts/{POST_ID}/",
    headers={"Authorization": f"Ghost {token}", "Content-Type": "application/json"},
    json={"posts": [{
        "title": "⚖️ Agentes de IA vão processar um ao outro, quem é o tribunal?",
        "lexical": lexical,
        "status": "draft",
        "updated_at": updated_at
    }]},
    timeout=40
)

if r.status_code == 200:
    print(f"\n✅ Draft atualizado — imagens + CTA")
    print(f"   URL: {GHOST_URL}/ghost/#/editor/post/{POST_ID}")
else:
    print(f"\n❌ Erro: {r.status_code}")
    print(r.text[:300])
