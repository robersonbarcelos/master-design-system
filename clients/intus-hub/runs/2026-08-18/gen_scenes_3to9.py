# -*- coding: utf-8 -*-
"""Gera as cenas dos Slides 3-9 via OpenAI API. Mantém os personagens aprovados."""
import sys, base64, time
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

RUNS = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub\runs\2026-08-18")

# Personagens canônicos aprovados na Capa A:
PAPER_MAN = "humanoid figure made entirely of cascading white paper sheets and printed code pages, red boxing gloves"
ROBOT     = "heavy industrial robot with dark metallic body, visible circuit boards, power cables and hydraulic arms, red boxing gloves"

SCENES = {
    "slide3-impact": {
        "file": "slide3-impact-raw.png",
        "prompt": f"""Extreme close-up freeze-frame of the exact moment of punch impact inside a boxing ring.
{PAPER_MAN} — their red glove making contact with the {ROBOT}'s face/chest area.
Papers and code sheets exploding outward from the impact point like shrapnel.
Motion blur on the fist, sharp on the impact zone. Dramatic depth of field.
Slow-motion freeze frame aesthetic — dramatic sports photography.
Black and white scene — only the red boxing gloves and ring ropes in color.
Overhead arena spotlight, cinematic high contrast. No text, no logos. Widescreen 16:9."""
    },
    "slide4-marathon": {
        "file": "slide4-marathon-raw.png",
        "prompt": f"""Professional boxing arena scoreboard visible in background showing "ROUND 7 / 12".
Foreground: {ROBOT} still standing in the ring — tired but determined, hydraulic arms still raised in guard position.
Steam rising from overheated circuits, cables slightly frayed, still fighting.
Corner lights and arena crowd blurred in background. Red corner ropes visible.
Black and white photograph aesthetic — only the red boxing gloves and ring ropes in color.
Dramatic arena lighting from above. Cinematic editorial sports photography.
No text, no logos, no watermarks. Widescreen 16:9."""
    },
    "slide5-ropes": {
        "file": "slide5-ropes-raw.png",
        "prompt": f"""Low angle camera shot from inside a boxing ring, looking upward at the four corner ropes in forced perspective.
The ropes fill the entire frame diagonally — four distinct ropes, each visible as a separate line converging toward center.
Arena floodlights visible through the ropes creating dramatic lens flare.
Black and white photography — only the corner ropes in red.
Minimal, geometric, architectural. Empty ring, no fighters.
Cinematic, high contrast, editorial sports photography. No text, no logos. Widescreen 16:9."""
    },
    "slide6-judges": {
        "file": "slide6-judges-raw.png",
        "prompt": f"""Three boxing judges seated at the ringside judges table, viewed from the front.
Each judge holds up a different official scorecard — formal, serious expressions.
The {PAPER_MAN} and {ROBOT} visible blurred in background inside the ring.
Official scorecards with columns and numbers visible but not readable. Pens and clipboards.
Warm arena lighting from above. Serious, formal, institutional atmosphere.
Black and white aesthetic — only the red ring ropes and scorecards detail in color.
Cinematic sports editorial photography. No text, no logos. Widescreen 16:9."""
    },
    "slide7-warmup": {
        "file": "slide7-warmup-raw.png",
        "prompt": f"""Backstage arena corridor, fluorescent lights overhead.
{PAPER_MAN} shadowboxing alone — throwing jabs at the air, lightweight quick movement, papers scattering with each punch.
No opponent. No audience. Practicing alone before the real fight.
Gritty backstage realism — concrete walls, hanging equipment, locker room doors visible.
Black and white — red boxing gloves the only color.
Cinematic, high contrast, raw editorial sports photography. No text, no logos. Widescreen 16:9."""
    },
    "slide8-frequency": {
        "file": "slide8-frequency-raw.png",
        "prompt": f"""Horizontal split composition. Two scenes stacked:

TOP HALF: Empty boxing arena from above — just one {PAPER_MAN} and {ROBOT} sparring in the ring, almost alone, sparse crowd, casual exhibition feel. One round only.

BOTTOM HALF: Locker room wall with a large paper calendar — dozens of fight dates circled and marked in red. The calendar nearly full, heavily annotated, showing months of scheduled fights.

Both halves share the same black and white aesthetic. Ropes and calendar marks in red.
Cinematic editorial contrast between one-off and routine. No text, no logos. Widescreen 16:9."""
    },
    "slide9-champion": {
        "file": "slide9-champion-raw.png",
        "prompt": f"""Center of the boxing ring — championship victory moment.
{ROBOT} standing triumphant, one arm raised by the referee, championship belt held high with the other arm.
Team surrounding them: corner team, trainer, medical staff — all celebrating.
The {PAPER_MAN} visible respectfully in the background corner.
Confetti falling from above. Arena lights blazing. Crowd roaring.
Black and white with RED details: championship belt accent, corner ropes, gloves, confetti.
Cinematic Hollywood victory aesthetic, dramatic arena lighting. No text, no logos. Widescreen 16:9."""
    },
}

for key, scene in SCENES.items():
    out = RUNS / scene["file"]
    print(f"Gerando {key}...")
    try:
        response = client.images.generate(
            model="gpt-image-1",
            prompt=scene["prompt"],
            size="1536x1024",
            quality="high",
            n=1,
        )
        out.write_bytes(base64.b64decode(response.data[0].b64_json))
        print(f"  OK → {out.name}")
    except Exception as e:
        print(f"  ERRO: {e}")
    time.sleep(2)  # pausa entre chamadas

print("\nTodas as cenas geradas.")
