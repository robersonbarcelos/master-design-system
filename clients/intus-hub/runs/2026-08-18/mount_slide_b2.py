# -*- coding: utf-8 -*-
"""
Passo 2 — monta o slide B2 (trading cards) via Pillow.
Mesmo canonical do mount_slide_a.py: avt_size=125, ax=73, ay=53, cy=115, text_x=214.
Headline grande — mesmo estilo tipográfico da Capa A.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

BASE       = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub")
SCENE_PATH = BASE / "runs" / "2026-08-18" / "pokemon-scene-raw.png"
AVT_PATH   = BASE / "assets" / "avatar-diego.jpeg"
OUT_PATH   = BASE / "runs" / "2026-08-18" / "capa-b2-pokemon-PILLOW-FINAL.png"

ARIAL_BLACK = r"C:\Windows\Fonts\Ariblk.ttf"
ARIAL_BOLD  = r"C:\Windows\Fonts\Arialbd.ttf"
ARIAL_REG   = r"C:\Windows\Fonts\Arial.ttf"

WHITE = (255, 255, 255)
BLACK = (10,  10,  10)
DARK  = (26,  26,  26)
GRAY  = (100, 100, 100)
LGRAY = (136, 136, 136)
BLUE  = (29,  155, 240)

W, H   = 1080, 1350
MARGIN = 64


def make_circle_avatar(path, size):
    img = Image.open(path).convert("RGBA")
    aw, ah = img.size
    m = min(aw, ah)
    img = img.crop(((aw-m)//2, (ah-m)//2, (aw-m)//2+m, (ah-m)//2+m))
    img = img.resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size, size), fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img, (0, 0)); out.putalpha(mask)
    return out


def draw_badge(draw, x, y, size):
    draw.ellipse((x, y, x+size, y+size), fill=BLUE)
    pad = size * 0.22
    cx, cy = x + size/2, y + size/2
    p1 = (x+pad,        cy+1)
    p2 = (cx-1,         y+size-pad)
    p3 = (x+size-pad,   y+pad+1)
    lw = max(2, int(size * 0.13))
    draw.line([p1, p2], fill=(255,255,255), width=lw)
    draw.line([p2, p3], fill=(255,255,255), width=lw)


def text_size(font, text):
    bb = font.getbbox(text)
    return bb[2]-bb[0], bb[3]-bb[1]


def main():
    slide = Image.new("RGB", (W, H), WHITE)
    draw  = ImageDraw.Draw(slide)

    # ── FONTS ────────────────────────────────────────────────
    fn_name   = ImageFont.truetype(ARIAL_BOLD,  22)
    fn_handle = ImageFont.truetype(ARIAL_REG,   18)
    fn_l1     = ImageFont.truetype(ARIAL_BOLD,  42)   # "Prompt e agente"
    fn_l2     = ImageFont.truetype(ARIAL_BLACK, 58)   # "não são a"
    fn_l3     = ImageFont.truetype(ARIAL_BLACK, 58)   # "mesma coisa."
    fn_sub    = ImageFont.truetype(ARIAL_REG,   23)   # subtítulo

    # ── HEADER — canonical params ─────────────────────────────
    avt_size = 125
    text_x   = 214
    cy       = 115
    ax       = text_x - 16 - avt_size   # 73
    ay       = cy - avt_size // 2        # 53

    name_str   = "Diego Spanevello | Inteligência Artificial"
    handle_str = "@diego.spanevello"

    nw, nh = text_size(fn_name,   name_str)
    hw, hh = text_size(fn_handle, handle_str)
    gap_txt   = 6
    total_txt = nh + gap_txt + hh
    name_y    = cy - total_txt // 2
    handle_y  = name_y + nh + gap_txt

    draw.text((text_x, name_y),   name_str,   font=fn_name,   fill=DARK)
    draw.text((text_x, handle_y), handle_str, font=fn_handle, fill=LGRAY)

    badge_sz = 18
    badge_x  = text_x + nw + 6
    badge_y  = name_y + (nh - badge_sz) // 2
    draw_badge(draw, badge_x, badge_y, badge_sz)

    avatar = make_circle_avatar(AVT_PATH, avt_size)
    slide.paste(avatar, (ax, ay), avatar)

    # ── HEADLINE — 3 linhas grandes ──────────────────────────
    y0 = ay + avt_size + 36

    l1 = "Prompt e agente"
    l2 = "não são a"
    l3 = "mesma coisa."

    l1w, l1h = text_size(fn_l1, l1)
    l2w, l2h = text_size(fn_l2, l2)
    l3w, l3h = text_size(fn_l3, l3)

    gap_lines = 4

    draw.text((MARGIN, y0),                            l1, font=fn_l1, fill=DARK)
    draw.text((MARGIN, y0 + l1h + gap_lines),          l2, font=fn_l2, fill=BLACK)
    draw.text((MARGIN, y0 + l1h + gap_lines + l2h + gap_lines), l3, font=fn_l3, fill=BLACK)

    y_after_headline = y0 + l1h + gap_lines + l2h + gap_lines + l3h + 24

    # ── SUBTÍTULO ────────────────────────────────────────────
    sub = "A maioria usa os dois errado. Aqui está a diferença."
    draw.text((MARGIN, y_after_headline), sub, font=fn_sub, fill=GRAY)
    _, sub_h = text_size(fn_sub, sub)

    # ── IMAGEM CARDS (slot 16:9) ─────────────────────────────
    img_m  = 44
    img_w  = W - 2 * img_m            # 992
    img_h  = round(img_w * 9 / 16)    # 558
    img_y  = H - img_h - 40
    img_x  = img_m

    scene = Image.open(SCENE_PATH).convert("RGB")
    scene = scene.resize((img_w, img_h), Image.LANCZOS)

    radius = 16
    mask   = Image.new("L", (img_w, img_h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, img_w, img_h), radius=radius, fill=255)
    scene_rgba = scene.convert("RGBA")
    scene_rgba.putalpha(mask)
    slide.paste(scene_rgba, (img_x, img_y), scene_rgba)

    slide.save(OUT_PATH, quality=95)
    print(f"Slide B2 final: {OUT_PATH}")


if __name__ == "__main__":
    main()
