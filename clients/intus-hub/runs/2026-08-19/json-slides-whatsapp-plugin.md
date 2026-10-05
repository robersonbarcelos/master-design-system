# JSONs Slides 2-8 — Carrossel WhatsApp Claude Plugin
Template: TEMPLATE-SLIDE-TWITTER-POST · Personagem via referência anexada em cada geração

---

## Slide 2 — Checklist riscado

```json
{
  "variacao": "Slide 2 — Checklist riscado",
  "slide": "2/8",
  "template": "TEMPLATE-SLIDE-TWITTER-POST",
  "format": { "dimensions": "1080x1350px", "aspect_ratio": "4:5", "background": "#FFFFFF" },
  "zones": {
    "header": {
      "avatar": "vazio — adicionar foto de perfil manualmente no Canva",
      "line_1": { "content": "Diego Spanevello | Inteligência Artificial", "font_size": "26px", "font_weight": "semibold 600", "font_color": "#1A1A1A" },
      "line_2": { "content": "@diego.spanevello", "font_size": "22px", "font_weight": "regular 400", "font_color": "#888888" }
    },
    "content": {
      "hook": { "text": "Sem API key. Sem Docker. Sem número de bot.", "font_size": "52px", "font_weight": "900", "font_color": "#1A1A1A" },
      "body": { "text": "O plugin conecta o Claude ao seu número pessoal.\nComo o WhatsApp Web. Só que pra usar o Claude.", "font_size": "28px", "font_weight": "400", "font_color": "#1A1A1A" }
    },
    "image": {
      "slot": "992x558px / 16:9 / border-radius 18px / margem lateral 44px",
      "generation_size": "1920x1080px landscape",
      "asset_prompt": {
        "scene": {
          "description": "Character from attached reference photo stands centered on pure white background holding a giant oversized paper checklist, larger than the character. Checklist has four items in bold black sans-serif: three crossed out with thick red X — '✗ API KEY', '✗ DOCKER', '✗ BOT NUMBER' — and one with a green checkmark below — '✓ Seu WhatsApp'. Character holds paper with both appendages toward camera. Expression: relieved and satisfied, slight smile. Character wears deep purple zip fleece vest. Pure white #FFFFFF background, soft paper shadow.",
          "subject": "Character from attached reference — deep purple zip vest, tortoiseshell glasses. Both appendages holding oversized checklist toward camera. Relieved satisfied expression.",
          "setting": "Pure white seamless background, minimal studio.",
          "action": "Standing, holding giant paper checklist displayed to camera."
        },
        "style": {
          "primary": "Clean commercial 3D CGI, editorial minimalist advertising quality",
          "rendering_quality": "Hyperrealistic 3D render, crisp typography, clean commercial finish",
          "surface_textures": "Paper: off-white matte texture with soft shadow. Red strike-through: bold brush stroke. Green checkmark: clean vector-like. Vest: fleece fabric.",
          "lighting": "Soft even studio lighting from front-top, minimal shadows."
        },
        "technical": {
          "camera": { "focal_length": "85mm", "aperture": "f/8", "depth_of_field": "deep — fully sharp", "angle": "eye level, straight on" },
          "resolution": "1920x1080px landscape 16:9",
          "rendering": "Clean bright render, vivid red/green on white, no grain."
        },
        "materials": { "surfaces": "Paper: cream-white texture, matte. Red marks: bold opaque strokes. Green checkmark: clean flat graphic." },
        "composition": {
          "framing": "Character centered, paper filling most of body width, white background fills edges.",
          "subject_placement": "Character center-frame, paper forward-facing camera, text readable.",
          "safe_area": "1920x1080px. Elements within central 1600x900px safe zone."
        },
        "quality": {
          "include": ["giant oversized paper checklist", "readable red X on 3 items", "readable green check on WhatsApp item", "relieved satisfied expression", "pure white background", "clean commercial composition"],
          "avoid": ["complex background", "small unreadable text", "character not holding paper toward camera", "dark background"],
          "reference_standard": "Apple advertising minimalism, clean tech product advertising"
        }
      }
    }
  },
  "negative_rules": [
    "NUNCA usar travessão (—) no copy",
    "NUNCA usar cor no corpo do texto — apenas negrito",
    "hook travado 52px/900, body travado 28px/400",
    "header line_1 26px semibold, line_2 22px regular — travados",
    "imagem obrigatório 16:9 landscape 1920x1080",
    "border-radius 18px no slot",
    "avatar sempre vazio"
  ]
}
```

---

## Slide 3 — Terminal minimalista

```json
{
  "variacao": "Slide 3 — Terminal minimalista",
  "slide": "3/8",
  "template": "TEMPLATE-SLIDE-TWITTER-POST",
  "format": { "dimensions": "1080x1350px", "aspect_ratio": "4:5", "background": "#FFFFFF" },
  "zones": {
    "header": {
      "avatar": "vazio — adicionar foto de perfil manualmente no Canva",
      "line_1": { "content": "Diego Spanevello | Inteligência Artificial", "font_size": "26px", "font_weight": "semibold 600", "font_color": "#1A1A1A" },
      "line_2": { "content": "@diego.spanevello", "font_size": "22px", "font_weight": "regular 400", "font_color": "#888888" }
    },
    "content": {
      "hook": { "text": "Você instala com 3 comandos.", "font_size": "52px", "font_weight": "900", "font_color": "#1A1A1A" },
      "body": { "text": "O Claude passa a ouvir seu WhatsApp em tempo real.\nVocê manda mensagem, ele responde.\nDo seu número. Como uma conversa normal.", "font_size": "28px", "font_weight": "400", "font_color": "#1A1A1A" }
    },
    "image": {
      "slot": "992x558px / 16:9 / border-radius 18px / margem lateral 44px",
      "generation_size": "1920x1080px landscape",
      "asset_prompt": {
        "scene": {
          "description": "Character from attached reference photo sits hunched forward at retro CRT computer terminal in dark room. Monitor has green phosphor glow (#00FF41) showing exactly three lines of command text in green monospace: 'npm install whatsapp-claude-plugin', 'node config.js', 'node start.js', blinking cursor after third line. One appendage extended toward keyboard, index finger about to press enter. Expression: concentrated, focused, intense. Deep purple zip fleece vest. Dark room (#0A0A0A) lit only by green CRT glow. Empty coffee cup beside keyboard.",
          "subject": "Character from attached reference — deep purple zip vest, tortoiseshell glasses. Hunched forward, appendage extended toward keyboard. Concentrated focused expression, green light on face.",
          "setting": "Dark room, retro CRT terminal, dark wooden desk, empty coffee cup.",
          "action": "Seated, leaning toward screen, about to press enter on third command line."
        },
        "style": {
          "primary": "Cinematic 3D CGI, dark tech atmosphere, retro computing aesthetic",
          "rendering_quality": "Hyperrealistic cinematic render, dramatic single-source lighting",
          "surface_textures": "CRT screen: glass curvature, phosphor scanlines. Keyboard: aged plastic keys. Desk: dark wood.",
          "lighting": "Single source: green CRT glow (#00FF41), dramatic green-tinted light on character, deep shadows behind, high contrast."
        },
        "technical": {
          "camera": { "focal_length": "35mm", "aperture": "f/2.8", "depth_of_field": "moderate shallow — character/screen sharp, room falls to darkness", "angle": "slight low angle, dramatic" },
          "resolution": "1920x1080px landscape 16:9",
          "rendering": "Dark cinematic grade, strong green cast, deep blacks, slight film grain."
        },
        "materials": { "surfaces": "CRT monitor: glass curvature, scanlines, green glow. Keyboard: worn cream/gray plastic. Coffee cup: matte ceramic, empty." },
        "composition": {
          "framing": "Character left-center, monitor right-center, green glow fills left side, darkness fills right/background.",
          "subject_placement": "Character facing screen, monitor with 3 command lines visible right-of-center.",
          "safe_area": "1920x1080px. Elements within central 1700x900px safe zone."
        },
        "quality": {
          "include": ["green CRT phosphor glow as primary light", "exactly 3 command lines in green monospace", "blinking cursor after third line", "appendage extended toward keyboard", "concentrated expression", "dark room atmosphere", "scanlines on CRT", "empty coffee cup"],
          "avoid": ["modern LCD screen", "bright room lighting", "missing command text", "wrong green tone", "extra elements on screen"],
          "reference_standard": "Mr. Robot cinematography, The Matrix terminal scenes, dark developer aesthetic"
        }
      }
    }
  },
  "negative_rules": [
    "NUNCA usar travessão (—) no copy",
    "NUNCA usar cor no corpo do texto — apenas negrito",
    "hook travado 52px/900, body travado 28px/400",
    "header line_1 26px semibold, line_2 22px regular — travados",
    "imagem obrigatório 16:9 landscape 1920x1080",
    "border-radius 18px no slot",
    "avatar sempre vazio"
  ]
}
```

---

## Slide 4 — Controle remoto da vida

```json
{
  "variacao": "Slide 4 — Controle remoto da vida",
  "slide": "4/8",
  "template": "TEMPLATE-SLIDE-TWITTER-POST",
  "format": { "dimensions": "1080x1350px", "aspect_ratio": "4:5", "background": "#FFFFFF" },
  "zones": {
    "header": {
      "avatar": "vazio — adicionar foto de perfil manualmente no Canva",
      "line_1": { "content": "Diego Spanevello | Inteligência Artificial", "font_size": "26px", "font_weight": "semibold 600", "font_color": "#1A1A1A" },
      "line_2": { "content": "@diego.spanevello", "font_size": "22px", "font_weight": "regular 400", "font_color": "#888888" }
    },
    "content": {
      "hook": { "text": "O Claude pediu permissão pra executar uma tarefa.", "font_size": "52px", "font_weight": "900", "font_color": "#1A1A1A" },
      "body": { "text": "Você reage com 👍 no WhatsApp. Ele executa.\nVocê reagiu com 👎. Ele cancela.\nSem abrir o computador.", "font_size": "28px", "font_weight": "400", "font_color": "#1A1A1A" }
    },
    "image": {
      "slot": "992x558px / 16:9 / border-radius 18px / margem lateral 44px",
      "generation_size": "1920x1080px landscape",
      "asset_prompt": {
        "scene": {
          "description": "Character from attached reference photo reclined comfortably on large modern sofa, fully relaxed. Holds giant oversized remote control with two large buttons: green button with 👍 emoji, red button with 👎 emoji. Appendage rests over remote, thumb hovering over green button. In front: floating TV screen (no visible stand) showing WhatsApp interface with message 'Claude está executando...' and progress bar. Expression: completely relaxed, slightly smug, casual power. Deep purple zip fleece vest. Warm living room ambient lighting.",
          "subject": "Character from attached reference — deep purple zip vest, tortoiseshell glasses. Fully reclined on sofa, giant remote in appendage, thumb hovering over green button. Relaxed smug expression.",
          "setting": "Modern comfortable living room, large sofa, floating TV screen showing WhatsApp-Claude task execution, warm ambient lighting.",
          "action": "Reclined on sofa, holding giant remote toward floating screen, thumb hovering over green button."
        },
        "style": {
          "primary": "Hyperrealistic 3D CGI, warm lifestyle commercial, oversized prop comedy",
          "rendering_quality": "Hyperrealistic commercial render, warm photography feel",
          "surface_textures": "Sofa: plush fabric upholstery. Remote: glossy hard plastic with physical buttons. TV screen: OLED with slight glow.",
          "lighting": "Warm ambient room lighting, soft glow from TV screen on character and sofa."
        },
        "technical": {
          "camera": { "focal_length": "50mm", "aperture": "f/3.5", "depth_of_field": "moderate — character/remote sharp, room edges soft", "angle": "slight high angle, three-quarter view" },
          "resolution": "1920x1080px landscape 16:9",
          "rendering": "Warm color grade, soft shadows, commercial lifestyle quality."
        },
        "materials": {
          "fabric": "Sofa: plush upholstery, neutral warm tone.",
          "surfaces": "Remote: glossy ABS plastic, large 👍 green and 👎 red buttons with visible depth. TV screen: OLED displaying WhatsApp interface."
        },
        "composition": {
          "framing": "Character on sofa left-center, floating TV screen right-of-center, remote held forward.",
          "subject_placement": "Character reclined center-left, remote prominently displayed, TV screen background-right.",
          "safe_area": "1920x1080px. Elements within central 1700x900px safe zone."
        },
        "quality": {
          "include": ["giant oversized remote control", "large green 👍 and red 👎 buttons visible", "character fully reclined", "relaxed smug expression", "floating TV showing WhatsApp task", "warm room atmosphere"],
          "avoid": ["character sitting upright", "normal-sized remote", "missing buttons on remote", "cold atmosphere", "blank TV screen"],
          "reference_standard": "Lazy Boy commercial photography, Samsung lifestyle advertising, oversized prop comedy in tech ads"
        }
      }
    }
  },
  "negative_rules": [
    "NUNCA usar travessão (—) no copy",
    "NUNCA usar cor no corpo do texto — apenas negrito",
    "hook travado 52px/900, body travado 28px/400",
    "header line_1 26px semibold, line_2 22px regular — travados",
    "imagem obrigatório 16:9 landscape 1920x1080",
    "border-radius 18px no slot",
    "avatar sempre vazio"
  ]
}
```

---

## Slide 5 — Lista VIP na mão

```json
{
  "variacao": "Slide 5 — Lista VIP na mão",
  "slide": "5/8",
  "template": "TEMPLATE-SLIDE-TWITTER-POST",
  "format": { "dimensions": "1080x1350px", "aspect_ratio": "4:5", "background": "#FFFFFF" },
  "zones": {
    "header": {
      "avatar": "vazio — adicionar foto de perfil manualmente no Canva",
      "line_1": { "content": "Diego Spanevello | Inteligência Artificial", "font_size": "26px", "font_weight": "semibold 600", "font_color": "#1A1A1A" },
      "line_2": { "content": "@diego.spanevello", "font_size": "22px", "font_weight": "regular 400", "font_color": "#888888" }
    },
    "content": {
      "hook": { "text": "Estranhos não chegam até o Claude.", "font_size": "52px", "font_weight": "900", "font_color": "#1A1A1A" },
      "body": { "text": "Você define quem pode interagir.\nNúmero por número. Grupo por grupo.\nNinguém fora da lista toca no seu Claude.", "font_size": "28px", "font_weight": "400", "font_color": "#1A1A1A" }
    },
    "image": {
      "slot": "992x558px / 16:9 / border-radius 18px / margem lateral 44px",
      "generation_size": "1920x1080px landscape",
      "asset_prompt": {
        "scene": {
          "description": "Character from attached reference photo stands in front of glowing doorway, acting as bouncer/gatekeeper. Holds large clipboard with printed name list, some highlighted green (approved). One appendage extended right in 'stop' palm-out gesture toward someone off frame. Behind character, through glowing door: warm exclusive environment with WhatsApp green ambient light. Expression: strict, bureaucratic, one eyebrow raised, unimpressed. Deep purple zip fleece vest. Velvet rope visible at side.",
          "subject": "Character from attached reference — deep purple zip vest, tortoiseshell glasses. One appendage holding clipboard, one extended in stop gesture. Strict unimpressed expression, eyebrow raised.",
          "setting": "Exclusive venue entrance: dark exterior, glowing doorway behind character, velvet rope, warm green-tinted interior visible through door.",
          "action": "Standing guard at door, clipboard in one appendage, other extended in stop gesture."
        },
        "style": {
          "primary": "Cinematic hyperrealistic 3D CGI, nightlife/exclusive venue atmosphere",
          "rendering_quality": "Cinematic render, dramatic door backlighting",
          "surface_textures": "Clipboard: rigid plastic back, matte paper with green highlights. Velvet rope: rich dark velvet. Door: warm glowing backlight.",
          "lighting": "Strong backlight from warm green-tinted doorway creating rim light on character. Dark moody exterior."
        },
        "technical": {
          "camera": { "focal_length": "35mm", "aperture": "f/2.8", "depth_of_field": "shallow — character sharp, interior soft, exterior dark", "angle": "eye level, slight low angle, imposing" },
          "resolution": "1920x1080px landscape 16:9",
          "rendering": "Dramatic moody color grade, strong backlight rim, deep shadows."
        },
        "materials": { "surfaces": "Clipboard: hard plastic, white paper with green highlighted names. Velvet rope: deep burgundy. Door frame: warm glow." },
        "composition": {
          "framing": "Character centered, door behind as backlight source, stop gesture extended right, velvet rope lower-left.",
          "subject_placement": "Character center-frame, slightly blocking doorway, clipboard angled toward camera.",
          "safe_area": "1920x1080px. Character within central safe zone."
        },
        "quality": {
          "include": ["clipboard with visible name list", "green highlights on approved names", "stop gesture extended", "strict unimpressed expression", "dramatic backlight rim", "velvet rope visible"],
          "avoid": ["warm friendly expression", "missing clipboard", "bright even lighting", "missing velvet rope"],
          "reference_standard": "Nightclub photography, exclusive venue commercial imagery, dramatic backlit portrait"
        }
      }
    }
  },
  "negative_rules": [
    "NUNCA usar travessão (—) no copy",
    "NUNCA usar cor no corpo do texto — apenas negrito",
    "hook travado 52px/900, body travado 28px/400",
    "header line_1 26px semibold, line_2 22px regular — travados",
    "imagem obrigatório 16:9 landscape 1920x1080",
    "border-radius 18px no slot",
    "avatar sempre vazio"
  ]
}
```

---

## Slide 6 — Ouvido gigante

```json
{
  "variacao": "Slide 6 — Ouvido gigante",
  "slide": "6/8",
  "template": "TEMPLATE-SLIDE-TWITTER-POST",
  "format": { "dimensions": "1080x1350px", "aspect_ratio": "4:5", "background": "#FFFFFF" },
  "zones": {
    "header": {
      "avatar": "vazio — adicionar foto de perfil manualmente no Canva",
      "line_1": { "content": "Diego Spanevello | Inteligência Artificial", "font_size": "26px", "font_weight": "semibold 600", "font_color": "#1A1A1A" },
      "line_2": { "content": "@diego.spanevello", "font_size": "22px", "font_weight": "regular 400", "font_color": "#888888" }
    },
    "content": {
      "hook": { "text": "Mandou áudio. Ele transcreveu e respondeu.", "font_size": "52px", "font_weight": "900", "font_color": "#1A1A1A" },
      "body": { "text": "Funciona com notas de voz.\nO Whisper roda localmente.\nNada sai do seu computador.", "font_size": "28px", "font_weight": "400", "font_color": "#1A1A1A" }
    },
    "image": {
      "slot": "992x558px / 16:9 / border-radius 18px / margem lateral 44px",
      "generation_size": "1920x1080px landscape",
      "asset_prompt": {
        "scene": {
          "description": "Character from attached reference photo in dramatic close-medium shot in dark purple space. Left appendage extended toward glowing smartphone floating left, playing a voice message with audio waveform lines on screen and WhatsApp interface. Sound wave lines radiate from phone toward character. Right appendage extended toward floating illuminated keyboard, actively typing response. Expression: concentrated, in the zone. Deep purple zip fleece vest. Background: deep dark purple gradient #1A0A2E with luminous sound wave lines.",
          "subject": "Character from attached reference — deep purple zip vest, tortoiseshell glasses. Left appendage toward floating phone, right typing on floating keyboard. Concentrated processing expression.",
          "setting": "Dark surreal digital space, deep purple gradient, floating phone with waveform left, floating keyboard right, glowing sound wave lines.",
          "action": "Actively listening to voice message while simultaneously typing response — parallel input/output."
        },
        "style": {
          "primary": "Cinematic surreal 3D CGI, dark tech atmosphere, AI processing visual metaphor",
          "rendering_quality": "Hyperrealistic cinematic render with luminous glowing elements against dark background",
          "surface_textures": "Phone screen: OLED WhatsApp interface with waveform. Keyboard: translucent illuminated keys. Sound waves: glowing particle lines.",
          "lighting": "Primary: blue-white glow from sound waves. Secondary: green WhatsApp glow from phone. Deep dark purple ambient."
        },
        "technical": {
          "camera": { "focal_length": "50mm", "aperture": "f/2.8", "depth_of_field": "moderate shallow — character/floating elements sharp, space soft", "angle": "eye level, slight three-quarter" },
          "resolution": "1920x1080px landscape 16:9",
          "rendering": "Dark cinematic grade, vivid glowing elements, deep purple treatment."
        },
        "materials": {
          "surfaces": "Floating phone: glass back, OLED with waveform bars. Floating keyboard: translucent acrylic backlit keys. Sound wave lines: glowing particle paths.",
          "transparency": "Keyboard: semi-transparent illuminated acrylic. Sound waves: luminous, slightly transparent."
        },
        "environment": {
          "atmosphere": "Deep dark surreal digital space, purple gradient, glowing elements as only light sources.",
          "particles": "Sound wave lines as glowing particle paths from phone to character."
        },
        "composition": {
          "framing": "Character center, floating phone left-of-center, floating keyboard right-of-center, sound waves connecting left to center.",
          "subject_placement": "Character central, flanked by floating tech elements in one horizontal plane.",
          "safe_area": "1920x1080px. Elements within central 1700x900px safe zone."
        },
        "quality": {
          "include": ["glowing sound wave lines from phone to character", "WhatsApp voice message interface", "floating illuminated keyboard being typed", "concentrated expression", "deep dark purple cinematic atmosphere", "dual action listening/typing"],
          "avoid": ["bright room setting", "character not interacting with both elements", "missing sound wave visualization", "phone screen blank"],
          "reference_standard": "Spotify sound wave visualizations, Apple AirPods commercial cinematography, AI processing visual metaphors"
        }
      }
    }
  },
  "negative_rules": [
    "NUNCA usar travessão (—) no copy",
    "NUNCA usar cor no corpo do texto — apenas negrito",
    "hook travado 52px/900, body travado 28px/400",
    "header line_1 26px semibold, line_2 22px regular — travados",
    "imagem obrigatório 16:9 landscape 1920x1080",
    "border-radius 18px no slot",
    "avatar sempre vazio"
  ]
}
```

---

## Slide 7 — Vitrine do marketplace

```json
{
  "variacao": "Slide 7 — Vitrine do marketplace",
  "slide": "7/8",
  "template": "TEMPLATE-SLIDE-TWITTER-POST",
  "format": { "dimensions": "1080x1350px", "aspect_ratio": "4:5", "background": "#FFFFFF" },
  "zones": {
    "header": {
      "avatar": "vazio — adicionar foto de perfil manualmente no Canva",
      "line_1": { "content": "Diego Spanevello | Inteligência Artificial", "font_size": "26px", "font_weight": "semibold 600", "font_color": "#1A1A1A" },
      "line_2": { "content": "@diego.spanevello", "font_size": "22px", "font_weight": "regular 400", "font_color": "#888888" }
    },
    "content": {
      "hook": { "text": "A Anthropic publicou no marketplace oficial.", "font_size": "52px", "font_weight": "900", "font_color": "#1A1A1A" },
      "body": { "text": "Primeiro plugin de comunidade aprovado por eles.\nUm dev independente construiu.\nA Anthropic revisou e publicou.", "font_size": "28px", "font_weight": "400", "font_color": "#1A1A1A" }
    },
    "image": {
      "slot": "992x558px / 16:9 / border-radius 18px / margem lateral 44px",
      "generation_size": "1920x1080px landscape",
      "asset_prompt": {
        "scene": {
          "description": "Character from attached reference photo stands inside premium retail window display, Apple Store aesthetic. Clean white interior, brightly lit from above. Large backlit sign above reads 'FEATURED'. Character stands on small circular white platform center-frame, posed confidently, one appendage on hip, other extended presenting itself. Expression: proud and poised, professional. Deep purple zip fleece vest. Outside glass: 3-4 dark human silhouettes leaning in, hands cupped against glass looking in admiringly, one pointing at character.",
          "subject": "Character from attached reference — deep purple zip vest, tortoiseshell glasses. Standing on circular platform, one appendage on hip, posed confidently. Proud poised expression.",
          "setting": "Premium retail window display: Apple Store style, white interior, 'FEATURED' backlit sign, circular platform, admirers outside glass.",
          "action": "Standing and posing on display platform, being admired through window by silhouettes outside."
        },
        "style": {
          "primary": "Hyperrealistic 3D CGI, premium retail commercial photography, Apple Store aesthetic",
          "rendering_quality": "Hyperrealistic commercial render, clean product display lighting",
          "surface_textures": "White platform: smooth matte surface. Glass storefront: clear with slight exterior reflection. Backlit sign: even LED illumination.",
          "lighting": "Clean bright overhead display lighting inside, warm product photography feel. Slight warm reflection on glass."
        },
        "technical": {
          "camera": { "focal_length": "50mm", "aperture": "f/4", "depth_of_field": "moderate — character/interior sharp, figures outside slightly soft", "angle": "eye level, straight on" },
          "resolution": "1920x1080px landscape 16:9",
          "rendering": "Clean bright commercial render, premium product display quality, slight glass reflection."
        },
        "materials": {
          "surfaces": "Display platform: smooth white matte pedestal. Glass storefront: clear float glass. 'FEATURED' sign: backlit LED panel. Interior walls: painted white.",
          "transparency": "Storefront glass: clear, slight exterior reflection."
        },
        "composition": {
          "framing": "View from outside looking through glass, character centered on platform inside, sign above, silhouettes at glass edges.",
          "subject_placement": "Character on platform center-frame inside window, silhouettes frame left/right exterior.",
          "safe_area": "1920x1080px. Elements within central 1600x900px safe zone."
        },
        "quality": {
          "include": ["'FEATURED' backlit sign above character", "circular white display platform", "premium Apple Store aesthetic", "admirers outside glass hands cupped", "proud poised expression", "clean white interior lighting"],
          "avoid": ["cluttered retail environment", "missing FEATURED sign", "figures inside with character", "dark moody lighting"],
          "reference_standard": "Apple Store product display photography, premium flagship retail window displays"
        }
      }
    }
  },
  "negative_rules": [
    "NUNCA usar travessão (—) no copy",
    "NUNCA usar cor no corpo do texto — apenas negrito",
    "hook travado 52px/900, body travado 28px/400",
    "header line_1 26px semibold, line_2 22px regular — travados",
    "imagem obrigatório 16:9 landscape 1920x1080",
    "border-radius 18px no slot",
    "avatar sempre vazio"
  ]
}
```

---

## Slide 8 — CTA Megafone no ZAP

```json
{
  "variacao": "Slide 8 — CTA Megafone no ZAP",
  "slide": "8/8",
  "template": "TEMPLATE-SLIDE-TWITTER-POST",
  "format": { "dimensions": "1080x1350px", "aspect_ratio": "4:5", "background": "#FFFFFF" },
  "zones": {
    "header": {
      "avatar": "vazio — adicionar foto de perfil manualmente no Canva",
      "line_1": { "content": "Diego Spanevello | Inteligência Artificial", "font_size": "26px", "font_weight": "semibold 600", "font_color": "#1A1A1A" },
      "line_2": { "content": "@diego.spanevello", "font_size": "22px", "font_weight": "regular 400", "font_color": "#888888" }
    },
    "content": {
      "hook": { "text": "Comenta ZAP que eu te mando o link.", "font_size": "52px", "font_weight": "900", "font_color": "#1A1A1A" },
      "body": { "text": "Plugin gratuito. Código aberto.\nFunciona com seu número pessoal.", "font_size": "28px", "font_weight": "400", "font_color": "#1A1A1A" }
    },
    "image": {
      "slot": "992x558px / 16:9 / border-radius 18px / margem lateral 44px",
      "generation_size": "1920x1080px landscape",
      "asset_prompt": {
        "scene": {
          "description": "Character from attached reference photo stands energetically in wide open space holding giant megaphone with both appendages. Megaphone horn has WhatsApp icon (green circle #128C7E, white phone symbol) printed on it. Radiating from horn: massive bold 3D floating typographic letters spelling 'ZAP' as physical objects in the air. Character leans into megaphone with full energy. Expression: excited, rallying shout, eyes wide, mouth open. Deep purple zip fleece vest. Background: vibrant warm orange gradient #FF6B1A to #E8400A.",
          "subject": "Character from attached reference — deep purple zip vest, tortoiseshell glasses. Both appendages holding giant megaphone, leaning in with full energy. Excited rallying expression, mouth open.",
          "setting": "Minimal wide open space, vivid orange gradient background #FF6B1A to #E8400A.",
          "action": "Shouting into giant megaphone, 'ZAP' letters flying out as physical 3D typography, full-body energy forward."
        },
        "style": {
          "primary": "Hyperrealistic 3D CGI, high energy advertising, bold typographic visual",
          "rendering_quality": "Hyperrealistic commercial render, vivid saturated colors",
          "surface_textures": "Megaphone: metal cone with painted WhatsApp icon. ZAP letters: bold glossy 3D typography with slight bevel.",
          "lighting": "Bright energetic lighting, warm orange rim light matching background, slight glow on ZAP letters."
        },
        "technical": {
          "camera": { "focal_length": "35mm", "aperture": "f/4", "depth_of_field": "moderate — character and megaphone sharp, ZAP letters sharp mid-air", "angle": "slight low angle, dynamic energy" },
          "resolution": "1920x1080px landscape 16:9",
          "rendering": "Vivid saturated commercial render, high energy color grade, no grain."
        },
        "materials": {
          "surfaces": "Megaphone: brushed metal cone, painted green WhatsApp icon. ZAP letters: glossy bold 3D typography, slight bevel and shadow."
        },
        "composition": {
          "framing": "Character centered, megaphone extended forward-left, ZAP letters flying toward camera-right.",
          "subject_placement": "Character center-frame, megaphone diagonal toward camera, typography filling right portion of frame.",
          "safe_area": "1920x1080px. Elements within central 1700x900px safe zone."
        },
        "quality": {
          "include": ["WhatsApp icon clearly visible on megaphone horn", "bold 'ZAP' 3D typography flying from horn", "excited rallying expression", "vibrant orange gradient background", "high energy dynamic pose", "glossy typography with bevel"],
          "avoid": ["small or unreadable ZAP text", "missing WhatsApp icon on megaphone", "flat static pose", "muted or dark background", "calm expression — must be energetic shout"],
          "reference_standard": "Nike energetic advertising campaigns, bold typography motion graphics, high-energy commercial character advertising"
        }
      }
    }
  },
  "negative_rules": [
    "NUNCA usar travessão (—) no copy",
    "NUNCA usar cor no corpo do texto — apenas negrito",
    "hook travado 52px/900, body travado 28px/400",
    "header line_1 26px semibold, line_2 22px regular — travados",
    "imagem obrigatório 16:9 landscape 1920x1080",
    "border-radius 18px no slot",
    "avatar sempre vazio"
  ]
}
```
