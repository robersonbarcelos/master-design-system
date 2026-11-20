# -*- coding: utf-8 -*-
"""Monta Slide 9 com AGENTE em bold+caixa alta e R$87,95 em laranja."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

BASE  = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub")
RUNS  = BASE / "runs" / "2026-08-18"
AVT   = BASE / "assets" / "avatar-diego.jpeg"
OUT   = RUNS / "slide9-champion-FINAL.png"

ARIAL_BLACK = r"C:\Windows\Fonts\Ariblk.ttf"
ARIAL_BOLD  = r"C:\Windows\Fonts\Arialbd.ttf"
ARIAL_REG   = r"C:\Windows\Fonts\Arial.ttf"

WHITE  = (255, 255, 255)
BLACK  = (10,  10,  10)
DARK   = (26,  26,  26)
GRAY   = (102, 102, 102)
LGRAY  = (136, 136, 136)
BLUE   = (29,  155, 240)
ORANGE = (230, 100, 20)
W, H   = 1080, 1350


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
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img, (0, 0)); out.putalpha(mask)
    return out


def draw_badge(draw, x, y, size):
    draw.ellipse((x, y, x+size, y+size), fill=BLUE)
    pad = size * 0.22
    cx, cy = x + size/2, y + size/2
    p1 = (x+pad,      cy+1);  p2 = (cx-1, y+size-pad);  p3 = (x+size-pad, y+pad+1)
    lw = max(2, int(size * 0.13))
    draw.line([p1, p2], fill=(255,255,255), width=lw)
    draw.line([p2, p3], fill=(255,255,255), width=lw)


def draw_inline(slide, draw, segments, y, fonts, center_w=W):
    """Desenha linha com estilo misto centralizada corretamente:
    1. Centra a string completa em body font (idêntico às linhas simples)
    2. Percorre segmentos calculando x por getlength
    3. Sobrescreve palavras destacadas com bold/cor"""
    full_text = "".join(s["text"] for s in segments)
    full_w, full_h = text_size(fonts["body"], full_text)
    x_start = (center_w - full_w) // 2

    x = x_start
    for seg in segments:
        font  = fonts[seg["font"]]
        color = seg.get("color", GRAY)
        draw.text((x, y), seg["text"], font=font, fill=color)
        x += int(fonts["body"].getlength(seg["text"]))  # avança pelo body para consistência
    return full_h


def main():
    fn_name   = ImageFont.truetype(ARIAL_BOLD,  22)
    fn_handle = ImageFont.truetype(ARIAL_REG,   18)
    fn_head   = ImageFont.truetype(ARIAL_BLACK, 38)
    fn_body   = ImageFont.truetype(ARIAL_REG,   27)
    fn_bold   = ImageFont.truetype(ARIAL_BLACK, 27)

    fonts = {"name": fn_name, "handle": fn_handle,
             "body": fn_body, "bold": fn_bold, "head": fn_head}

    slide = Image.new("RGB", (W, H), WHITE)
    draw  = ImageDraw.Draw(slide)

    # ── HEADER canonical ─────────────────────────────────────
    avt_size = 125; text_x = 214; cy_h = 115
    ax = text_x - 16 - avt_size; ay = cy_h - avt_size // 2

    nw, nh = text_size(fn_name,   "Diego Spanevello | Inteligência Artificial")
    hw, hh = text_size(fn_handle, "@diego.spanevello")
    name_y   = cy_h - (nh + 6 + hh) // 2
    handle_y = name_y + nh + 6

    draw.text((text_x, name_y),   "Diego Spanevello | Inteligência Artificial", font=fn_name,   fill=DARK)
    draw.text((text_x, handle_y), "@diego.spanevello",                          font=fn_handle, fill=LGRAY)
    draw_badge(draw, text_x + nw + 6, name_y + (nh - 18) // 2, 18)
    slide.paste(make_circle_avatar(AVT, avt_size), (ax, ay), make_circle_avatar(AVT, avt_size))

    # ── COPY ────────────────────────────────────────────────
    y = ay + avt_size + 44

    # Headline
    head = "Seu próximo passo não é escolher."
    hw2, hh2 = text_size(fn_head, head)
    draw.text(((W - hw2) // 2, y), head, font=fn_head, fill=BLACK)
    y += hh2 + 18

    # Linhas simples
    simple = [
        "É ter um agente com memória, ferramentas",
        "e identidade própria rodando enquanto você dorme.",
    ]
    for line in simple:
        lw, lh = text_size(fn_body, line)
        draw.text(((W - lw) // 2, y), line, font=fn_body, fill=GRAY)
        y += lh + 8

    y += 20  # espaço extra

    # "Isso é o Super AGENTE. R$87,95."
    h1 = draw_inline(slide, draw, [
        {"font": "body", "text": "Isso é o Super ", "color": GRAY},
        {"font": "bold", "text": "AGENTE",          "color": BLACK},
        {"font": "body", "text": ". ",               "color": GRAY},
        {"font": "bold", "text": "R$87,95",          "color": ORANGE},
        {"font": "body", "text": ".",                "color": GRAY},
    ], y, fonts)
    y += h1 + 10

    # "Comenta AGENTE — eu te mando o link."
    h2 = draw_inline(slide, draw, [
        {"font": "body", "text": "Comenta ",                  "color": GRAY},
        {"font": "bold", "text": "AGENTE",                    "color": BLACK},
        {"font": "body", "text": " — eu te mando o link.",    "color": GRAY},
    ], y, fonts)
    y += h2 + 44

    # ── CENA ────────────────────────────────────────────────
    MARGIN = 64; BOT = 40
    scene_path = RUNS / "slide9-champion-raw.png"
    img_w = W - 2*MARGIN
    img_h = H - y - BOT

    scene = Image.open(scene_path).convert("RGB")
    scene = scene.resize((img_w, img_h), Image.LANCZOS)
    mask  = Image.new("L", (img_w, img_h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, img_w, img_h), radius=16, fill=255)
    sr = scene.convert("RGBA"); sr.putalpha(mask)
    slide.paste(sr, (MARGIN, y), sr)

    slide.save(OUT, quality=95)
    print(f"Slide 9 final: {OUT}")


if __name__ == "__main__":
    main()
