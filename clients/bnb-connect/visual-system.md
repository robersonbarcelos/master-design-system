# Visual System — [NOME DO CLIENTE]

> Sistema de produção visual: grupos editoriais, JSON padrão, regras de prompt, especificações técnicas.

---

## 01 | FLUXO DE PRODUÇÃO VISUAL

Sempre seguir esta ordem — nunca gerar JSON sem aprovação:

1. Propor **3 ideias visuais em texto** — conceito, composição, paleta, tipografia
2. **Aguardar aprovação** do usuário
3. Gerar **JSON completo** apenas para as ideias aprovadas

---

## 02 | ESPECIFICAÇÕES TÉCNICAS

### [Plataforma 1 — ex: Instagram]

| Formato | Dimensões | Proporção | Obs |
|---------|-----------|-----------|-----|
| Feed Retrato ★ | **1080 × 1350 px** | 4:5 | Formato principal |
| Feed Quadrado | 1080 × 1080 px | 1:1 | Alternativa |
| Carrossel | 1080 × 1350 px | 4:5 | Todos os slides iguais |
| Stories | 1080 × 1920 px | 9:16 | Safe zone: 250px topo e base |
| Reels | 1080 × 1920 px | 9:16 | Legenda obrigatória |

### [Plataforma 2 — ex: LinkedIn]

| Formato | Dimensões | Proporção | Obs |
|---------|-----------|-----------|-----|
| Post Quadrado ★ | **1200 × 1200 px** | 1:1 | Formato principal |
| Post Paisagem | 1200 × 627 px | 1.91:1 | Para links |
| Carrossel PDF ★ | **1080 × 1080 px** por slide | 1:1 | Enviar como PDF nativo |

> Regra geral: JPG para fotos. PNG para artes com texto/logo.

---

## 03 | GRUPOS VISUAIS

Usar como referência ao propor ideias visuais. Cada grupo tem lógica de composição distinta.

**GRUPO 1 — [NOME DO GRUPO]**
[Descrição: tipo de composição, ângulo, iluminação, elemento principal, onde fica o texto]
Quando usar: [tipos de post / editoria]

**GRUPO 2 — [NOME DO GRUPO]**
[Descrição: composição, perspectiva, fundo, elementos, conceito visual]
Quando usar: [tipos de post / editoria]

**GRUPO 3 — [NOME DO GRUPO]**
[Descrição: pessoa/personagem, iluminação, expressão, fundo, dados ao redor]
Quando usar: [tipos de post / editoria]

**GRUPO 4 — [NOME DO GRUPO]**
[Descrição: dado/número como protagonista, tipografia grande, fundo limpo]
Quando usar: [tipos de post / editoria]

**GRUPO 5 — [NOME DO GRUPO]**
[Descrição: macro/close, superfície reflexiva, profundidade de campo, contraste]
Quando usar: [tipos de post / editoria]

**GRUPO 6 — [NOME DO GRUPO]**
[Descrição: composição tipográfica pura, sem foto, hierarquia por tamanho/peso]
Quando usar: [tipos de post / editoria]

---

## 04 | JSON PADRÃO

```json
{
  "prompt": "[Proporção e plataforma]. BACKGROUND: [cor/gradiente padrão]. CENTER: [elemento principal]. TYPOGRAPHY: HEADLINE (large bold sans-serif, [cor headline]): '[texto]'. SUBHEADLINE (medium, [cor subheadline]): '[texto]'. CTA isolated: '[call to action]'. FOOTER: [logo + posição]. Color accents: [cor destaque] on [tipo de fundo]. [Estética geral]. Ultra sharp, high contrast, professional.",
  "negative_prompt": "[lista do que não quer: blurry, low contrast, cluttered, cartoonish, handwritten font, serif font, warm colors, watermark, extra logos, ...]",
  "aspect_ratio": "[4:5 / 1:1 / 9:16]",
  "style": "[descrição do estilo visual — ex: tech finance editorial, dark background, neon accent, bold typography, clean layout]"
}
```

---

## 05 | REGRAS DE PROMPT

- Fundo padrão: [cor/estilo — ex: dark #0D1B2A / branco #FFFFFF / gradiente X]
- Cor de destaque obrigatória: [hex]
- Tipografia: [estilo — ex: bold sans-serif — nunca serif, nunca handwritten]
- Elementos visuais característicos: [ex: coins cripto, gráficos, ícones tech / produtos físicos / pessoas reais]
- Logo: [posição padrão — ex: topo esquerdo]
- Para conteúdo cultural/meme: [regra específica]
- Safe zone stories: [medidas]

### Paleta expandida (se aplicável)

Posts com elemento visual central ganham profundidade com contraste de temperatura de luz:

| Elemento | Cor | Hex | Uso |
|----------|-----|-----|-----|
| Luz quente de acento | [nome] | [hex] | [de onde vem, o que aquece] |
| Luz fria de preenchimento | [nome] | [hex] | [de onde vem, o que mantém] |
| [outro elemento] | [nome] | [hex] | [uso] |

Regra: [como aplicar sem substituir a paleta oficial]
