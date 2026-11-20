# -*- coding: utf-8 -*-
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

PROMPT = """Low angle camera shot from inside a professional boxing ring, looking upward toward the arena lights.
EXACTLY FOUR horizontal ropes visible — four distinct parallel ropes stacked vertically, evenly spaced.
The four ropes run diagonally across the entire frame from left to right in forced perspective.
Each rope is thick, red, clearly separated from the others — count must be exactly 4.
Arena floodlights glow behind and between the ropes creating dramatic lens flare.
Black and white photography — ONLY the four ropes in vivid red, everything else monochrome.
Ring canvas visible at bottom edge. Empty ring, no fighters, no people.
Cinematic, high contrast, architectural composition. No text, no logos. Widescreen 16:9."""

OUT = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub\runs\2026-08-18\slide5-ropes-raw.png")

print("Gerando cena com 4 cordas...")
response = client.images.generate(
    model="gpt-image-1",
    prompt=PROMPT,
    size="1536x1024",
    quality="high",
    n=1,
)
OUT.write_bytes(base64.b64decode(response.data[0].b64_json))
print(f"Salvo: {OUT}")
