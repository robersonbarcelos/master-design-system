# DESIGN.md : Banheiros LABELLE

## Visão geral
Editorial de arquitetura residencial: creme, verde-petróleo e dourado, serifa elegante com itálico. Calmo, organizado, "casa bem cuidada". Oposto visual da Mônaco (que é noite/marinho).

## Cores
```css
:root{
  --color-bg:#FAF7F1;        /* creme, fundo padrão */
  --color-surface:#FFFFFF;   /* cards */
  --color-primary:#043333;   /* verde-petróleo: títulos, header escuro */
  --color-accent:#B7881D;    /* dourado: itálicos, botões */
  --color-accent-2:#E2C05B;  /* dourado claro: gradiente, filetes */
  --color-ink:#14110C;       /* seções escuras de citação */
  --color-text:#4A4238;      /* corpo */
}
```

## Tipografia
```css
--font-display:'Cormorant Garamond', Georgia, serif; /* 500/600, itálico para destaque */
--font-body:'Gilroy','Plus Jakarta Sans',system-ui,sans-serif; /* 400/500/600 */
```
| Nível | Tamanho desktop / mobile | Família |
|---|---|---|
| Display | 64 / 40px, line-height 1.05 | Cormorant 500 |
| H1 | 48 / 32px | Cormorant 500 |
| H2 | 36 / 26px | Cormorant 500 |
| Eyebrow | 12px caixa alta, tracking .15em, dourado, "● " antes | Gilroy 600 |
| Body | 17 / 16px, line-height 1.6 | Gilroy 400 |
| Caption | 13px | Gilroy 500 |

## Layout e espaçamento
- Escala 4/8/16/24/40/64/96px. Container 1200px. Seções com respiro grande (96px desktop).
- Cards com borda 1px `rgba(4,51,51,.08)`, raio 16px, sem sombra pesada.

## Componentes
- **Botão primário:** pílula, gradiente `#B7881D → #E2C05B`, texto `#14110C` 600, padding 14px 28px.
- **Botão secundário:** pílula com borda 1px `#043333`, texto `#043333`.
- **Cards de módulo:** foto em fundo creme, nome, medidas, peso, "a partir de R$/mês".
- **Inputs:** fundo branco, borda 1px `#043333` 20%, raio 12px, foco com anel dourado.

## Tom visual
Revista de arquitetura, luz de dia, fotos reais, muito espaço em branco.

## Voz do design
"Resolvido, discreto, permanente." Nada pisca, nada grita.
