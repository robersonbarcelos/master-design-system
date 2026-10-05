# Visual System — Ciência Chocante

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

**GRUPO 1 — Escala/comparação científica**
Fundo carbono (#141414), ilustração estilizada mostrando escala (planeta vs objeto conhecido, célula ampliada etc.), número/dado em verde laser (#2BEE34) dominando o frame.
Quando usar: fatos de espaço/escala.

**GRUPO 2 — Corpo humano em diagrama**
Fundo carbono, ilustração tipo "raio-x/diagrama técnico" de parte do corpo relevante, dado chocante em verde laser sobreposto.
Quando usar: curiosidades de corpo humano.

**GRUPO 3 — Natureza extrema em foco**
Fundo carbono, ilustração/render estilizado do animal/planta/fenômeno em destaque com leve glow verde laser, texto de apoio minimalista.
Quando usar: curiosidades de natureza.

**GRUPO 4 — Fechamento/CTA**
Fundo carbono, frase de fechamento em Galano Grotesque branco, elemento verde laser isolado como assinatura.
Quando usar: último slide do carrossel.

---

## 04 | JSON PADRÃO

```json
{
  "prompt": "1080x1350 4:5 Instagram carousel slide. BACKGROUND: solid matte black #141414, no gradient, no texture. CENTER: [elemento científico principal do slide — ilustração estilizada, não foto stock]. TYPOGRAPHY: HEADLINE (Brunson bold, laser green #2BEE34, huge, dominates frame): '[texto]'. SUPPORT TEXT (Galano Grotesque regular, white #F2F2F2, small): '[texto]'. No logo, no watermark. Ultra sharp, high contrast, scientific editorial style.",
  "negative_prompt": "blurry, low contrast, cluttered, cartoonish, handwritten font, serif font, warm gradient, watermark, generic stock photo, pseudoscientific imagery, white background",
  "aspect_ratio": "4:5",
  "style": "bold scientific editorial, dark background, laser green accent, huge display typography"
}
```

---

## 05 | REGRAS DE PROMPT

- Fundo padrão: carbono `#141414`
- Cor de destaque obrigatória: verde laser `#2BEE34`
- Tipografia: Brunson bold para headline — nunca serif, nunca handwritten
- Elementos visuais: ilustração/render estilizado (científico), nunca imagem pseudocientífica ou meme
- Logo: a definir quando existir
- Safe zone stories: 250px topo e base
