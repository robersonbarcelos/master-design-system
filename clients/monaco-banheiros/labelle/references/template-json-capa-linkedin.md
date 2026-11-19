# Template JSON: capa de artigo LinkedIn da LABELLE (versão clara)

Padrão aprovado em 18/11/2026. **Fundo SEMPRE claro (creme `#FAF7F1`)**: nunca verde, nunca escuro. O verde-petróleo `#043333` entra só como cor de texto, nunca como fundo.

Modelo adaptado dos banners LinkedIn da Mônaco (só a estrutura: moldura, gancho, 3 ícones, foto à direita, logo no canto). Cores, logo e trailer da Mônaco não entram.

## Regras fixas
- Formato 16:9, 1600x900, com recuos claros (cerca de 100 px em cima e embaixo, 130 px nas laterais) e moldura fina dourada arredondada.
- Gancho curto em 2 ou 3 linhas, em **Cinzel Regular 400**, caixa alta, fino e delicado. A palavra-chave vai numa barra dourada `#B7881D` com texto em verde-petróleo `#043333`.
- Linha de apoio curta e 3 ícones de linha dourada com legenda curta (só benefício confirmado no perfil: sem climatização, sem preço, sem medida, sem número não validado).
- Foto da cabine LABELLE à direita, fundida ao fundo creme, via `reference_lock` (foto real anexada). Logo da LABELLE no canto superior direito (arquivo anexado, versão escura sobre fundo claro).
- Texto exato dentro da imagem, com acentos. Se o gerador errar letra, corrigir no Canva.
- Telefone, quando aparecer: (11) 95223-2818.

## Título de cada bloco (formato canônico)
```
ARTIGO LINKEDIN · [TEMA]
CAPA [A/B/C]: [EXTERNA/INTERNA/AÉREA] · [cena, enquadramento, luz, elementos de contexto]. Gancho "[GANCHO]" com [PALAVRA] na barra dourada. Anexar: foto externa da cabine LABELLE + logo LABELLE (+ foto do módulo PNE quando for PNE)
```

## Template (preencher os campos entre colchetes)
```json
{
  "format": "LinkedIn article cover, 16:9, 1600x900 (generate at the widest 16:9 size supported and resize to 1600x900)",
  "style": "premium corporate banner: light cream background, thin gold line frame, cinematic photo blended into the right side, clean thin typography",
  "reference_lock": {
    "reference_image": "real photo of the LABELLE restroom cabin, attached to the generation request as the visual reference",
    "instruction": "Use the attached cabin photo as the exact model of the cabin. Reproduce that same cabin inside the scene. Do not invent a new design.",
    "preserve_exactly": [
      "overall shape and proportions",
      "door, handle and lock position",
      "white finish and surface texture",
      "edges, corners and roof line",
      "vents and free/occupied indicator",
      "gold star logo and its position",
      "material and color"
    ],
    "do_not": [
      "redesign the cabin",
      "add windows or extra doors",
      "change colors",
      "add an air conditioner",
      "add any text or logo on the cabin that is not in the reference",
      "make it look like a plastic portable toilet"
    ],
    "adapt_to_scene": {
      "scale": "[real-world scale of the cabin in this scene, proportional to nearby elements]",
      "perspective": "[eye-level three-quarter view | drone view at about 45 degrees], cabin sitting flat on the ground",
      "lighting": "[match the light of the scene]",
      "shadow": "soft contact shadow on the ground consistent with the scene light",
      "reflection": "subtle ambient light and color bounce on the cabin surfaces, no glare",
      "color_grading": "warm neutral grading with soft gold highlights, same as the rest of the photo"
    }
  },
  "layout_reference": {
    "reference_image": "[Mônaco banner used only as layout reference, optional]",
    "instruction": "Use only as a layout reference: thin gold rounded frame with light margins around it, text block on the left, photo on the right fading into the background, logo at the top right, row of 3 icons at the bottom left. Do not copy the Mônaco logo, dark background, colors, trailer or text. Ignore the dark colors of the reference: the LABELLE banner is light."
  },
  "brand_logo": {
    "reference_image": "LABELLE logo file, attached to the generation request",
    "instruction": "Place the attached LABELLE logo exactly as provided, in its original colors as provided (use the dark version on the light background), at the top right corner inside the frame, about 11% of the frame width. Do not redraw or alter it."
  },
  "canvas": {
    "background": "light cream #FAF7F1 (clear and bright, no green, no dark background) with a very subtle warmer tone toward the edges",
    "outer_margin": "light cream margin band of about 100px at top and bottom and about 130px at left and right, as in the reference banners but in light color",
    "frame": "thin rounded rectangle line in gold #B7881D, 2px, inside the margins, about 1340x700px",
    "safe_area": "keep all text and icons at least 48px inside the gold frame; nothing touches the frame or the canvas edges"
  },
  "typography": {
    "headline_font": "Cinzel Regular (weight 400), uppercase, thin and delicate, letter-spacing about 0.08em",
    "headline_colors": "deep teal #043333 for normal lines (dark text on the light background)",
    "highlight_bar": "rounded rectangle filled with gold #B7881D, headline word inside in deep teal #043333, same font",
    "support_and_labels_font": "clean thin sans-serif (Montserrat Medium look), uppercase for icon labels, deep teal"
  },
  "text_elements": {
    "headline_lines": [
      { "text": "[LINHA 1]", "style": "deep teal, large, about 72px" },
      { "text": "[PALAVRA-CHAVE]", "style": "inside gold bar, teal text" }
    ],
    "support_line": {
      "text": "[linha de apoio curta]",
      "style": "deep teal, small sans-serif, with a small gold sparkle icon at the start"
    },
    "icon_row": [
      { "icon": "[thin line icon]", "label": "[LEGENDA 1]" },
      { "icon": "[thin line icon]", "label": "[LEGENDA 2]" },
      { "icon": "[thin line icon]", "label": "[LEGENDA 3]" }
    ],
    "icon_row_style": "3 columns separated by thin gold vertical lines, thin gold line icons inside gold circles, labels in deep teal uppercase small, bottom left of the frame",
    "exact_text_rule": "Render every text exactly as written, with all Portuguese accents (Ó, Ã, Ç, É, Í). No extra words, no placeholder text, no other logos."
  },
  "subject": "[the cabin from the reference image placed in the scene, with 3 or more elements that identify the article theme]",
  "lighting": "[light of the scene]",
  "camera": "[eye-level, 35mm look, f/4, sharp on the cabin | drone view at about 45 degrees, 24mm look, deep focus]",
  "palette": ["#FAF7F1", "#043333", "#B7881D", "#FFFFFF"],
  "composition": "photo occupies the right 55% of the frame and fades into the light cream background on its left edge; cabin at the right third; text block stays on the left",
  "mood": "[mood]",
  "quality": "photorealistic photo, crisp thin typography, clean icon strokes, high resolution, banner-grade finish",
  "negative": "dark green background, teal background, dark background, blue plastic portable toilet, mud, debris piles, air conditioner, third-party logos, Mônaco logo, misspelled words, extra text, watermark, distorted letters, thick heavy fonts, a different cabin design from the reference"
}
```

## Exemplos já gerados (versão clara)
Ver `runs/2026-11-18/capas-linkedin-labelle.md`: plantão de vendas (A), galpão alugado (C e A) e alternativa ao químico (B e C). Ganchos usados: "E O BANHEIRO DO VISITANTE?", "IMÓVEL DE TERCEIRO, BANHEIRO ALUGADO", "GALPÃO ALUGADO: CONSTRUIR OU ALUGAR?", "UM BANHEIRO DE CASA NA OBRA", "A REFORMA NÃO PARA".

Relacionado: `skills/banheiros/banheiros-base-criativos/artigos-labelle-linkedin.md` (modelo de texto e visual).
