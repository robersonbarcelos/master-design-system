"""
fix_header.py
Sobrescreve o header do slide com renderização pixel-a-pixel via Pillow.
Corrige o problema do gpt-image que renderiza o texto centralizado em vez de alinhado à direita do avatar.

Layout do template (TEMPLATE-SLIDE-TWITTER-POST.json):
  Avatar:       64px circle, x=44, y=32
  Texto nome:   26px semibold, x=avatar_right+16=124, vertically centered with avatar
  Badge verif:  20px circle #1D9BF0, inline após o nome
  Handle:       22px regular #888888, x=124, abaixo do nome
"""

import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BASE_DIR   = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub")
RAW_PATH   = BASE_DIR / "runs" / "2026-08-18" / "slide-twitter-defi-05-raw.png"
AVT_PATH   = BASE_DIR / "assets" / "avatar-diego.jpeg"
OUT_PATH   = BASE_DIR / "runs" / "2026-08-18" / "slide-twitter-defi-05-v3.png"

# Coordenadas do template
AV_X, AV_Y, AV_SIZE = 44, 32, 64   # avatar top-left + diâmetro
TEXT_X     = AV_X + AV_SIZE + 16    # 124px
HEADER_H   = 185                    # altura da área que será limpa (px)

# Fontes do Windows
FONT_BOLD  = r"C:\Windows\Fonts\Arialbd.ttf"
FONT_REG   = r"C:\Windows\Fonts\Arial.ttf"
FONT_NAME_SZ   = 26
FONT_HANDLE_SZ = 22
BADGE_SIZE     = 20

# Cores
COLOR_NAME   = "#1A1A1A"
COLOR_HANDLE = "#888888"
COLOR_BADGE  = "#1D9BF0"
COLOR_WHITE  = "#FFFFFF"


def make_circle_avatar(img_path, size):
    img = Image.open(img_path).convert("RGBA")
    w, h = img.size
    m = min(w, h)
    img = img.crop(((w - m) // 2, (h - m) // 2, (w - m) // 2 + m, (h - m) // 2 + m))
    img = img.resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size, size), fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img, (0, 0))
    out.putalpha(mask)
    return out


def draw_verified_badge(draw, x, y, size, color):
    """Desenha badge de verificado: círculo preenchido + checkmark branco."""
    draw.ellipse((x, y, x + size, y + size), fill=color)
    # checkmark: dois segmentos de linha
    pad = size * 0.2
    cx, cy = x + size / 2, y + size / 2
    # ponto inicial do check (bottom-left da parte curta)
    p1 = (x + pad, cy + 1)
    p2 = (cx - 1, y + size - pad)       # ponto médio (base do check)
    p3 = (x + size - pad, y + pad + 1)  # ponto final (top-right)
    lw = max(2, int(size * 0.12))
    draw.line([p1, p2], fill=COLOR_WHITE, width=lw)
    draw.line([p2, p3], fill=COLOR_WHITE, width=lw)


def main():
    slide = Image.open(RAW_PATH).convert("RGBA")
    slide = slide.resize((1080, 1350), Image.LANCZOS)

    # 1. Limpar header — retângulo branco
    draw = ImageDraw.Draw(slide)
    draw.rectangle((0, 0, 1080, HEADER_H), fill=COLOR_WHITE)

    # 2. Fontes
    try:
        font_name   = ImageFont.truetype(FONT_BOLD, FONT_NAME_SZ)
        font_handle = ImageFont.truetype(FONT_REG,  FONT_HANDLE_SZ)
    except OSError:
        print("ERRO: Fontes Arial não encontradas. Usando fallback.")
        font_name   = ImageFont.load_default()
        font_handle = ImageFont.load_default()

    # 3. Calcular alturas das linhas para centralizar verticalmente com o avatar
    bbox_name   = font_name.getbbox("Diego Spanevello | Inteligência Artificial")
    bbox_handle = font_handle.getbbox("@diego.spanevello")
    name_h   = bbox_name[3] - bbox_name[1]
    handle_h = bbox_handle[3] - bbox_handle[1]
    gap      = 6  # px entre nome e handle

    # Centro vertical do avatar
    av_center_y = AV_Y + AV_SIZE // 2  # 32 + 32 = 64

    # Bloco de texto total: name_h + gap + handle_h
    total_text_h = name_h + gap + handle_h
    text_block_top = av_center_y - total_text_h // 2

    name_y   = text_block_top
    handle_y = text_block_top + name_h + gap

    # 4. Desenhar nome (sem o badge ainda, para medir largura)
    name_str = "Diego Spanevello | Inteligência Artificial"
    draw.text((TEXT_X, name_y), name_str, font=font_name, fill=COLOR_NAME)

    # 5. Badge verificado — inline após o nome
    name_w = bbox_name[2] - bbox_name[0]
    badge_x = TEXT_X + name_w + 8
    badge_y = name_y + (name_h - BADGE_SIZE) // 2  # centrado na linha do nome
    draw_verified_badge(draw, badge_x, badge_y, BADGE_SIZE, COLOR_BADGE)

    # 6. Handle
    draw.text((TEXT_X, handle_y), "@diego.spanevello", font=font_handle, fill=COLOR_HANDLE)

    # 7. Composite avatar (por cima — sobrescreve o retângulo branco)
    avatar = make_circle_avatar(AVT_PATH, AV_SIZE)
    slide.paste(avatar, (AV_X, AV_Y), avatar)

    # 8. Salvar
    slide.convert("RGB").save(OUT_PATH, quality=95)
    print(f"Salvo: {OUT_PATH}")


if __name__ == "__main__":
    main()
