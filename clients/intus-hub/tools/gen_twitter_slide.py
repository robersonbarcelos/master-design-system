# -*- coding: utf-8 -*-
"""
gen_twitter_slide.py — CLI canônico para slides Twitter Post Intus Hub

Uso:
  python gen_twitter_slide.py --slide-num 2 --hook "Frase de abertura" --body "Linha 1\nLinha 2\nLinha 3" --scene C:/path/to/002.png

Flags:
  --slide-num   Número do slide (para naming de arquivos)
  --hook        Hook line (primeira linha, 52px/900)
  --body        Corpo do texto, linhas separadas por \n
  --scene       Caminho para a imagem de cena (PNG/JPG). Omitir para slides sem imagem
  --output-dir  Pasta de saída (padrão: runs/YYYY-MM-DD/ relativo ao clients/intus-hub)
  --skip-gen    Pular geração GPT, usar raw existente (só recomposta)
  --bold-red    Palavra/frase a deixar em bold vermelho #E53935 no body
"""
import os, sys, argparse, subprocess
from datetime import date
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw

# ─── CAMINHOS CANÔNICOS ────────────────────────────────────────────────────
BASE    = Path(__file__).resolve().parents[1]          # clients/intus-hub/
ENV     = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\gpt-image2-skill\.env")
GPT_EXE = r"C:\Users\Pichau\AppData\Roaming\Python\Python314\Scripts\gpt-image.exe"
AVT     = BASE / "assets" / "avatar-diego.jpeg"

AVT_X, AVT_Y, AVT_SIZE = 66, 61, 120


# ─── ENV ───────────────────────────────────────────────────────────────────
def load_env(path: Path) -> dict:
    env = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


# ─── PROMPT ────────────────────────────────────────────────────────────────
def build_prompt(hook: str, body: str, bold_red: str | None, with_image: bool) -> str:
    body_lines = body.replace("\\n", "\n")

    bold_note = ""
    if bold_red:
        bold_note = f'\n  NOTE: "{bold_red}" must appear in bold weight and color #E53935 (red). All other body text stays #1A1A1A.'

    image_slot = ""
    if with_image:
        image_slot = """
IMAGE PLACEHOLDER SLOT (directly below the last body line, 24px gap, 44px side margins, 44px bottom margin):
  A solid uniform light gray (#E0E0E0) filled rounded rectangle, 16:9 landscape proportions, border-radius 18px.
  The slot must start AFTER the last line of body text — never overlap text.
  Empty inside — no icons, no label text, no gradient.
"""

    return f"""Twitter/X style Instagram post slide, white background #FFFFFF, portrait 4:5.

HEADER (top, 88px tall, 44px from left edge, 32px from top):
  - LEFT: solid light gray circle (#D8D8D8), exactly 64x64px at position left=44px top=32px. No border.
  - RIGHT of circle (16px gap), two text lines left-aligned, vertically centered with the circle:
      Line 1: "Diego Spanevello | Inteligência Artificial" + blue verified checkmark inline — bold sans-serif 26px, color #1A1A1A
      Line 2: "@diego.spanevello" — regular sans-serif 22px, color #888888

CONTENT (below header, 44px left and right margins, 32px top margin):
  TWO DISTINCT TEXT SIZES:

  HOOK LINE (first line only) — ultra-heavy black/900 weight, 52px, left-aligned, color #1A1A1A, line-height 1.1:
  "{hook}"

  BODY TEXT (all remaining lines) — regular 400 weight, 28px, left-aligned, color #1A1A1A, line-height 1.4:
  "{body_lines}"
{bold_note}

  CRITICAL: hook line visually 2x heavier and larger than body. All text #1A1A1A unless noted above, no italic.
{image_slot}
STRICT RULES:
- NO separator lines, dividers, footer
- Background pure white #FFFFFF throughout
- Gray avatar circle exactly 64x64px at left=44 top=32
- Image slot is landscape 16:9, never square, never portrait
""".strip()


# ─── GPT GENERATE ──────────────────────────────────────────────────────────
def generate(prompt: str, raw_path: Path) -> None:
    env_vars = load_env(ENV)
    env_copy = os.environ.copy()
    env_copy["OPENAI_API_KEY"] = env_vars["OPENAI_API_KEY"]
    cmd = [GPT_EXE, "-p", prompt, "--size", "1088x1360", "--quality", "high", "-f", str(raw_path)]
    print(f"[GPT] Gerando → {raw_path.name} ...")
    result = subprocess.run(cmd, env=env_copy, capture_output=True, text=True)
    if result.returncode != 0:
        print("ERRO GPT:", result.stderr)
        sys.exit(1)
    print(f"[GPT] Raw salvo: {raw_path}")


# ─── AVATAR ────────────────────────────────────────────────────────────────
def make_circle_avatar(img_path: Path, size: int) -> Image.Image:
    img = Image.open(img_path).convert("RGBA")
    aw, ah = img.size
    m = min(aw, ah)
    img = img.crop(((aw - m) // 2, (ah - m) // 2, (aw - m) // 2 + m, (ah - m) // 2 + m))
    img = img.resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size - 1, size - 1), fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img, (0, 0))
    out.putalpha(mask)
    return out


# ─── SLOT DETECTION ────────────────────────────────────────────────────────
def detect_slot(img_rgb: Image.Image, min_width_ratio: float = 0.5, search_from_y: int = 400):
    """
    Detecta o placeholder cinza ignorando texto estreito.
    Critério: linha com >= 50% de pixels cinzas uniformes a partir de y=400.
    @handle (~200px) não passa. Slot (~992px) passa.
    Fallback ancorado no fundo quando nenhuma linha larga for encontrada.
    """
    arr = np.array(img_rgb)
    h, w = arr.shape[:2]
    R = arr[:, :, 0].astype(int)
    G = arr[:, :, 1].astype(int)
    B = arr[:, :, 2].astype(int)
    gray_mask = (
        (np.abs(R - G) < 15) & (np.abs(R - B) < 15) & (np.abs(G - B) < 15)
        & (R > 150) & (R < 235)
    )
    min_cols = int(w * min_width_ratio)
    slot_rows = [y for y in range(search_from_y, h) if gray_mask[y].sum() >= min_cols]
    if not slot_rows:
        sw = w - 88
        sh = int(sw * 9 / 16)
        sx = 44
        sy = h - sh - 44
        print(f"[slot] fallback → x={sx}, y={sy}, w={sw}, h={sh}")
        return sx, sy, sw, sh
    y0, y1 = slot_rows[0], slot_rows[-1]
    cols = np.where(gray_mask[y0:y1 + 1].any(axis=0))[0]
    x0, x1 = int(cols[0]), int(cols[-1])
    print(f"[slot] detectado → x={x0}, y={y0}, w={x1 - x0}, h={y1 - y0}")
    return x0, y0, x1 - x0, y1 - y0


# ─── SCENE COMPOSITE ───────────────────────────────────────────────────────
def composite_scene(slide_rgba: Image.Image, scene_path: Path,
                    sx: int, sy: int, sw: int, sh: int, radius: int = 18) -> None:
    scene = Image.open(scene_path).convert("RGB").resize((sw, sh), Image.LANCZOS)
    mask = Image.new("L", (sw, sh), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, sw, sh), radius=radius, fill=255)
    scene_rgba = scene.convert("RGBA")
    scene_rgba.putalpha(mask)
    slide_rgba.paste(scene_rgba, (sx, sy), scene_rgba)


# ─── COMPOSITE FINAL ───────────────────────────────────────────────────────
def composite(raw_path: Path, out_path: Path, scene_path: Path | None) -> None:
    slide = Image.open(raw_path).convert("RGBA").resize((1080, 1350), Image.LANCZOS)
    draw = ImageDraw.Draw(slide)

    # Avatar: apagar cinza do GPT (+30 embaixo — GPT gera ligeiramente maior que 120px)
    draw.rectangle(
        (AVT_X - 10, AVT_Y - 10, AVT_X + AVT_SIZE + 10, AVT_Y + AVT_SIZE + 30),
        fill=(255, 255, 255, 255)
    )
    avatar = make_circle_avatar(AVT, AVT_SIZE)
    slide.paste(avatar, (AVT_X, AVT_Y), avatar)

    # Scene (apenas se foi fornecida)
    if scene_path is not None:
        sx, sy, sw, sh = detect_slot(slide.convert("RGB"))
        composite_scene(slide, scene_path, sx, sy, sw, sh)

    slide.convert("RGB").save(out_path, quality=95)
    print(f"[ok] Final: {out_path}")


# ─── MAIN ──────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Gera slide Twitter Post para Intus Hub")
    parser.add_argument("--slide-num", required=True, help="Número do slide (ex: 2, 07)")
    parser.add_argument("--hook", required=True, help="Hook line (primeira linha, 52px/900)")
    parser.add_argument("--body", required=True,
                        help="Corpo do texto. Usar \\n para quebras de linha.")
    parser.add_argument("--scene", default=None,
                        help="Caminho da imagem de cena. Omitir para slide sem imagem.")
    parser.add_argument("--output-dir", default=None,
                        help="Pasta de saída. Padrão: clients/intus-hub/runs/YYYY-MM-DD/")
    parser.add_argument("--skip-gen", action="store_true",
                        help="Pular geração GPT — usar raw existente, só recomposta")
    parser.add_argument("--bold-red", default=None,
                        help="Palavra ou frase a aparecer em bold vermelho #E53935 no body")
    args = parser.parse_args()

    # Pasta de saída
    if args.output_dir:
        out_dir = Path(args.output_dir)
    else:
        out_dir = BASE / "runs" / date.today().isoformat()
    out_dir.mkdir(parents=True, exist_ok=True)

    slide_num = str(args.slide_num).zfill(2)
    raw_path = out_dir / f"slide{slide_num}-raw.png"
    out_path = out_dir / f"slide{slide_num}-FINAL.png"
    scene_path = Path(args.scene) if args.scene else None

    with_image = scene_path is not None
    prompt = build_prompt(args.hook, args.body, args.bold_red, with_image)

    if not args.skip_gen:
        generate(prompt, raw_path)
    else:
        if not raw_path.exists():
            print(f"ERRO: --skip-gen ativo mas raw não existe: {raw_path}")
            sys.exit(1)
        print(f"[skip-gen] Usando raw existente: {raw_path}")

    composite(raw_path, out_path, scene_path)


if __name__ == "__main__":
    main()
