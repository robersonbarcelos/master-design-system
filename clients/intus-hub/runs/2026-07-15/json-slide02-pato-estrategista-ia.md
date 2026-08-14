# JSON de imagem — Slide 02 — "Eu fui o pato do meu negócio"

Tema: pato-estrategista-ia
Template base: carrossel-twitter-post-style

## Variação 1 — Pato malabarista

```json
{
  "template": "carrossel-twitter-post-style",
  "slide": "02",
  "variacao": "1 - Pato malabarista",
  "cliente": "Intus Hub",
  "tema": "pato-estrategista-ia",
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "background_color": "#FFFFFF",
    "orientation": "portrait - slide completo, imagem interna e sempre 16:9 landscape"
  },
  "zones": {
    "header": {
      "avatar": { "note": "DEIXAR VAZIO - adicionar foto de perfil manualmente no Canva" },
      "text_block": {
        "line_1": "Diego Spanevello | Inteligência Artificial",
        "line_2": "@diego.spanevello"
      },
      "verified_badge": true
    },
    "content": {
      "copy": "Por anos, eu fui assim.\n\n**EU FUI O PATO DO MEU NEGÓCIO.**\n\nMarketing, atendimento, financeiro, estratégia: tudo ao mesmo tempo.\n\nE nada saía do jeito que deveria.",
      "font_size": "34px - fixo",
      "bold_marking_only": true,
      "no_color_in_text": true
    },
    "image": {
      "slot_within_slide": { "width_px": 992, "height_px": 558, "aspect_ratio": "16:9" },
      "image_generation": { "dimensions": "1920x1080px", "aspect_ratio": "16:9", "orientation": "landscape obrigatorio" },
      "asset_prompt": {
        "scene": {
          "description": "A single flat vector illustration in landscape 16:9 format, one continuous solid dark background in warm brand tones (#0a0a0a base with #E8722A orange accents). The same white duck character from the series, orange beak and orange webbed feet, stands center frame juggling four small flat icon objects in the air around it: a megaphone (marketing), a headset (customer service), a coin with a dollar sign (financial), and a chess pawn (strategy). The duck's eyes are drawn as small spirals or crossed lines to convey dizziness, its body slightly off balance, wings raised mid motion as if trying to keep all four objects afloat. Small curved motion lines trail behind each juggled object showing they are all in simultaneous motion. Minimalist flat design, comedic overwhelmed tone, no text within the image.",
          "subject": "Same white duck character (flat vector, orange beak and feet) as previous slides, now juggling four icon objects",
          "setting": "Neutral flat solid dark background, no ground clutter, duck centered",
          "action": "Juggling four objects simultaneously overhead and around the body, visibly dizzy and overwhelmed"
        },
        "style": {
          "primary": "flat vector illustration, minimalist 2D character design, consistent with prior slides in the series",
          "rendering_quality": "clean vector, crisp edges, stylized",
          "surface_textures": "flat color fills, no texture noise, simple soft ground shadow beneath the duck",
          "lighting": "flat even illustrative lighting, no directional light source"
        },
        "materials": {
          "surfaces": "flat matte fills, duck body solid white, beak and feet solid #E8722A orange, juggled icons in simple flat colors (megaphone dark gray, headset dark gray, coin gold-orange, chess pawn light gray)"
        },
        "composition": {
          "perspective": "flat 2D, no depth, frontal view of the duck",
          "framing": "centered single-subject composition, landscape 16:9, icons arranged in a loose circular orbit around the duck's head and wings to suggest juggling motion",
          "subject_placement": "duck centered horizontally and vertically, icons distributed evenly in the upper half of the frame to leave breathing room below",
          "safe_area": "64px padding on all sides within 1920x1080 canvas, keep all elements within a 1792x952 safe zone so nothing crops when placed in the 992x558 Canva slot",
          "ui_elements": "none - pure illustration asset, copy lives in the content zone"
        },
        "quality": {
          "include": ["flat vector illustration", "minimalist character design", "consistent duck design with prior slides", "clean solid dark background", "comedic overwhelmed expression", "circular juggling arrangement", "warm orange accent harmony with brand color", "crisp vector edges"],
          "avoid": ["photorealism", "3D rendering", "gradient heavy shading", "cluttered background details", "text or typography baked into image", "inconsistent duck design versus other slides in the series"],
          "reference_standard": "flat vector meme-illustration style consistent with the carousel's established duck character, adapted into a Duolingo-style flat character illustration system"
        }
      }
    },
    "footer": { "exists": false }
  },
  "negative_rules": [
    "nunca usar travessao",
    "nunca usar linha divisoria entre secoes",
    "nunca gerar imagem quadrada ou retrato - sempre 16:9 landscape no slot de imagem",
    "imagem nunca full bleed, sempre com recuo de 44px e border radius 18px",
    "avatar sempre vazio para Canva",
    "zero cor no corpo do texto, so negrito",
    "manter o mesmo design do pato usado no Slide 01 - consistencia de personagem"
  ]
}
```

## Variação 2 — Pato com braços extras (exagero surreal)

```json
{
  "template": "carrossel-twitter-post-style",
  "slide": "02",
  "variacao": "2 - Pato com bracos extras",
  "cliente": "Intus Hub",
  "tema": "pato-estrategista-ia",
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "background_color": "#FFFFFF",
    "orientation": "portrait - slide completo, imagem interna e sempre 16:9 landscape"
  },
  "zones": {
    "header": {
      "avatar": { "note": "DEIXAR VAZIO - adicionar foto de perfil manualmente no Canva" },
      "text_block": {
        "line_1": "Diego Spanevello | Inteligência Artificial",
        "line_2": "@diego.spanevello"
      },
      "verified_badge": true
    },
    "content": {
      "copy": "Por anos, eu fui assim.\n\n**EU FUI O PATO DO MEU NEGÓCIO.**\n\nMarketing, atendimento, financeiro, estratégia: tudo ao mesmo tempo.\n\nE nada saía do jeito que deveria.",
      "font_size": "34px - fixo",
      "bold_marking_only": true,
      "no_color_in_text": true
    },
    "image": {
      "slot_within_slide": { "width_px": 992, "height_px": 558, "aspect_ratio": "16:9" },
      "image_generation": { "dimensions": "1920x1080px", "aspect_ratio": "16:9", "orientation": "landscape obrigatorio" },
      "asset_prompt": {
        "scene": {
          "description": "A single flat vector illustration in landscape 16:9 format, one continuous solid dark background in warm brand tones (#0a0a0a base with #E8722A orange accents). The same white duck character from the series, orange beak and orange webbed feet, is drawn with four small extra cartoon arms sprouting from its body in a surreal comedic exaggeration. Each arm holds a different object: one holds a ringing smartphone, one holds a small calculator, one holds a megaphone, one holds a small bar chart or steering wheel representing strategy. Small sweat drop shapes and a couple of tiny spinning stars float near the duck's head to convey overwhelm and exhaustion. The duck's normal wings remain at its sides, unbothered, emphasizing that the extra arms are an absurd addition rather than its real body. Minimalist flat design, comedic surreal tone, no text within the image.",
          "subject": "Same white duck character (flat vector, orange beak and feet) as previous slides, now with four small extra cartoon arms each holding a task object",
          "setting": "Neutral flat solid dark background, no ground clutter, duck centered",
          "action": "Simultaneously holding and operating four different task objects with extra arms while visibly overwhelmed"
        },
        "style": {
          "primary": "flat vector illustration, minimalist 2D character design, consistent with prior slides in the series",
          "rendering_quality": "clean vector, crisp edges, stylized",
          "surface_textures": "flat color fills, no texture noise, simple soft ground shadow beneath the duck",
          "lighting": "flat even illustrative lighting, no directional light source"
        },
        "materials": {
          "surfaces": "flat matte fills, duck body solid white, beak, feet and extra arms solid #E8722A orange, held objects in simple flat colors (phone dark gray with orange screen glow, calculator light gray, megaphone dark gray, chart in orange and white)"
        },
        "composition": {
          "perspective": "flat 2D, no depth, frontal three quarter view of the duck",
          "framing": "centered single-subject composition, landscape 16:9, four extra arms radiating outward from the body at different angles to fill the horizontal frame",
          "subject_placement": "duck centered horizontally and vertically, arms extending toward the four corners of the frame to use the full landscape width",
          "safe_area": "64px padding on all sides within 1920x1080 canvas, keep all elements within a 1792x952 safe zone so nothing crops when placed in the 992x558 Canva slot",
          "ui_elements": "none - pure illustration asset, copy lives in the content zone"
        },
        "quality": {
          "include": ["flat vector illustration", "minimalist character design", "consistent duck design with prior slides", "clean solid dark background", "surreal comedic exaggeration", "clear silhouette readability despite extra arms", "warm orange accent harmony with brand color", "crisp vector edges"],
          "avoid": ["photorealism", "3D rendering", "gradient heavy shading", "cluttered background details", "text or typography baked into image", "inconsistent duck design versus other slides in the series", "arms overlapping into an unreadable tangle"],
          "reference_standard": "flat vector meme-illustration style consistent with the carousel's established duck character, adapted into a Duolingo-style flat character illustration system with cartoon exaggeration"
        }
      }
    },
    "footer": { "exists": false }
  },
  "negative_rules": [
    "nunca usar travessao",
    "nunca usar linha divisoria entre secoes",
    "nunca gerar imagem quadrada ou retrato - sempre 16:9 landscape no slot de imagem",
    "imagem nunca full bleed, sempre com recuo de 44px e border radius 18px",
    "avatar sempre vazio para Canva",
    "zero cor no corpo do texto, so negrito",
    "manter o mesmo design do pato usado no Slide 01 - consistencia de personagem"
  ]
}
```
