# -*- coding: utf-8 -*-
"""Gera a cena do Slide 2 — Árbitro no ringue via OpenAI API."""
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

PROMPT = """Boxing referee standing dead center of a professional boxing ring, seen from behind.
Classic black and white referee uniform — long-sleeved white shirt, black bow tie, black trousers.
Both arms stretched wide, separating the two fighters.

LEFT FIGHTER (blurred, soft focus): humanoid figure made entirely of cascading white paper sheets and printed code pages, red boxing gloves.
RIGHT FIGHTER (blurred, soft focus): heavy industrial robot with dark metallic body, visible circuit boards, power cables, red boxing gloves.

Referee is the sharp focal point at center. Both fighters are out of focus, flanking him.
Dramatic single overhead arena spotlight from directly above, casting strong shadow downward.
Black and white photograph aesthetic — only the corner ropes and boxing gloves in red are in color.
Cinematic, high contrast, editorial sports photography.
No text, no logos, no watermarks. Widescreen 16:9."""

OUT = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub\runs\2026-08-18\slide2-referee-raw.png")

print("Gerando cena via OpenAI API...")
response = client.images.generate(
    model="gpt-image-1",
    prompt=PROMPT,
    size="1536x1024",
    quality="high",
    n=1,
)
img_b64 = response.data[0].b64_json
OUT.write_bytes(base64.b64decode(img_b64))
print(f"Cena salva: {OUT}")
