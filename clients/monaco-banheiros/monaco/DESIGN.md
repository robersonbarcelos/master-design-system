# DESIGN.md : Banheiros Mônaco

## Visão geral
Hospitalidade de evento noturno: marinho profundo, índigo e dourado, serifa clássica em caixa alta. Sensação de hotel cinco estrelas e festa elegante. Oposto visual da LABELLE (que é dia/creme).

## Cores
```css
:root{
  --color-bg:#100C43;        /* marinho profundo */
  --color-surface:#26207A;   /* índigo escuro, cards */
  --color-primary:#3533CD;   /* índigo Mônaco, botões do site */
  --color-accent:#FFBD59;    /* dourado claro, destaques */
  --color-accent-2:#AC914B;  /* dourado envelhecido, molduras */
  --color-light:#FFFFFF;
  --color-text-on-light:#4E566D;
}
```

## Tipografia
```css
--font-display:'Cinzel', 'Trajan Pro', serif; /* ⚠️ confirmar fonte do logotipo; caixa alta, tracking .08em */
--font-body:'Plus Jakarta Sans', system-ui, sans-serif; /* fonte do site */
```
| Nível | Desktop / mobile | Família |
|---|---|---|
| Display | 60 / 38px caixa alta | Cinzel 600 |
| H1 | 44 / 30px | Cinzel 600 |
| H2 | 32 / 24px | Plus Jakarta Sans 700 |
| Body | 17 / 16px, line-height 1.6 | Plus Jakarta Sans 400 |
| Caption | 13px | Plus Jakarta Sans 500 |

## Layout e espaçamento
- Escala 4/8/16/24/40/64/96px. Seções escuras alternando com faixas de foto em tela cheia.
- Molduras finas douradas (1px `#AC914B`) com cantos internos, como nos posts do IG.

## Componentes
- **Botão primário:** retângulo raio 8px, fundo `#3533CD` (site) ou dourado `#FFBD59` com texto `#100C43` (peças sociais).
- **Botão secundário:** fundo branco, texto `#100C43`.
- **Cards:** foto do evento com overlay marinho 40%, título em caixa alta.
- **Inputs:** fundo `#FFFFFF`, borda `#3533CD` 30%, raio 8px.

## Tom visual
Noite de evento, luz quente, dourado, interiores brancos com LED. Fotos reais dos trailers em eventos.

## Voz do design
"Pronto, impecável, inesquecível."
