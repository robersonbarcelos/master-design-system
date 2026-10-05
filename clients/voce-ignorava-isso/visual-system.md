# Visual System — Você Ignorava Isso

> Sistema de produção visual: grupos editoriais, JSON padrão, regras de prompt, especificações técnicas.

---

## 01 | FLUXO DE PRODUÇÃO VISUAL

Sempre seguir esta ordem — nunca gerar JSON sem aprovação:

1. Propor **3 ideias visuais em texto** — conceito, composição, paleta, tipografia
2. **Aguardar aprovação** do usuário
3. Gerar **JSON completo** apenas para as ideias aprovadas (nunca widget HTML para peça final)

---

## 02 | ESPECIFICAÇÕES TÉCNICAS

### Instagram

| Formato | Dimensões | Proporção | Obs |
|---------|-----------|-----------|-----|
| Carrossel ★ | **1080 × 1350 px** | 4:5 | Formato canônico — todos os slides iguais |
| Feed Quadrado | 1080 × 1080 px | 1:1 | Alternativa |
| Stories/Reels | 1080 × 1920 px | 9:16 | Safe zone: 250px topo e base |

> Pipeline: gpt-image `--size 1088x1360` → resize Pillow 1080x1350 (LANCZOS). Nunca usar portrait 1024x1536 como final.

---

## 03 | GRUPOS VISUAIS

**GRUPO 1 — Palavra de impacto**
Fundo preto fosco (#141414) liso, uma palavra ou número curto em Brunson gigante centralizado em neon limão (#A4F900), sem elementos decorativos.
Quando usar: capa/slide 1 (hook).

**GRUPO 2 — Dado + ícone simples**
Fundo preto fosco, número/dado grande no topo em neon limão, ícone/silhueta minimalista relacionado ao tema abaixo, texto de apoio em Galano Grotesque branco.
Quando usar: slides de desenvolvimento do fato.

**GRUPO 3 — Comparação lado a lado**
Split vertical do frame: metade com contexto "antes/o que todo mundo pensa", metade com "o real motivo" — mesma paleta, contraste por opacidade do neon.
Quando usar: fatos que desmontam uma crença comum.

**GRUPO 4 — Fechamento/CTA**
Fundo preto, frase de fechamento curta em Galano Grotesque branco, elemento neon isolado como assinatura visual (não logo ainda).
Quando usar: último slide do carrossel.

---

## 04 | JSON PADRÃO

```json
{
  "prompt": "1080x1350 4:5 Instagram carousel slide. BACKGROUND: solid matte black #141414, no gradient, no texture. CENTER: [elemento principal do slide]. TYPOGRAPHY: HEADLINE (Brunson bold, neon lime #A4F900, huge, dominates frame): '[texto]'. SUPPORT TEXT (Galano Grotesque regular, white #F2F2F2, small): '[texto]'. No logo, no watermark, no extra decoration. Ultra sharp, high contrast, bold minimal editorial style.",
  "negative_prompt": "blurry, low contrast, cluttered, cartoonish, handwritten font, serif font, warm gradient, watermark, stock photo, extra logos, white background",
  "aspect_ratio": "4:5",
  "style": "bold minimal editorial, dark background, neon lime accent, huge display typography"
}
```

---

## 05 | REGRAS DE PROMPT

- Fundo padrão: preto fosco `#141414`
- Cor de destaque obrigatória: neon limão `#A4F900`
- Tipografia: Brunson bold para headline — nunca serif, nunca handwritten
- Elementos visuais característicos: ícones/silhuetas minimalistas, nunca foto stock genérica de "pessoas sorrindo"
- Logo: a definir quando existir
- Safe zone stories: 250px topo e base
