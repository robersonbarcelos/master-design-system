# Cobalt Pop Cutout Editorial

**Mood:** Editorial pop · jovem · impacto de cor · full-body cutout
**Melhor uso:** Capa de carrossel de produto ou creator, post de lançamento, conteúdo de lifestyle
**Compatibilidade de brand:** Melhor para clientes com paleta vibrante (Aurum, Super Agente) · adaptável para Intus Hub trocando laranja por dourado

---

## Variáveis

| Variável | Descrição |
|---|---|
| `SUBJECT` | Sujeito fotográfico principal — pessoa full-body |
| `SUBJECT_ACTION` | Ação clara com gesto de corpo inteiro |
| `PRODUCT_OR_PROP` | Objeto único no primeiro plano como âncora visual |
| `LOCATION` | Ambiente real — usado como detalhe inferior mínimo |
| `BACKGROUND_ELEMENTS` | Dois ou três detalhes de cena contidos na borda inferior |
| `MAIN_TEXT` | Headline curta oversized |
| `SECONDARY_TEXT` | Microcópia de suporte breve |
| `ACCENT_SYMBOL` | Seta, chevron, sparkle ou marca geométrica pequena |
| `WARDROBE_STYLE` | Direção editorial de figurino — alta saturação |
| `ASPECT_RATIO` | 4:5 ou 5:4 |

---

## Âncoras de fidelidade (Style Fidelity Anchors)

```
1. A saturated cobalt-to-sky-blue field fills nearly the entire frame, with only restrained environmental details allowed near the lower edge.
2. One crisp full-body photographic cutout dominates the center at roughly 55 to 70 percent of the frame height, shot from a low 24–28mm wide-angle viewpoint.
3. A single oversized warm-orange headline spans the upper third, using solid-fill, chunky, hand-warped display letters on an uneven baseline.
4. Two to four botanical-green organic edge shapes appear at the frame corners as restrained graphic anchors.
5. Sparse cream microcopy with accent sparkles or arrows floats near the lower zone.
6. Palette: 60% cobalt blue, 18% botanical green, 17% warm orange, 5% cream.
7. The subject is a crisp photoreal full-body cutout — no background bleed, no shadow cast.
8. Editorial, commercial, youthful energy. Not corporate, not minimal.
```

---

## Prompt Template (completo)

```
Create a {ASPECT_RATIO} raster editorial poster in the Cobalt Pop Cutout visual style.

Style priority: preserve these observable anchors before introducing new content:
1. A saturated cobalt-to-sky-blue field fills nearly the entire frame, with only restrained environmental details near the lower edge.
2. One crisp full-body photographic cutout of the subject dominates the center at roughly 55 to 70 percent of the frame height, shot from a low 24–28mm wide-angle viewpoint creating slight upward perspective.
3. A single oversized warm-orange headline in the upper third, using solid-fill chunky hand-warped uppercase display letters on an uneven baseline, overlapping the top of the subject's body.
4. Two to four botanical-green organic edge shapes at frame corners as restrained graphic anchors.
5. Sparse cream microcopy with accent sparkles or arrows near the lower zone.
6. Palette: 60% cobalt blue, 18% botanical green, 17% warm orange, 5% cream.
7. Crisp photoreal full-body cutout — no background bleed, no cast shadow.
8. Editorial, commercial, youthful energy.

SUBJECT: {SUBJECT}
SUBJECT_ACTION: {SUBJECT_ACTION}
PRODUCT_OR_PROP: {PRODUCT_OR_PROP}
LOCATION: {LOCATION}
BACKGROUND_ELEMENTS: {BACKGROUND_ELEMENTS}
MAIN_TEXT: {MAIN_TEXT}
SECONDARY_TEXT: {SECONDARY_TEXT}
ACCENT_SYMBOL: {ACCENT_SYMBOL}
WARDROBE_STYLE: {WARDROBE_STYLE}

Fill nearly the entire frame with a saturated cobalt-to-sky-blue field. Position one crisp photoreal full-body cutout of the subject centrally at 55–70% of frame height, low wide-angle 24–28mm viewpoint, slight upward perspective making the subject appear monumental. One massive warm-orange headline in chunky solid-fill uppercase condensed display letters spans the upper third on an uneven baseline, slightly warped, overlapping the top of the subject. Two to four botanical-green organic rounded shapes at the bottom corners and edges grounding the composition. Small cream microcopy with {ACCENT_SYMBOL} near the lower zone. Palette: 60% cobalt blue field, 18% botanical green shapes, 17% warm orange headline, 5% cream microcopy. No background scene visible beyond the restrained lower-edge details. Photoreal subject, editorial quality, no logos, no watermarks.

Avoid: white background, warm background, busy scene, realistic environment behind subject, text overlapping face, watermark, logo, illustration, cartoon, stock photo smile, multiple subjects, soft focus on subject.
```

---

## Adaptação de cor — Intus Hub

| Original | Intus Hub |
|---|---|
| `warm-orange` headline | `gold (#F0B429)` headline |
| `cobalt-to-sky-blue` field | `cobalt (#1E4D9B) to near-black (#050D1F)` — mais escuro |
| `botanical-green` shapes | `deep navy (#0a1628)` shapes |
| `cream` microcopy | `white` microcopy |
