# -*- coding: utf-8 -*-
import os, sys, subprocess
from pathlib import Path
from PIL import Image, ImageDraw

BASE     = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub")
RUNS     = BASE / "runs" / "2026-08-18"
ENV      = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\gpt-image2-skill\.env")
AVT      = BASE / "assets" / "avatar-diego.jpeg"
SCENE    = Path(r"C:\ARQUIVOS\INTUS CLUB MATERIAL\CARROSSEIS\008.png")
RAW      = RUNS / "slide08-prompt-agente-raw.png"
OUT      = RUNS / "slide08-prompt-agente-FINAL.png"
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
  "A frequência muda tudo."

  BODY TEXT (all remaining lines) — regular 400 weight, 28px, left-aligned, color #1A1A1A, line-height 1.4:
  "Uma tarefa complexa executada uma vez por mês raramente compensa o esforço de um agente.
A mesma tarefa repetida 40 vezes por dia inverte completamente essa conta."

  CRITICAL: hook line visually 2x heavier and larger than body. All text #1A1A1A, no colors, no italic.

BOTTOM AREA (below content, 44px side margins, 44px bottom margin):
  Pure white space — no rectangle, no placeholder, no gray shape. Leave completely empty white.

STRICT RULES:
- NO separator lines, dividers, footer
- NO gray rectangle or placeholder box anywhere
- Background pure white #FFFFFF throughout
- Gray avatar circle exactly 64x64px at left=44 top=32
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
    print("Gerando slide 8...")
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

def composite_scene(slide_rgba, scene_path, sx, sy, sw, sh, radius=18):
    scene = Image.open(scene_path).convert("RGB").resize((sw, sh), Image.LANCZOS)
    mask = Image.new("L", (sw, sh), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, sw, sh), radius=radius, fill=255)
    scene_rgba = scene.convert("RGBA"); scene_rgba.putalpha(mask)
    slide_rgba.paste(scene_rgba, (sx, sy), scene_rgba)

def composite():
    slide = Image.open(RAW).convert("RGBA").resize((1080, 1350), Image.LANCZOS)
    draw  = ImageDraw.Draw(slide)
    draw.rectangle((AVT_X-10, AVT_Y-10, AVT_X+AVT_SIZE+10, AVT_Y+AVT_SIZE+30), fill=(255,255,255,255))
    avatar = make_circle_avatar(AVT, AVT_SIZE)
    slide.paste(avatar, (AVT_X, AVT_Y), avatar)
    sw = 1080-88; sh = int(sw*9/16); sx = 44; sy = 1350-sh-44
    composite_scene(slide, SCENE, sx, sy, sw, sh)
    slide.convert("RGB").save(OUT, quality=95)
    print(f"Final: {OUT}")

if __name__ == "__main__":
    generate()
    composite()
