# Template JSON: capa de artigo LinkedIn da Mônaco

Padrão aprovado em 18/11/2026. Estrutura e fontes da arte de referência "Conforto para o agro" (moldura creme, aba com logo, serifa com dourado), com as **cores normais da Mônaco: azul marinho, dourado e creme. Nunca roxo, violeta, magenta ou índigo** (o roxo da arte vinha da luz de palco da foto).

## Regras fixas
- Formato 16:9, 1600x900 (a referência é vertical; no LinkedIn o texto fica à esquerda e a foto à direita).
- Cartão arredondado com moldura creme grossa, dentro de uma margem com o mesmo cenário desfocado em azul marinho.
- Aba creme com diagonal no canto superior esquerdo, com o símbolo da Mônaco em azul marinho. No canto superior direito: "MÔNACO MOBILE TOILET" e "EVENTOS • PRODUÇÕES", com fio fino e pontos acima.
- Eyebrow fino e espaçado (branco), headline em serifa de alto contraste (Playfair Display Bold, caixa alta): linha 1 em dourado degradê, linha 2 em branco. Uma linha de apoio em sans. Pílula no rodapé com contorno dourado e 3 benefícios separados por "•".
- Benefícios só com dado do perfil (ar-condicionado quente e frio, tanque lacrado, equipe no local, sem fossa e sem rede, equipe em PT, EN e ES). Sobre cheiro: "o objetivo é que não exista cheiro", sem promessa absoluta.
- Foto real do trailer (ou da bancada interna) via `reference_lock`. A arte de referência é anexada só como estilo e contém logo e nome de cliente real: não copiar.
- Texto exato dentro da imagem, com acentos; se o gerador errar letra, corrigir no Canva.

## Título de cada bloco (formato canônico)
```
ARTIGO LINKEDIN · [TEMA]
CAPA [A/B/C]: [EXTERNA/INTERNA/AÉREA] · [cena, enquadramento, luz, elementos de contexto]. Anexar: foto externa do trailer Mônaco (ou foto interna da cabine) + logo Mônaco (símbolo) + arte de referência 'Conforto para o agro' (só estilo, sem as cores roxas)
```

## Template (preencher os campos entre colchetes)
```json
{
  "format": "LinkedIn article cover, 16:9, 1600x900 (generate at the widest 16:9 size supported and resize to 1600x900)",
  "style": "premium event banner: deep Mônaco navy blue, rounded cream-bordered card with a cinematic photo inside, elegant serif headline with gold gradient, clean sans-serif details",
  "reference_lock": {
    "reference_image": "[real photo of the Mônaco luxury restroom trailer | real photo of the inside of a Mônaco cabin], attached to the generation request as the visual reference",
    "instruction": "Use the attached photo as the exact model. Reproduce that same trailer (or cabin interior) in the scene. Do not invent a new design.",
    "preserve_exactly": [
      "overall shape and proportions of the trailer",
      "body color and gold details exactly as in the photo",
      "Mônaco logo and its position",
      "doors, awning, steps and lower skirt exactly as in the photo",
      "reflective strip and lights at the rear if visible in the photo"
    ],
    "do_not": [
      "redesign the trailer",
      "add or remove doors, awnings or steps",
      "change colors",
      "write any extra text or new logo on the trailer",
      "make it look like a blue plastic chemical toilet"
    ],
    "adapt_to_scene": {
      "scale": "[real-world scale in this scene]",
      "perspective": "[eye-level three-quarter view | close-up at countertop height], sitting flat on the ground",
      "lighting": "[match the light of the scene]",
      "shadow": "soft contact shadow on the ground consistent with the scene light",
      "reflection": "subtle ambient light and color bounce on the body, no glare",
      "color_grading": "deep navy blue tones with warm gold highlights, same as the rest of the photo"
    }
  },
  "style_reference": {
    "reference_image": "arte de referência Mônaco 'CONFORTO PARA O AGRO' (vertical, moldura creme)",
    "instruction": "Use only for style: rounded card with a thick cream border, cream tab with the logo cut into the top-left corner, brand name at the top right with a thin line and dots, spaced-out eyebrow, serif headline in gold gradient plus white, one subline, pill with gold outline at the bottom, blurred and tinted background outside the card. Do NOT copy its purple or indigo colors: use the Mônaco navy blue and gold instead. Do not copy its photo, the horse logo, the event name, the city names or any of its text. The reference is vertical; this cover is horizontal, so the text block goes on the left and the photo fills the right."
  },
  "brand_logo": {
    "reference_image": "Mônaco logo file (the three-point symbol), attached to the generation request",
    "instruction": "Place the attached Mônaco symbol exactly as provided, in dark navy on a cream tab cut into the top-left corner of the card. Do not redraw or alter it."
  },
  "canvas": {
    "background": "outside the card: the same photo enlarged, heavily blurred and tinted deep navy blue #0B1A3A and #16306B, darker toward the bottom, no purple or violet tint",
    "outer_margin": "about 90px of blurred navy blue around the card on all sides",
    "card": "rounded rectangle with 24px radius and a thick cream #F4EFE4 border of about 10px, about 1420x720px, containing the photo",
    "top_left_tab": "cream #F4EFE4 tab with a diagonal cut, holding the logo, cut into the top-left corner of the card",
    "safe_area": "keep all text at least 48px inside the card; nothing touches the border or the canvas edges"
  },
  "typography": {
    "eyebrow_font": "thin geometric sans-serif, uppercase, very wide letter-spacing (about 0.4em), white",
    "headline_font": "high-contrast display serif, bold, uppercase (Playfair Display Bold look)",
    "headline_line_1": "gold gradient from #F2D27A at the top to #B8862B at the bottom",
    "headline_line_2": "white",
    "subline_font": "humanist sans-serif regular (Source Sans look), white, sentence case",
    "brand_text_font": "bold sans-serif uppercase, wide letter-spacing, white; second line lighter weight",
    "pill_font": "sans-serif uppercase, wide letter-spacing, white with gold #F2D27A separators"
  },
  "text_elements": {
    "top_right_brand": { "line_1": "MÔNACO MOBILE TOILET", "line_2": "EVENTOS • PRODUÇÕES", "detail": "thin white line with a dot at each end above the text" },
    "eyebrow": "[EYEBROW]",
    "headline_line_1_gold": "[LINHA 1 EM DOURADO]",
    "headline_line_2_white": "[LINHA 2 EM BRANCO]",
    "subline": "[linha de apoio curta]",
    "bottom_pill": {
      "text": "[BENEFÍCIO 1] • [BENEFÍCIO 2] • [BENEFÍCIO 3]",
      "style": "rounded pill, navy fill #0B1A3A, 2px gold outline, small gold sparkle icon at the start, centered at the bottom inside the card"
    },
    "exact_text_rule": "Render every text exactly as written, with all Portuguese accents (Ô, Ã, Ç, É, Í, À). No extra words, no placeholder text, no other logos."
  },
  "subject": "[the trailer from the reference image placed in the scene, with 3 or more elements that identify the article theme]",
  "lighting": "[light of the scene, no purple]",
  "camera": "[eye-level, 35mm look, f/2.8 to f/4 | close-up, 85mm look, f/2.8]",
  "palette": ["#0B1A3A", "#16306B", "#F2D27A", "#B8862B", "#F4EFE4", "#FFFFFF"],
  "composition": "photo fills the card; trailer on the right two thirds; left third darkened with a smooth navy blue gradient to hold the text",
  "mood": "[mood]",
  "quality": "photorealistic photo, crisp serif headline, clean details, high resolution, banner-grade finish",
  "negative": "light cream background, green background, purple, violet, magenta or indigo tint, blue plastic portable toilet, mud, debris piles, third-party logos, the horse logo and event text from the style reference, misspelled words, extra text, watermark, distorted letters, thick blocky fonts, a different design from the reference photo"
}
```

## Exemplos já gerados
Ver `runs/2026-11-18/capas-linkedin-monaco.md`: "Quem limpa o banheiro às 3 da manhã?", "Seu convidado vem de fora" e "5 cuidados contra o cheiro".

Relacionado: `skills/banheiros/banheiros-base-criativos/artigos-monaco-linkedin.md` (modelo de texto) e o template equivalente da LABELLE (`clients/monaco-banheiros/labelle/references/template-json-capa-linkedin.md`, fundo claro).
