# Brand Spec — História Proibida

last_updated: 2026-08-29

> Paleta e fonte selecionadas via gate de catálogo (`reference/colors/paletas-index.md` + `reference/fonts-index.md`).

---

## Logo

**Arquivo principal:** a definir (ainda não produzido)
**Variações necessárias:** horizontal, símbolo isolado, versão branca, versão preta, favicon
**Uso do logo:** a definir quando o logo for criado

---

## Cores

### Paleta principal — "Ferrugem Industrial"

| Papel | Nome | Hex | RGB | Uso |
|---|---|---|---|---|
| Fundo escuro | Grafite | `#1B1D1E` | rgb(27,29,30) | background principal dos slides |
| Acento | Ferrugem | `#C13B00` | rgb(193,59,0) | destaques, headline, alertas, "selo de caso" |
| Suporte | Ardósia | `#5E6D70` | rgb(94,109,112) | textos secundários, metadados, divisores |

### Variáveis CSS
```css
:root {
  --color-bg-dark: #1B1D1E;
  --color-accent: #C13B00;
  --color-support: #5E6D70;
}
```

### Verificação de acessibilidade
| Combinação | Ratio | WCAG |
|---|---|---|
| Ferrugem sobre Grafite | ~4.9:1 | AA (texto grande) |
| Branco sobre Grafite | ~16.9:1 | AAA |

---

## Tipografia

| Papel | Família | Peso | Fonte |
|---|---|---|---|
| Display / Headline | Tusker Grotesk | 700 Bold | `reference/fonts/tusker-grotesk/tusker-grotesk-6700-bold.ttf` |
| Body / legenda | Galano Grotesque Alt Regular | 400 | `reference/fonts/galano-grotesque/GalanoGrotesqueAltRegular.otf` |

> Licença: Tusker Grotesk e Galano Grotesque são fontes pagas de foundry — confirmar licença antes de uso em material publicado.

### CSS
```css
:root {
  --font-display: 'Tusker Grotesk', sans-serif;
  --font-body: 'Galano Grotesque Alt', sans-serif;
}
```

---

## Estilo visual geral

**Referência visual:** carrossel investigativo/sombrio — fundo grafite quase preto, headline condensada e pesada em ferrugem, textura sutil de "arquivo/dossiê" (grão, scanline leve), sem sangue ou violência gráfica explícita.
**Estilo de fotografia:** fotos de época em tom dessaturado/sépia quando existirem (domínio público) ou ilustração estilo "capa de dossiê" — nunca foto de vítima real identificável.
**Atmosfera:** investigativo, sóbrio, peso histórico

---

## Notas de aplicação

Perfil irmão de [voce-ignorava-isso](../voce-ignorava-isso/brand-spec.md) e [ciencia-chocante](../ciencia-chocante/brand-spec.md). Ferrugem Industrial é exclusiva deste perfil — nunca usar nos outros dois. Casos com vítimas reais: sem imagem de rosto de vítima sem estar em domínio público extensamente documentado.
