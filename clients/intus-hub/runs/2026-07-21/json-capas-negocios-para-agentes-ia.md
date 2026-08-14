# JSONs de Capa — Os Próximos Grandes Negócios Não Vão Atender Humanos

Data: 2026-07-21
Template usado: `TEMPLATE-SLIDE-TWITTER-POST.json` (versão clara, estilo post de Twitter/X)
Regras aplicadas: fundo branco, corpo 34px fixo sem cor (só negrito), imagem SEMPRE 16:9 landscape (1920x1080px), slot 992x558px, sem footer, avatar vazio para Canva, zero travessão.

---

## JSON 1 — COPY 1 + Ideia 1 (Robô dentro da caixa / gráfico 8B→52B como "céu")

```json
{
  "template": "carrossel-twitter-post-style",
  "version": "clara",
  "slide": "Capa — Variação A",
  "zones": {
    "header": {
      "avatar": { "shape": "circle", "size": "64px", "content": "EMPTY — adicionar no Canva" },
      "text_block": {
        "line_1": "Diego Spanevello | Inteligência Artificial",
        "line_2": "@diego.spanevello"
      },
      "verified_badge": true
    },
    "content": {
      "copy_text": "Esse mercado vai sair de quase **8 bilhões de dólares** para mais de **52 bilhões** até 2030\n\nCrescendo quase **50% ao ano**",
      "font_size": "34px — fixo",
      "font_color": "#1A1A1A",
      "bold_only_marking": true,
      "no_color_in_copy": true
    },
    "image": {
      "slot_px": "992x558 (16:9)",
      "generation_dimensions": "1920x1080px",
      "border_radius": "18px",
      "overlay": "none",
      "asset_prompt": {
        "prompt": {
          "scene": {
            "description": "Wide-angle shot from deep inside a cardboard box looking straight up through the open top flaps, but instead of sky, the opening reveals a glowing exponential growth chart rendered as if it were the sky itself — a steep orange-to-white gradient curve climbing from lower-left to upper-right, with faint grid lines like a stock chart, set against a dark navy-to-black gradient background (#0a0a0a). A compact orange droid robot (rounded head, large glowing cyan-blue oval eyes, small antenna, articulated toy-like body, matte orange plastic shell with visible panel seams) has poked its head fully into the frame from below, muzzle-like sensor array pointed up at the chart, whiskers-like wire antennae catching a soft rim light. The cardboard box interior surrounds the frame on all four sides in soft focus, warm brown corrugated texture visible top and sides, creating a natural vignette around the glowing chart. Dominant palette: cardboard brown (#8B5A2B) framing, deep black-navy background (#0a0a0a), Intus orange accent (#E84000, #FF6020) in the chart line and the robot's shell.",
            "subject": "Compact orange articulated toy-style robot, rounded helmet head, two large glowing cyan-blue eyes, small twin antennae, matte orange plastic body with visible seams and a couple of scuff marks, no human elements",
            "setting": "Interior of an open cardboard box, shot from inside looking up, opening replaced by a glowing data-chart sky",
            "action": "Robot pokes its head/sensor array into the box opening and looks straight up at the glowing growth curve, static pose, curious tilt of the head"
          },
          "style": {
            "primary": "commercial hyperrealistic product photography with a surreal data-visualization twist",
            "rendering_quality": "hyperrealistic, high-detail, glossy plastic render mixed with photographic cardboard texture",
            "surface_textures": "matte painted plastic on the robot with subtle wear, corrugated cardboard fiber texture on the box interior, smooth glowing gradient on the chart",
            "lighting": "single soft key light from directly above simulating the glow of the chart, warm rim light bouncing off the cardboard walls, cool cyan fill from the robot's own eye-glow"
          },
          "technical": {
            "camera": {
              "focal_length": "16mm",
              "aperture": "f/1.4",
              "depth_of_field": "very shallow — robot head sharp, box walls falling into soft blur at the edges of frame",
              "angle": "extreme low angle, first-person POV from inside the box looking straight up"
            },
            "resolution": "ultra high definition",
            "rendering": "clean digital render, no grain, deep dynamic range between the dark box interior and the glowing chart",
            "physics_accuracy": "correct perspective distortion from the wide-angle lens, chart glow casting believable soft light on the cardboard walls closest to the opening"
          },
          "materials": {
            "surfaces": "corrugated cardboard with visible fiber strands and a few soft creases; robot shell in semi-gloss orange plastic with fine dust and light scuffing for realism; chart surface has a subtle emissive glow like an OLED display"
          },
          "environment": {
            "atmosphere": "no haze, clean crisp air inside the box, soft glow bloom around the chart",
            "time": "ambiguous / studio-lit, glow reads as an artificial data light rather than natural daylight",
            "particles": "faint dust motes visible catching the light near the box opening"
          },
          "composition": {
            "perspective": "strong wide-angle convergence toward the chart, box edges as natural framing lines pulling the eye to center",
            "framing": "centered subject with box walls as a natural frame-within-frame",
            "subject_placement": "robot head centered low in frame, chart glow fills the upper two-thirds",
            "safe_area": "image occupies a locked 992x558px 16:9 slot inside the 1080x1350px slide; keep all key visual elements (robot head, chart peak) within the central 90% of the 16:9 frame so nothing is lost to the 18px border-radius crop",
            "ui_elements": "none inside the generated image — headline and copy are handled separately by the content zone of the template, not baked into the image"
          },
          "quality": {
            "include": ["hyperrealistic plastic robot", "cardboard macro texture", "exponential growth chart glow", "extreme wide-angle distortion", "commercial product photography", "high dynamic range", "cyan-orange color contrast", "cute-meets-tech mood"],
            "avoid": ["human hands or human presence", "text baked into the image", "cartoonish flat illustration", "washed out low-contrast chart", "distorted or unreadable numbers", "cluttered background", "logo watermarks", "blown-out highlights on the chart"],
            "reference_standard": "commercial pet-product advertising photography (wide-angle box-POV genre) crossed with fintech data-visualization design language"
          }
        }
      }
    },
    "footer": { "exists": false }
  },
  "negative_rules": [
    "sem travessao",
    "sem headline ultra bold condensada",
    "sem cor no corpo do texto — so negrito",
    "imagem sempre 16:9 landscape, nunca quadrada ou retrato",
    "avatar vazio para Canva",
    "sem footer duplicado"
  ]
}
```

---

## JSON 2 — COPY 1 + Ideia 2 (Robô com celular / gráfico pixelado 8B→52B)

```json
{
  "template": "carrossel-twitter-post-style",
  "version": "clara",
  "slide": "Capa — Variação B",
  "zones": {
    "header": {
      "avatar": { "shape": "circle", "size": "64px", "content": "EMPTY — adicionar no Canva" },
      "text_block": {
        "line_1": "Diego Spanevello | Inteligência Artificial",
        "line_2": "@diego.spanevello"
      },
      "verified_badge": true
    },
    "content": {
      "copy_text": "Esse mercado vai sair de quase **8 bilhões de dólares** para mais de **52 bilhões** até 2030\n\nCrescendo quase **50% ao ano**",
      "font_size": "34px — fixo",
      "font_color": "#1A1A1A",
      "bold_only_marking": true,
      "no_color_in_copy": true
    },
    "image": {
      "slot_px": "992x558 (16:9)",
      "generation_dimensions": "1920x1080px",
      "border_radius": "18px",
      "overlay": "none",
      "asset_prompt": {
        "prompt": {
          "scene": {
            "description": "A white humanoid cyberpunk robot with a smooth helmet-like head and a glowing cyan-blue visor holds up a smartphone in a selfie-style pose with both articulated robotic hands, arms extended toward camera. The phone screen faces the viewer and displays a growth chart graphic that is heavily pixelated/mosaic-blurred across most of its surface, except two crisp, sharp numeric labels floating over the blur: '8B' near the bottom-left of the chart and '52B' near the top-right, connected by a barely-visible ascending line ghosted through the pixelation. Background is a rain-slicked nighttime city street with bokeh from colorful neon signage (magenta, cyan, amber) heavily defocused, classic Times-Square-at-night mood. Dominant palette: cool white/silver robot chassis, glowing cyan-blue accents, warm-cool neon bokeh background, with the Intus orange (#E84000) appearing subtly as one of the numeric labels' glow color to tie to brand.",
            "subject": "White humanoid robot, smooth helmet head, glowing cyan visor with a single vertical light strip, articulated white plastic and dark joint hands holding a black smartphone",
            "setting": "Rainy neon-lit city street at night, shallow focus turning the background into soft colorful bokeh",
            "action": "Robot holds the phone up toward camera in selfie framing; the phone screen shows a mostly-obscured growth chart with only two numbers legible"
          },
          "style": {
            "primary": "cinematic cyberpunk commercial photography",
            "rendering_quality": "hyperrealistic, glossy CG-photo hybrid render",
            "surface_textures": "smooth semi-matte white plastic/metal robot shell with fine panel lines, wet reflective asphalt in the background, glass screen surface with visible pixelation artifact texture",
            "lighting": "mixed neon color lighting from the background bouncing onto the robot's glossy shell, a cool blue key light from the phone screen illuminating the robot's face and hands from below"
          },
          "technical": {
            "camera": {
              "focal_length": "35mm",
              "aperture": "f/2.0",
              "depth_of_field": "shallow — robot head and phone sharp, background neon fully melted into bokeh",
              "angle": "eye level, slightly low, selfie POV looking up at the robot"
            },
            "resolution": "ultra high definition",
            "rendering": "cinematic color grade, subtle bloom around neon highlights and screen glow, clean noise-free render",
            "physics_accuracy": "correct screen-glow bounce light on robot chassis, believable rain reflections on wet pavement in background bokeh"
          },
          "materials": {
            "surfaces": "robot: smooth painted polymer with fine seams and subtle wear scuffs on the knuckles; phone: matte-black chassis with a glossy glass screen showing a deliberately pixelated mosaic texture over the chart graphic"
          },
          "environment": {
            "atmosphere": "light rain haze, wet-street reflections, humid night air with visible neon glow diffusion",
            "time": "night, urban",
            "particles": "fine rain droplets caught in the neon light near the edges of frame"
          },
          "composition": {
            "perspective": "slight low angle selfie perspective, phone screen positioned dead-center as the focal point",
            "framing": "centered, phone screen occupying the visual middle third",
            "subject_placement": "robot head and phone screen both within the central safe zone, hands framing the screen symmetrically",
            "safe_area": "image occupies a locked 992x558px 16:9 slot inside the 1080x1350px slide; keep the phone screen and the two numeric labels within the central 85% of frame so they are never cropped by the 18px border-radius",
            "ui_elements": "on the phone screen only: two sharp floating numeric labels '8B' and '52B' in a clean sans-serif white/orange glow font, positioned respectively lower-left and upper-right of the pixelated chart graphic — no other text anywhere in the image"
          },
          "quality": {
            "include": ["cyberpunk humanoid robot", "neon bokeh city night", "pixelated screen mystery effect", "sharp floating numeric labels", "cinematic commercial lighting", "rain-slicked reflections", "curiosity-driven composition", "high production value CG-photo hybrid"],
            "avoid": ["fully readable chart details", "human faces in background", "text anywhere outside the phone screen", "flat illustration style", "overexposed neon blowing out detail", "cluttered signage text", "logo watermarks", "cartoonish robot design"],
            "reference_standard": "cyberpunk product-tech advertising photography in the style of Blade-Runner-inspired commercial campaigns, mixed with fintech app-screen mockup design language"
          }
        }
      }
    },
    "footer": { "exists": false }
  },
  "negative_rules": [
    "sem travessao",
    "sem headline ultra bold condensada",
    "sem cor no corpo do texto — so negrito",
    "imagem sempre 16:9 landscape, nunca quadrada ou retrato",
    "avatar vazio para Canva",
    "sem footer duplicado"
  ]
}
```

---

## JSON 3 — COPY 2 + Ideia 2 (Robô com celular / silhueta humana pixelada com X)

```json
{
  "template": "carrossel-twitter-post-style",
  "version": "clara",
  "slide": "Capa — Variação C",
  "zones": {
    "header": {
      "avatar": { "shape": "circle", "size": "64px", "content": "EMPTY — adicionar no Canva" },
      "text_block": {
        "line_1": "Diego Spanevello | Inteligência Artificial",
        "line_2": "@diego.spanevello"
      },
      "verified_badge": true
    },
    "content": {
      "copy_text": "Em 2030 esse mercado vai valer **52 bilhões de dólares**\n\nE o cliente **não existe**",
      "font_size": "34px — fixo",
      "font_color": "#1A1A1A",
      "bold_only_marking": true,
      "no_color_in_copy": true
    },
    "image": {
      "slot_px": "992x558 (16:9)",
      "generation_dimensions": "1920x1080px",
      "border_radius": "18px",
      "overlay": "none",
      "asset_prompt": {
        "prompt": {
          "scene": {
            "description": "A white humanoid cyberpunk robot with a smooth helmet head and glowing cyan-blue visor holds up a smartphone in selfie pose with both articulated hands, arms extended toward camera. The phone screen shows a heavily pixelated/mosaic-blurred human silhouette outline, generic and faceless, with a single sharp glowing red-orange X mark and a floating question mark hovering over the chest area of the silhouette, both crisp against the blur. Background is the same rain-slicked nighttime city street with defocused colorful neon bokeh (magenta, cyan, amber). Dominant palette: cool white/silver robot chassis, glowing cyan visor, warm-cool neon bokeh, with a sharp red-orange X/question-mark as the single high-contrast focal accent tying to the Intus orange brand tone.",
            "subject": "White humanoid robot, smooth helmet head, glowing cyan visor, articulated white plastic hands holding a black smartphone",
            "setting": "Rainy neon-lit city street at night, shallow focus turning background into soft bokeh",
            "action": "Robot holds the phone toward camera; the screen shows a pixelated human silhouette marked with an X and a question mark, implying the human customer cannot be found or defined"
          },
          "style": {
            "primary": "cinematic cyberpunk commercial photography",
            "rendering_quality": "hyperrealistic, glossy CG-photo hybrid render",
            "surface_textures": "smooth semi-matte white plastic/metal robot shell with fine panel lines, wet reflective asphalt in background, glass screen with visible pixelation artifact texture",
            "lighting": "mixed neon color lighting from the background bouncing onto the robot's glossy shell, cool blue key light from the phone screen illuminating the robot's face and hands from below, warm red-orange glow emanating specifically from the X/question-mark graphic"
          },
          "technical": {
            "camera": {
              "focal_length": "35mm",
              "aperture": "f/2.0",
              "depth_of_field": "shallow — robot head and phone sharp, background fully melted into bokeh",
              "angle": "eye level, slightly low, selfie POV looking up at the robot"
            },
            "resolution": "ultra high definition",
            "rendering": "cinematic color grade, subtle bloom around neon highlights and screen glow, clean noise-free render",
            "physics_accuracy": "correct screen-glow bounce light on robot chassis, believable rain reflections on wet pavement in background"
          },
          "materials": {
            "surfaces": "robot: smooth painted polymer with fine seams and subtle wear scuffs on the knuckles; phone: matte-black chassis with glossy glass screen showing a deliberately pixelated human silhouette"
          },
          "environment": {
            "atmosphere": "light rain haze, wet-street reflections, humid night air with visible neon diffusion",
            "time": "night, urban",
            "particles": "fine rain droplets caught in neon light near frame edges"
          },
          "composition": {
            "perspective": "slight low angle selfie perspective, phone screen positioned dead-center as focal point",
            "framing": "centered, phone screen occupying the visual middle third",
            "subject_placement": "robot head and phone screen within central safe zone, silhouette and X/question-mark centered on the screen",
            "safe_area": "image occupies a locked 992x558px 16:9 slot inside the 1080x1350px slide; keep the phone screen and the X/question-mark graphic within the central 85% of frame so nothing is cropped by the 18px border-radius",
            "ui_elements": "on the phone screen only: a pixelated grey human silhouette outline with a sharp glowing red-orange X mark over the chest and a floating question mark near the head — no legible text or letters anywhere in the image"
          },
          "quality": {
            "include": ["cyberpunk humanoid robot", "neon bokeh city night", "pixelated silhouette mystery effect", "sharp red-orange X accent", "cinematic commercial lighting", "rain-slicked reflections", "conceptual absence-of-human-customer visual metaphor", "high production value CG-photo hybrid"],
            "avoid": ["recognizable human face on screen", "readable text or letters in the image", "human faces in background", "flat illustration style", "overexposed neon blowing out detail", "cluttered signage text", "logo watermarks", "cartoonish robot design"],
            "reference_standard": "cyberpunk product-tech advertising photography in the style of Blade-Runner-inspired commercial campaigns, mixed with UX-error-state iconography design language"
          }
        }
      }
    },
    "footer": { "exists": false }
  },
  "negative_rules": [
    "sem travessao",
    "sem headline ultra bold condensada",
    "sem cor no corpo do texto — so negrito",
    "imagem sempre 16:9 landscape, nunca quadrada ou retrato",
    "avatar vazio para Canva",
    "sem footer duplicado"
  ]
}
```

---

## JSON 4 — COPY 2 + Ideia 3 (Vigilância / mira vazia — "NO HUMAN DETECTED")

```json
{
  "template": "carrossel-twitter-post-style",
  "version": "clara",
  "slide": "Capa — Variação D",
  "zones": {
    "header": {
      "avatar": { "shape": "circle", "size": "64px", "content": "EMPTY — adicionar no Canva" },
      "text_block": {
        "line_1": "Diego Spanevello | Inteligência Artificial",
        "line_2": "@diego.spanevello"
      },
      "verified_badge": true
    },
    "content": {
      "copy_text": "Em 2030 esse mercado vai valer **52 bilhões de dólares**\n\nE o cliente **não existe**",
      "font_size": "34px — fixo",
      "font_color": "#1A1A1A",
      "bold_only_marking": true,
      "no_color_in_copy": true
    },
    "image": {
      "slot_px": "992x558 (16:9)",
      "generation_dimensions": "1920x1080px",
      "border_radius": "18px",
      "overlay": "none",
      "asset_prompt": {
        "prompt": {
          "scene": {
            "description": "A CCTV-surveillance-alert style composition on a light grey background with subtle horizontal scanline texture. Bold red uppercase typography at the top reads 'SURVEILLANCE ALERT'. Below it, a white facial-recognition bounding-box reticle (corner-bracket rectangle) is positioned in the center of the frame, but it frames completely empty space — no face, no subject, nothing inside it, just the grey scanline background. A single blurred claw-like mechanical gripper hand reaches into frame from the bottom-left corner, out of focus, pointing toward the empty bounding box. Small uppercase technical caption text sits in the bottom-right corner reading 'NO HUMAN DETECTED' and below it 'CLIENT: UNDEFINED'. A data timestamp reading 'DATA UPDATE 17:56:00' sits at the bottom, and 'CCTV 01' appears in the top-left corner in small monospace type. Dominant palette: light grey (#D9D9D9) background, alert red (#E8342A) headline, white UI elements, black monospace caption text, with a faint Intus orange (#E84000) tint on the bounding-box corners to tie to brand.",
            "subject": "An empty facial-recognition bounding box floating in the center of the frame — no human or animal subject present, the absence itself is the subject",
            "setting": "Flat studio-style CCTV monitor aesthetic, light grey scanline background",
            "action": "Static surveillance frame scanning for a subject and finding nothing, gripper hand reaching toward the void"
          },
          "style": {
            "primary": "editorial commercial graphic design with photographic gripper-hand element",
            "rendering_quality": "hyperrealistic for the mechanical hand, clean flat vector-like precision for the UI/typography elements",
            "surface_textures": "matte grey scanline texture background, glossy metallic mechanical claw with visible joints and light reflections",
            "lighting": "flat, even studio lighting with no strong shadows, a single soft rim light on the mechanical claw for dimensionality"
          },
          "technical": {
            "camera": {
              "focal_length": "50mm",
              "aperture": "f/5.6",
              "depth_of_field": "moderate — background and UI elements sharp, gripper hand in foreground softly defocused",
              "angle": "eye level, flat frontal composition"
            },
            "resolution": "high definition",
            "rendering": "clean digital composite, crisp vector-sharp typography, subtle scanline noise texture across the background",
            "physics_accuracy": "believable metallic reflections on the claw, correct soft-focus falloff on the foreground gripper"
          },
          "materials": {
            "surfaces": "brushed metal and dark rubber joints on the mechanical claw with fine scratches; matte paper-like grey background with fine horizontal scanline grain"
          },
          "composition": {
            "perspective": "flat frontal, minimal depth, graphic-poster style layering",
            "framing": "centered bounding-box reticle as focal point with typography anchored to top and bottom edges",
            "subject_placement": "empty reticle dead-center, red headline top-center, gripper hand entering from bottom-left, captions bottom-right, timestamp bottom-center, 'CCTV 01' top-left",
            "safe_area": "image occupies a locked 992x558px 16:9 slot inside the 1080x1350px slide; keep all typography and the reticle within the central 88% of frame, at least 40px from all image edges so nothing is clipped by the 18px border-radius",
            "ui_elements": "top-left small monospace label 'CCTV 01' in black; top-center bold red condensed headline 'SURVEILLANCE ALERT' in two lines; center white bounding-box reticle (corner brackets only, no fill); bottom-right small uppercase monospace caption in two lines 'NO HUMAN DETECTED' and 'CLIENT: UNDEFINED'; bottom-center small monospace timestamp 'DATA UPDATE 17:56:00'"
          },
          "quality": {
            "include": ["CCTV surveillance graphic aesthetic", "empty facial-recognition reticle", "bold red alert typography", "mechanical claw foreground element", "editorial poster composition", "conceptual absence-of-customer metaphor", "clean scanline texture", "high-contrast red-grey-white palette"],
            "avoid": ["any face or figure inside the bounding box", "cluttered background elements", "cartoonish claw design", "low-contrast unreadable typography", "color bleeding outside intended red/grey/white palette", "logo watermarks other than the specified CCTV/timestamp labels"],
            "reference_standard": "surveillance-alert meme poster design language (CCTV/facial-recognition graphic genre) combined with clean editorial tech-brand typography systems"
          }
        }
      }
    },
    "footer": { "exists": false }
  },
  "negative_rules": [
    "sem travessao",
    "sem headline ultra bold condensada",
    "sem cor no corpo do texto — so negrito",
    "imagem sempre 16:9 landscape, nunca quadrada ou retrato",
    "avatar vazio para Canva",
    "sem footer duplicado"
  ]
}
```

---

## JSON 5a — COPY 3 + Ideia 3 (Vigilância com humano no lugar do animal — "ROLE UNDER REDEFINITION")

```json
{
  "template": "carrossel-twitter-post-style",
  "version": "clara",
  "slide": "Capa — Variação E",
  "zones": {
    "header": {
      "avatar": { "shape": "circle", "size": "64px", "content": "EMPTY — adicionar no Canva" },
      "text_block": {
        "line_1": "Diego Spanevello | Inteligência Artificial",
        "line_2": "@diego.spanevello"
      },
      "verified_badge": true
    },
    "content": {
      "copy_text": "O cargo que mais vai crescer em 2026 **não existe ainda**\n\n**Gestor de agentes de IA**",
      "font_size": "34px — fixo",
      "font_color": "#1A1A1A",
      "bold_only_marking": true,
      "no_color_in_copy": true
    },
    "image": {
      "slot_px": "992x558 (16:9)",
      "generation_dimensions": "1920x1080px",
      "border_radius": "18px",
      "overlay": "none",
      "asset_prompt": {
        "prompt": {
          "scene": {
            "description": "A CCTV-surveillance-alert style composition on a light grey background with subtle horizontal scanline texture, same visual system as the original fox reference but with the animal replaced by a human. Bold red uppercase typography at the top reads 'SURVEILLANCE ALERT'. Below it, a white facial-recognition bounding-box reticle frames the face of an adult person emerging from underneath a large black computer mouse prop, exactly at the same low angle and camera height as the original reference, mouth open in the same startled, alert expression, wide eyes looking directly at camera. A blurred human hand with fingers spread like a claw reaches into frame from the bottom-left foreground, fingertips soft and defocused, mirroring the original claw pose. Small uppercase technical caption text in the bottom-right corner reads 'ROLE UNDER REDEFINITION'. A data timestamp reading 'DATA UPDATE 17:56:00' sits at the bottom, and 'CCTV 01' appears in the top-left corner in small monospace type. Dominant palette: light grey (#D9D9D9) background, alert red (#E8342A) headline, black computer-mouse prop, natural skin tones, white UI elements.",
            "subject": "An adult human face and one raised hand emerging from beneath an oversized black computer mouse, same pose/angle/expression as the original fox reference — startled, mouth slightly open, eyes wide and alert, looking straight at the camera",
            "setting": "Flat studio-style CCTV monitor aesthetic, light grey scanline background, oversized black mouse prop as the central object",
            "action": "The person peeks out from under the mouse with an alarmed expression while a facial-recognition reticle locks onto their face"
          },
          "style": {
            "primary": "editorial commercial graphic design with photographic human-portrait element",
            "rendering_quality": "hyperrealistic for the human subject and mouse prop, clean flat vector-like precision for UI/typography elements",
            "surface_textures": "matte grey scanline texture background, glossy black plastic on the oversized mouse prop, natural skin texture on the person",
            "lighting": "flat, even studio lighting with a soft key light on the face to preserve visible skin texture, minimal shadow, gentle rim light separating the subject from the grey background"
          },
          "technical": {
            "camera": {
              "focal_length": "50mm",
              "aperture": "f/4",
              "depth_of_field": "moderate-shallow — face and mouse sharp, foreground hand softly defocused",
              "angle": "low angle, camera at the same low height as the original reference looking slightly up at the face"
            },
            "resolution": "ultra high definition",
            "rendering": "clean digital composite, crisp vector-sharp typography, subtle scanline noise texture across the background",
            "physics_accuracy": "believable soft shadow of the mouse prop on the person's shoulders, correct soft-focus falloff on the foreground hand"
          },
          "materials": {
            "skin": "medium skin tone, neutral undertone. Visible open pores on forehead and cheekbones. Fine individual peach fuzz hairs catching light. Natural minor imperfections scattered across nose and cheekbones. Matte finish — skin absorbs light rather than reflects. NO foundation finish, NO highlight powder, NO cosmetic gloss, NO airbrushed smoothing. Zero post-processing. Natural lived-in skin.",
            "surfaces": "glossy black plastic mouse shell with fine scuff marks and a visible scroll-wheel texture; matte grey paper-like background with fine horizontal scanline grain"
          },
          "composition": {
            "perspective": "flat frontal-low angle, graphic-poster style layering matching the original reference exactly",
            "framing": "centered bounding-box reticle around the face as focal point, typography anchored to top and bottom edges",
            "subject_placement": "face centered within the reticle, hand entering from bottom-left foreground, captions bottom-right, timestamp bottom-center, 'CCTV 01' top-left",
            "safe_area": "image occupies a locked 992x558px 16:9 slot inside the 1080x1350px slide; keep the face, reticle, and all typography within the central 88% of frame, at least 40px from all image edges so nothing is clipped by the 18px border-radius",
            "ui_elements": "top-left small monospace label 'CCTV 01' in black; top-center bold red condensed headline 'SURVEILLANCE ALERT' in two lines; center white bounding-box reticle framing the person's face; bottom-right small uppercase monospace caption 'ROLE UNDER REDEFINITION'; bottom-center small monospace timestamp 'DATA UPDATE 17:56:00'"
          },
          "quality": {
            "include": ["CCTV surveillance graphic aesthetic", "realistic human skin texture", "facial-recognition reticle on human subject", "bold red alert typography", "startled authentic expression", "editorial poster composition", "conceptual role-shift metaphor", "high-contrast red-grey-white palette"],
            "avoid": ["plastic skin", "airbrushed skin", "poreless skin", "CGI smoothness", "wax texture", "cosmetic sheen", "specular hotspot on forehead", "beauty retouch", "frequency separation", "cartoonish exaggerated expression", "logo watermarks other than specified labels"],
            "reference_standard": "surveillance-alert meme poster design language (CCTV/facial-recognition graphic genre) combined with Peter Lindbergh-style unretouched portrait realism for the human subject"
          }
        }
      }
    },
    "footer": { "exists": false }
  },
  "negative_rules": [
    "sem travessao",
    "sem headline ultra bold condensada",
    "sem cor no corpo do texto — so negrito",
    "imagem sempre 16:9 landscape, nunca quadrada ou retrato",
    "avatar vazio para Canva",
    "sem footer duplicado",
    "pele humana nunca plastica ou com retoque de beleza"
  ]
}
```

---

## JSON 5b — COPY 3 + Ideia 1 (Robô dentro da caixa / "céu" com janelas/telas dos agentes geridos)

```json
{
  "template": "carrossel-twitter-post-style",
  "version": "clara",
  "slide": "Capa — Variação F",
  "zones": {
    "header": {
      "avatar": { "shape": "circle", "size": "64px", "content": "EMPTY — adicionar no Canva" },
      "text_block": {
        "line_1": "Diego Spanevello | Inteligência Artificial",
        "line_2": "@diego.spanevello"
      },
      "verified_badge": true
    },
    "content": {
      "copy_text": "O cargo que mais vai crescer em 2026 **não existe ainda**\n\n**Gestor de agentes de IA**",
      "font_size": "34px — fixo",
      "font_color": "#1A1A1A",
      "bold_only_marking": true,
      "no_color_in_copy": true
    },
    "image": {
      "slot_px": "992x558 (16:9)",
      "generation_dimensions": "1920x1080px",
      "border_radius": "18px",
      "overlay": "none",
      "asset_prompt": {
        "prompt": {
          "scene": {
            "description": "Wide-angle shot from deep inside a cardboard box looking straight up through the open top flaps, but instead of sky, the opening reveals a dark navy void filled with multiple softly glowing rectangular windows/screens floating at different depths, like a grid of dashboard panels or agent-status monitors, each screen a soft blue-white or orange glow with abstract UI shapes (no readable text), arranged like scattered floating windows receding into depth. A compact orange droid robot (rounded head, large glowing cyan-blue oval eyes, small antenna, articulated toy-like matte orange plastic body with visible panel seams) has poked its head fully into frame from below, sensor array pointed up at the floating panels as if surveying a team it now oversees. The cardboard box interior surrounds the frame on all sides in soft focus, warm brown corrugated texture visible top and sides. Dominant palette: cardboard brown (#8B5A2B) framing, deep navy-black background (#0a0a0a), Intus orange accent (#E84000, #FF6020) glowing on the robot shell and echoed faintly in one or two of the floating panels.",
            "subject": "Compact orange articulated toy-style robot, rounded helmet head, two large glowing cyan-blue eyes, small twin antennae, matte orange plastic body with visible seams",
            "setting": "Interior of an open cardboard box shot from inside looking up, opening replaced by a floating grid of glowing agent-dashboard windows in a dark void",
            "action": "Robot pokes its head into the box opening and looks up at the floating panels, as if surveying a team of agents it now manages, static curious pose"
          },
          "style": {
            "primary": "commercial hyperrealistic product photography with a surreal data-dashboard twist",
            "rendering_quality": "hyperrealistic, glossy plastic render mixed with photographic cardboard texture, soft-glow UI panel rendering",
            "surface_textures": "matte painted plastic on the robot with subtle wear, corrugated cardboard fiber texture on the box interior, smooth glowing gradient on each floating panel",
            "lighting": "multiple soft point-light sources from the floating panels casting gentle mixed blue and orange glow upward onto the cardboard walls, cool cyan fill from the robot's own eye-glow"
          },
          "technical": {
            "camera": {
              "focal_length": "16mm",
              "aperture": "f/1.4",
              "depth_of_field": "very shallow — robot head sharp, box walls softly blurred, floating panels sharp near center and softly blurred toward the edges of frame to suggest depth",
              "angle": "extreme low angle, first-person POV from inside the box looking straight up"
            },
            "resolution": "ultra high definition",
            "rendering": "clean digital render, no grain, deep dynamic range between the dark box interior and the glowing panels",
            "physics_accuracy": "correct wide-angle perspective distortion, panel glow casting believable soft light on the nearest cardboard walls"
          },
          "materials": {
            "surfaces": "corrugated cardboard with visible fiber strands and soft creases; robot shell in semi-gloss orange plastic with fine dust and light scuffing; panel surfaces have a subtle emissive glow like layered OLED windows"
          },
          "environment": {
            "atmosphere": "no haze, clean crisp air inside the box, soft glow bloom around each floating panel",
            "time": "ambiguous / studio-lit, glow reads as artificial dashboard light",
            "particles": "faint dust motes visible catching light near the box opening"
          },
          "composition": {
            "perspective": "strong wide-angle convergence toward the panel grid, box edges as natural framing lines pulling the eye upward and to center",
            "framing": "centered subject with box walls as a natural frame-within-frame",
            "subject_placement": "robot head centered low in frame, floating panel grid fills the upper two-thirds at varying depths",
            "safe_area": "image occupies a locked 992x558px 16:9 slot inside the 1080x1350px slide; keep the robot head and the densest cluster of panels within the central 90% of the 16:9 frame so nothing is lost to the 18px border-radius crop",
            "ui_elements": "none inside the generated image — the floating panels show only abstract glowing UI shapes, no readable text; headline and copy are handled separately by the content zone of the template"
          },
          "quality": {
            "include": ["hyperrealistic plastic robot", "cardboard macro texture", "floating agent-dashboard panels", "extreme wide-angle distortion", "commercial product photography", "high dynamic range", "cyan-orange color contrast", "management/oversight visual metaphor"],
            "avoid": ["human hands or human presence", "readable text baked into the image", "cartoonish flat illustration", "washed out low-contrast panels", "cluttered or overly busy panel grid", "logo watermarks", "blown-out highlights on the panels"],
            "reference_standard": "commercial pet-product advertising photography (wide-angle box-POV genre) crossed with SaaS command-center dashboard visual design language"
          }
        }
      }
    },
    "footer": { "exists": false }
  },
  "negative_rules": [
    "sem travessao",
    "sem headline ultra bold condensada",
    "sem cor no corpo do texto — so negrito",
    "imagem sempre 16:9 landscape, nunca quadrada ou retrato",
    "avatar vazio para Canva",
    "sem footer duplicado"
  ]
}
```
