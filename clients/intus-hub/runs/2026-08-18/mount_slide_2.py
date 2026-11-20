# -*- coding: utf-8 -*-
"""Monta o Slide 2 — Árbitro no ringue. Mesmos canonical params do Slide 1."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

BASE       = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub")
SCENE_PATH = BASE / "runs" / "2026-08-18" / "slide2-referee-raw.png"
AVT_PATH   = BASE / "assets" / "avatar-diego.jpeg"
OUT_PATH   = BASE / "runs" / "2026-08-18" / "slide2-referee-FINAL.png"

ARIAL_BLACK = r"C:\Windows\Fonts\Ariblk.ttf"
ARIAL_BOLD  = r"C:\Windows\Fonts\Arialbd.ttf"
ARIAL_REG   = r"C:\Windows\Fonts\Arial.ttf"

WHITE = (255, 255, 255)
BLACK = (10,  10,  10)
DARK  = (26,  26,  26)
GRAY  = (102, 102, 102)
LGRAY = (136, 136, 136)
BLUE  = (29,  155, 240)

W, H = 1080, 1350


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
    cx, cy_b = x + size/2, y + size/2
    p1 = (x+pad,      cy_b+1)
    p2 = (cx-1,       y+size-pad)
    p3 = (x+size-pad, y+pad+1)
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
    fn_name    = ImageFont.truetype(ARIAL_BOLD,  22)
    fn_handle  = ImageFont.truetype(ARIAL_REG,   18)
    fn_intro   = ImageFont.truetype(ARIAL_REG,   28)   # linha de contexto
    fn_key     = ImageFont.truetype(ARIAL_BLACK, 46)   # frases-chave em destaque
    fn_close   = ImageFont.truetype(ARIAL_REG,   26)   # frase de fechamento

    # ── HEADER — canonical ────────────────────────────────────
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

    # ── COPY — bloco de texto ─────────────────────────────────
    MARGIN = 64
    y = ay + avt_size + 50   # começa abaixo do header

    # Linha intro
    intro = "A diferença fundamental cabe em uma frase:"
    intro_w, intro_h = text_size(fn_intro, intro)
    draw.text(((W - intro_w) // 2, y), intro, font=fn_intro, fill=GRAY)
    y += intro_h + 32

    # Frase 1 — destaque
    line1 = "O prompt pede uma resposta."
    l1w, l1h = text_size(fn_key, line1)
    draw.text(((W - l1w) // 2, y), line1, font=fn_key, fill=BLACK)
    y += l1h + 14

    # Frase 2 — destaque
    line2 = "O agente persegue um objetivo."
    l2w, l2h = text_size(fn_key, line2)
    draw.text(((W - l2w) // 2, y), line2, font=fn_key, fill=BLACK)
    y += l2h + 32

    # Fechamento
    close = "Tudo que vem depois é consequência dessa distinção."
    cl_w, cl_h = text_size(fn_close, close)
    draw.text(((W - cl_w) // 2, y), close, font=fn_close, fill=GRAY)
    y += cl_h

    # ── IMAGEM — preenche do copy até o fundo ────────────────
    img_gap = 48
    img_bot = 40
    img_x   = MARGIN
    img_w   = W - 2 * MARGIN
    img_y   = y + img_gap
    img_h   = H - img_y - img_bot

    scene = Image.open(SCENE_PATH).convert("RGB")
    scene = scene.resize((img_w, img_h), Image.LANCZOS)

    radius = 16
    mask   = Image.new("L", (img_w, img_h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, img_w, img_h), radius=radius, fill=255)
    scene_rgba = scene.convert("RGBA")
    scene_rgba.putalpha(mask)
    slide.paste(scene_rgba, (img_x, img_y), scene_rgba)

    slide.save(OUT_PATH, quality=95)
    print(f"Slide 2 final: {OUT_PATH}")


if __name__ == "__main__":
    main()
