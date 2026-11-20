# -*- coding: utf-8 -*-
import subprocess, sys
from pathlib import Path

PROMPT = """Twitter/X style Instagram post slide, white background #FFFFFF, portrait 4:5.

HEADER (88px tall, top of slide):
  LEFT: solid light gray circle (#D8D8D8), 64x64px, at x=44 y=32. Profile photo placeholder.
  RIGHT of circle: "Diego Spanevello | Inteligência Artificial" bold 26px #1A1A1A + blue verified checkmark.
  Below name: "@diego.spanevello" regular 22px #888888.

CONTENT AREA — starts 60px below the header bottom, 80px from left and right edges:

  CONFRONTATION HEADLINE — two columns facing center, like a movie face-off poster:
    LEFT COLUMN — RIGHT-ALIGNED toward center (text pushes right, away from left edge):
      "Engenharia"  bold 34px #1A1A1A — right-aligned
      "de prompt"   extra-bold 52px #0a0a0a — right-aligned
    CENTER — exactly at horizontal midpoint of slide:
      "vs"  bold 38px #888888 — centered
    RIGHT COLUMN — LEFT-ALIGNED from center (text pushes right, toward right edge):
      "Engenharia"  bold 34px #1A1A1A — left-aligned
      "de agentes." extra-bold 52px #0a0a0a — left-aligned

  Both columns are vertically aligned on the same baseline.
  Minimum left margin for any text: 80px from left edge — no letter touches the left border.

  SUBTITLE — 32px below headline, left margin 80px:
    "Um resolve. O outro executa. Você sabe qual é qual?"
    regular 22px #666666

IMAGE SLOT — 40px below subtitle:
  Width: slide width minus 80px each side (total width = 920px).
  Height: 920 x 9/16 = 518px. Maintain strict 16:9 ratio.
  Border-radius: 14px.
  Bottom margin: 44px from bottom edge of slide.

  SCENE INSIDE THE IMAGE SLOT:
  Boxing match. Two fighters facing each other. Dramatic overhead spotlight.
  LEFT: humanoid figure made of cascading white paper sheets with code text — slim, red boxing gloves, aggressive stance, papers scattering.
  RIGHT: heavy industrial robot — dark metal, circuit boards, power cables, red boxing gloves, defensive stance.
  Black and white scene, only gloves and ring ropes in red. Cinematic high contrast.
  No text, no logos, no watermarks inside the image slot.

STRICT RULES:
- No text within 80px of left edge — left margin is mandatory
- Content starts 60px below header bottom
- Image slot is 920px wide, 518px tall, 16:9 strict
- NO dividers, NO footer
- Background #FFFFFF"""

OUT = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub\runs\2026-08-18\capa-a-boxing-v5-raw.png")

result = subprocess.run(
    ["gpt-image", "-p", PROMPT, "--size", "1088x1360", "--quality", "high", "-f", str(OUT)],
    capture_output=True, text=True, encoding="utf-8"
)
print(result.stdout)
if result.returncode != 0:
    print("ERRO:", result.stderr)
    sys.exit(1)
print(f"Salvo: {OUT}")
