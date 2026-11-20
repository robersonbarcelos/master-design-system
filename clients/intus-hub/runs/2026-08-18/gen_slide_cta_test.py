# -*- coding: utf-8 -*-
"""Teste — gera o slide CTA (só tipografia) via GPT Image."""
import sys, base64
from pathlib import Path

ENV = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\gpt-image2-skill\.env")
env_vars = {}
for line in ENV.read_text().splitlines():
    line = line.strip()
    if line and not line.startswith("#") and "=" in line:
        k, v = line.split("=", 1)
        env_vars[k.strip()] = v.strip()

import openai
client = openai.OpenAI(api_key=env_vars["OPENAI_API_KEY"])

PROMPT = """Typography-only Instagram post slide, portrait 4:5, warm off-white background color #F7F5F1.
No images, no illustrations, no icons. Pure text layout, clean editorial design.

LAYOUT — all content vertically centered in the frame, 56px side margins:

LINE 1 — pre-headline label:
  Text: "SALVA ESSE CARROSSEL"
  Font: sans-serif regular, uppercase, 16px, letter-spacing 2px
  Color: #E8722A (burnt orange)
  Margin below: 16px

LINE 2 — main headline (takes 3 lines):
  Text: "Quem controla a infraestrutura, controla o mercado."
  Font: serif display italic (Fraunces style), 48px, entirely in italic
  Color: #1A1A1A
  Line-height: 1.1
  Margin below: 48px

LINE 3 — paragraph 1:
  Text: "Sempre foi assim nos negócios ao longo da história."
  Font: sans-serif regular, 22px
  Color: rgba(26,26,26,0.6) — medium gray
  Line-height: 1.5
  Margin below: 18px

LINE 4 — paragraph 2:
  Text: "Agora é a vez da IA."
  Font: sans-serif regular, 22px
  Color: medium gray same as above
  Margin below: 18px

LINE 5 — paragraph 3 CTA:
  Text: "Segue o perfil para mais análises assim toda semana.
Compartilha com quem precisa ficar sabendo."
  Font: sans-serif regular, 22px
  Color: medium gray same as above
  Line-height: 1.5

STRICT RULES:
- Background solid #F7F5F1 only — no gradients, no textures
- No header, no footer, no avatar, no images
- All text left-aligned, 56px from left edge
- Clean, minimal, editorial aesthetic
- No logos, no watermarks, no decorative elements"""

OUT = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub\runs\2026-08-18\slide-cta-gpt-test.png")

print("Gerando slide CTA via GPT Image...")
response = client.images.generate(
    model="gpt-image-1",
    prompt=PROMPT,
    size="1024x1536",
    quality="high",
    n=1,
)
img_b64 = response.data[0].b64_json
OUT.write_bytes(base64.b64decode(img_b64))
print(f"Salvo: {OUT}")
