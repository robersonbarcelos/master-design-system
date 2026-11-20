# Visual System : Banheiros Mônaco

## Formatos
| Plataforma | Formato |
|---|---|
| Instagram feed / carrossel | 1080x1350 (4:5) |
| Reels / TikTok / Shorts | 1080x1920 (9:16), safe zone 250px topo e base |
| LinkedIn | 1200x1500 (carrossel PDF) ou 1200x627 |
| Blog (capa) | 1600x900 |

## Grupos visuais
| Grupo | Quando usar | Descrição |
|---|---|---|
| G1 Interior premium | L3, L1 | Foto real do interior, luz LED, branco + detalhe dourado. Texto mínimo |
| G2 Contraste | L1 | Split: banheiro químico genérico dessaturado x interior Mônaco quente |
| G3 Editorial marinho | L2, L5 | Fundo `#100C43`, título serifado dourado, ícones finos dourados, tabelas/checklists |
| G4 Evento real | L6, L4 | Foto do trailer no evento, overlay marinho 40%, título curto |
| G5 Prova social | L4 | Print de feedback em mockup de celular sobre fundo marinho (já usado no IG, manter) |
| G6 Ficha técnica | L5 (LinkedIn) | Layout claro tipo referência Labelle: produto recortado, especificações, opções |

## Regras de prompt
- Sempre foto real do trailer quando existir. IA só para fundo, cena de contexto ou ilustração editorial.
- Nunca gerar interior de banheiro "inventado" como se fosse da Mônaco.
- Luz quente, ambiente noturno ou golden hour para eventos.
- Negativos: banheiro químico azul de plástico, sujeira, fila, obra, pessoas em situação constrangedora, texto ilegível, logos de terceiros.

## JSON base (contexto de cena)
```json
{
  "style": "editorial luxury event photography, warm golden hour light",
  "subject": "sleek white mobile restroom trailer with metal steps, installed at an elegant outdoor wedding venue",
  "palette": ["#100C43", "#FFBD59", "#AC914B", "#FFFFFF"],
  "composition": "trailer on right third, negative space on left for headline",
  "mood": "sophisticated, calm, five-star hospitality",
  "negative": "blue plastic portable toilet, dirt, queue, construction site, distorted text, third-party logos"
}
```
