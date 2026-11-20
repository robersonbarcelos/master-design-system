# Visual System : Banheiros LABELLE

## Formatos
| Plataforma | Formato |
|---|---|
| IG feed / carrossel | 1080x1350 |
| Reels / TikTok / Shorts | 1080x1920, safe zone 250px topo e base |
| LinkedIn | 1200x1500 (carrossel PDF) ou 1200x627 |
| Blog capa | 1600x900 |

## Famílias visuais
| Família | Linhas | Descrição |
|---|---|---|
| **FL1 Editorial creme** | LB1, LB2, LB5 | Fundo `#FAF7F1`, título Cormorant `#043333` com palavra em itálico dourado, eyebrow "● TEMA" dourado, foto real recortada ou em moldura fina. É o padrão do IG atual: manter |
| **FL2 Foto real + faixa** | LB3, LB7 | Foto do módulo no galpão/jardim ocupando 70%, faixa inferior creme com título e 1 dado técnico |
| **FL3 Ficha técnica** | LB3, LB5 (LinkedIn) | Estilo flyer do galpão: produto recortado, módulos lado a lado (1, 2, chuveiro, PNE), medidas, peso, "autônomo x ligado na rede", contato |
| **FL4 Citação escura** | Depoimentos, LB6 | Fundo `#14110C`, estrela dourada, citação em Cormorant itálico, assinatura com cargo ("Gestor de operação"). Já usado no IG ("Eu não sabia que isso existia") |
| **FL5 Diagrama técnico** | LB4 | Fundo creme, linhas finas verde-petróleo, corte do módulo mostrando tanque x ligação na rede, setas douradas |
| **FL6 Contraste** | LB6 | Split: cabine química azul dessaturada x módulo LABELLE em luz natural |

## Regras de prompt
- Sempre foto real do módulo quando existir. IA só para cenário (jardim, galpão, condomínio) e composição.
- Nunca gerar interior "inventado" como se fosse da LABELLE.
- Nunca mostrar ar-condicionado no módulo.
- Luz natural de dia, tons neutros, sem noite de festa (isso é território visual da Mônaco).
- Negativos: blue plastic portable toilet (exceto FL6), dirty construction site, mud, night party lights, air conditioner unit, distorted text, third-party logos.

## JSON base (cenário reforma residencial)
```json
{
  "style": "editorial architecture photography, soft natural daylight",
  "subject": "white modular restroom cabin with gold star logo discreetly placed in the side garden of an upscale Brazilian house under renovation, neat and clean surroundings",
  "palette": ["#FAF7F1", "#043333", "#B7881D", "#FFFFFF"],
  "composition": "cabin on right third, generous negative space on left for headline",
  "mood": "calm, orderly, discreet, home continuity",
  "negative": "blue plastic portable toilet, mud, debris piles, night lights, air conditioner, distorted text, third-party logos"
}
```

## JSON base (cenário galpão)
```json
{
  "style": "clean industrial documentary photography, bright even light",
  "subject": "row of three white modular restroom cabins installed inside a large modern logistics warehouse, conveyor belts and boxes softly blurred in background",
  "palette": ["#FAF7F1", "#043333", "#B7881D"],
  "composition": "cabins centered lower half, headroom for headline",
  "mood": "organized, dignified, efficient",
  "negative": "blue plastic portable toilet, dirt, people in degrading situations, distorted text, retailer logos"
}
```
