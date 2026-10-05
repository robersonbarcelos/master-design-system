# Brand Spec — [NOME DO CLIENTE]

last_updated: AAAA-MM-DD

> Gerado via huashu-design Core Asset Protocol.
> Nunca adivinhe valores — sempre extraia de fontes oficiais.

---

## Logo

**Arquivo principal:** [caminho relativo ou URL — ex: assets/logo.svg]
**Variações disponíveis:**
- [ ] Versão horizontal
- [ ] Versão vertical / símbolo isolado
- [ ] Versão branca (para fundos escuros)
- [ ] Versão preta (para fundos claros)
- [ ] Favicon

**Uso do logo:**
- Espaço mínimo ao redor: [X]
- Tamanho mínimo: [Xpx]
- Fundos permitidos: [branco / escuro / cor primária]
- Nunca: [esticar, rotacionar, alterar cores, adicionar sombra]

---

## Cores

### Paleta principal

| Papel | Nome | Hex | RGB | Uso |
|---|---|---|---|---|
| Primária | [nome] | #XXXXXX | rgb(X,X,X) | CTAs, destaques, links |
| Secundária | [nome] | #XXXXXX | rgb(X,X,X) | Elementos de suporte |
| Acento | [nome] | #XXXXXX | rgb(X,X,X) | Badges, tags, alertas |
| Fundo claro | [nome] | #XXXXXX | rgb(X,X,X) | Background principal |
| Fundo escuro | [nome] | #XXXXXX | rgb(X,X,X) | Seções de destaque |
| Texto principal | [nome] | #XXXXXX | rgb(X,X,X) | Body text |
| Texto secundário | [nome] | #XXXXXX | rgb(X,X,X) | Metadados, captions |

### Variáveis CSS
```css
:root {
  --color-primary: #XXXXXX;
  --color-secondary: #XXXXXX;
  --color-accent: #XXXXXX;
  --color-bg-light: #XXXXXX;
  --color-bg-dark: #XXXXXX;
  --color-text-main: #XXXXXX;
  --color-text-secondary: #XXXXXX;
}
```

### Verificação de acessibilidade
| Combinação | Ratio | WCAG |
|---|---|---|
| Texto main sobre bg light | X:1 | AA / AAA / Falha |
| Texto main sobre primária | X:1 | AA / AAA / Falha |
| Branco sobre primária | X:1 | AA / AAA / Falha |

---

## Tipografia

### Fontes

| Papel | Família | Peso(s) | Fonte de importação |
|---|---|---|---|
| Display / Headline | [nome] | [700, 800] | [Google Fonts / Adobe / local] |
| Body | [nome] | [400, 500] | [Google Fonts / Adobe / local] |
| Mono (se aplicável) | [nome] | [400] | [Google Fonts / Adobe / local] |

### Escala tipográfica

| Token | Tamanho | Peso | Line-height | Uso |
|---|---|---|---|---|
| display | 64px | 800 | 1.1 | Hero headline |
| h1 | 48px | 700 | 1.2 | Título de seção |
| h2 | 36px | 700 | 1.25 | Subtítulo |
| h3 | 24px | 600 | 1.3 | Card title |
| body-lg | 18px | 400 | 1.6 | Parágrafos principais |
| body | 16px | 400 | 1.6 | Body text |
| caption | 14px | 400 | 1.5 | Metadados |
| label | 12px | 500 | 1.4 | Labels, badges |

### CSS
```css
:root {
  --font-display: '[nome]', sans-serif;
  --font-body: '[nome]', sans-serif;
}
```

---

## Assets do produto

**Screenshots / mockups:**
- [caminho ou URL — ex: assets/product-screenshot-1.png]
- [ex: assets/dashboard-preview.png]

**Vídeos de demonstração:**
- [caminho ou URL]

**Imagens de resultado (antes/depois, provas):**
- [caminho ou URL]

---

## Estilo visual geral

**Referência visual:** [descreva em 2-3 frases o estilo — ex: "minimalista com acento bold, tipografia grande, muito espaço negativo, fotografia real sem stock photo genérico"]

**Estilo de fotografia:**
- [ ] Fotografia real (bastidor, pessoal)
- [ ] Mockups de produto
- [ ] Ilustração
- [ ] Misto

**Atmosfera:** [ex: premium e sério / descontraído e próximo / técnico e confiável]

**DESIGN.md de referência:** [nome do arquivo usado — ex: notion.DESIGN.md]

---

## Notas de aplicação

- Ver `analise-comparativa-brand-books.md` para o comparativo completo entre os 2 documentos recebidos (V1 "estratégica 1.0" e V2 "Final") e os conflitos/lacunas identificados.
- Cliente novo (onboarding 2026-09-10). Foco inicial de produção: Instagram e LinkedIn.
- Possibilidade futura (não decidida): redesenho de logo e do posicionamento visual de marca — não produzir arte definitiva de logo até essa decisão ser tomada com o Diego.
- Tipografia, tons de acento/fundo escuro, contraste WCAG e assets de produto (fotos reais de imóveis) ainda não foram fornecidos — pendente de coleta antes de fechar este brand-spec como definitivo.
