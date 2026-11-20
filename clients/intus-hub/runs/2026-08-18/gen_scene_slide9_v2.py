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

PROMPT = """Professional boxing arena — championship victory moment.
Heavy industrial robot with dark metallic body, visible circuit boards, power cables and hydraulic arms.
The robot standing triumphant in center of the ring, HOLDING THE CHAMPIONSHIP BELT WITH BOTH HANDS raised high above its head.
Both arms fully extended upward, hands gripping the belt on each side — belt clearly visible between both hands.
Team surrounding: corner team, trainer, celebranting with the robot.
Confetti falling from arena lights above.
Black and white — only the championship belt accents, red corner ropes, and red boxing gloves in color.
Cinematic Hollywood victory aesthetic, dramatic arena lighting from above.
No text, no logos, no watermarks. Widescreen 16:9."""

OUT = Path(r"C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub\runs\2026-08-18\slide9-champion-raw.png")

print("Gerando cena Slide 9 v2...")
response = client.images.generate(
    model="gpt-image-1",
    prompt=PROMPT,
    size="1536x1024",
    quality="high",
    n=1,
)
OUT.write_bytes(base64.b64decode(response.data[0].b64_json))
print(f"Salvo: {OUT}")
