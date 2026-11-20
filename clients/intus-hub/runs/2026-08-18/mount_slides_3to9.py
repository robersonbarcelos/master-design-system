# -*- coding: utf-8 -*-
"""Monta os Slides 3-9 via Pillow. Canonical header params de todos os slides."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

BASE  = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub")
RUNS  = BASE / "runs" / "2026-08-18"
AVT   = BASE / "assets" / "avatar-diego.jpeg"

ARIAL_BLACK = r"C:\Windows\Fonts\Ariblk.ttf"
ARIAL_BOLD  = r"C:\Windows\Fonts\Arialbd.ttf"
ARIAL_REG   = r"C:\Windows\Fonts\Arial.ttf"

WHITE = (255, 255, 255)
BLACK = (10,  10,  10)
DARK  = (26,  26,  26)
GRAY  = (102, 102, 102)
LGRAY = (136, 136, 136)
BLUE  = (29,  155, 240)
W, H  = 1080, 1350


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
    p1 = (x+pad,      cy+1)
    p2 = (cx-1,       y+size-pad)
    p3 = (x+size-pad, y+pad+1)
    lw = max(2, int(size * 0.13))
    draw.line([p1, p2], fill=(255,255,255), width=lw)
    draw.line([p2, p3], fill=(255,255,255), width=lw)


def draw_header(slide, draw, fonts):
    avt_size = 125
    text_x   = 214
    cy_h     = 115
    ax       = text_x - 16 - avt_size
    ay       = cy_h - avt_size // 2

    name_str   = "Diego Spanevello | Inteligência Artificial"
    handle_str = "@diego.spanevello"

    nw, nh = text_size(fonts["name"],   name_str)
    hw, hh = text_size(fonts["handle"], handle_str)
    total_txt = nh + 6 + hh
    name_y    = cy_h - total_txt // 2
    handle_y  = name_y + nh + 6

    draw.text((text_x, name_y),   name_str,   font=fonts["name"],   fill=DARK)
    draw.text((text_x, handle_y), handle_str, font=fonts["handle"], fill=LGRAY)
    draw_badge(draw, text_x + nw + 6, name_y + (nh - 18) // 2, 18)

    avatar = make_circle_avatar(AVT, avt_size)
    slide.paste(avatar, (ax, ay), avatar)
    return ay + avt_size  # bottom of header


def paste_scene(slide, scene_path, y_start, margin=64, bottom_pad=40):
    img_w = W - 2 * margin
    img_h = H - y_start - bottom_pad
    img_h = max(img_h, 200)

    scene = Image.open(scene_path).convert("RGB")
    scene = scene.resize((img_w, img_h), Image.LANCZOS)

    mask = Image.new("L", (img_w, img_h), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, img_w, img_h), radius=16, fill=255)
    scene_rgba = scene.convert("RGBA")
    scene_rgba.putalpha(mask)
    slide.paste(scene_rgba, (margin, y_start), scene_rgba)


def build_slide(scene_file, out_file, header_text, body_lines, header_size=36, body_size=28):
    fn_name   = ImageFont.truetype(ARIAL_BOLD,  22)
    fn_handle = ImageFont.truetype(ARIAL_REG,   18)
    fn_head   = ImageFont.truetype(ARIAL_BLACK, header_size)
    fn_body   = ImageFont.truetype(ARIAL_REG,   body_size)

    slide = Image.new("RGB", (W, H), WHITE)
    draw  = ImageDraw.Draw(slide)

    fonts = {"name": fn_name, "handle": fn_handle}
    header_bottom = draw_header(slide, draw, fonts)

    MARGIN = 64
    y = header_bottom + 44

    # Header text (bold) — centralizado
    hw, hh = text_size(fn_head, header_text)
    if hw <= W - 2*MARGIN:
        draw.text(((W - hw) // 2, y), header_text, font=fn_head, fill=BLACK)
        y += hh + 20
    else:
        # quebra em 2 linhas no meio
        words = header_text.split()
        mid = len(words) // 2
        l1 = " ".join(words[:mid])
        l2 = " ".join(words[mid:])
        for line in [l1, l2]:
            lw, lh = text_size(fn_head, line)
            draw.text(((W - lw) // 2, y), line, font=fn_head, fill=BLACK)
            y += lh + 6
        y += 14

    # Body lines — centralizadas
    for line in body_lines:
        if line == "":
            y += body_size // 2
            continue
        bw, bh = text_size(fn_body, line)
        if bw <= W - 2*MARGIN:
            draw.text(((W - bw) // 2, y), line, font=fn_body, fill=GRAY)
            y += bh + 10
        else:
            # quebra em 2
            words = line.split()
            mid = len(words) // 2
            for part in [" ".join(words[:mid]), " ".join(words[mid:])]:
                pw, ph = text_size(fn_body, part)
                draw.text(((W - pw) // 2, y), part, font=fn_body, fill=GRAY)
                y += ph + 8

    y += 40  # gap antes da imagem

    scene_path = RUNS / scene_file
    if scene_path.exists():
        paste_scene(slide, scene_path, y)
    else:
        print(f"  AVISO: cena não encontrada — {scene_file}")

    slide.save(RUNS / out_file, quality=95)
    print(f"  Salvo: {out_file}")


SLIDES = [
    {
        "scene":  "slide3-impact-raw.png",
        "out":    "slide3-impact-FINAL.png",
        "header": "Prompt brilha quando a tarefa cabe em uma resposta.",
        "body": [
            "Redigir, resumir, traduzir, classificar.",
            "Você pede, o modelo responde, você refina.",
            "Sem execução no mundo real. Sem memória entre sessões.",
        ],
        "header_size": 34,
        "body_size":   26,
    },
    {
        "scene":  "slide4-marathon-raw.png",
        "out":    "slide4-marathon-FINAL.png",
        "header": "Agente faz sentido quando o gargalo é o passo manual.",
        "body": [
            "Pesquisa em várias fontes. Automação com etapas condicionais.",
            "Tarefas que exigem ler, agir e ajustar no meio do caminho.",
            "Se você conduz cada etapa manualmente, o agente é você.",
        ],
        "header_size": 32,
        "body_size":   26,
    },
    {
        "scene":  "slide5-ropes-raw.png",
        "out":    "slide5-ropes-FINAL.png",
        "header": "4 perguntas decidem qual você precisa.",
        "body": [
            "Complexidade, erro aceitável, latência, governança.",
            "Responda as 4 antes de construir qualquer coisa.",
        ],
        "header_size": 38,
        "body_size":   28,
    },
    {
        "scene":  "slide6-judges-raw.png",
        "out":    "slide6-judges-FINAL.png",
        "header": "As outras 3 perguntas importam tanto quanto.",
        "body": [
            "Qual o custo de uma ação errada?",
            "A resposta precisa ser imediata?",
            "O processo toca dados sensíveis?",
            "Quanto maior o impacto, mais validação humana.",
        ],
        "header_size": 36,
        "body_size":   26,
    },
    {
        "scene":  "slide7-warmup-raw.png",
        "out":    "slide7-warmup-FINAL.png",
        "header": "Comece sempre pelo prompt.",
        "body": [
            "Se a tarefa se resolve com uma boa instrução,",
            "você economiza tempo, dinheiro e risco.",
            "Só migre para agente quando o passo manual",
            "entre respostas virou o gargalo.",
        ],
        "header_size": 42,
        "body_size":   27,
    },
    {
        "scene":  "slide8-frequency-raw.png",
        "out":    "slide8-frequency-FINAL.png",
        "header": "A frequência muda tudo.",
        "body": [
            "Uma tarefa complexa uma vez por mês",
            "raramente compensa o esforço de um agente.",
            "A mesma tarefa 40 vezes por dia",
            "inverte completamente essa conta.",
        ],
        "header_size": 44,
        "body_size":   27,
    },
    {
        "scene":  "slide9-champion-raw.png",
        "out":    "slide9-champion-FINAL.png",
        "header": "Seu próximo passo não é escolher.",
        "body": [
            "É ter um agente com memória, ferramentas",
            "e identidade própria rodando enquanto você dorme.",
            "",
            "Isso é o Super Agente. R$87,95.",
            "Comenta Agente — eu te mando o link.",
        ],
        "header_size": 38,
        "body_size":   27,
    },
]

for s in SLIDES:
    print(f"Montando {s['out']}...")
    build_slide(
        scene_file=s["scene"],
        out_file=s["out"],
        header_text=s["header"],
        body_lines=s["body"],
        header_size=s["header_size"],
        body_size=s["body_size"],
    )

print("\nTodos os slides montados.")
