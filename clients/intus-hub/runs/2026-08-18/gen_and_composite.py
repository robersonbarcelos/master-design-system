"""
gen_and_composite.py
Pipeline completo:
  1. Gera o slide com gpt-image (com círculo cinza placeholder no header)
  2. Detecta o círculo cinza via numpy
  3. Substitui pelo avatar circular do Diego no tamanho exato detectado
"""

import os, sys, json, subprocess
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw

# ── Caminhos ────────────────────────────────────────────────────────────────
BASE   = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub")
RUNS   = BASE / "runs" / "2026-08-18"
ENV    = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\gpt-image2-skill\.env")
AVT    = BASE / "assets" / "avatar-diego.jpeg"
RAW    = RUNS / "slide-twitter-defi-06-raw.png"
OUT    = RUNS / "slide-twitter-defi-06-final.png"

# ── API key ──────────────────────────────────────────────────────────────────
def load_env(path):
    env = {}
    for line in Path(path).read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env

# ── Prompt ───────────────────────────────────────────────────────────────────
PROMPT = """
Twitter/X style Instagram post slide, white background #FFFFFF, portrait 4:5.

HEADER (top section, 88px tall):
  - LEFT: a solid light gray circle (#D8D8D8), exactly 64x64px, positioned at 44px from left edge, 32px from top edge. This is a profile photo placeholder. The circle must be exactly 64px diameter, solid fill, no border.
  - RIGHT of circle (16px gap): two lines of text left-aligned:
      Line 1: "Diego Spanevello | Inteligência Artificial" followed by a blue verified checkmark circle ✓ — font: bold sans-serif 26px, color #1A1A1A
      Line 2: "@diego.spanevello" — font: regular sans-serif 22px, color #888888
  The header text block is vertically centered with the gray circle.

CONTENT (below header, 44px side margins):
  Text at 34px regular sans-serif, color #1A1A1A, line-height 1.4:
  "68% dos novos protocolos DeFi lançados em 2026 foram hackeados.

  A maioria usava o mesmo erro.

  **VAMOS DESTRINCHAR ISSO.**"
  (bold only for the last line, no color change)

IMAGE SLOT (below content, 44px side margins, 44px bottom margin):
  Landscape 16:9 image slot, 992x558px, border-radius 18px.
  Scene: glowing blockchain nodes network, electric blue neon lines connecting luminous cube nodes on a dark background, cinematic lighting, ultra-realistic, no text.

STRICT RULES:
- NO separator lines, NO dividers, NO horizontal rules anywhere
- NO footer
- Background is pure white #FFFFFF
- Gray circle MUST be exactly 64x64px solid fill at position left=44px top=32px
- Image slot is landscape 16:9, never square, never portrait
""".strip()

# ── Step 1: gerar imagem ──────────────────────────────────────────────────────
def generate():
    env = load_env(ENV)
    env_copy = os.environ.copy()
    env_copy["OPENAI_API_KEY"] = env["OPENAI_API_KEY"]
    env_copy["PATH"] = env_copy.get("PATH","") + r";C:\Users\Pichau\AppData\Roaming\Python\Python314\Scripts"

    cmd = ["gpt-image", "-p", PROMPT, "--size", "1088x1360", "--quality", "high", "-f", str(RAW)]
    print("Gerando slide com gpt-image...")
    result = subprocess.run(cmd, env=env_copy, capture_output=True, text=True)
    if result.returncode != 0:
        print("ERRO:", result.stderr)
        sys.exit(1)
    print(f"Raw salvo: {RAW}")

# ── Step 2: detectar círculo cinza ───────────────────────────────────────────
def detect_gray_circle(img_rgb, search_region_h=200):
    """
    Encontra o bounding-box do círculo cinza no header.
    Retorna (x, y, w, h) — coordenadas no img redimensionado para 1080×1350.
    """
    arr = np.array(img_rgb)
    header = arr[:search_region_h, :, :]  # só topo

    R, G, B = header[:,:,0], header[:,:,1], header[:,:,2]
    # Pixels cinza: canais próximos entre si e valor entre 140–230
    diff_rg = np.abs(R.astype(int) - G.astype(int))
    diff_rb = np.abs(R.astype(int) - B.astype(int))
    diff_gb = np.abs(G.astype(int) - B.astype(int))

    gray_mask = (
        (diff_rg < 20) & (diff_rb < 20) & (diff_gb < 20) &
        (R > 140) & (R < 235)  # não branco, não preto
    )

    rows = np.where(gray_mask.any(axis=1))[0]
    cols = np.where(gray_mask.any(axis=0))[0]

    if len(rows) == 0 or len(cols) == 0:
        print("AVISO: círculo cinza não detectado. Usando coordenadas do template.")
        return 44, 32, 64, 64  # fallback do template

    y0, y1 = int(rows[0]), int(rows[-1])
    x0, x1 = int(cols[0]), int(cols[-1])
    w, h = x1 - x0, y1 - y0

    print(f"Círculo detectado: x={x0}, y={y0}, w={w}, h={h}")

    # Sanidade: o círculo deve ser razoável (entre 40px e 200px)
    if w < 40 or w > 200 or h < 40 or h > 200:
        print(f"AVISO: dimensão suspeita ({w}×{h}). Usando coordenadas do template.")
        return 44, 32, 64, 64

    return x0, y0, w, h

# ── Step 3: composite do avatar ──────────────────────────────────────────────
def make_circle_avatar(img_path, size):
    img = Image.open(img_path).convert("RGBA")
    aw, ah = img.size
    m = min(aw, ah)
    img = img.crop(((aw-m)//2, (ah-m)//2, (aw-m)//2+m, (ah-m)//2+m))
    img = img.resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size, size), fill=255)
    out = Image.new("RGBA", (size, size), (0,0,0,0))
    out.paste(img, (0,0))
    out.putalpha(mask)
    return out

def composite():
    slide = Image.open(RAW).convert("RGBA")
    slide = slide.resize((1080, 1350), Image.LANCZOS)

    x, y, w, h = detect_gray_circle(slide.convert("RGB"))
    size = max(w, h)  # usar o maior eixo como diâmetro

    avatar = make_circle_avatar(AVT, size)
    slide.paste(avatar, (x, y), avatar)
    slide.convert("RGB").save(OUT, quality=95)
    print(f"Final salvo: {OUT}")

# ── Main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    generate()
    composite()
