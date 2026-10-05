# Burnt Orange Halftone Hero Collage

**Mood:** Editorial denso · herói de personagem · halftone artesanal · colagem em camadas
**Melhor uso:** Post de autoridade/creator, conteúdo de bastidor, editorial de expert
**Compatibilidade de brand:** Melhor para Aurum Lingerie, Mercurius · adaptável com inversão de fundo para clientes dark

---

## Variáveis

| Variável | Descrição |
|---|---|
| `SUBJECT` | Retrato e identidade do herói — personagem principal |
| `SUBJECT_ACTION` | Gesto específico ou ofício que a pessoa executa |
| `PRODUCT_OR_PROP` | Um objeto distinto e não-marcado |
| `LOCATION` | Ambiente abstraído em camadas de poster |
| `BACKGROUND_ELEMENTS` | Diagramas, silhuetas e elementos específicos do sujeito |
| `MAIN_TEXT` | Headline em maiúsculas de 2 a 4 palavras |
| `SECONDARY_TEXT` | Kicker factual e footer |
| `ACCENT_SYMBOL` | Emblema original não-marcado |
| `WARDROBE_STYLE` | Roupas sem logo |
| `ASPECT_RATIO` | 4:5 ou 5:4 |

---

## Âncoras de fidelidade (Style Fidelity Anchors)

```
1. Warm uncoated cream paper ground with a restricted burnt-tangerine, near-black, cream, and white graphic palette around a selectively colorful photographic subject.
2. One enormous condensed headline spanning nearly full width, partly hidden by the hero's head.
3. Dominant waist-up cutout occupying 60–70% of canvas, center-right bias.
4. Irregular pasted-sticker edges with cream contour plus dark keyline on the hero cutout.
5. Dense shallow layer stack in fixed sequence: cream ground → headline behind → orange panel → hero → brush stroke → prop → loop → halftone strip → footer.
6. Coarse controlled Ben-Day dots, white-on-orange silhouettes, photocopy grain, dry ink, and subtle screenprint misregistration.
7. Black-and-cream halftone strip along the bottom edge.
8. Direct warm frontal flash on subject with bright highlights and crisp shadows.
9. Color values: #F0DFC1 cream, #E66D22 burnt tangerine, #211B1A near-black.
```

---

## Prompt Template (completo)

```
Create a {ASPECT_RATIO} editorial collage poster in the Burnt Orange Halftone Hero Collage visual style.

Style priority: preserve these observable anchors before introducing new content:
1. Warm uncoated cream paper ground (#F0DFC1) with restricted burnt-tangerine (#E66D22), near-black (#211B1A), cream, and white palette around a selectively colorful photographic subject.
2. One enormous condensed uppercase headline spanning nearly full width, partly hidden by the hero's head.
3. Dominant waist-up photographic cutout occupying 60–70% of canvas, center-right bias.
4. Irregular pasted-sticker edges with cream contour plus dark keyline on the hero cutout.
5. Dense shallow layer stack: cream ground → headline behind → orange panel → hero cutout → brush stroke → prop → loop → halftone strip → footer.
6. Coarse controlled Ben-Day dots, white-on-orange silhouettes, photocopy grain, dry ink, subtle screenprint misregistration.
7. Black-and-cream halftone strip along bottom edge.
8. Direct warm frontal flash on subject, bright highlights, crisp shadows.

SUBJECT: {SUBJECT}
SUBJECT_ACTION: {SUBJECT_ACTION}
PRODUCT_OR_PROP: {PRODUCT_OR_PROP}
LOCATION: {LOCATION}
BACKGROUND_ELEMENTS: {BACKGROUND_ELEMENTS}
MAIN_TEXT: {MAIN_TEXT}
SECONDARY_TEXT: {SECONDARY_TEXT}
ACCENT_SYMBOL: {ACCENT_SYMBOL}
WARDROBE_STYLE: {WARDROBE_STYLE}

Warm uncoated cream paper ground (#F0DFC1) as base layer. Stack layers in this exact sequence: cream ground → enormous condensed headline in burnt tangerine behind the hero → orange graphic panel → waist-up hero cutout (center-right, 60–70% of canvas) → brush stroke mark → prop element → loop gesture → coarse halftone strip at bottom → footer text. Apply irregular pasted-sticker edges with cream contour plus dark keyline to the hero cutout. Coarse Ben-Day dots in burnt tangerine on cream zones. Photocopy grain texture and subtle screenprint misregistration unify all layers. Direct warm frontal flash lighting on subject. Black-and-cream halftone strip spans full width at bottom. Headline partly hidden by hero's head. Emblem {ACCENT_SYMBOL} placed at lower corner. Footer: {SECONDARY_TEXT}. Render supplied text exactly. No watermarks, no real logos.

Avoid: clean digital look, no texture, white background dominant, soft focus, gradient modeling, watermark, real brand logo, multiple subjects, realistic bouquet or literal decorative elements.
```

---

## Adaptação de cor — Dark Brand (Intus Hub, Novadax)

| Original | Dark brand |
|---|---|
| `cream ground (#F0DFC1)` | `near-black (#050D1F)` |
| `burnt-tangerine (#E66D22)` | `gold (#F0B429)` |
| `cream contour` no sticker | `dark gold rim` |
| `black-and-cream halftone strip` | `black-and-gold halftone strip` |

**Nota:** inversão de fundo altera significativamente o mood — de "artesanal quente" para "editorial noturno". Testar antes de aplicar a cliente dark.
