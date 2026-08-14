# JSONs de Capa — "Claude recuperou a consciência? Não, ainda não"

Tema: claude-consciencia-ia
Cliente: Intus Hub
Template base: carrossel-twitter-post-style (TEMPLATE-SLIDE-TWITTER-POST)
Personagem: robô laranja blocky/quadrado, ilustração sketch/lápis com hachura, absorvido das 3 referências enviadas pelo usuário (mesa desenhando frustrado, skate pixelado com brilho em fundo preto, cabeça com capacete em caixa de ferramentas).

6 variações = 2 visuais por headline × 3 headlines aprovadas para exploração visual.

---

## Headline ① — "3 COISAS QUE O PAPER DA ANTHROPIC SOBRE O CLAUDE PROVA, E NENHUMA É 'A IA TEM CONSCIÊNCIA'"

### Variação H1-V3 — Lupa sobre o peito da IA

```json
{
  "template": "carrossel-twitter-post-style",
  "slide": "01-capa",
  "variacao": "H1-V3 - Lupa sobre o peito da IA",
  "cliente": "Intus Hub",
  "tema": "claude-consciencia-ia",
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
      "copy": "Um paper da Anthropic sobre o Claude viralizou.\n\n**3 COISAS QUE O PAPER PROVA.**\n\nE nenhuma delas é **'A IA TEM CONSCIÊNCIA.'**",
      "font_size": "34px - fixo",
      "bold_marking_only": true,
      "no_color_in_text": true
    },
    "image": {
      "slot_within_slide": { "width_px": 992, "height_px": 558, "aspect_ratio": "16:9" },
      "image_generation": { "dimensions": "1920x1080px", "aspect_ratio": "16:9", "orientation": "landscape obrigatorio" },
      "asset_prompt": {
        "scene": {
          "description": "A single hand-drawn pencil-sketch illustration in landscape 16:9 format, warm light beige paper-toned background (#EDE6DA). An orange blocky robot mascot — square geometric head and torso built from simple cube-like forms, dark charcoal joints and seams, the same character used across the brand's robot series — stands in profile, facing right. A large magnifying glass, held by a simple mechanical arm or floating in frame, is positioned directly over the center of the robot's chest panel. Through the lens, magnified and glowing faintly, is revealed a small illuminated control panel with a few simple square buttons and a soft internal light — not a heart, not an organic shape, just visible circuitry and switches. The rest of the robot's chest outside the lens is plain orange block with pencil hatching shadow. Fine graphite cross-hatch lines build all shading — on the robot's body, the magnifying glass rim, and the ground shadow beneath the robot's feet. No text within the image.",
          "subject": "Orange blocky robot mascot in profile, chest exposed under a magnifying glass revealing a small lit control panel instead of an organic core",
          "setting": "Flat light beige textured paper background, minimal ground shadow, no other props",
          "action": "Static pose, one arm or a floating magnifying glass held steady over the chest, inviting inspection"
        },
        "style": {
          "primary": "hand-drawn pencil-sketch illustration, editorial explainer style",
          "rendering_quality": "detailed sketch linework, consistent hatching density",
          "surface_textures": "cross-hatched pencil shading on all surfaces, visible paper grain in background, rough sketch outline (not clean vector)",
          "lighting": "flat diffused sketch lighting, soft graphite shadow beneath the robot and around the magnifying glass rim, faint warm glow radiating from the lens interior only"
        },
        "materials": {
          "surfaces": "matte orange blocky robot shell (#E8722A) with dark charcoal (#1A1A1A) joint seams, magnifying glass rim in dull graphite gray, glass lens rendered with light hatching to suggest transparency and a subtle circular highlight, control panel interior in warm soft-glow orange-white"
        },
        "composition": {
          "perspective": "flat 2D sketch perspective, slight profile angle, no deep depth of field",
          "framing": "centered single-subject composition, landscape 16:9, magnifying glass positioned at the horizontal center of the frame over the chest",
          "subject_placement": "robot occupies the center-left to center of the frame, magnifying glass and revealed panel centered, generous negative space of textured beige background around the figure",
          "safe_area": "64px padding on all sides within 1920x1080 canvas, keep all elements within a 1792x952 safe zone so nothing crops when placed in the 992x558 Canva slot",
          "ui_elements": "none - pure illustration asset, copy lives in the content zone"
        },
        "quality": {
          "include": ["hand-drawn pencil sketch style", "consistent orange blocky robot design", "cross-hatch shading", "warm beige paper background", "clear focal point on the magnifying glass reveal", "editorial explainer mood", "clean readable silhouette", "subtle internal glow contrast"],
          "avoid": ["photorealism", "flat vector clean fills", "3D CGI rendering", "organic heart or brain shapes inside the panel", "cluttered background props", "text or typography baked into image", "inconsistent robot design"],
          "reference_standard": "hand-drawn technical explainer sketch style, in the spirit of New Yorker-style pencil editorial illustration crossed with a blocky robot mascot design system"
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
    "manter o mesmo design do robo em todas as capas - consistencia de personagem",
    "nunca desenhar coracao ou cerebro organico dentro do painel revelado pela lupa"
  ]
}
```

### Variação H1-V1 — Raio-X do mecanismo

```json
{
  "template": "carrossel-twitter-post-style",
  "slide": "01-capa",
  "variacao": "H1-V1 - Raio-X do mecanismo",
  "cliente": "Intus Hub",
  "tema": "claude-consciencia-ia",
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
      "copy": "Um paper da Anthropic sobre o Claude viralizou.\n\n**3 COISAS QUE O PAPER PROVA.**\n\nE nenhuma delas é **'A IA TEM CONSCIÊNCIA.'**",
      "font_size": "34px - fixo",
      "bold_marking_only": true,
      "no_color_in_text": true
    },
    "image": {
      "slot_within_slide": { "width_px": 992, "height_px": 558, "aspect_ratio": "16:9" },
      "image_generation": { "dimensions": "1920x1080px", "aspect_ratio": "16:9", "orientation": "landscape obrigatorio" },
      "asset_prompt": {
        "scene": {
          "description": "A single hand-drawn pencil-sketch illustration in landscape 16:9 format, solid black background (#0A0A0A) with a faint warm orange glow radiating outward from the robot's head, echoing the sparkle-trail energy of the brand's skateboard reference image. An orange blocky robot mascot — square geometric head and torso, dark charcoal joints, same consistent character — faces forward, front-and-center. The upper portion of its square head is shown in cross-section, as if sliced open in an X-ray diagram style: a clean geometric cutaway line reveals the interior is NOT organic neurons or brain tissue, but simple visible mechanisms — a few interlocking gears, small circuit traces, and two or three basic square microchips, all rendered in the same pencil-hatch style. Thin dotted or dashed sketch lines (like technical diagram callouts) point from the gears and circuits outward, in the manner of an explainer diagram, though with no text labels. Small glowing orange sparkle particles float near the head, consistent with the reference character's energetic glow accents. No text within the image.",
          "subject": "Orange blocky robot mascot facing forward, top of head shown in X-ray cutaway revealing gears and simple circuits instead of an organic brain",
          "setting": "Solid black background with soft ambient orange glow and a few floating sparkle particles",
          "action": "Static frontal pose, cutaway diagram is the active visual focus"
        },
        "style": {
          "primary": "hand-drawn pencil-sketch illustration with technical-diagram cutaway convention",
          "rendering_quality": "detailed sketch linework with precise diagram-style cutaway edge",
          "surface_textures": "cross-hatched pencil shading on the robot's shell, smoother controlled linework on the interior gears and circuit traces to read as mechanical, subtle grain texture in the black background",
          "lighting": "high-contrast dark scene, warm orange rim glow around the head and cutaway edge, gears and circuits lit faintly from within, sparkle highlights scattered near the head"
        },
        "materials": {
          "surfaces": "matte orange blocky robot shell (#E8722A) with dark charcoal (#1A1A1A) joint seams, interior mechanism in muted metallic gray gears and dull copper-orange circuit traces, cutaway edge outlined in a clean thin sketch line"
        },
        "composition": {
          "perspective": "flat 2D frontal perspective with a diagrammatic cutaway insert on the head",
          "framing": "centered single-subject composition, landscape 16:9, cutaway detail positioned in the upper-center of the frame at eye level",
          "subject_placement": "robot centered horizontally, head cutaway in the upper third of the frame, sparkle particles distributed loosely around the head for energy without crowding the diagram",
          "safe_area": "64px padding on all sides within 1920x1080 canvas, keep all elements within a 1792x952 safe zone so nothing crops when placed in the 992x558 Canva slot",
          "ui_elements": "none - pure illustration asset, copy lives in the content zone"
        },
        "quality": {
          "include": ["hand-drawn pencil sketch style", "consistent orange blocky robot design", "cross-hatch shading", "solid black background with orange glow", "clear X-ray cutaway diagram convention", "mechanical gears and circuits, no organic shapes", "sparkle accent consistent with reference", "high contrast readability"],
          "avoid": ["photorealism", "flat vector clean fills", "3D CGI rendering", "organic brain or neuron shapes", "cluttered background details", "text or typography baked into image", "inconsistent robot design"],
          "reference_standard": "hand-drawn technical cutaway diagram illustration, blending editorial pencil sketch texture with a blocky robot mascot design system and a dark glowing sparkle-trail energy accent"
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
    "manter o mesmo design do robo em todas as capas - consistencia de personagem",
    "nunca desenhar neuronios organicos ou cerebro dentro do corte - so engrenagens e circuitos simples"
  ]
}
```

---

## Headline ② — "3 FATOS REAIS ESCONDIDOS ATRÁS DA MANCHETE 'CLAUDE ACORDOU'"

### Variação H2-V1 — Manchete rasgada

```json
{
  "template": "carrossel-twitter-post-style",
  "slide": "01-capa",
  "variacao": "H2-V1 - Manchete rasgada",
  "cliente": "Intus Hub",
  "tema": "claude-consciencia-ia",
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
      "copy": "Uma manchete rodou a internet: **'CLAUDE ACORDOU.'**\n\n**3 FATOS REAIS** escondidos atrás dela.\n\nNenhum é o que você imagina.",
      "font_size": "34px - fixo",
      "bold_marking_only": true,
      "no_color_in_text": true
    },
    "image": {
      "slot_within_slide": { "width_px": 992, "height_px": 558, "aspect_ratio": "16:9" },
      "image_generation": { "dimensions": "1920x1080px", "aspect_ratio": "16:9", "orientation": "landscape obrigatorio" },
      "asset_prompt": {
        "scene": {
          "description": "A single hand-drawn pencil-sketch illustration in landscape 16:9 format, warm light beige paper-toned background (#EDE6DA), consistent with the reference image's desk-and-paper scene. A torn newspaper clipping or screen-shaped card sits center frame, its surface printed in a bold sketch-style headline reading exactly 'CLAUDE ACORDOU', the paper physically ripped down the middle into two jagged halves that are peeling apart. Behind the tear, revealed in the gap between the two torn halves, is a simple technical diagram sketched in thin pencil lines: a small neural-network-style diagram of a few connected circles (nodes) and lines (a simplified, non-organic node diagram, not a brain). To the side of the torn clipping, the orange blocky robot mascot — same consistent square-block design, dark charcoal joints — stands with one blocky arm reaching toward the tear, as if it just pulled the paper apart itself, observing the diagram underneath with a simple flat expression (no exaggerated organic face, just a small screen-like display panel where a face would be, showing a neutral flat line). Fine pencil cross-hatching builds the shadow beneath both the paper and the robot. No other text within the image.",
          "subject": "A torn paper headline reading 'CLAUDE ACORDOU' revealing a simple neural-network diagram behind it, with the orange blocky robot mascot beside it pulling the tear open",
          "setting": "Flat light beige textured paper background, single desk-like implied surface, minimal props",
          "action": "The torn halves of the headline peeling apart mid-motion, robot's arm actively engaged in the tear"
        },
        "style": {
          "primary": "hand-drawn pencil-sketch illustration, editorial explainer style with a torn-paper diagram reveal",
          "rendering_quality": "detailed sketch linework, consistent hatching density, controlled diagrammatic linework for the revealed network",
          "surface_textures": "cross-hatched pencil shading on the robot and paper, rough torn paper edge texture, visible paper grain in background",
          "lighting": "flat diffused sketch lighting, soft graphite shadow beneath both elements, subtle warm highlight on the paper's torn edges"
        },
        "materials": {
          "surfaces": "matte orange blocky robot shell (#E8722A) with dark charcoal (#1A1A1A) joint seams, paper clipping in off-white with dark sketch-style bold lettering, torn edges rendered with jagged fibrous pencil linework, revealed diagram in thin uniform graphite lines"
        },
        "composition": {
          "perspective": "flat 2D sketch perspective, slight elevated angle looking down at the torn paper as if on a desk",
          "framing": "centered composition, landscape 16:9, torn paper positioned center-frame with the robot to one side actively interacting",
          "subject_placement": "torn headline occupies the horizontal center of the frame, robot positioned to the left or right third reaching toward it, generous negative space of beige background surrounding both",
          "safe_area": "64px padding on all sides within 1920x1080 canvas, keep all elements within a 1792x952 safe zone so nothing crops when placed in the 992x558 Canva slot",
          "ui_elements": "the only text baked into the image is the torn headline itself, reading exactly 'CLAUDE ACORDOU' in bold hand-sketched capital lettering, dark charcoal ink, positioned across the torn paper prop — not part of the content zone copy"
        },
        "quality": {
          "include": ["hand-drawn pencil sketch style", "consistent orange blocky robot design", "cross-hatch shading", "warm beige paper background", "clear torn-paper reveal mechanic", "simple non-organic node diagram", "editorial explainer mood", "legible torn headline text"],
          "avoid": ["photorealism", "flat vector clean fills", "3D CGI rendering", "organic brain shapes in the revealed diagram", "cluttered background props", "extra unintended text beyond the single headline", "inconsistent robot design"],
          "reference_standard": "hand-drawn technical explainer sketch style, in the spirit of editorial pencil illustration combined with a torn-newspaper reveal device and a blocky robot mascot design system"
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
    "zero cor no corpo do texto no content zone (o texto dentro da imagem e apenas o headline rasgado, elemento de cena)",
    "manter o mesmo design do robo em todas as capas - consistencia de personagem",
    "o texto rasgado deve ser exatamente 'CLAUDE ACORDOU', sem variacao",
    "diagrama revelado deve ser simples e nao organico - nada de formato de cerebro"
  ]
}
```

### Variação H2-V3 — Lupa de detetive sobre a manchete

```json
{
  "template": "carrossel-twitter-post-style",
  "slide": "01-capa",
  "variacao": "H2-V3 - Lupa de detetive sobre a manchete",
  "cliente": "Intus Hub",
  "tema": "claude-consciencia-ia",
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
      "copy": "Uma manchete rodou a internet: **'CLAUDE ACORDOU.'**\n\n**3 FATOS REAIS** escondidos atrás dela.\n\nNenhum é o que você imagina.",
      "font_size": "34px - fixo",
      "bold_marking_only": true,
      "no_color_in_text": true
    },
    "image": {
      "slot_within_slide": { "width_px": 992, "height_px": 558, "aspect_ratio": "16:9" },
      "image_generation": { "dimensions": "1920x1080px", "aspect_ratio": "16:9", "orientation": "landscape obrigatorio" },
      "asset_prompt": {
        "scene": {
          "description": "A single hand-drawn pencil-sketch illustration in landscape 16:9 format, warm light beige paper-toned background (#EDE6DA). A flat headline card lies center frame with bold hand-sketched capital lettering reading exactly 'CLAUDE ACORDOU'. The orange blocky robot mascot — same consistent square-block design, dark charcoal joints — stands beside the card holding a large detective-style magnifying glass with one blocky arm, angling the lens directly over the headline text like it is investigating evidence. Through the circular lens, the headline text underneath is replaced by a small simplified technical diagram — a few connected circles and lines representing a basic network, rendered in thin uniform pencil strokes — visible only within the lens's circular boundary, contrasting with the plain bold headline text outside the lens. Fine pencil cross-hatching builds shadow beneath the robot, the card, and along the magnifying glass rim. No other text within the image.",
          "subject": "Orange blocky robot mascot holding a detective magnifying glass over a headline reading 'CLAUDE ACORDOU', revealing a simple technical diagram through the lens",
          "setting": "Flat light beige textured paper background, headline card as the only prop besides the robot",
          "action": "Robot actively holding and angling the magnifying glass over the headline, investigative pose"
        },
        "style": {
          "primary": "hand-drawn pencil-sketch illustration, editorial explainer / detective-investigation style",
          "rendering_quality": "detailed sketch linework, consistent hatching density, controlled diagrammatic linework visible through the lens",
          "surface_textures": "cross-hatched pencil shading on the robot and card, visible paper grain in background, glass lens rendered with light hatching to suggest transparency and a subtle circular highlight",
          "lighting": "flat diffused sketch lighting, soft graphite shadow beneath all elements, subtle warm highlight along the lens rim"
        },
        "materials": {
          "surfaces": "matte orange blocky robot shell (#E8722A) with dark charcoal (#1A1A1A) joint seams, headline card in off-white with dark sketch-style bold lettering, magnifying glass rim in dull graphite gray, revealed diagram in thin uniform graphite lines"
        },
        "composition": {
          "perspective": "flat 2D sketch perspective, slight three-quarter angle on the robot and card",
          "framing": "centered composition, landscape 16:9, magnifying glass positioned over the horizontal center of the headline card",
          "subject_placement": "headline card centered in the frame, robot positioned to one side holding the lens over the card's middle section, generous negative space of beige background surrounding both",
          "safe_area": "64px padding on all sides within 1920x1080 canvas, keep all elements within a 1792x952 safe zone so nothing crops when placed in the 992x558 Canva slot",
          "ui_elements": "the only text baked into the image is the headline card itself, reading exactly 'CLAUDE ACORDOU' in bold hand-sketched capital lettering, dark charcoal ink — not part of the content zone copy"
        },
        "quality": {
          "include": ["hand-drawn pencil sketch style", "consistent orange blocky robot design", "cross-hatch shading", "warm beige paper background", "clear magnifying-glass reveal mechanic", "simple non-organic node diagram inside the lens", "editorial detective mood", "legible headline text"],
          "avoid": ["photorealism", "flat vector clean fills", "3D CGI rendering", "organic brain shapes in the revealed diagram", "cluttered background props", "extra unintended text beyond the single headline", "inconsistent robot design"],
          "reference_standard": "hand-drawn technical explainer sketch style, in the spirit of editorial pencil illustration combined with a detective magnifying-glass reveal device and a blocky robot mascot design system"
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
    "zero cor no corpo do texto no content zone (o texto dentro da imagem e apenas o headline, elemento de cena)",
    "manter o mesmo design do robo em todas as capas - consistencia de personagem",
    "o texto do headline card deve ser exatamente 'CLAUDE ACORDOU', sem variacao",
    "diagrama revelado dentro da lupa deve ser simples e nao organico"
  ]
}
```

---

## Headline ③ — "ANTES DE COMPARTILHAR QUE A IA GANHOU CONSCIÊNCIA, LEIA ESSES 3 FATOS"

### Variação H3-V2 — Ícone de compartilhamento congelado

```json
{
  "template": "carrossel-twitter-post-style",
  "slide": "01-capa",
  "variacao": "H3-V2 - Icone de compartilhamento congelado",
  "cliente": "Intus Hub",
  "tema": "claude-consciencia-ia",
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
      "copy": "Antes de compartilhar que a IA ganhou consciência...\n\n**LEIA ESSES 3 FATOS.**\n\nDepois decide se ainda quer postar.",
      "font_size": "34px - fixo",
      "bold_marking_only": true,
      "no_color_in_text": true
    },
    "image": {
      "slot_within_slide": { "width_px": 992, "height_px": 558, "aspect_ratio": "16:9" },
      "image_generation": { "dimensions": "1920x1080px", "aspect_ratio": "16:9", "orientation": "landscape obrigatorio" },
      "asset_prompt": {
        "scene": {
          "description": "A single hand-drawn pencil-sketch illustration in landscape 16:9 format, solid black background (#0A0A0A) with a faint warm orange ambient glow, echoing the sparkle-trail energy of the brand's skateboard reference image. The orange blocky robot mascot — square geometric head and torso, dark charcoal joints, same consistent character — stands to one side of the frame, one blocky arm raised toward a classic 'share' icon (three small circles connected by two diagonal lines, the universal share glyph) floating frozen in mid-air at the center of the frame, rendered in the same pencil-hatch linework with a thin outline and subtle orange glow. A small hand-sketched question mark hovers just beside the frozen icon, drawn with the same graphite hatching, conveying hesitation and doubt rather than immediate action. A few small glowing orange sparkle particles are scattered near the icon, consistent with the reference character's energetic glow accents, but the icon itself is visibly static and suspended, not mid-motion. No other text within the image.",
          "subject": "Orange blocky robot mascot standing beside a frozen, floating share icon with a small question mark beside it",
          "setting": "Solid black background with soft ambient orange glow and a few floating sparkle particles",
          "action": "Robot reaching toward the icon but paused, the icon itself suspended motionless in the air"
        },
        "style": {
          "primary": "hand-drawn pencil-sketch illustration, editorial explainer style with a suspended-icon device",
          "rendering_quality": "detailed sketch linework, consistent hatching density, clean controlled linework on the share icon glyph",
          "surface_textures": "cross-hatched pencil shading on the robot's shell, smoother controlled linework on the share icon to read as a clean symbol, subtle grain texture in the black background",
          "lighting": "high-contrast dark scene, warm orange glow radiating faintly from the icon and sparkle particles, soft rim light on the robot's silhouette"
        },
        "materials": {
          "surfaces": "matte orange blocky robot shell (#E8722A) with dark charcoal (#1A1A1A) joint seams, share icon rendered in thin light graphite outline with a faint orange glow fill, question mark in matching thin graphite linework"
        },
        "composition": {
          "perspective": "flat 2D frontal perspective, no deep depth of field",
          "framing": "centered composition, landscape 16:9, frozen share icon positioned at the horizontal center of the frame, robot positioned to one side reaching toward it",
          "subject_placement": "share icon centered in the frame with clear negative space around it to emphasize its suspended stillness, robot occupying roughly one third of the frame to the side, question mark placed just above or beside the icon",
          "safe_area": "64px padding on all sides within 1920x1080 canvas, keep all elements within a 1792x952 safe zone so nothing crops when placed in the 992x558 Canva slot",
          "ui_elements": "none - pure illustration asset, copy lives in the content zone"
        },
        "quality": {
          "include": ["hand-drawn pencil sketch style", "consistent orange blocky robot design", "cross-hatch shading", "solid black background with orange glow", "clean recognizable share icon glyph", "sense of suspended stillness", "subtle question mark for hesitation", "sparkle accent consistent with reference"],
          "avoid": ["photorealism", "flat vector clean fills", "3D CGI rendering", "icon appearing mid-motion or blurred", "cluttered background details", "text or typography baked into image beyond the glyph and question mark", "inconsistent robot design"],
          "reference_standard": "hand-drawn technical explainer sketch style, in the spirit of editorial pencil illustration combined with a frozen-icon suspense device and a blocky robot mascot design system with a dark glowing sparkle-trail energy accent"
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
    "manter o mesmo design do robo em todas as capas - consistencia de personagem",
    "o icone de compartilhar deve estar visivelmente parado/congelado, nunca em movimento ou borrado"
  ]
}
```

### Variação H3-V1 — Dedo pausado no compartilhar

```json
{
  "template": "carrossel-twitter-post-style",
  "slide": "01-capa",
  "variacao": "H3-V1 - Dedo pausado no compartilhar",
  "cliente": "Intus Hub",
  "tema": "claude-consciencia-ia",
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
      "copy": "Antes de compartilhar que a IA ganhou consciência...\n\n**LEIA ESSES 3 FATOS.**\n\nDepois decide se ainda quer postar.",
      "font_size": "34px - fixo",
      "bold_marking_only": true,
      "no_color_in_text": true
    },
    "image": {
      "slot_within_slide": { "width_px": 992, "height_px": 558, "aspect_ratio": "16:9" },
      "image_generation": { "dimensions": "1920x1080px", "aspect_ratio": "16:9", "orientation": "landscape obrigatorio" },
      "asset_prompt": {
        "scene": {
          "description": "A single hand-drawn pencil-sketch illustration in landscape 16:9 format, warm light beige paper-toned background (#EDE6DA), consistent with the reference image's desk-scene lighting. The orange blocky robot mascot — square geometric head and torso, dark charcoal joints, same consistent character — is positioned in front of a simple flat rectangular screen prop (a phone or tablet silhouette, drawn in thin pencil outline, no brand logos), one of its simple blocky manipulator-arms extended with a single squared fingertip hovering just above a circular 'share' button icon on the screen, not yet touching it. Beside the screen, a small hand-sketched warning/pause light — a simple circle with two vertical bars inside it, like a pause symbol, rendered in the same graphite hatching with a subtle warm orange fill — glows softly to signal hesitation. Fine pencil cross-hatching builds shadow beneath the robot and the screen prop. No other text within the image.",
          "subject": "Orange blocky robot mascot with one manipulator arm paused just above a share button on a screen, a small pause/alert light glowing beside it",
          "setting": "Flat light beige textured paper background, a single simple screen prop as the only other object",
          "action": "Robot's fingertip frozen mid-reach, not yet touching the button, a moment of hesitation captured"
        },
        "style": {
          "primary": "hand-drawn pencil-sketch illustration, editorial explainer style with a paused-gesture device",
          "rendering_quality": "detailed sketch linework, consistent hatching density, clean controlled linework on the screen and icon",
          "surface_textures": "cross-hatched pencil shading on the robot's shell, smoother controlled linework on the screen prop and icons to read as clean UI elements, visible paper grain in background",
          "lighting": "flat diffused sketch lighting, soft graphite shadow beneath both elements, a subtle warm orange glow emanating from the pause/alert light only"
        },
        "materials": {
          "surfaces": "matte orange blocky robot shell (#E8722A) with dark charcoal (#1A1A1A) joint seams, screen prop in light gray outline with a thin bezel, share button icon in simple flat dark linework, pause/alert light in warm orange glow fill with dark outline"
        },
        "composition": {
          "perspective": "flat 2D sketch perspective, slight three-quarter angle on the robot and screen",
          "framing": "centered composition, landscape 16:9, screen and share button positioned at the horizontal center-right, robot's arm extending in from the left",
          "subject_placement": "screen prop occupies the center of the frame, robot positioned to the left third with arm extended toward center, pause/alert light placed just above or beside the screen for visual balance",
          "safe_area": "64px padding on all sides within 1920x1080 canvas, keep all elements within a 1792x952 safe zone so nothing crops when placed in the 992x558 Canva slot",
          "ui_elements": "none baked into the image beyond the simple share icon glyph and pause symbol — no additional text, copy lives in the content zone"
        },
        "quality": {
          "include": ["hand-drawn pencil sketch style", "consistent orange blocky robot design", "cross-hatch shading", "warm beige paper background", "clear paused-gesture storytelling", "recognizable share icon glyph", "subtle alert/pause light for tension", "editorial explainer mood"],
          "avoid": ["photorealism", "flat vector clean fills", "3D CGI rendering", "fingertip shown already touching the button", "cluttered background details", "extra unintended text or logos", "inconsistent robot design"],
          "reference_standard": "hand-drawn technical explainer sketch style, in the spirit of editorial pencil illustration combined with a paused-interaction suspense device and a blocky robot mascot design system"
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
    "manter o mesmo design do robo em todas as capas - consistencia de personagem",
    "o fingertip do robo nunca deve estar tocando o botao - deve estar visivelmente pausado antes do toque",
    "nunca incluir logos de marcas reais na tela"
  ]
}
```

---

## Tweaks / Notas

1. Rosto do robô como painel neutro nas cenas H1-V3 e H3-V1 reforça o argumento central (mecanismo, não consciência) — se quiser mais expressividade, dá pra adicionar 2 LEDs simples como "olhos" sem perder o argumento.
2. Hoje só H1-V1 e H3-V2 usam fundo preto com glow; se quiser reforçar o padrão "escuro = tensão/revelação, claro = investigação didática" em todas as 6, dá pra mover H2-V1/H2-V3 para fundo preto também.
3. As 2 variações de cada headline compartilham o mesmo `content.copy` — se quiser testar leituras de copy diferentes por variação (não só a imagem), posso gerar isso.
