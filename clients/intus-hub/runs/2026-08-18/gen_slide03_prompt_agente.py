# -*- coding: utf-8 -*-
"""
Slide 3 — Quando o prompt resolve (Carrossel Prompt vs Agente)
Pipeline: gpt-image 1088x1360 → resize 1080x1350 → avatar composite → image slot composite
"""

import os, sys, subprocess
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw

BASE     = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub")
RUNS     = BASE / "runs" / "2026-08-18"
ENV      = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\gpt-image2-skill\.env")
AVT      = BASE / "assets" / "avatar-diego.jpeg"
SCENE    = Path(r"C:\ARQUIVOS\INTUS CLUB MATERIAL\CARROSSEIS\image-1787098395775.png")
RAW      = RUNS / "slide03-prompt-agente-raw.png"
OUT      = RUNS / "slide03-prompt-agente-FINAL.png"
GPT_EXE  = r"C:\Users\Pichau\AppData\Roaming\Python\Python314\Scripts\gpt-image.exe"

# Parâmetros canônicos fixos (confirmados no Slide 2)
AVT_X    = 66
AVT_Y    = 61
AVT_SIZE = 120

PROMPT = """
Twitter/X style Instagram post slide, white background #FFFFFF, portrait 4:5.

HEADER (top, 88px tall, 44px from left edge, 32px from top):
  - LEFT: solid light gray circle (#D8D8D8), exactly 64x64px at position left=44px top=32px. Profile photo placeholder. No border.
  - RIGHT of circle (16px gap), two text lines left-aligned, vertically centered with the circle:
      Line 1: "Diego Spanevello | Inteligência Artificial" + blue verified checkmark ✓ inline — bold sans-serif 26px, color #1A1A1A
      Line 2: "@diego.spanevello" — regular sans-serif 22px, color #888888

CONTENT (below header, 44px left and right margins, 32px top margin):
  TWO DISTINCT TEXT SIZES:

  HOOK LINE (first line only) — very large, ultra-heavy black/900 weight, approximately 52px, left-aligned, color #1A1A1A:
  "Prompt brilha quando a tarefa cabe em uma resposta."

  BODY TEXT (all remaining lines) — regular 400 weight, clearly smaller (~28px), left-aligned, color #1A1A1A, line-height 1.4:
  "Redigir, resumir, traduzir, classificar.
Você pede, o modelo responde, você refina.
Sem execução no mundo real. Sem memória entre sessões."

  CRITICAL: hook line must be visually 2x heavier and larger than body. No colors — all #1A1A1A.

IMAGE PLACEHOLDER SLOT (below content, 44px side margins, 44px bottom margin):
  A light gray (#E0E0E0) rounded rectangle, 16:9 landscape proportions, border-radius 18px. Empty — no content inside.

STRICT RULES:
- NO separator lines, dividers anywhere
- NO footer
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
    cmd = [GPT_EXE, "-p", PROMPT, "--size", "1088x1360", "--quality", "high", "-f", str(RAW)]
    print("Gerando slide 3...")
    result = subprocess.run(cmd, env=env_copy, capture_output=True, text=True)
    if result.returncode != 0:
        print("ERRO:", result.stderr)
        sys.exit(1)
    print(f"Raw salvo: {RAW}")


def make_circle_avatar(img_path, size):
    img = Image.open(img_path).convert("RGBA")
    aw, ah = img.size
    m = min(aw, ah)
    img = img.crop(((aw-m)//2, (ah-m)//2, (aw-m)//2+m, (ah-m)//2+m))
    img = img.resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size-1, size-1), fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img, (0, 0)); out.putalpha(mask)
    return out


def find_image_slot(img_rgb):
    """Detecta o slot cinza 16:9 na metade inferior do slide."""
    arr = np.array(img_rgb)
    h, w = arr.shape[:2]
    bottom = arr[h//2:, :, :]
    R, G, B = bottom[:,:,0].astype(int), bottom[:,:,1].astype(int), bottom[:,:,2].astype(int)
    diff_rg = np.abs(R - G)
    diff_rb = np.abs(R - B)
    diff_gb = np.abs(G - B)
    gray = (diff_rg < 12) & (diff_rb < 12) & (diff_gb < 12) & (R > 160) & (R < 230)
    rows = np.where(gray.any(axis=1))[0]
    cols = np.where(gray.any(axis=0))[0]
    if len(rows) == 0 or len(cols) == 0:
        # fallback canônico: slot 44px das bordas, 44px do fundo
        slot_x = 44
        slot_w = w - 88
        slot_h = int(slot_w * 9 / 16)
        slot_y = h - slot_h - 44
        print(f"Slot fallback: x={slot_x}, y={slot_y}, w={slot_w}, h={slot_h}")
        return slot_x, slot_y, slot_w, slot_h
    y0 = int(rows[0]) + h//2
    y1 = int(rows[-1]) + h//2
    x0 = int(cols[0])
    x1 = int(cols[-1])
    sw, sh = x1 - x0, y1 - y0
    print(f"Slot detectado: x={x0}, y={y0}, w={sw}, h={sh}")
    return x0, y0, sw, sh


def composite_scene(slide_rgba, scene_path, slot_x, slot_y, slot_w, slot_h, radius=18):
    """Redimensiona cena para o slot e aplica border-radius."""
    scene = Image.open(scene_path).convert("RGB")
    scene = scene.resize((slot_w, slot_h), Image.LANCZOS)
    mask = Image.new("L", (slot_w, slot_h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, slot_w, slot_h), radius=radius, fill=255)
    scene_rgba = scene.convert("RGBA")
    scene_rgba.putalpha(mask)
    slide_rgba.paste(scene_rgba, (slot_x, slot_y), scene_rgba)


def composite():
    slide = Image.open(RAW).convert("RGBA")
    slide = slide.resize((1080, 1350), Image.LANCZOS)
    draw  = ImageDraw.Draw(slide)

    # 1. Limpar e colar avatar
    draw.rectangle((AVT_X-10, AVT_Y-10, AVT_X+AVT_SIZE+10, AVT_Y+AVT_SIZE+10),
                   fill=(255, 255, 255, 255))
    avatar = make_circle_avatar(AVT, AVT_SIZE)
    slide.paste(avatar, (AVT_X, AVT_Y), avatar)

    # 2. Detectar slot e colar imagem do usuário
    slot_x, slot_y, slot_w, slot_h = find_image_slot(slide.convert("RGB"))
    composite_scene(slide, SCENE, slot_x, slot_y, slot_w, slot_h)

    slide.convert("RGB").save(OUT, quality=95)
    print(f"Final salvo: {OUT}")


if __name__ == "__main__":
    generate()
    composite()
