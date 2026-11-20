# -*- coding: utf-8 -*-
"""
Passo 2 — monta o slide completo via Pillow.
Texto 100% controlado: sem corte, com acentos, tipografia real.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

BASE       = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub")
SCENE_PATH = BASE / "runs" / "2026-08-18" / "boxing-scene-raw.png"
AVT_PATH   = BASE / "assets" / "avatar-diego.jpeg"
OUT_PATH   = BASE / "runs" / "2026-08-18" / "capa-a-boxing-PILLOW-FINAL.png"

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
    fn_eng    = ImageFont.truetype(ARIAL_BOLD,  36)   # "Engenharia"
    fn_term   = ImageFont.truetype(ARIAL_BLACK, 58)   # "de prompt" / "de agentes."
    fn_vs     = ImageFont.truetype(ARIAL_BOLD,  40)   # "vs"
    fn_sub    = ImageFont.truetype(ARIAL_BOLD,  30)   # subtítulo

    # ── HEADER ───────────────────────────────────────────────
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

    # ── HEADLINE — duas colunas ───────────────────────────────
    y0 = ay + avt_size + 40   # início do bloco de headline

    eng_w,  eng_h  = text_size(fn_eng,  "Engenharia")
    prm_w,  prm_h  = text_size(fn_term, "de prompt")
    agt_w,  agt_h  = text_size(fn_term, "de agentes.")
    vs_w,   vs_h   = text_size(fn_vs,   "vs")

    left_col_w  = max(eng_w, prm_w)
    right_col_w = max(eng_w, agt_w)
    col_gap     = 24

    total_w = left_col_w + col_gap + vs_w + col_gap + right_col_w
    avail_w = W - 2 * MARGIN
    offset  = MARGIN + max(0, (avail_w - total_w) // 2)

    lx = offset
    vx = offset + left_col_w + col_gap
    rx = vx + vs_w + col_gap

    row1_h  = eng_h
    row2_h  = max(prm_h, agt_h)
    row_gap = 2
    block_h = row1_h + row_gap + row2_h

    vy = y0 + (block_h - vs_h) // 2

    # Coluna esquerda — alinhada à direita dentro de left_col_w
    draw.text((lx + (left_col_w - eng_w), y0),                  "Engenharia",  font=fn_eng,  fill=DARK)
    draw.text((lx + (left_col_w - prm_w), y0 + row1_h + row_gap), "de prompt",   font=fn_term, fill=BLACK)

    # vs centralizado
    draw.text((vx, vy), "vs", font=fn_vs, fill=GRAY)

    # Coluna direita — alinhada à esquerda
    draw.text((rx, y0),                    "Engenharia",   font=fn_eng,  fill=DARK)
    draw.text((rx, y0 + row1_h + row_gap), "de agentes.",  font=fn_term, fill=BLACK)

    y_after = y0 + block_h + 28

    # ── SUBTÍTULO — centralizado ─────────────────────────────
    sub = "Um resolve. O outro executa. Você sabe qual é qual?"
    sub_w, sub_h = text_size(fn_sub, sub)
    sub_x = (W - sub_w) // 2
    draw.text((sub_x, y_after), sub, font=fn_sub, fill=GRAY)

    # ── IMAGEM BOXING — preenche do subtitle até o fundo ────────
    img_m  = 44
    img_gap = 48                        # gap entre subtitle e imagem
    img_bot = 40                        # margem inferior
    img_x  = img_m
    img_w  = W - 2 * img_m            # 992
    img_y  = y_after + sub_h + img_gap
    img_h  = H - img_y - img_bot       # preenche restante

    scene = Image.open(SCENE_PATH).convert("RGB")
    scene = scene.resize((img_w, img_h), Image.LANCZOS)

    radius = 16
    mask   = Image.new("L", (img_w, img_h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, img_w, img_h), radius=radius, fill=255)
    scene_rgba = scene.convert("RGBA")
    scene_rgba.putalpha(mask)
    slide.paste(scene_rgba, (img_x, img_y), scene_rgba)

    slide.save(OUT_PATH, quality=95)
    print(f"Slide final: {OUT_PATH}")


if __name__ == "__main__":
    main()
