# JSONs de imagem — Slides 03, 04, 05 e CTA — "Pato Estrategista"

Tema: pato-estrategista-ia
Template base: carrossel-twitter-post-style
Personagem: mesmo pato flat vetorial das slides anteriores (bico e pes #E8722A, fundo #0a0a0a)

---

## SLIDE 03

Copy: "Até que entendi uma coisa:\n\n**MINHA FUNÇÃO NÃO ERA FAZER TUDO.**\n\nEra pensar estratégia.\n\nCada hora trabalhando errado era uma hora que eu não decidia o futuro do negócio."

### Variação 1 — Lâmpada da virada

```json
{
  "template": "carrossel-twitter-post-style",
  "slide": "03",
  "variacao": "1 - Lampada da virada",
  "cliente": "Intus Hub",
  "tema": "pato-estrategista-ia",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "background_color": "#FFFFFF", "orientation": "portrait - imagem interna sempre 16:9 landscape" },
  "zones": {
    "header": { "avatar": { "note": "DEIXAR VAZIO - Canva" }, "text_block": { "line_1": "Diego Spanevello | Inteligência Artificial", "line_2": "@diego.spanevello" }, "verified_badge": true },
    "content": { "copy": "Até que entendi uma coisa:\n\n**MINHA FUNÇÃO NÃO ERA FAZER TUDO.**\n\nEra pensar estratégia.\n\nCada hora trabalhando errado era uma hora que eu não decidia o futuro do negócio.", "font_size": "34px - fixo", "bold_marking_only": true, "no_color_in_text": true },
    "image": {
      "slot_within_slide": { "width_px": 992, "height_px": 558, "aspect_ratio": "16:9" },
      "image_generation": { "dimensions": "1920x1080px", "aspect_ratio": "16:9", "orientation": "landscape obrigatorio" },
      "asset_prompt": {
        "scene": {
          "description": "Flat vector illustration, landscape 16:9, solid dark background (#0a0a0a with #E8722A accents). The same white duck character, orange beak and feet, sits calmly with a straight, composed posture. A single glowing orange lightbulb icon floats above its head, flat style, simple glow. In front of the duck, a small flat strategy chessboard grid rests on the ground. Behind the duck, faint, semi-transparent ghost versions of the four juggling icons from a previous scene (megaphone, headset, coin, chess pawn) are dissolving into the background at low opacity, visually fading away. Minimalist, calm, contemplative tone, no text within the image.",
          "action": "Calm realization moment, looking at the lightbulb and the chessboard, operational chaos fading into the background"
        },
        "style": { "primary": "flat vector illustration, minimalist 2D, consistent with prior slides", "lighting": "flat even illustrative lighting, soft orange glow only around the lightbulb" },
        "composition": {
          "framing": "duck centered-left, lightbulb above head, chessboard grid in front, fading icons scattered at low opacity in the background",
          "safe_area": "64px padding all sides, safe zone 1792x952 within 1920x1080",
          "ui_elements": "none - copy lives in content zone"
        },
        "quality": {
          "include": ["flat vector illustration", "consistent duck design with prior slides", "calm contemplative pose", "orange glow accent", "fading background icons conveying transition", "clean solid dark background"],
          "avoid": ["photorealism", "3D rendering", "cluttered fully-opaque background", "text baked into image", "inconsistent duck design"]
        }
      }
    },
    "footer": { "exists": false }
  },
  "negative_rules": ["nunca travessao", "nunca linha divisoria", "sempre 16:9 landscape", "nunca full bleed", "avatar vazio", "zero cor no texto so negrito", "manter design do pato das slides anteriores"]
}
```

### Variação 2 — Pato na torre

```json
{
  "template": "carrossel-twitter-post-style",
  "slide": "03",
  "variacao": "2 - Pato na torre",
  "cliente": "Intus Hub",
  "tema": "pato-estrategista-ia",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "background_color": "#FFFFFF", "orientation": "portrait - imagem interna sempre 16:9 landscape" },
  "zones": {
    "header": { "avatar": { "note": "DEIXAR VAZIO - Canva" }, "text_block": { "line_1": "Diego Spanevello | Inteligência Artificial", "line_2": "@diego.spanevello" }, "verified_badge": true },
    "content": { "copy": "Até que entendi uma coisa:\n\n**MINHA FUNÇÃO NÃO ERA FAZER TUDO.**\n\nEra pensar estratégia.\n\nCada hora trabalhando errado era uma hora que eu não decidia o futuro do negócio.", "font_size": "34px - fixo", "bold_marking_only": true, "no_color_in_text": true },
    "image": {
      "slot_within_slide": { "width_px": 992, "height_px": 558, "aspect_ratio": "16:9" },
      "image_generation": { "dimensions": "1920x1080px", "aspect_ratio": "16:9", "orientation": "landscape obrigatorio" },
      "asset_prompt": {
        "scene": {
          "description": "Flat vector illustration, landscape 16:9, solid dark background (#0a0a0a with #E8722A accents). The same white duck character, orange beak and feet, stands atop a small minimalist flat pedestal or tower shape, calm and upright. Below the tower, a tiny flat illustrated maze or business floor-plan grid pattern is visible, rendered small to emphasize distance and perspective from above. The duck looks down at the grid with a composed, observant expression. Minimalist flat design, no text within the image.",
          "action": "Standing elevated, looking down at the operational maze below, symbolizing rising above the chaos to see the big picture"
        },
        "style": { "primary": "flat vector illustration, minimalist 2D, consistent with prior slides", "lighting": "flat even illustrative lighting" },
        "composition": {
          "framing": "vertical emphasis within the horizontal canvas, tower and duck on one side, maze grid small at the base to suggest height and distance",
          "safe_area": "64px padding all sides, safe zone 1792x952 within 1920x1080",
          "ui_elements": "none - copy lives in content zone"
        },
        "quality": {
          "include": ["flat vector illustration", "consistent duck design with prior slides", "elevated confident pose", "clear sense of height and perspective", "clean solid dark background"],
          "avoid": ["photorealism", "3D rendering", "cluttered background", "text baked into image", "inconsistent duck design"]
        }
      }
    },
    "footer": { "exists": false }
  },
  "negative_rules": ["nunca travessao", "nunca linha divisoria", "sempre 16:9 landscape", "nunca full bleed", "avatar vazio", "zero cor no texto so negrito", "manter design do pato das slides anteriores"]
}
```

---

## SLIDE 04

Copy: "Foi então que decidi estudar.\n\n**COMECEI A USAR AGENTES DE IA.**\n\nPra marketing, produção de conteúdo, atendimento, financeiro.\n\nParei de tentar voar, nadar e andar tudo ao mesmo tempo."

### Variação 1 — Entrega pros robôs

```json
{
  "template": "carrossel-twitter-post-style",
  "slide": "04",
  "variacao": "1 - Entrega pros robos",
  "cliente": "Intus Hub",
  "tema": "pato-estrategista-ia",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "background_color": "#FFFFFF", "orientation": "portrait - imagem interna sempre 16:9 landscape" },
  "zones": {
    "header": { "avatar": { "note": "DEIXAR VAZIO - Canva" }, "text_block": { "line_1": "Diego Spanevello | Inteligência Artificial", "line_2": "@diego.spanevello" }, "verified_badge": true },
    "content": { "copy": "Foi então que decidi estudar.\n\n**COMECEI A USAR AGENTES DE IA.**\n\nPra marketing, produção de conteúdo, atendimento, financeiro.\n\nParei de tentar voar, nadar e andar tudo ao mesmo tempo.", "font_size": "34px - fixo", "bold_marking_only": true, "no_color_in_text": true },
    "image": {
      "slot_within_slide": { "width_px": 992, "height_px": 558, "aspect_ratio": "16:9" },
      "image_generation": { "dimensions": "1920x1080px", "aspect_ratio": "16:9", "orientation": "landscape obrigatorio" },
      "asset_prompt": {
        "scene": {
          "description": "Flat vector illustration, landscape 16:9, solid dark background (#0a0a0a with #E8722A accents). The same white duck character, orange beak and feet, calmly hands off four small flat icon objects (megaphone, headset, coin, bar chart) to four small simple geometric robot or agent characters lined up in front of it, one robot per object. Each robot has a tiny orange indicator light glowing to signal it is now active and handling the task. Duck's posture is relaxed, wings extended forward in a handing-off gesture. Minimalist flat design, no text within the image.",
          "action": "Handing off each task item to a dedicated small robot agent, calm and relieved posture"
        },
        "style": { "primary": "flat vector illustration, minimalist 2D, consistent with prior slides", "lighting": "flat even illustrative lighting, small orange glow on each robot indicator light" },
        "composition": {
          "framing": "duck on one side, four robots lined up receiving the handed-off objects, landscape composition with even spacing",
          "safe_area": "64px padding all sides, safe zone 1792x952 within 1920x1080",
          "ui_elements": "none - copy lives in content zone"
        },
        "quality": {
          "include": ["flat vector illustration", "consistent duck design with prior slides", "simple geometric robot characters", "relaxed handing-off gesture", "orange indicator lights", "clean solid dark background"],
          "avoid": ["photorealism", "3D rendering", "overly detailed robots breaking flat style", "cluttered background", "text baked into image"]
        }
      }
    },
    "footer": { "exists": false }
  },
  "negative_rules": ["nunca travessao", "nunca linha divisoria", "sempre 16:9 landscape", "nunca full bleed", "avatar vazio", "zero cor no texto so negrito", "manter design do pato das slides anteriores"]
}
```

### Variação 2 — Central de comando

```json
{
  "template": "carrossel-twitter-post-style",
  "slide": "04",
  "variacao": "2 - Central de comando",
  "cliente": "Intus Hub",
  "tema": "pato-estrategista-ia",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "background_color": "#FFFFFF", "orientation": "portrait - imagem interna sempre 16:9 landscape" },
  "zones": {
    "header": { "avatar": { "note": "DEIXAR VAZIO - Canva" }, "text_block": { "line_1": "Diego Spanevello | Inteligência Artificial", "line_2": "@diego.spanevello" }, "verified_badge": true },
    "content": { "copy": "Foi então que decidi estudar.\n\n**COMECEI A USAR AGENTES DE IA.**\n\nPra marketing, produção de conteúdo, atendimento, financeiro.\n\nParei de tentar voar, nadar e andar tudo ao mesmo tempo.", "font_size": "34px - fixo", "bold_marking_only": true, "no_color_in_text": true },
    "image": {
      "slot_within_slide": { "width_px": 992, "height_px": 558, "aspect_ratio": "16:9" },
      "image_generation": { "dimensions": "1920x1080px", "aspect_ratio": "16:9", "orientation": "landscape obrigatorio" },
      "asset_prompt": {
        "scene": {
          "description": "Flat vector illustration, landscape 16:9, solid dark background (#0a0a0a with #E8722A accents). The same white duck character, orange beak and feet, stands with wings crossed in a calm, overseeing posture in front of a small floating flat dashboard panel. The panel is a simple flat rectangle divided into four smaller sections, each showing a small icon (megaphone, headset, coin, chart) with a tiny glowing orange indicator light marked active. No real screen glare or gradient, kept flat and iconographic. Minimalist flat design, no text within the image.",
          "action": "Calmly overseeing an automated dashboard handling the four tasks"
        },
        "style": { "primary": "flat vector illustration, minimalist 2D, consistent with prior slides", "lighting": "flat even illustrative lighting, small orange glow on each active indicator" },
        "composition": {
          "framing": "duck to one side with crossed wings, floating dashboard panel centered or to the other side, landscape composition",
          "safe_area": "64px padding all sides, safe zone 1792x952 within 1920x1080",
          "ui_elements": "none - copy lives in content zone"
        },
        "quality": {
          "include": ["flat vector illustration", "consistent duck design with prior slides", "confident overseeing posture", "simple flat dashboard panel", "orange active indicators", "clean solid dark background"],
          "avoid": ["photorealism", "3D rendering", "realistic screen glare or UI complexity", "cluttered background", "text baked into image"]
        }
      }
    },
    "footer": { "exists": false }
  },
  "negative_rules": ["nunca travessao", "nunca linha divisoria", "sempre 16:9 landscape", "nunca full bleed", "avatar vazio", "zero cor no texto so negrito", "manter design do pato das slides anteriores"]
}
```

---

## SLIDE 05

Copy: "Deixei isso pros agentes.\n\n**E FOQUEI NO PRINCIPAL.**\n\nGestão e estratégia do meu negócio."

### Variação 1 — Pato no leme

```json
{
  "template": "carrossel-twitter-post-style",
  "slide": "05",
  "variacao": "1 - Pato no leme",
  "cliente": "Intus Hub",
  "tema": "pato-estrategista-ia",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "background_color": "#FFFFFF", "orientation": "portrait - imagem interna sempre 16:9 landscape" },
  "zones": {
    "header": { "avatar": { "note": "DEIXAR VAZIO - Canva" }, "text_block": { "line_1": "Diego Spanevello | Inteligência Artificial", "line_2": "@diego.spanevello" }, "verified_badge": true },
    "content": { "copy": "Deixei isso pros agentes.\n\n**E FOQUEI NO PRINCIPAL.**\n\nGestão e estratégia do meu negócio.", "font_size": "34px - fixo", "bold_marking_only": true, "no_color_in_text": true },
    "image": {
      "slot_within_slide": { "width_px": 992, "height_px": 558, "aspect_ratio": "16:9" },
      "image_generation": { "dimensions": "1920x1080px", "aspect_ratio": "16:9", "orientation": "landscape obrigatorio" },
      "asset_prompt": {
        "scene": {
          "description": "Flat vector illustration, landscape 16:9, solid dark background (#0a0a0a with #E8722A accents). The same white duck character, orange beak and feet, stands confidently at a flat illustrated ship's steering wheel (helm), calm flat wave shapes beneath suggesting a calm sea. In the background, small simple robot agent characters are visible on a stylized deck, handling minor tasks quietly. Duck's posture is upright, focused forward, hands (wings) on the wheel. Minimalist flat design, no text within the image.",
          "action": "Steering confidently while small agents handle background tasks"
        },
        "style": { "primary": "flat vector illustration, minimalist 2D, consistent with prior slides", "lighting": "flat even illustrative lighting" },
        "composition": {
          "framing": "duck centered at the helm, calm wave shapes below, small robot agents in soft-focus background scale",
          "safe_area": "64px padding all sides, safe zone 1792x952 within 1920x1080",
          "ui_elements": "none - copy lives in content zone"
        },
        "quality": {
          "include": ["flat vector illustration", "consistent duck design with prior slides", "confident steering pose", "calm sea shapes", "background agents at work", "clean solid dark background"],
          "avoid": ["photorealism", "3D rendering", "cluttered background", "text baked into image"]
        }
      }
    },
    "footer": { "exists": false }
  },
  "negative_rules": ["nunca travessao", "nunca linha divisoria", "sempre 16:9 landscape", "nunca full bleed", "avatar vazio", "zero cor no texto so negrito", "manter design do pato das slides anteriores"]
}
```

### Variação 2 — Mesa limpa

```json
{
  "template": "carrossel-twitter-post-style",
  "slide": "05",
  "variacao": "2 - Mesa limpa",
  "cliente": "Intus Hub",
  "tema": "pato-estrategista-ia",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "background_color": "#FFFFFF", "orientation": "portrait - imagem interna sempre 16:9 landscape" },
  "zones": {
    "header": { "avatar": { "note": "DEIXAR VAZIO - Canva" }, "text_block": { "line_1": "Diego Spanevello | Inteligência Artificial", "line_2": "@diego.spanevello" }, "verified_badge": true },
    "content": { "copy": "Deixei isso pros agentes.\n\n**E FOQUEI NO PRINCIPAL.**\n\nGestão e estratégia do meu negócio.", "font_size": "34px - fixo", "bold_marking_only": true, "no_color_in_text": true },
    "image": {
      "slot_within_slide": { "width_px": 992, "height_px": 558, "aspect_ratio": "16:9" },
      "image_generation": { "dimensions": "1920x1080px", "aspect_ratio": "16:9", "orientation": "landscape obrigatorio" },
      "asset_prompt": {
        "scene": {
          "description": "Flat vector illustration, landscape 16:9, solid dark background (#0a0a0a with #E8722A accents). The same white duck character, orange beak and feet, sits calmly at a minimalist flat desk with only a single item on it: a small flat strategy map or chessboard grid. No clutter, no extra objects, wide open negative space around the desk emphasizing calm and clarity, in direct visual contrast to a previous cluttered desk scene. Duck posture relaxed and composed. Minimalist flat design, no text within the image.",
          "action": "Sitting calmly at an uncluttered desk, focused on the single strategy item"
        },
        "style": { "primary": "flat vector illustration, minimalist 2D, consistent with prior slides", "lighting": "flat even illustrative lighting" },
        "composition": {
          "framing": "duck and desk centered with generous negative space around, emphasizing minimalism",
          "safe_area": "64px padding all sides, safe zone 1792x952 within 1920x1080",
          "ui_elements": "none - copy lives in content zone"
        },
        "quality": {
          "include": ["flat vector illustration", "consistent duck design with prior slides", "calm composed posture", "minimalist uncluttered desk", "clean solid dark background"],
          "avoid": ["photorealism", "3D rendering", "cluttered desk objects", "text baked into image"]
        }
      }
    },
    "footer": { "exists": false }
  },
  "negative_rules": ["nunca travessao", "nunca linha divisoria", "sempre 16:9 landscape", "nunca full bleed", "avatar vazio", "zero cor no texto so negrito", "manter design do pato das slides anteriores"]
}
```

---

## CTA

Copy: "E você? Chega de ser o PATO.\n\n**VIRE O ESTRATEGISTA.**\n\nO agente de IA cuida do resto.\n\nAtivação em menos de 5 minutos, sem saber programar.\n\nComenta **AGENTE** que eu te mando o link."

### Variação 1 — Pato "I Want You" (aponta pro leitor)

```json
{
  "template": "carrossel-twitter-post-style",
  "slide": "CTA",
  "variacao": "1 - Pato apontando estilo recrutamento, espaco reservado para imagem do Aspira",
  "cliente": "Intus Hub",
  "tema": "pato-estrategista-ia",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "background_color": "#FFFFFF", "orientation": "portrait - imagem interna sempre 16:9 landscape" },
  "zones": {
    "header": { "avatar": { "note": "DEIXAR VAZIO - Canva" }, "text_block": { "line_1": "Diego Spanevello | Inteligência Artificial", "line_2": "@diego.spanevello" }, "verified_badge": true },
    "content": { "copy": "E você? Chega de ser o PATO.\n\n**VIRE O ESTRATEGISTA.**\n\nO agente de IA cuida do resto.\n\nAtivação em menos de 5 minutos, sem saber programar.\n\nComenta **AGENTE** que eu te mando o link.", "font_size": "34px - fixo", "bold_marking_only": true, "no_color_in_text": true },
    "image": {
      "slot_within_slide": { "width_px": 992, "height_px": 558, "aspect_ratio": "16:9" },
      "image_generation": { "dimensions": "1920x1080px", "aspect_ratio": "16:9", "orientation": "landscape obrigatorio" },
      "asset_prompt": {
        "scene": {
          "description": "Flat vector illustration, landscape 16:9, solid dark background (#0a0a0a with #E8722A accents). The same white duck character, orange beak and feet, stands tall and confident in the left two-thirds of the frame, facing directly forward. One wing extends straight toward the viewer in the classic direct recruitment-poster pointing gesture, firm and direct eye contact with the camera. Posture is upright, chest forward, no hat or costume elements, just the established flat duck character with a confident, commanding expression. Minimalist flat design, no text within the image.",
          "action": "Standing tall, pointing directly at the viewer with a firm, direct gaze"
        },
        "style": { "primary": "flat vector illustration, minimalist 2D, consistent with prior slides", "lighting": "flat even illustrative lighting" },
        "composition": {
          "framing": "duck occupies the left two-thirds of the frame in a strong frontal pointing pose",
          "manual_asset_placeholder": "Right third of the 1920x1080 canvas (approx x:1280-1920, full height) must be left as clean empty solid background, no illustrated elements, reserved for the user to manually insert a screenshot/image of 'Aspira' in Canva afterward",
          "safe_area": "64px padding all sides, safe zone 1792x952 within 1920x1080",
          "ui_elements": "none - copy lives in content zone"
        },
        "quality": {
          "include": ["flat vector illustration", "consistent duck design with prior slides", "strong direct pointing pose", "firm confident eye contact", "clean reserved negative space on the right", "clean solid dark background"],
          "avoid": ["photorealism", "3D rendering", "Uncle Sam hat or American flag costume elements", "filling the reserved right-side space with any illustration", "text baked into image"]
        }
      }
    },
    "footer": { "exists": false }
  },
  "negative_rules": ["nunca travessao", "nunca linha divisoria", "sempre 16:9 landscape", "nunca full bleed", "avatar vazio", "zero cor no texto so negrito", "manter design do pato das slides anteriores", "nao preencher a area reservada para o Aspira"]
}
```

### Variação 2 — Pato de óculos escuros no celular, espaço pro Aspira flutuando

```json
{
  "template": "carrossel-twitter-post-style",
  "slide": "CTA",
  "variacao": "2 - Pato de oculos escuros na cadeira com celular, espaco para Aspira flutuando",
  "cliente": "Intus Hub",
  "tema": "pato-estrategista-ia",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "background_color": "#FFFFFF", "orientation": "portrait - imagem interna sempre 16:9 landscape" },
  "zones": {
    "header": { "avatar": { "note": "DEIXAR VAZIO - Canva" }, "text_block": { "line_1": "Diego Spanevello | Inteligência Artificial", "line_2": "@diego.spanevello" }, "verified_badge": true },
    "content": { "copy": "E você? Chega de ser o PATO.\n\n**VIRE O ESTRATEGISTA.**\n\nO agente de IA cuida do resto.\n\nAtivação em menos de 5 minutos, sem saber programar.\n\nComenta **AGENTE** que eu te mando o link.", "font_size": "34px - fixo", "bold_marking_only": true, "no_color_in_text": true },
    "image": {
      "slot_within_slide": { "width_px": 992, "height_px": 558, "aspect_ratio": "16:9" },
      "image_generation": { "dimensions": "1920x1080px", "aspect_ratio": "16:9", "orientation": "landscape obrigatorio" },
      "asset_prompt": {
        "scene": {
          "description": "Flat vector illustration, landscape 16:9, solid dark background (#0a0a0a with #E8722A accents). The same white duck character, orange beak and feet, sits relaxed in a simple flat illustrated armchair, wearing flat dark sunglasses, cool and calm posture, one leg casually crossed. The duck holds a smartphone in one wing, the phone screen shown as a simple flat glowing rectangle. Above and slightly beside the phone, a clearly empty negative-space area is left deliberately blank, reserved for the user to manually insert a floating image of 'Aspira' as if emerging from the phone screen. Minimalist flat design, no text within the image.",
          "action": "Sitting relaxed in a chair, holding a phone, cool and confident, with a floating asset area left empty above the phone"
        },
        "style": { "primary": "flat vector illustration, minimalist 2D, consistent with prior slides", "lighting": "flat even illustrative lighting, small flat glow on the phone screen only" },
        "composition": {
          "framing": "duck seated to one side of the frame in the armchair, phone held toward the empty reserved space",
          "manual_asset_placeholder": "Upper-center-right area of the 1920x1080 canvas (approx x:960-1728, y:0-560) left as clean empty solid background above the phone, reserved for the user to manually insert the floating 'Aspira' image in Canva afterward",
          "safe_area": "64px padding all sides, safe zone 1792x952 within 1920x1080",
          "ui_elements": "none - copy lives in content zone"
        },
        "quality": {
          "include": ["flat vector illustration", "consistent duck design with prior slides", "relaxed cool posture", "sunglasses accessory", "clean reserved floating space above phone", "clean solid dark background"],
          "avoid": ["photorealism", "3D rendering", "filling the reserved floating space with any illustration", "cluttered background", "text baked into image"]
        }
      }
    },
    "footer": { "exists": false }
  },
  "negative_rules": ["nunca travessao", "nunca linha divisoria", "sempre 16:9 landscape", "nunca full bleed", "avatar vazio", "zero cor no texto so negrito", "manter design do pato das slides anteriores", "nao preencher a area reservada para o Aspira"]
}
```
