#!/usr/bin/env python3
"""
Teste: geração de imagem via OpenAI (gpt-image-1 ou dall-e-3)
Saída canônica: 1080x1350px, proporção 4:5 (padrão todos os carrosseis)

Uso:
  python test_openai_image.py "seu prompt aqui"
  python test_openai_image.py --model dall-e-3 "seu prompt aqui"
  python test_openai_image.py --quality high "seu prompt aqui"

Saída: salva img_openai_test.png na pasta atual e abre no visualizador padrão.
"""

import sys
import os
import argparse
import base64
import io
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    print("ERRO: OPENAI_API_KEY não encontrada no .env")
    sys.exit(1)

try:
    from openai import OpenAI
except ImportError:
    print("ERRO: pacote openai não instalado. Rode: pip install openai")
    sys.exit(1)

try:
    from PIL import Image
except ImportError:
    print("ERRO: pacote Pillow não instalado. Rode: pip install Pillow")
    sys.exit(1)

# Dimensão canônica de todos os carrosseis — não alterar
TARGET_W = 1080
TARGET_H = 1350

# Tamanho de geração por modelo (o mais próximo de 4:5 disponível)
GENERATION_SIZE = {
    "gpt-image-1": "1024x1536",   # 2:3 → crop center para 4:5
    "dall-e-3":    "1024x1792",   # ~4:7 → crop center para 4:5
}


def crop_to_target(img_bytes: bytes) -> bytes:
    """Redimensiona e corta ao centro para exatamente 1080x1350 (4:5)."""
    img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    src_w, src_h = img.size

    # Scale: qual dimensão limita primeiro ao manter proporção alvo
    scale = max(TARGET_W / src_w, TARGET_H / src_h)
    new_w = int(src_w * scale)
    new_h = int(src_h * scale)
    img = img.resize((new_w, new_h), Image.LANCZOS)

    # Crop central
    left = (new_w - TARGET_W) // 2
    top  = (new_h - TARGET_H) // 2
    img  = img.crop((left, top, left + TARGET_W, top + TARGET_H))

    out = io.BytesIO()
    img.save(out, format="PNG", optimize=True)
    return out.getvalue()


def gerar_imagem(prompt: str, modelo: str, quality: str, output_path: Path) -> None:
    client = OpenAI(api_key=OPENAI_API_KEY)
    gen_size = GENERATION_SIZE[modelo]

    print(f"\nModelo       : {modelo}")
    print(f"Geração API  : {gen_size}")
    print(f"Saída final  : {TARGET_W}x{TARGET_H}px (4:5 canônico)")
    print(f"Quality      : {quality}")
    print(f"Prompt       : {prompt[:80]}{'...' if len(prompt) > 80 else ''}")
    print("\nGerando imagem...")

    kwargs = dict(
        model=modelo,
        prompt=prompt,
        n=1,
        size=gen_size,
        quality=quality,
    )

    if modelo == "dall-e-3":
        kwargs["response_format"] = "b64_json"

    response = client.images.generate(**kwargs)
    item = response.data[0]

    if hasattr(item, "b64_json") and item.b64_json:
        raw_bytes = base64.b64decode(item.b64_json)
    elif hasattr(item, "url") and item.url:
        import urllib.request
        with urllib.request.urlopen(item.url) as r:
            raw_bytes = r.read()
    else:
        print("ERRO: resposta sem imagem")
        sys.exit(1)

    print(f"Raw recebido : {len(raw_bytes):,} bytes")
    print("Redimensionando para 1080x1350...")

    final_bytes = crop_to_target(raw_bytes)
    output_path.write_bytes(final_bytes)

    print(f"Final        : {len(final_bytes):,} bytes")
    print(f"Salvo        : {output_path.resolve()}")

    if sys.platform == "win32":
        os.startfile(str(output_path.resolve()))


def main():
    parser = argparse.ArgumentParser(description="Teste de geração de imagem OpenAI — saída 1080x1350")
    parser.add_argument("prompt", help="Prompt de geração")
    parser.add_argument("--model", default="gpt-image-1",
                        choices=["gpt-image-1", "dall-e-3"])
    parser.add_argument("--quality", default="medium",
                        help="gpt-image-1: auto/low/medium/high | dall-e-3: standard/hd")
    parser.add_argument("--output", default="img_openai_test.png",
                        help="Nome do arquivo de saída")
    args = parser.parse_args()

    output_path = Path(__file__).parent / args.output
    gerar_imagem(args.prompt, args.model, args.quality, output_path)


if __name__ == "__main__":
    main()
