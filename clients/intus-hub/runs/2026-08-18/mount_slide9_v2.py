# -*- coding: utf-8 -*-
"""
Slide 9 — pipeline híbrido:
  TOPO : Pillow desenha header (avatar real + nome + handle)
  BAIXO: GPT Image gera copy estilizado + cena campeão
  MERGE: Pillow cola o bloco API abaixo do header
"""
import sys, base64
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BASE  = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub")
RUNS  = BASE / "runs" / "2026-08-18"
AVT   = BASE / "assets" / "avatar-diego.jpeg"
ENV   = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\gpt-image2-skill\.env")

ARIAL_BLACK = r"C:\Windows\Fonts\Ariblk.ttf"
ARIAL_BOLD  = r"C:\Windows\Fonts\Arialbd.ttf"
ARIAL_REG   = r"C:\Windows\Fonts\Arial.ttf"

WHITE = (255, 255, 255)
DARK  = (26,  26,  26)
LGRAY = (136, 136, 136)
BLUE  = (29,  155, 240)
W, H  = 1080, 1350

# ── helpers ─────────────────────────────────────────────────

def text_size(font, text):
    bb = font.getbbox(text)
    return bb[2]-bb[0], bb[3]-bb[1]

def make_circle_avatar(path, size):
    img = Image.open(path).convert("RGBA")
    aw, ah = img.size
    m = min(aw, ah)
    img = img.crop(((aw-m)//2, (ah-m)//2, (aw-m)//2+m, (ah-m)//2+m))
    img = img.resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size, size), fill=255)
    out = Image.new("RGBA", (size, size), (0,0,0,0))
    out.paste(img, (0,0)); out.putalpha(mask)
    return out

def draw_badge(draw, x, y, size):
    draw.ellipse((x, y, x+size, y+size), fill=BLUE)
    pad = size * 0.22
    cx, cy = x+size/2, y+size/2
    p1=(x+pad,cy+1); p2=(cx-1,y+size-pad); p3=(x+size-pad,y+pad+1)
    lw = max(2, int(size*0.13))
    draw.line([p1,p2], fill=(255,255,255), width=lw)
    draw.line([p2,p3], fill=(255,255,255), width=lw)

# ── STEP 1: header via Pillow ────────────────────────────────

def draw_header(slide):
    draw = ImageDraw.Draw(slide)
    fn_name   = ImageFont.truetype(ARIAL_BOLD, 22)
    fn_handle = ImageFont.truetype(ARIAL_REG,  18)

    avt_size = 125; text_x = 214; cy_h = 115
    ax = text_x - 16 - avt_size   # 73
    ay = cy_h - avt_size // 2      # 53

    name_str   = "Diego Spanevello | Inteligência Artificial"
    handle_str = "@diego.spanevello"

    nw, nh = text_size(fn_name,   name_str)
    hw, hh = text_size(fn_handle, handle_str)
    name_y   = cy_h - (nh + 6 + hh) // 2
    handle_y = name_y + nh + 6

    draw.text((text_x, name_y),   name_str,   font=fn_name,   fill=DARK)
    draw.text((text_x, handle_y), handle_str, font=fn_handle, fill=LGRAY)
    draw_badge(draw, text_x+nw+6, name_y+(nh-18)//2, 18)

    avatar = make_circle_avatar(AVT, avt_size)
    slide.paste(avatar, (ax, ay), avatar)

    return ay + avt_size   # y onde o header termina

# ── STEP 2: bloco inferior via GPT Image ────────────────────

BOTTOM_PROMPT = """White background #FFFFFF, portrait layout. No header, no avatar, no profile info.

COPY — all text centered, 64px side margins:

  Line 1: "É ter um agente com memória, ferramentas"
  Font: Arial regular 27px, color #666666, centered.

  Line 2: "e identidade própria rodando enquanto você dorme."
  Font: Arial regular 27px, color #666666, centered.

  [vertical gap 24px]

  Line 3 — MIXED STYLES, all on one line, centered as a unit:
    "Isso é o Super "  → Arial regular 27px #666666
    "AGENTE"           → Arial Black 27px #0A0A0A (bold, heavier weight)
    ". "               → Arial regular 27px #666666
    "R$87,95"          → Arial Black 27px #E6641E (orange)
    "."                → Arial regular 27px #666666

  Line 4 — MIXED STYLES, all on one line, centered as a unit:
    "Comenta "                → Arial regular 27px #666666
    "AGENTE"                  → Arial Black 27px #0A0A0A (bold)
    " — eu te mando o link."  → Arial regular 27px #666666

IMAGE — 40px below last text line, fills remaining height, 64px side margins, border-radius 16px:
  Heavy industrial robot with dark metallic body, circuit boards and power cables.
  Robot standing in boxing ring center, holding championship belt with BOTH HANDS raised above head.
  Team of cornermen celebrating around the robot. Confetti falling from arena lights.
  Black and white — only red corner ropes, red gloves, and gold championship belt details in color.
  Cinematic dramatic arena lighting. No text, no logos inside image.

STRICT RULES:
- Background pure white #FFFFFF
- No header, no avatar circle, no profile name
- Text centered horizontally
- NO dividers, NO footer"""

def generate_bottom():
    env_vars = {}
    for line in ENV.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env_vars[k.strip()] = v.strip()

    import openai
    client = openai.OpenAI(api_key=env_vars["OPENAI_API_KEY"])

    print("Gerando bloco inferior via API...")
    response = client.images.generate(
        model="gpt-image-1",
        prompt=BOTTOM_PROMPT,
        size="1024x1024",
        quality="high",
        n=1,
    )
    raw = RUNS / "slide9-bottom-raw.png"
    raw.write_bytes(base64.b64decode(response.data[0].b64_json))
    print(f"Bloco inferior salvo: {raw}")
    return raw

# ── STEP 3: merge ────────────────────────────────────────────

def merge(header_bottom_y, bottom_raw):
    slide = Image.new("RGB", (W, H), WHITE)
    draw_header(slide)

    # Redimensiona o bloco inferior para ocupar o espaço restante
    available_h = H - header_bottom_y - 20   # 20px gap
    bottom = Image.open(bottom_raw).convert("RGB")
    bottom = bottom.resize((W, available_h), Image.LANCZOS)

    slide.paste(bottom, (0, header_bottom_y + 20))

    out = RUNS / "slide9-hybrid-FINAL.png"
    slide.save(out, quality=95)
    print(f"Slide 9 final: {out}")

# ── main ─────────────────────────────────────────────────────

if __name__ == "__main__":
    # Medir onde o header termina
    tmp = Image.new("RGB", (W, H), WHITE)
    header_bottom_y = draw_header(tmp)

    bottom_raw = generate_bottom()
    merge(header_bottom_y, bottom_raw)
