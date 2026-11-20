# -*- coding: utf-8 -*-
"""Passo 1 — gera APENAS a cena das trading cards (sem texto, sem slide)."""
import subprocess, sys, os
from pathlib import Path

ENV = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\gpt-image2-skill\.env")
env_vars = {}
for line in ENV.read_text().splitlines():
    line = line.strip()
    if line and not line.startswith("#") and "=" in line:
        k, v = line.split("=", 1)
        env_vars[k.strip()] = v.strip()

env_copy = os.environ.copy()
env_copy["OPENAI_API_KEY"] = env_vars["OPENAI_API_KEY"]
env_copy["PATH"] = env_copy.get("PATH", "") + r";C:\Users\Pichau\AppData\Roaming\Python\Python314\Scripts"

PROMPT = """Two holographic Pokémon-style trading cards lying on a dark matte surface.
Dramatic overhead spotlight illuminating the cards from above.

LEFT CARD — "PROMPT": smaller card, basic design, warm golden-yellow holographic foil border.
Illustrated minimal robot character on the card face, simple geometric form, basic design aesthetic.
Muted warm holographic sheen — common card rarity.

RIGHT CARD — "AGENT": larger card, premium design, electric blue-purple holographic foil border.
Illustrated powerful evolved creature radiating multiple energy auras, glowing orbital rings around it,
dynamic power lines extending outward. Ultra rare card aesthetic — rainbow foil treatment.
Rainbow holographic light refraction across card surface.

Both cards tilted at slight angles, partially overlapping. Dark charcoal matte table surface.
Cinematic product photography style. Soft depth of field background.
Ultra-realistic render. No text, no logos, no watermarks. Widescreen 16:9."""

OUT = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub\runs\2026-08-18\pokemon-scene-raw.png")

result = subprocess.run(
    ["gpt-image", "-p", PROMPT, "--size", "1280x720", "--quality", "high", "-f", str(OUT)],
    capture_output=True, text=True, encoding="utf-8"
)
print(result.stdout)
if result.returncode != 0:
    print("ERRO:", result.stderr)
    sys.exit(1)
print(f"Cena salva: {OUT}")
