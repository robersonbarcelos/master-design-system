# -*- coding: utf-8 -*-
"""Teste: slide 9 inteiro via GPT Image (texto + cena), depois composite do avatar."""
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

PROMPT = """Twitter/X style Instagram post slide, white background #FFFFFF, portrait 4:5.

HEADER (88px tall):
  LEFT: solid light gray circle (#D8D8D8), 64x64px, at x=44 y=32. Profile photo placeholder.
  RIGHT: "Diego Spanevello | Inteligência Artificial" bold 22px #1A1A1A + blue verified checkmark.
  Below: "@diego.spanevello" regular 18px #888888.

CONTENT — centered, below header, 64px side margins:

  Line 1 — headline: "Seu próximo passo não é escolher."
  Font: Arial Black, 38px, color #0A0A0A, centered.

  Line 2: "É ter um agente com memória, ferramentas"
  Font: Arial regular, 27px, color #666666, centered.

  Line 3: "e identidade própria rodando enquanto você dorme."
  Font: Arial regular, 27px, color #666666, centered.

  [blank line space]

  Line 4 — MIXED STYLE, centered:
    "Isso é o Super " — Arial regular 27px #666666
    "AGENTE" — Arial Black 27px #0A0A0A (bold, uppercase, visually heavier)
    ". " — Arial regular 27px #666666
    "R$87,95" — Arial Black 27px #E6641E (orange color)
    "." — Arial regular 27px #666666

  Line 5 — MIXED STYLE, centered:
    "Comenta " — Arial regular 27px #666666
    "AGENTE" — Arial Black 27px #0A0A0A (bold, uppercase)
    " — eu te mando o link." — Arial regular 27px #666666

IMAGE SLOT — 40px below last text line, 64px side margins, fills to 40px from bottom:
  Heavy industrial robot with dark metallic body, circuit boards, power cables.
  Robot standing triumphant in boxing ring center, holding championship belt with BOTH HANDS raised high.
  Team celebrating around robot. Confetti falling from above.
  Black and white — only red corner ropes, red boxing gloves, championship belt details in color.
  Cinematic dramatic arena lighting. No text, no logos inside the image slot.
  Border-radius: 16px.

STRICT RULES:
- Background pure white #FFFFFF
- Gray circle MUST be solid 64x64px at x=44 y=32
- All text centered horizontally
- NO dividers, NO footer"""

OUT = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub\runs\2026-08-18\slide9-api-full-raw.png")

print("Gerando slide 9 completo via API...")
response = client.images.generate(
    model="gpt-image-1",
    prompt=PROMPT,
    size="1024x1536",
    quality="high",
    n=1,
)
OUT.write_bytes(base64.b64decode(response.data[0].b64_json))
print(f"Raw salvo: {OUT}")
