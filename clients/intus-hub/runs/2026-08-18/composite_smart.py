# -*- coding: utf-8 -*-
"""
composite_smart.py
Detecta dinamicamente a posição do círculo cinza e o início do texto
para posicionar o avatar sem cobrir letras — funciona para qualquer slide.
"""
import sys
import numpy as np
from PIL import Image, ImageDraw
from pathlib import Path

RAW_PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else None
OUT_PATH = Path(sys.argv[2]) if len(sys.argv) > 2 else None

if not RAW_PATH or not OUT_PATH:
    print("Uso: python composite_smart.py <raw.png> <out.png>")
    sys.exit(1)

BASE = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub")
AVT  = BASE / "assets" / "avatar-diego.jpeg"


def detect_circle_and_text(img_rgb):
    """Detecta círculo cinza e início do texto no header."""
    arr    = np.array(img_rgb)
    header = arr[:220, :, :]

    R, G, B = header[:,:,0].astype(int), header[:,:,1].astype(int), header[:,:,2].astype(int)
    gray_mask = (
        (np.abs(R-G) < 20) & (np.abs(R-B) < 20) & (np.abs(G-B) < 20) &
        (R > 130) & (R < 235)
    )
    # Limitar busca ao lado esquerdo (x < 280)
    gray_mask[:, 280:] = False

    rows = np.where(gray_mask.any(axis=1))[0]
    cols = np.where(gray_mask.any(axis=0))[0]

    if len(rows) == 0 or len(cols) == 0:
        print("Círculo não detectado — usando fallback ax=73, ay=53, size=125")
        return 73, 53, 125, 214

    ay = int(rows[0])
    ax = int(cols[0])
    cx_right = int(cols[-1])
    avt_size = int(rows[-1]) - ay
    avt_size = max(80, min(avt_size, 180))  # sanidade
    cy       = ay + avt_size // 2

    # Detectar onde o texto começa: varrer à direita do círculo na altura do centro
    text_x = cx_right + 8  # fallback mínimo
    scan_row = arr[cy, cx_right+4:cx_right+120, :]
    for i, px in enumerate(scan_row):
        if int(px[0]) < 60 and int(px[1]) < 60 and int(px[2]) < 60:
            text_x = cx_right + 4 + i
            break

    # Avatar sempre 125px — só a POSIÇÃO muda entre slides
    AVT_SIZE_CANONICAL = 125
    # Recentrar o avatar de 125px no centro do círculo detectado
    circle_cx = ax + avt_size // 2
    circle_cy = cy
    ax_final  = circle_cx - AVT_SIZE_CANONICAL // 2
    ay_final  = circle_cy - AVT_SIZE_CANONICAL // 2

    print(f"Círculo detectado: cx={circle_cx} cy={circle_cy} size={avt_size}")
    print(f"Avatar 125px posicionado em: ax={ax_final} ay={ay_final} text_x={text_x}")
    return ax_final, ay_final, AVT_SIZE_CANONICAL, text_x


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


def main():
    slide = Image.open(RAW_PATH).convert("RGBA")
    slide = slide.resize((1080, 1350), Image.LANCZOS)
    draw  = ImageDraw.Draw(slide)

    ax, ay, avt_size, text_x = detect_circle_and_text(slide.convert("RGB"))
    gap = 8  # gap mínimo de segurança entre avatar e texto

    # Cleanup cirúrgico — nunca passa de text_x
    draw.rectangle((0,  0,               text_x - gap, ay),              fill='#FFFFFF')  # acima
    draw.rectangle((0,  ay,              ax,            ay + avt_size),   fill='#FFFFFF')  # esquerda
    draw.rectangle((0,  ay + avt_size,   text_x - gap, ay + avt_size + 80), fill='#FFFFFF')  # abaixo
    draw.rectangle((ax + avt_size, ay,   text_x - gap, ay + avt_size),   fill='#FFFFFF')  # gap
    draw.rectangle((ax, ay,              ax + avt_size, ay + avt_size),   fill='#FFFFFF')  # bbox

    avatar = make_circle_avatar(AVT, avt_size)
    slide.paste(avatar, (ax, ay), avatar)

    slide.convert("RGB").save(OUT_PATH, quality=95)
    print(f"Salvo: {OUT_PATH}")


if __name__ == "__main__":
    main()
