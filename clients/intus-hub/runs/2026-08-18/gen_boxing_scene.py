# -*- coding: utf-8 -*-
"""Passo 1 — gera APENAS a cena do boxing (sem texto, sem slide)."""
import subprocess, sys
from pathlib import Path

PROMPT = """Boxing match scene inside a professional boxing ring.
Two fighters facing each other, dramatic overhead spotlight from above center.

LEFT FIGHTER — PROMPT: humanoid figure made entirely of cascading white paper sheets
and printed code pages. Slim lightweight silhouette. Body composed of floating text pages
with monospace code text visible across surface. Red boxing gloves. Aggressive
forward-leaning fighting stance. Loose papers scattering behind the figure.

RIGHT FIGHTER — AGENT: heavy industrial robot. Dark metallic body with visible circuit
boards, power cables connecting joints, hydraulic arms, multiple sensor nodes and
mechanical components. Imposing massive physique. Red boxing gloves. Solid
defensive fighting stance.

Red corner ropes and ring posts visible on left and right sides.
Black and white photorealistic scene — only the boxing gloves and ring ropes in red.
Dramatic single overhead spotlight beam creating strong shadows.
Cinematic tension between the two figures. Audience blurred in background.
Style: cinematic graphic illustration, high contrast, Batman vs Superman face-off
poster aesthetic. Ultra-realistic render.
No text, no logos, no watermarks. Widescreen 16:9."""

OUT = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub\runs\2026-08-18\boxing-scene-raw.png")

result = subprocess.run(
    ["gpt-image", "-p", PROMPT, "--size", "1280x720", "--quality", "high", "-f", str(OUT)],
    capture_output=True, text=True, encoding="utf-8"
)
print(result.stdout)
if result.returncode != 0:
    print("ERRO:", result.stderr)
    sys.exit(1)
print(f"Cena salva: {OUT}")
