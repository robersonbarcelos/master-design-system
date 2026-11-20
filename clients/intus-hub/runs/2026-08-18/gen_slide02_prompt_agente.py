# -*- coding: utf-8 -*-
"""
Slide 2 — Contexto (Carrossel Prompt vs Agente)
Pipeline: gpt-image 1088x1360 → resize Pillow 1080x1350 → avatar composite
"""

import os, sys, subprocess
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw

BASE  = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub")
RUNS  = BASE / "runs" / "2026-08-18"
ENV   = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\gpt-image2-skill\.env")
AVT   = BASE / "assets" / "avatar-diego.jpeg"
RAW   = RUNS / "slide02-prompt-agente-raw.png"
OUT   = RUNS / "slide02-prompt-agente-FINAL.png"

PROMPT = """
Twitter/X style Instagram post slide, white background #FFFFFF, portrait 4:5.

HEADER (top, 88px tall, 44px from left edge, 32px from top):
  - LEFT: solid light gray circle (#D8D8D8), exactly 64x64px at position left=44px top=32px. Profile photo placeholder. No border.
  - RIGHT of circle (16px gap), two text lines left-aligned, vertically centered with the circle:
      Line 1: "Diego Spanevello | Inteligência Artificial" + blue verified checkmark ✓ inline — bold sans-serif 26px, color #1A1A1A
      Line 2: "@diego.spanevello" — regular sans-serif 22px, color #888888

CONTENT (below header, 44px left and right margins, 32px top margin):
  TWO DISTINCT TEXT SIZES — this distinction is the most important rule:

  HOOK LINE (first line only) — very large, ultra-heavy black/900 weight, approximately 52px, left-aligned, color #1A1A1A:
  "A diferença fundamental cabe em uma frase:"

  BODY TEXT (all remaining lines) — regular 400 weight, clearly and noticeably smaller than hook (~28px), left-aligned, color #1A1A1A, line-height 1.4:
  "O prompt pede uma resposta.
O agente persegue um objetivo.
Tudo que vem depois é consequência dessa distinção."

  CRITICAL: hook line must look visually 2x heavier and larger than body. No colors in text — all #1A1A1A. No italic.

IMAGE PLACEHOLDER SLOT (below content, 44px side margins, 44px bottom margin):
  A light gray (#E0E0E0) rounded rectangle, 16:9 landscape proportions (wide), border-radius 18px. Empty — no scene inside. No label text.

STRICT RULES:
- NO separator lines, dividers, or horizontal rules anywhere
- NO footer text, NO @handle at bottom
- Background pure white #FFFFFF
- Gray avatar circle exactly 64x64px at left=44 top=32
- Image slot is landscape 16:9, never square, never portrait
""".strip()


def load_env(path):
    env = {}
    for line in Path(path).read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


def generate():
    env = load_env(ENV)
    env_copy = os.environ.copy()
    env_copy["OPENAI_API_KEY"] = env["OPENAI_API_KEY"]
    env_copy["PATH"] = env_copy.get("PATH", "") + r";C:\Users\Pichau\AppData\Roaming\Python\Python314\Scripts"
    gpt_image_exe = r"C:\Users\Pichau\AppData\Roaming\Python\Python314\Scripts\gpt-image.exe"

    cmd = [gpt_image_exe, "-p", PROMPT, "--size", "1088x1360", "--quality", "high", "-f", str(RAW)]
    print("Gerando slide 2...")
    result = subprocess.run(cmd, env=env_copy, capture_output=True, text=True)
    if result.returncode != 0:
        print("ERRO:", result.stderr)
        sys.exit(1)
    print(f"Raw salvo: {RAW}")


def detect_gray_circle(img_rgb, search_region_h=200):
    arr = np.array(img_rgb)
    # Busca apenas na faixa esquerda (x < 250) onde o círculo deve estar
    header = arr[:search_region_h, :250, :]
    R, G, B = header[:,:,0], header[:,:,1], header[:,:,2]
    diff_rg = np.abs(R.astype(int) - G.astype(int))
    diff_rb = np.abs(R.astype(int) - B.astype(int))
    diff_gb = np.abs(G.astype(int) - B.astype(int))
    gray_mask = (
        (diff_rg < 15) & (diff_rb < 15) & (diff_gb < 15) &
        (R > 160) & (R < 225)  # cinza médio — exclui branco e texto escuro
    )
    rows = np.where(gray_mask.any(axis=1))[0]
    cols = np.where(gray_mask.any(axis=0))[0]
    if len(rows) == 0 or len(cols) == 0:
        print("AVISO: círculo não detectado. Usando fallback (44, 32, 100, 100).")
        return 44, 32, 100, 100
    y0, y1 = int(rows[0]), int(rows[-1])
    x0, x1 = int(cols[0]), int(cols[-1])
    w, h = x1 - x0, y1 - y0
    print(f"Círculo detectado: x={x0}, y={y0}, w={w}, h={h}")
    if w < 40 or w > 200 or h < 40 or h > 200:
        print(f"AVISO: dimensão suspeita ({w}x{h}). Usando fallback (44, 32, 100, 100).")
        return 44, 32, 100, 100
    return x0, y0, w, h


def make_circle_avatar(img_path, size):
    img = Image.open(img_path).convert("RGBA")
    aw, ah = img.size
    m = min(aw, ah)
    img = img.crop(((aw-m)//2, (ah-m)//2, (aw-m)//2+m, (ah-m)//2+m))
    img = img.resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size, size), fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img, (0, 0))
    out.putalpha(mask)
    return out


def composite():
    slide = Image.open(RAW).convert("RGBA")
    slide = slide.resize((1080, 1350), Image.LANCZOS)
    x, y, w, h = detect_gray_circle(slide.convert("RGB"))
    size = max(w, h)

    # Limpar área do círculo cinza com branco antes de colar avatar
    draw = ImageDraw.Draw(slide)
    draw.rectangle((x - 4, y - 4, x + size + 4, y + size + 4), fill=(255, 255, 255, 255))

    avatar = make_circle_avatar(AVT, size)
    slide.paste(avatar, (x, y), avatar)
    slide.convert("RGB").save(OUT, quality=95)
    print(f"Final salvo: {OUT}")


if __name__ == "__main__":
    generate()
    composite()
