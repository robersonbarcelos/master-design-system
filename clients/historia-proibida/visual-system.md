# Visual System — História Proibida

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

**GRUPO 1 — Dossiê/arquivo**
Fundo grafite (#1B1D1E) com textura sutil de papel/grão de scanner, título do caso em Tusker Grotesk condensado e pesado em ferrugem (#C13B00), aparência de "documento confidencial".
Quando usar: capa/slide 1 (hook do caso).

**GRUPO 2 — Linha do tempo/local**
Fundo grafite, elemento gráfico de mapa/linha do tempo estilizado em ardósia (#5E6D70), dado/data em destaque ferrugem.
Quando usar: contextualização do caso (onde/quando).

**GRUPO 3 — Foto de época estilizada**
Fundo grafite, foto de domínio público em tom dessaturado/sépia com overlay escuro, texto sobreposto em área de contraste garantido.
Quando usar: quando existir registro fotográfico real de domínio público — nunca rosto de vítima não documentada publicamente.

**GRUPO 4 — Fechamento/CTA**
Fundo grafite, frase de fechamento em Galano Grotesque branco, selo/elemento ferrugem isolado como assinatura.
Quando usar: último slide do carrossel.

---

## 04 | JSON PADRÃO

```json
{
  "prompt": "1080x1350 4:5 Instagram carousel slide. BACKGROUND: matte dark graphite #1B1D1E, subtle paper grain / scan-line texture, no bright colors. CENTER: [elemento principal — documento estilizado, mapa, ou foto de época dessaturada]. TYPOGRAPHY: HEADLINE (Tusker Grotesk bold condensed, rust orange #C13B00, huge): '[texto]'. SUPPORT TEXT (Galano Grotesque regular, white, small): '[texto]'. No logo, no watermark, no graphic violence, no explicit gore. Ultra sharp, high contrast, investigative dossier editorial style.",
  "negative_prompt": "blurry, low contrast, cluttered, cartoonish, handwritten font, bright warm gradient, watermark, gore, graphic violence, identifiable victim face, white background",
  "aspect_ratio": "4:5",
  "style": "dark investigative dossier editorial, graphite background, rust accent, condensed heavy typography"
}
```

---

## 05 | REGRAS DE PROMPT

- Fundo padrão: grafite `#1B1D1E`
- Cor de destaque obrigatória: ferrugem `#C13B00`
- Tipografia: Tusker Grotesk bold para headline — nunca serif decorativo, nunca handwritten
- Elementos visuais: textura de dossiê/scanner, mapas estilizados, fotos de época dessaturadas — nunca gore ou violência explícita, nunca rosto de vítima não documentada em domínio público
- Logo: a definir quando existir
- Safe zone stories: 250px topo e base
