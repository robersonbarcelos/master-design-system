# Brand Spec — Você Ignorava Isso

last_updated: 2026-08-29

> Paleta e fonte selecionadas via gate de catálogo (`reference/colors/paletas-index.md` + `reference/fonts-index.md`).

---

## Logo

**Arquivo principal:** a definir (ainda não produzido)
**Variações necessárias:** horizontal, símbolo isolado, versão branca, versão preta, favicon
**Uso do logo:** a definir quando o logo for criado

---

## Cores

### Paleta principal — "Neon Limão"

| Papel | Nome | Hex | RGB | Uso |
|---|---|---|---|---|
| Primária | Neon Limão | `#A4F900` | rgb(164,249,0) | destaques, headline de impacto, CTA |
| Fundo escuro | Preto Fosco | `#141414` | rgb(20,20,20) | background principal dos slides |
| Fundo/texto claro | Branco Gelo | `#F2F2F2` | rgb(242,242,242) | texto sobre fundo escuro, contraponto |

> Fundo branco + neon lime tende a falhar visualmente — usar sempre fundo escuro (`#141414`) como base, com o neon como acento (ver `feedback_super-agente-palette-behavior` de outros clientes).

### Variáveis CSS
```css
:root {
  --color-primary: #A4F900;
  --color-bg-dark: #141414;
  --color-text-light: #F2F2F2;
}
```

### Verificação de acessibilidade
| Combinação | Ratio | WCAG |
|---|---|---|
| Neon Limão sobre Preto Fosco | ~13.8:1 | AAA |
| Branco Gelo sobre Preto Fosco | ~17.9:1 | AAA |

---

## Tipografia

| Papel | Família | Peso | Fonte |
|---|---|---|---|
| Display / Headline | Brunson | 700 Bold | `reference/fonts/brunson/Brunson.ttf` |
| Display alternativa (textura) | Brunson Rough | 700 | `reference/fonts/brunson/Brunson-Rough.ttf` |
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

**Referência visual:** carrossel de impacto — fundo escuro sólido, palavra/número gigante em neon limão, tipografia blocão dominando o frame, pouco elemento decorativo.
**Estilo de fotografia:** nenhuma foto real por padrão — composição tipográfica pura ou ilustração simples de apoio ao dado.
**Atmosfera:** pop, direto, jovem, "print de descoberta"

---

## Notas de aplicação

Perfil irmão de [ciencia-chocante](../ciencia-chocante/brand-spec.md) e [historia-proibida](../historia-proibida/brand-spec.md) — mesma lógica de fundo escuro + acento neon/dominante, mas cor de acento e fonte display exclusivas deste perfil. Nunca usar Neon Limão nos outros dois.
