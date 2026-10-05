# Brand Spec — Ciência Chocante

last_updated: 2026-08-29

> Paleta e fonte selecionadas via gate de catálogo (`reference/colors/paletas-index.md` + `reference/fonts-index.md`).

---

## Logo

**Arquivo principal:** a definir (ainda não produzido)
**Variações necessárias:** horizontal, símbolo isolado, versão branca, versão preta, favicon
**Uso do logo:** a definir quando o logo for criado

---

## Cores

### Paleta principal — "Verde Laser"

| Papel | Nome | Hex | RGB | Uso |
|---|---|---|---|---|
| Primária | Verde Laser | `#2BEE34` | rgb(43,238,52) | destaques, headline de impacto, CTA |
| Fundo escuro | Carbono | `#141414` | rgb(20,20,20) | background principal dos slides |

> Manter sempre fundo escuro — verde laser sobre branco perde o efeito "energia/laboratório".

### Variáveis CSS
```css
:root {
  --color-primary: #2BEE34;
  --color-bg-dark: #141414;
}
```

### Verificação de acessibilidade
| Combinação | Ratio | WCAG |
|---|---|---|
| Verde Laser sobre Carbono | ~13.2:1 | AAA |

---

## Tipografia

| Papel | Família | Peso | Fonte |
|---|---|---|---|
| Display / Headline | Brunson | 700 Bold | `reference/fonts/brunson/Brunson.ttf` |
| Body / legenda | Galano Grotesque Alt Regular | 400 | `reference/fonts/galano-grotesque/GalanoGrotesqueAltRegular.otf` |

> Licença: Brunson e Galano Grotesque são fontes pagas de foundry — confirmar licença antes de uso em material publicado.

### CSS
```css
:root {
  --font-display: 'Brunson', sans-serif;
  --font-body: 'Galano Grotesque Alt', sans-serif;
}
```

---

## Estilo visual geral

**Referência visual:** carrossel de choque científico — fundo escuro tipo "laboratório/espaço", dado numérico ou fato gigante em verde laser, imagens de apoio (planeta, célula, órgão) estilizadas, nunca stock photo genérico.
**Estilo de fotografia:** ilustração/render estilizado quando precisar de imagem (espaço, corpo humano) — não usar foto realista genérica de banco de imagens.
**Atmosfera:** científico, energético, "uau isso é real?"

---

## Notas de aplicação

Perfil irmão de [voce-ignorava-isso](../voce-ignorava-isso/brand-spec.md) e [historia-proibida](../historia-proibida/brand-spec.md). Mesma lógica de fundo escuro + acento neon, mas Verde Laser é exclusivo deste perfil — nunca usar nos outros dois.
