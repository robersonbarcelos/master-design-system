# Template Carrossel — Colagem de Poses + Shop the Look
**Cliente:** Carol Staggemeier
**Formato fixo:** 1080x1350px · 4:5 Instagram Feed
**Criado em:** 2026-07-16

> Template de carrossel completo — CAPA (colagem de N modelos/poses) + SLIDE (card shop the look: peças + acessórios + modelo).
> Ambas as peças usam os mesmos gates de pré-geração: **nunca gerar JSON sem passar pelo gate primeiro.**
> Este template complementa (não substitui) `TEMPLATE-CAPA-CAROL.json`, `TEMPLATE-SLIDE-CAROL.json`, `TEMPLATE-CTA-CAROL.json`, `TEMPLATE-CABIDE-CAROL.md` e `TEMPLATE-COLAGEM-CAROL.md`.

---

## Como usar

```
1. Rode o GATE CAPA (seção abaixo) antes de montar a capa do carrossel
2. Rode o GATE SLIDE (seção abaixo) para CADA card do carrossel — um gate por card
3. Preencha os placeholders só com o que foi confirmado no gate — nunca deixe campo aberto para a IA "completar"
4. Todo item marcado como "não incluído" vira proibição explícita em negative_rules — nunca apenas omissão
5. Cole o JSON no gerador junto com TODAS as fotos de referência confirmadas no gate (peça, acessório, modelo)
```

---

## ⚠️ Regra central deste template

**Nunca gerar um JSON de capa ou de card sem antes obter as respostas do gate correspondente.**

Motivo: nas primeiras gerações de teste, a IA generativa recebeu placeholders vazios (`[MOLETOM/BLUSA]`, `[BRINCO]`) sem gate nem foto de referência — e "inventou" peças e acessórios que não existem no acervo da Carol (moletom verde militar, calça bege, relógio dourado genérico). O gate existe para eliminar esse risco: cada campo do JSON final só existe se foi explicitamente confirmado.

---

## GATE CAPA — Colagem de N modelos/poses

**Perguntar sempre, nesta ordem, antes de montar o JSON da capa:**

| # | Pergunta | Formato de resposta |
|---|----------|---------------------|
| 1 | Quantas modelos/poses vão aparecer na capa? | número exato — 1, 2, 3 ou 4 |
| 2 | As poses são idênticas (espelhadas/simétricas) ou cada modelo com pose própria? | idêntica / variada |
| 3 | Qual o título da capa? | texto exato — ex: "Looks em preto." |
| 4 | Qual fundo? | Linho `#e5ded3` / Areia Quente `#c2b6a5` / Verde Floresta `#273d29` / Café Terroso `#4c3529` |
| 5 | Vai ter foto de referência de cada modelo/look anexada? | obrigatório sim — sem foto não há fidelidade de rosto/roupa |
| 6 | Para cada modelo: descrição do look (peça a peça) e traços físicos (cabelo, maquiagem, joias) | uma descrição por modelo, na ordem em que aparecem na capa |

**Regra de geração:** o JSON monta **exatamente N blocos de modelo** — nunca mais, nunca "arredondado" para 4 por padrão. Se a resposta for "2", o `scene.description` e o `composition` descrevem apenas duas figuras, cada uma ocupando a mesma proporção de frame, e nenhuma menção a uma terceira ou quarta figura aparece em lugar nenhum do prompt.

---

## GATE SLIDE — Card Shop the Look

**Perguntar sempre, nesta ordem, antes de montar o JSON de cada card:**

| # | Pergunta | Formato de resposta |
|---|----------|---------------------|
| 1 | Quais peças de roupa serão carregadas? | listar exatamente — ex: "vestido" (1 peça) ou "moletom + calça" (2 peças) |
| 2 | Quais acessórios serão carregados? | marcar item a item: brinco / colar / relógio / óculos / bolsa / sapato / cinto / boné / anel / pulseira — sim ou não para cada um |
| 3 | Vai ter modelo vestindo o look completo no card? | sim / não |
| 4 | Qual fundo? | Linho `#e5ded3` / Areia Quente `#c2b6a5` — escolher pelo contraste com a cor da peça |
| 5 | Foto de referência de cada item confirmado (peça, acessório, modelo) anexada? | obrigatório sim |
| 6 | Vai ter label/pill com nome do look? | sim (texto exato) / não |

**Regra de geração:**
- O JSON cria **um bloco por item confirmado como "sim"** — nada além disso.
- Todo item marcado "não" entra em `negative_rules_dinamicas` como proibição explícita (não apenas omissão do campo) — ver exemplo abaixo.
- O layout se reconfigura pela quantidade real de itens: 1 peça só ocupa a coluna inteira da zona esquerda; 1 acessório fica centralizado na coluna do meio em vez de 4 espaços vazios ou inventados.

**Exemplo de preenchimento do gate (vestido + brinco, sem mais nada):**

```json
"itens_confirmados": {
  "roupa": ["vestido — 1 peça, sem peça de baixo separada"],
  "acessorios_incluidos": ["brinco"],
  "acessorios_excluidos_explicitamente": ["relógio", "óculos", "bolsa", "sapato", "cinto", "colar", "boné", "anel", "pulseira"],
  "modelo": true,
  "label": false
}
```

---

## Regras fixas — aplicam-se a CAPA e SLIDE deste template

- **GARMENT FIDELITY LOCK:** reproduzir cada peça exatamente como na foto de referência — sem redesign, sem reinterpretação, sem detalhe adicionado
- **Tecido sempre MATTE:** zero shimmer, zero lurex, zero brilho metálico, zero sparkle — exceto sheen natural de queda em seda/cetim genuíno (nunca especular)
- **Skin realism standard obrigatório** em todo prompt com pessoa — pele com poro visível, sem retoque, sem acabamento plástico (ver fórmula completa abaixo)
- **PRESERVE EXACT MODEL FACIAL LIKENESS** — nunca suavizar, rejuvenescer ou padronizar rosto da modelo de referência
- **Header padrão fixo** (reutilizado do `TEMPLATE-CAPA-CAROL.json`): `CAROL STAGGEMEIER` (Nunito Sans Bold 18px, caixa alta, letter-spacing 3px, esquerda) + `MODA AUTORAL` (Nunito Sans Regular 18px, caixa alta, letter-spacing 3px, direita) — cor adaptada ao fundo, opacidade 45%
- **Footer da capa:** `arraste para ver →` centralizado, Nunito Sans Regular 18px, opacidade ~50%
- **Fundo:** nunca branco puro `#FFFFFF` nem preto puro `#000000` — sempre dentro da paleta oficial (Linho, Areia Quente, Verde Floresta, Café Terroso)
- **Sem travessão (—)** em qualquer texto do prompt ou da capa
- **Máximo 3 tamanhos de fonte** por peça

### Fórmula skin realism (aplicar em `materials.skin` sempre que houver pessoa)

```
[fair/medium/dark] skin, [warm/cool/neutral] undertone. Visible open pores on forehead
and cheekbones. Fine individual peach fuzz hairs catching light. Natural [freckles /
minor imperfections / uneven skin tone] scattered across nose and cheekbones. Matte
finish — skin absorbs light rather than reflects. NO foundation finish, NO highlight
powder, NO cosmetic gloss, NO airbrushed smoothing. Zero post-processing. Natural
lived-in skin.
```
Proibir sempre em `quality.avoid`: `plastic skin, airbrushed skin, poreless skin, CGI smoothness, wax texture, cosmetic sheen, specular hotspot on forehead, beauty retouch, frequency separation`
Referência: Peter Lindbergh + Paolo Roversi.

---

## CAPA — Estrutura D · Colagem de N Modelos (parametrizável)

> Preencher `N` e os blocos de modelo apenas com o que foi confirmado no GATE CAPA.

```json
{
  "template": "carrossel-carol",
  "peca": "capa",
  "estrutura": "D_colagem_poses",
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "safe_area": "952x1222px (64px mínimo todos os lados)"
  },
  "gate_respostas": {
    "quantidade_modelos": "[N — confirmado no gate]",
    "tipo_pose": "[idêntica | variada — confirmado no gate]",
    "titulo": "[TÍTULO EXATO — confirmado no gate]",
    "fundo_hex": "[#e5ded3 | #c2b6a5 | #273d29 | #4c3529 — confirmado no gate]"
  },
  "prompt": {
    "scene": {
      "description": "Editorial fashion Instagram carousel cover (1080x1350px, 4:5 ratio). [N] full-length models standing side by side against a shared seamless [FUNDO] background, captured as if in the exact same photo session — identical camera distance, identical eye-level height, identical floor plane, identical light direction and shadow falloff across all [N] figures, so all outfits read as one continuous scene rather than separate photos placed together. All [N] models occupy equal visual scale (same head-to-floor proportion in frame), evenly spaced left to right, feet aligned on the same baseline. [LISTAR AQUI 1 BLOCO POR MODELO CONFIRMADA NO GATE — nome/posição + descrição exata do look peça a peça + traços físicos exatos, na ordem em que aparecem da esquerda para a direita. NÃO adicionar blocos além dos N confirmados.] GARMENT FIDELITY LOCK: reproduce every outfit exactly as shown in reference photographs — no redesign, no silhouette alteration, no added details. PRESERVE EXACT MODEL FACIAL LIKENESS for each model per reference photos — do not smooth, rejuvenate or standardize faces. Header top of frame: 'CAROL STAGGEMEIER' Nunito Sans Bold 18px all caps letter-spacing 3px left-aligned + 'MODA AUTORAL' Nunito Sans Regular 18px all caps letter-spacing 3px right-aligned, thin horizontal separator line below at 30% opacity, both at 45% opacity adapted to background contrast. Above the models, centered headline in Halant Bold Italic: '[TÍTULO]' — sentence case, period at end. Footer bottom center: 'arraste para ver →' Nunito Sans Regular 18px, ~50% opacity.",
      "subject": "[N] full-length models standing side by side in matching scale and lighting, each in a distinct confirmed outfit, reading as one unified studio scene",
      "setting": "Seamless [FUNDO] backdrop, single studio session, identical camera and light setup across all figures",
      "action": "Static — all models standing naturally, pose per gate answer (idêntica ou variada), unified as one continuous frame"
    },
    "style": {
      "primary": "editorial fashion lookbook cover, slow-fashion styling guide, multi-look comparison in single scene",
      "rendering_quality": "hyperrealistic, editorial print quality, ultra high resolution",
      "surface_textures": "[DESCREVER TEXTURA DE CADA TECIDO CONFIRMADO — uma linha por peça]",
      "lighting": "Single large diffused softbox, 4200K warm, positioned identically relative to all models — same angle, same height, same falloff — producing matching soft shadow direction and length behind every figure. No lighting mismatch anywhere in the frame."
    },
    "technical": {
      "camera": {
        "focal_length": "50mm — same lens and distance for all models, ensures identical perspective compression on every figure",
        "aperture": "f/5.6",
        "depth_of_field": "moderate-deep — all models fully sharp, background clean and consistent",
        "angle": "eye level, straight on, zero tilt — camera height locked identical across all figures"
      },
      "resolution": "ultra high definition, 1080x1350px, 4:5 Instagram carousel cover ratio",
      "rendering": "Warm matte editorial tonality, very slight grain, single consistent color grade across the full frame — no visible seam or tonal jump between figures"
    },
    "materials": {
      "skin": "[fair/medium/dark] skin, [warm/cool/neutral] undertone. Visible open pores on forehead and cheekbones. Fine individual peach fuzz hairs catching light. Natural minor imperfections scattered across nose and cheekbones. Matte finish — skin absorbs light rather than reflects. NO foundation finish, NO highlight powder, NO cosmetic gloss, NO airbrushed smoothing. Zero post-processing. Natural lived-in skin — consistent treatment across all models.",
      "fabric": "EXACT REPRODUCTION MANDATORY per outfit — [DESCREVER TECIDO E CONSTRUÇÃO DE CADA LOOK CONFIRMADO] — FORBIDDEN: shimmer, sparkle, glitter, lurex, metallic thread, plastic sheen beyond each fabric's natural confirmed finish.",
      "surfaces": "Backdrop: seamless [FUNDO HEX], matte, uniform behind all models — no gradient shift anywhere across the frame."
    },
    "composition": {
      "perspective": "Flat frontal, [N]-panel symmetric split, identical vanishing point and horizon line for all models",
      "framing": "1080x1350px 4:5. [N] models evenly spaced, each occupying [100/N]% width approximately, generous negative space between figures.",
      "subject_placement": "Header spans full width at top. Headline centered ~15% from top edge. All [N] models centered vertically in the lower ~70% of frame, feet aligned on identical baseline.",
      "safe_area": "64px padding all sides. Safe zone 952x1222px inside 1080x1350px. Header 80px from top. Footer minimum 44px from bottom edge.",
      "ui_elements": "Header: 'CAROL STAGGEMEIER' + 'MODA AUTORAL' conforme padrão fixo. Headline: '[TÍTULO]' Halant Bold Italic ~56px. Footer: 'arraste para ver →' Nunito Sans Regular 18px."
    },
    "quality": {
      "include": [
        "[N] models matched in scale, camera distance and eye-level",
        "identical lighting direction and shadow quality across all figures",
        "seamless single-scene read despite distinct outfits",
        "exact garment fidelity per confirmed look",
        "natural unretouched skin on all models",
        "header and footer consistent with Carol Staggemeier brand system",
        "Halant Bold Italic headline legible and centered",
        "seamless matte backdrop in confirmed brand color"
      ],
      "avoid": [
        "mismatched scale between models",
        "different camera height or distance creating perspective inconsistency",
        "inconsistent shadow direction or light temperature between figures",
        "visible seam or tonal jump in background",
        "plastic skin, airbrushed skin, poreless skin, CGI smoothness, wax texture, cosmetic sheen, specular hotspot on forehead, beauty retouch, frequency separation",
        "shimmer, sparkle, glitter, lurex or metallic thread on any fabric",
        "headline or header overlapping models",
        "cropped feet or heads",
        "any model, pose or accessory NOT confirmed in the gate"
      ],
      "reference_standard": "Editorial styling-guide cover, twin/multi-figure studio comparison shoot, Kinfolk multi-figure editorial layout, consistent single-session studio lighting standard. Peter Lindbergh + Paolo Roversi for skin."
    }
  }
}
```

---

## SLIDE — Card Shop the Look (parametrizável)

> Preencher apenas os blocos de peça/acessório confirmados no GATE SLIDE. Todo item "não incluído" vira proibição explícita em `negative_rules_dinamicas`.

> ⚠️ **Correção canônica (aplicada após teste do SLIDE-01):** o card usa composição **split 50/50** — metade flat lay dos itens confirmados, metade modelo vestindo o look completo — sempre sobre **UM ÚNICO fundo contínuo** (nunca duas tonalidades/exposições diferentes, nunca costura visível no centro). O `header_padrao` (CAROL STAGGEMEIER / MODA AUTORAL) é **obrigatório em todo SLIDE**, não só na capa. O label do look vira **texto centralizado na base do frame, fonte Halant Bold Italic ~44px** (mesma família tipográfica do headline da capa) — nunca mais a pill pequena de 16px.

```json
{
  "template": "carrossel-carol",
  "peca": "slide",
  "estrutura": "shop_the_look_split",
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "safe_area": "952x1222px (64px mínimo todos os lados)"
  },
  "gate_respostas": {
    "roupa": ["[LISTAR PEÇAS CONFIRMADAS — ex: vestido]"],
    "acessorios_incluidos": ["[LISTAR SÓ OS CONFIRMADOS COMO SIM]"],
    "acessorios_excluidos": ["[LISTAR TODOS OS MARCADOS COMO NÃO]"],
    "modelo_presente": "[true | false]",
    "fundo_hex": "[#e5ded3 | #c2b6a5]",
    "label": "[texto exato ou false]"
  },
  "prompt": {
    "scene": {
      "description": "Editorial fashion Instagram feed post (1080x1350px, 4:5 ratio), 'shop the look' styling card. CRITICAL: the ENTIRE 1080x1350px canvas is ONE single continuous seamless [FUNDO HEX] backdrop — same exact color value, same exposure, same warm 4200K light temperature, same soft shadow falloff from edge to edge. This must read as one uncut photograph taken in a single studio session, NEVER as two separate photos placed side by side — absolutely no visible seam, no color shift, no gradient break, no exposure difference down the center line. At the very top, header_padrao fixo: 'CAROL STAGGEMEIER' Nunito Sans Bold 18px, caixa alta, letter-spacing 3px, alinhado à esquerda + 'MODA AUTORAL' Nunito Sans Regular 18px, mesmo estilo, alinhado à direita, cor adaptada ao fundo a 45% de opacidade, com linha separadora fina de 1px a 30% de opacidade logo abaixo, atravessando toda a largura da safe area. Below the header, split into 2 equal vertical halves on the same unbroken backdrop. LEFT half: exact flat-lay reproduction of [LISTAR APENAS AS PEÇAS DE ROUPA E ACESSÓRIOS CONFIRMADOS] arranged as in the reference flat-lay photograph, same relative scale and spacing, generous negative space between items — no other item type appears anywhere in frame. [SE modelo_presente = true:] RIGHT half: one full-length model photograph wearing the complete confirmed look, standing naturally, three-quarter angle, gazing off-camera — wearing ONLY the confirmed garments and accessories, nothing added. [SE modelo_presente = false:] no model in this card — flat-lay-only composition, layout reflows to fill the frame with garment and accessory items only. Both halves share the identical background color, identical light direction, identical shadow softness — verify no tonal mismatch anywhere. GARMENT FIDELITY LOCK: reproduce every confirmed garment and accessory exactly as shown in reference photographs — no redesign, no reinterpretation, no substitution, no addition of items not confirmed in the gate. ALL FABRIC STRICTLY MATTE — zero shimmer, zero lurex, zero metallic thread, zero sparkle, zero satin sheen except where source material is genuinely silk/satin (soft drape sheen only, never specular). [SE modelo_presente = true:] PRESERVE EXACT MODEL FACIAL LIKENESS from reference: [DESCREVER CABELO, TRAÇOS, MAQUIAGEM DA MODELO CONFIRMADA]. [SE label confirmado:] At the bottom of the frame, centered text in Halant Bold Italic (same typeface family used on the cover headline), size 44px: '[TEXTO DO LABEL]' — no pill, no background box, plain centered text sitting directly on the backdrop, GRANDE e claramente legível, nunca pequeno como legenda de rodapé.",
      "subject": "Shop-the-look split card containing only the confirmed items: [LISTAR TUDO CONFIRMADO]. No item outside this list appears anywhere in frame.",
      "setting": "Seamless single-tone [FUNDO HEX] backdrop, continuous across the entire frame with zero seam, single studio lighting session",
      "action": "Static editorial styling card — flat-lay-to-outfit visual translation, split composition on one unbroken background"
    },
    "style": {
      "primary": "editorial styling guide, shop-the-look product card, slow-fashion brand consistency",
      "rendering_quality": "hyperrealistic, editorial print quality, ultra high resolution",
      "surface_textures": "[DESCREVER TEXTURA DE CADA PEÇA E ACESSÓRIO CONFIRMADO — uma linha por item]",
      "lighting": "Single large diffused softbox, 4200K warm, identical angle, height and falloff across the ENTIRE frame — flat-lay half and model half must show matching light and shadow, no hot spots, no gradient jump, no exposure difference anywhere."
    },
    "technical": {
      "camera": {
        "focal_length": "50mm flat-lay half, 85mm model half (se presente)",
        "aperture": "f/8 flat-lay half, f/4 model half (se presente)",
        "depth_of_field": "deep flat-lay half, moderate-shallow model half (se presente)",
        "angle": "overhead/straight-on flat lay para o lado esquerdo, eye-level three-quarter para a modelo no lado direito (se presente)"
      },
      "resolution": "ultra high definition, 1080x1350px, 4:5 Instagram feed ratio",
      "rendering": "Warm matte editorial tonality, very slight grain, single consistent color grade applied to the ENTIRE canvas as one image — no per-half color correction, no visible seam. NO specular highlights on fabric."
    },
    "materials": {
      "skin": "[APENAS SE modelo_presente = true] [fair/medium/dark] skin, [warm/cool/neutral] undertone. Visible open pores on forehead and cheekbones. Fine individual peach fuzz hairs catching light. Natural minor imperfections scattered across nose and cheekbones. Matte finish. NO foundation finish, NO highlight powder, NO cosmetic gloss, NO airbrushed smoothing. Zero post-processing.",
      "fabric": "EXACT REPRODUCTION MANDATORY — [DESCREVER TECIDO, COR, SILHUETA, CONSTRUÇÃO DE CADA PEÇA CONFIRMADA] — FORBIDDEN on any fabric area: shimmer, sparkle, glitter, lurex, metallic thread, specular highlight.",
      "surfaces": "Backdrop: ONE single seamless [FUNDO HEX] surface, matte, perfectly uniform color from edge to edge — same value on left half, right half, top and bottom. Accessórios confirmados: [DESCREVER MATERIAL REAL DE CADA UM — ex: ouro escovado, couro grão]. Nenhum acessório fora da lista confirmada aparece em nenhuma parte do frame."
    },
    "composition": {
      "perspective": "Flat frontal overhead na metade esquerda, three-quarter eye-level na metade direita (se modelo presente), ambas sobre o mesmo plano de fundo",
      "framing": "1080x1350px 4:5, split vertical exato 50/50 — metade esquerda flat lay, metade direita modelo (se presente) — sobre UM ÚNICO fundo contínuo, sem costura visível",
      "subject_placement": "Header padrão no topo, largura total. [DESCREVER POSIÇÃO EXATA DE CADA PEÇA E ACESSÓRIO CONFIRMADO NA METADE ESQUERDA — sem mencionar itens excluídos]. Metade direita: modelo de corpo inteiro centralizada verticalmente (se presente). Rodapé: texto do label centralizado na base, largura total do frame (se confirmado).",
      "safe_area": "64px padding all sides. Safe zone 952x1222px inside 1080x1350px. Nenhum elemento encosta na borda ou na linha central de divisão. Header 80px do topo. Texto de rodapé no mínimo 60px da borda inferior.",
      "ui_elements": [
        { "elemento": "header esquerda", "texto": "CAROL STAGGEMEIER", "fonte": "Nunito Sans Bold", "tamanho": "18px", "posicao": "topo esquerda" },
        { "elemento": "header direita", "texto": "MODA AUTORAL", "fonte": "Nunito Sans Regular", "tamanho": "18px", "posicao": "topo direita" },
        { "elemento": "linha separadora", "descricao": "1px, 30% opacidade, largura total da safe area", "posicao": "abaixo do header" },
        { "elemento": "texto inferior", "texto": "[TEXTO DO LABEL, se confirmado]", "fonte": "Halant Bold Italic", "tamanho": "44px", "alinhamento": "centralizado", "posicao": "base do frame, sem pill, sem caixa de fundo", "observacao_critica": "texto deve renderizar GRANDE — nunca no tamanho de uma legenda pequena ou nota de rodapé" }
      ]
    },
    "quality": {
      "include": [
        "single continuous seamless background across the entire frame",
        "identical color, exposure and lighting on both halves",
        "exact reproduction of only the confirmed garments and accessories",
        "flat-lay arrangement matching reference layout closely",
        "true material response on accessories no artificial gloss",
        "editorial shop-the-look clarity",
        "model face consistent with reference photo (se presente)",
        "header_padrao presente e legível no topo",
        "texto inferior grande e centralizado, mesma fonte da capa (se label confirmado)"
      ],
      "avoid": [
        "two different background tones",
        "visible seam or color break down the center",
        "collage effect, two photos stitched together look",
        "exposure or lighting mismatch between halves",
        "any item not confirmed in the gate appearing anywhere in frame",
        "generic cold gray background",
        "any shimmer sparkle glitter lurex on fabric",
        "plastic or airbrushed skin (se modelo presente)",
        "specular hotspots on jewelry or bag hardware",
        "garment redesign or reinterpretation",
        "missing header_padrao",
        "rodapé pequeno ou ilegível",
        "vignette or heavy post-processing"
      ],
      "reference_standard": "Personal stylist shop-the-look editorial, Net-a-Porter styling grid, The Frankie Shop product-to-outfit translation, Baserange matte fabric standard."
    }
  },
  "negative_rules_dinamicas": [
    "[GERAR 1 LINHA POR ACESSÓRIO/PEÇA EXCLUÍDA NO GATE — formato: 'NO [item] anywhere in frame']"
  ],
  "negative_rules": [
    "Sem travessão (—) em nenhum texto",
    "GARMENT FIDELITY LOCK: reproduzir cada peça e acessório exatamente como nas fotos de referência, sem redesenhar",
    "PRESERVE EXACT MODEL FACIAL LIKENESS conforme foto de referência (se presente)",
    "Composição sempre split 50/50 sobre UM ÚNICO fundo contínuo — nunca duas tonalidades ou uma linha de corte visível",
    "header_padrao (CAROL STAGGEMEIER / MODA AUTORAL) sempre presente no topo",
    "Texto do label sempre centralizado na base, fonte Halant Bold Italic, tamanho grande — nunca pill pequena",
    "Fundo sempre dentro da paleta oficial, nunca branco puro",
    "Máximo 3 tamanhos de fonte na peça"
  ]
}
```

---

## SLIDE-01 — Look Moletom Preto ✅ APROVADO
**📸 Carregar 2 imagens de referência** (flat lay dos itens + foto da modelo vestindo o look completo)

```json
{
  "template": "carrossel-carol",
  "peca": "slide",
  "estrutura": "shop_the_look_split",
  "versao": "SLIDE-01_look_moletom_preto_v2",
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "safe_area": "952x1222px (64px mínimo todos os lados)"
  },
  "gate_respostas": {
    "roupa": ["moletom preto (gola careca, mangas raglan)", "calça preta alfaiatada wide-leg", "camisa branca de colarinho (usada por baixo do moletom)"],
    "acessorios_incluidos": ["relógio esportivo branco", "brincos trevo pretos", "bolsa tote creme e preta", "tênis branco (sapato)"],
    "acessorios_excluidos": ["colar", "óculos", "cinto", "boné", "anel", "pulseira"],
    "modelo_presente": true,
    "fundo_hex": "#e5ded3",
    "label": "Look Moletom Preto"
  },
  "prompt": {
    "scene": {
      "description": "Editorial fashion Instagram feed post (1080x1350px, 4:5 ratio), 'shop the look' styling card. CRITICAL: the ENTIRE 1080x1350px canvas is ONE single continuous seamless Linho #e5ded3 backdrop — same exact color value, same exposure, same warm 4200K light temperature, same soft shadow falloff from edge to edge. This must read as one uncut photograph taken in a single studio session, NEVER as two separate photos placed side by side — absolutely no visible seam, no color shift, no gradient break, no exposure difference down the center line. At the very top, header_padrao fixo: 'CAROL STAGGEMEIER' Nunito Sans Bold 18px, caixa alta, letter-spacing 3px, alinhado à esquerda, cor Café Terroso #4c3529 a 45% de opacidade + 'MODA AUTORAL' Nunito Sans Regular 18px, mesmo estilo, alinhado à direita, com linha separadora fina de 1px a 30% de opacidade logo abaixo, atravessando toda a largura da safe area. Below the header, split into 2 equal vertical halves on the same unbroken Linho backdrop. LEFT half: exact flat-lay reproduction of the confirmed items exactly as arranged in the reference flat-lay photograph — white collared button-up shirt top-left, black crew-neck raglan moletom sweatshirt centered, black wide-leg tailored trousers below-left, white sport smartwatch top-right, black clover-shaped stud earrings below the watch, cream-and-black colorblock canvas tote bag lower-right, white leather chunky sneakers bottom-center — same relative scale and spacing as the reference image, generous negative space between items. RIGHT half: one full-length photograph of the brunette model (long straight dark brown hair, medium skin tone, per reference photo) standing three-quarter angle, wearing the complete confirmed look — black moletom layered over the white collared shirt (collar and cuffs visible), black wide-leg trousers, white sneakers, black clover stud earrings, white smartwatch, holding the cream-and-black tote bag by the handles — natural relaxed stance, gaze softly off-camera, no phone in hand. Both halves share the identical background color, identical light direction, identical shadow softness — verify no tonal mismatch anywhere. GARMENT FIDELITY LOCK: reproduce every confirmed garment and accessory exactly as shown in the reference photographs — no redesign, no reinterpretation, no substitution, no addition of items not confirmed in the gate. ALL FABRIC STRICTLY MATTE — zero shimmer, zero lurex, zero metallic thread, zero sparkle. PRESERVE EXACT MODEL FACIAL LIKENESS from reference: long straight dark brown hair, medium skin tone, calm editorial expression. At the bottom of the frame, centered text in Halant Bold Italic (same typeface family used on the cover headline), color Café Terroso #4c3529, size 44px: 'Look Moletom Preto' — no pill, no background box, plain centered text sitting directly on the Linho backdrop, GRANDE e claramente legível, nunca pequeno como legenda de rodapé.",
      "subject": "Shop-the-look split card: left half flat-lay of the confirmed black moletom look items, right half the model wearing the complete look, unified by one continuous background",
      "setting": "Seamless single-tone Linho #e5ded3 backdrop, continuous across the entire frame with zero seam, single studio lighting session",
      "action": "Static editorial styling card — flat-lay-to-outfit visual translation, split composition on one unbroken background"
    },
    "style": {
      "primary": "editorial styling guide, shop-the-look product card, slow-fashion brand consistency",
      "rendering_quality": "hyperrealistic, editorial print quality, ultra high resolution",
      "surface_textures": "moletom fosco de malha grossa, algodão passado liso na camisa branca, alfaiataria fosca na calça, camurça/couro fosco no tênis e na bolsa, metal escovado fosco no relógio e brincos",
      "lighting": "Single large diffused softbox, 4200K warm, identical angle, height and falloff across the ENTIRE frame — flat-lay half and model half must show matching light and shadow, no hot spots, no gradient jump, no exposure difference anywhere."
    },
    "technical": {
      "camera": {
        "focal_length": "50mm flat-lay half, 85mm model half",
        "aperture": "f/8 flat-lay half, f/4 model half",
        "depth_of_field": "deep on flat-lay half, moderate-shallow on model half",
        "angle": "overhead/straight-on flat lay para o lado esquerdo, eye-level three-quarter para a modelo no lado direito"
      },
      "resolution": "ultra high definition, 1080x1350px, 4:5 Instagram feed ratio",
      "rendering": "Warm matte editorial tonality, very slight grain, single consistent color grade applied to the ENTIRE canvas as one image — no per-half color correction, no visible seam. NO specular highlights on fabric."
    },
    "materials": {
      "skin": "medium skin tone, neutral-warm undertone. Visible open pores on forehead and cheekbones. Fine individual peach fuzz hairs catching light. Natural minor imperfections scattered across nose and cheekbones. Matte finish. NO foundation finish, NO highlight powder, NO cosmetic gloss, NO airbrushed smoothing. Zero post-processing.",
      "fabric": "EXACT REPRODUCTION MANDATORY — moletom preto de malha grossa fosca, camisa branca de algodão passado, calça preta alfaiatada de tecido fosco. FORBIDDEN on any fabric area: shimmer, sparkle, glitter, lurex, metallic thread, specular highlight.",
      "surfaces": "Backdrop: ONE single seamless Linho #e5ded3 surface, matte, perfectly uniform color from edge to edge — same value on left half, right half, top and bottom. Acessórios: metal branco fosco (relógio), metal preto fosco (brincos), lona e couro fosco (bolsa tote), couro/malha fosca (tênis). Nenhum acessório fora da lista confirmada aparece em nenhuma parte do frame."
    },
    "composition": {
      "perspective": "Flat frontal overhead na metade esquerda, three-quarter eye-level na metade direita, ambas sobre o mesmo plano de fundo",
      "framing": "1080x1350px 4:5, split vertical exato 50/50 — metade esquerda flat lay, metade direita modelo de corpo inteiro — sobre UM ÚNICO fundo contínuo, sem costura visível",
      "subject_placement": "Header padrão no topo, largura total. Abaixo do header: metade esquerda com itens do flat lay organizados como na referência (camisa topo-esquerda, moletom central, calça abaixo, relógio topo-direita, brincos abaixo do relógio, bolsa inferior-direita, tênis inferior-central). Metade direita: modelo de corpo inteiro centralizada verticalmente, vestindo o look completo. Rodapé: texto 'Look Moletom Preto' centralizado na base, largura total do frame.",
      "safe_area": "64px padding all sides. Safe zone 952x1222px inside 1080x1350px. Nenhum elemento encosta na borda ou na linha central de divisão. Header 80px do topo. Texto de rodapé no mínimo 60px da borda inferior.",
      "ui_elements": [
        { "elemento": "header esquerda", "texto": "CAROL STAGGEMEIER", "fonte": "Nunito Sans Bold", "tamanho": "18px", "cor": "rgba(76,53,41,0.45)", "posicao": "topo esquerda" },
        { "elemento": "header direita", "texto": "MODA AUTORAL", "fonte": "Nunito Sans Regular", "tamanho": "18px", "cor": "rgba(76,53,41,0.45)", "posicao": "topo direita" },
        { "elemento": "linha separadora", "descricao": "1px, 30% opacidade, largura total da safe area", "posicao": "abaixo do header" },
        { "elemento": "texto inferior", "texto": "Look Moletom Preto", "fonte": "Halant Bold Italic", "tamanho": "44px", "cor": "#4c3529", "alinhamento": "centralizado", "posicao": "base do frame, sem pill, sem caixa de fundo", "observacao_critica": "texto deve renderizar GRANDE — nunca no tamanho de uma legenda pequena ou nota de rodapé, mesma fonte usada no headline da capa" }
      ]
    },
    "quality": {
      "include": [
        "single continuous seamless background across the entire frame",
        "identical color, exposure and lighting on both halves",
        "exact reproduction of only the confirmed garments and accessories",
        "flat-lay arrangement matching reference layout closely",
        "true material response on accessories no artificial gloss",
        "editorial shop-the-look clarity",
        "model face consistent with reference photo",
        "header_padrao presente e legível no topo",
        "texto inferior grande e centralizado, mesma fonte da capa"
      ],
      "avoid": [
        "two different background tones",
        "visible seam or color break down the center",
        "collage effect, two photos stitched together look",
        "exposure or lighting mismatch between halves",
        "any item not confirmed in the gate appearing anywhere in frame",
        "generic cold gray background",
        "any shimmer sparkle glitter lurex on fabric",
        "plastic or airbrushed skin",
        "specular hotspots on jewelry or bag hardware",
        "garment redesign or reinterpretation",
        "phone or selfie gesture",
        "missing header_padrao",
        "rodapé pequeno ou ilegível",
        "travessão em qualquer campo de texto"
      ],
      "reference_standard": "Personal stylist shop-the-look editorial, Net-a-Porter styling grid, The Frankie Shop product-to-outfit translation, Baserange matte fabric standard."
    }
  },
  "negative_rules_dinamicas": [
    "NO colar anywhere in frame",
    "NO óculos anywhere in frame",
    "NO cinto anywhere in frame",
    "NO boné anywhere in frame",
    "NO anel anywhere in frame",
    "NO pulseira anywhere in frame"
  ],
  "negative_rules": [
    "Sem travessão (—) em nenhum texto",
    "GARMENT FIDELITY LOCK: reproduzir cada peça e acessório exatamente como nas fotos de referência, sem redesenhar",
    "PRESERVE EXACT MODEL FACIAL LIKENESS conforme foto de referência",
    "Composição sempre split 50/50 sobre UM ÚNICO fundo contínuo — nunca duas tonalidades ou uma linha de corte visível",
    "header_padrao (CAROL STAGGEMEIER / MODA AUTORAL) sempre presente no topo",
    "Texto inferior 'Look Moletom Preto' sempre centralizado, fonte Halant Bold Italic, tamanho grande — nunca pill pequena",
    "Fundo sempre Linho #e5ded3, nunca branco puro",
    "Máximo 3 tamanhos de fonte na peça"
  ]
}
```

---

## Alternância sugerida no carrossel

```
CAPA  → Estrutura D (N modelos/poses confirmadas no gate)
SLIDE 1 → Shop the Look — card 1 (itens confirmados no gate)
SLIDE 2 → Shop the Look — card 2 (itens confirmados no gate)
SLIDE 3 → Shop the Look — card 3 (itens confirmados no gate)
CTA → V1 Verde Floresta (usar TEMPLATE-CTA-CAROL.json — sem alteração)
```

---

## Negative rules gerais do template

- Sem travessão (—) em qualquer texto
- Sem fundo branco puro ou preto puro
- Sem fonte abaixo de 18px
- Máximo 3 tamanhos de fonte por peça
- Header `CAROL STAGGEMEIER / MODA AUTORAL` sempre presente na capa
- Nunca gerar capa ou card sem antes rodar o gate correspondente
- Nunca deixar campo de peça/acessório em aberto — cada item existe no JSON só se confirmado
- Todo item excluído no gate vira proibição explícita em `negative_rules_dinamicas` — nunca apenas omissão silenciosa
- Fidelidade de peça e de rosto sempre dependem de foto de referência anexada — texto sozinho nunca garante isso
