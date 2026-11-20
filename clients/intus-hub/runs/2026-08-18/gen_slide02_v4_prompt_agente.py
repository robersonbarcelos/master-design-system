# -*- coding: utf-8 -*-
"""
Slide 2 v4 — detecção de slot por largura mínima (ignora texto cinza estreito)
"""
import os, sys, subprocess
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw

BASE     = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub")
RUNS     = BASE / "runs" / "2026-08-18"
ENV      = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\gpt-image2-skill\.env")
AVT      = BASE / "assets" / "avatar-diego.jpeg"
SCENE    = Path(r"C:\ARQUIVOS\INTUS CLUB MATERIAL\CARROSSEIS\002.png")
RAW      = RUNS / "slide02-prompt-agente-raw.png"
OUT      = RUNS / "slide02-prompt-agente-FINAL.png"
GPT_EXE  = r"C:\Users\Pichau\AppData\Roaming\Python\Python314\Scripts\gpt-image.exe"

AVT_X, AVT_Y, AVT_SIZE = 66, 61, 120

PROMPT = """
Twitter/X style Instagram post slide, white background #FFFFFF, portrait 4:5.

HEADER (top, 88px tall, 44px from left edge, 32px from top):
  - LEFT: solid light gray circle (#D8D8D8), exactly 64x64px at position left=44px top=32px. No border.
  - RIGHT of circle (16px gap), two text lines left-aligned, vertically centered with the circle:
      Line 1: "Diego Spanevello | Inteligência Artificial" + blue verified checkmark inline — bold sans-serif 26px, color #1A1A1A
      Line 2: "@diego.spanevello" — regular sans-serif 22px, color #888888

CONTENT (below header, 44px left and right margins, 32px top margin):
  TWO DISTINCT TEXT SIZES:

  HOOK LINE (first line only) — ultra-heavy black/900 weight, 52px, left-aligned, color #1A1A1A, line-height 1.1:
  "A diferença fundamental cabe em uma frase:"

  BODY TEXT (all remaining lines) — regular 400 weight, 28px, left-aligned, color #1A1A1A, line-height 1.4:
  "O prompt pede uma resposta.
O agente persegue um objetivo.
Tudo que vem depois é consequência dessa distinção."

  CRITICAL: hook line visually 2x heavier and larger than body. All text #1A1A1A, no colors, no italic.

IMAGE PLACEHOLDER SLOT (directly below the last body line, 24px gap, 44px side margins, 44px bottom margin):
  A solid uniform light gray (#E0E0E0) filled rounded rectangle, 16:9 landscape proportions, border-radius 18px.
  The slot must start AFTER the last line of body text — never overlap text.
  Empty inside — no icons, no label text, no gradient.

STRICT RULES:
- NO separator lines, dividers, footer
- Background pure white #FFFFFF throughout
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
    cmd = [GPT_EXE, "-p", PROMPT, "--size", "1088x1360", "--quality", "high", "-f", str(RAW)]
    print("Gerando slide 2 v4...")
    result = subprocess.run(cmd, env=env_copy, capture_output=True, text=True)
    if result.returncode != 0:
        print("ERRO:", result.stderr); sys.exit(1)
    print(f"Raw: {RAW}")

def make_circle_avatar(img_path, size):
    img = Image.open(img_path).convert("RGBA")
    aw, ah = img.size; m = min(aw, ah)
    img = img.crop(((aw-m)//2, (ah-m)//2, (aw-m)//2+m, (ah-m)//2+m))
    img = img.resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size-1, size-1), fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img, (0, 0)); out.putalpha(mask)
    return out

def detect_slot(img_rgb, min_width_ratio=0.5, search_from_y=400):
    """
    Detecta o slot cinza ignorando texto.
    Critério: linha com >= min_width_ratio da largura do slide sendo pixels cinzas uniformes.
    """
    arr = np.array(img_rgb)
    h, w = arr.shape[:2]
    R = arr[:,:,0].astype(int)
    G = arr[:,:,1].astype(int)
    B = arr[:,:,2].astype(int)
    gray_mask = (np.abs(R-G)<15) & (np.abs(R-B)<15) & (np.abs(G-B)<15) & (R>150) & (R<235)
    min_cols = int(w * min_width_ratio)
    slot_rows = []
    for y in range(search_from_y, h):
        if gray_mask[y].sum() >= min_cols:
            slot_rows.append(y)
    if not slot_rows:
        # fallback ancorado no fundo
        sw = w - 88; sh = int(sw * 9/16); sx = 44; sy = h - sh - 44
        print(f"Slot fallback: x={sx}, y={sy}, w={sw}, h={sh}")
        return sx, sy, sw, sh
    y0 = slot_rows[0]
    y1 = slot_rows[-1]
    # colunas cinzas nessas linhas
    region = gray_mask[y0:y1+1, :]
    col_mask = region.any(axis=0)
    cols = np.where(col_mask)[0]
    x0 = int(cols[0]); x1 = int(cols[-1])
    sw = x1 - x0; sh = y1 - y0
    print(f"Slot detectado: x={x0}, y={y0}, w={sw}, h={sh}")
    return x0, y0, sw, sh

def composite_scene(slide_rgba, scene_path, sx, sy, sw, sh, radius=18):
    scene = Image.open(scene_path).convert("RGB").resize((sw, sh), Image.LANCZOS)
    mask = Image.new("L", (sw, sh), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, sw, sh), radius=radius, fill=255)
    scene_rgba = scene.convert("RGBA"); scene_rgba.putalpha(mask)
    slide_rgba.paste(scene_rgba, (sx, sy), scene_rgba)

def composite():
    slide = Image.open(RAW).convert("RGBA").resize((1080, 1350), Image.LANCZOS)
    draw  = ImageDraw.Draw(slide)
    # avatar
    draw.rectangle((AVT_X-10, AVT_Y-10, AVT_X+AVT_SIZE+10, AVT_Y+AVT_SIZE+30), fill=(255,255,255,255))
    avatar = make_circle_avatar(AVT, AVT_SIZE)
    slide.paste(avatar, (AVT_X, AVT_Y), avatar)
    # slot — detecção por largura mínima (ignora texto estreito)
    sx, sy, sw, sh = detect_slot(slide.convert("RGB"))
    composite_scene(slide, SCENE, sx, sy, sw, sh)
    slide.convert("RGB").save(OUT, quality=95)
    print(f"Final: {OUT}")

if __name__ == "__main__":
    generate()
    composite()
