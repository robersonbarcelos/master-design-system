# Brand Spec — INTUS HUB / Super Agente de IA

last_updated: 2026-05-21

> Gerado via huashu-design Core Asset Protocol.
> Dados extraídos da brand skill intus-hub-brand + LP sections.jsx + PRD.md

---

## Logo

**Arquivo principal:** Hexágono com hub — símbolo vetorial
**Variações disponíveis:**
- [x] V1 Horizontal Completa (INTUS HUB + símbolo)
- [x] V2 Símbolo Isolado
- [x] V3 Badge Circular
- [x] V4 Empilhada
- [x] V5 Light (fundo claro)
- [x] V6 Monograma IH

**Paleta do logo (campanha Super Agente — LP):**
- Stroke hexágono: gradiente laranja #FF6020 → #E84000 → #8C2000
- Núcleo: radial #FF9055 → #E84000 → #6A1800
- Fundo hex interno: #0a0a0a

**Paleta institucional (brand oficial):**
- INTUS: branco #F0F4FF · HUB: dourado #F0B429 (NUNCA azul)
- Fundo: Hub Night #050D1F

**Uso do logo:**
- Fundo sempre escuro — NUNCA branco
- HUB sempre em dourado (#F0B429) na versão institucional
- Na campanha SA: laranja substitui dourado em aplicações específicas
- Nunca esticar, rotacionar, alterar cores ou adicionar sombra

---

## Cores

### Paleta campanha — Super Agente de IA (LP)

| Papel | Nome | Hex | Uso |
|---|---|---|---|
| Primária | Intus Orange | #E84000 | CTAs, bordas, destaques, botões |
| Primária clara | Fire Orange | #FF6020 | Gradientes, hovers |
| Fundo | Deep Black | #0a0a0a | Background principal |
| Fundo alt | Dark Surface | #111111 | Cards, surfaces |
| Texto principal | White | #FFFFFF | Headlines, corpo |
| Texto secundário | Muted White | rgba(255,255,255,0.6) | Metadados, captions |
| Acento laranja claro | Light Fire | #FF9055 | Gradientes internos |
| Escuro âmbar | Dark Ember | #6A1800 | Sombras, profundidade |

### Paleta institucional — INTUS HUB (brand oficial)

| Papel | Nome | Hex | Uso |
|---|---|---|---|
| Fundo | Hub Night | #050D1F | Fundo principal |
| Primária | Intus Blue | #0033AA | Estrutura |
| CTA | Electric Blue | #0055FF | Botões, bordas |
| Secundária | Light Blue | #3399FF | Textos secundários |
| Institucional | Hub Gold | #C8960A | Impresso |
| Destaque | Bright Gold | #F0B429 | Palavra HUB, núcleo |
| Impacto | Signal Gold | #FFD700 | Core do núcleo |
| Texto | White Ice | #F0F4FF | Texto principal |

### Proporção padrão institucional
70% azul / 20% dourado / 10% branco

### CSS campanha Super Agente
```css
:root {
  --color-primary: #E84000;
  --color-primary-light: #FF6020;
  --color-bg: #0a0a0a;
  --color-surface: #111111;
  --color-text: #FFFFFF;
  --color-text-muted: rgba(255,255,255,0.6);
  --color-accent: #FF9055;
  --color-dark: #6A1800;
}
```

### Verificação de acessibilidade
| Combinação | WCAG |
|---|---|
| Branco sobre #0a0a0a | AAA |
| Branco sobre #E84000 | AA |
| #E84000 sobre #0a0a0a | AA |

---

## Tipografia

### Fontes site institucional (mentoria.intushub.com.br — fonte real, confirmada por inspeção do CSS em produção)

| Papel | Família | Peso(s) | Fonte |
|---|---|---|---|
| Display / Headline | Inter | 900/700 | Google Fonts |
| Body | Space Grotesk | 400/500/600 | Google Fonts |
| Mono / Tags | JetBrains Mono | 400/500 | Google Fonts |

**IMPORTANTE — regra atualizada em 2026-07-20:** o site institucional real usa **Inter** (não Syne) como fonte de display. Syne foi identificada como escolha equivocada em materiais anteriores — carrega assinatura visual de template genérico gerado por IA e não corresponde à identidade em produção. **Syne está proibida em qualquer peça institucional/site (Intus IA Corporate) a partir de agora.** Ela permanece restrita apenas a peças legadas de social media já publicadas, se existirem — não usar em nada novo.

### Fontes institucionais (uso legado — social media, não usar em peças novas)

| Papel | Família | Peso(s) | Fonte |
|---|---|---|---|
| Display / Headline | ~~Syne~~ (descontinuada — ver regra acima) | 800/700/600 | Google Fonts |
| Body | Space Grotesk | 400/500/600 | Google Fonts |
| Mono / Tags | JetBrains Mono | 400/500 | Google Fonts |

### Fontes LP Super Agente (campanha)

| Papel | Família | Peso(s) | Fonte |
|---|---|---|---|
| Display | Inter Tight | 900/800 | Google Fonts |
| Body | Inter Tight | 400/500 | Google Fonts |
| Mono | JetBrains Mono | 400 | Google Fonts |

**IMPORTANTE:** Inter Tight (variante compacta) é exclusiva da campanha Super Agente — não confundir com Inter padrão, que é a fonte de display do site institucional. Nunca misturar as três paletas tipográficas (institucional/Inter, social legado/Syne, campanha/Inter Tight) no mesmo criativo.

### Escala tipográfica

| Token | Tamanho | Peso | Uso |
|---|---|---|---|
| display | 64-80px | 800 | Hero headline |
| h1 | 48px | 700 | Título de seção |
| h2 | 36px | 700 | Subtítulo |
| h3 | 24px | 600 | Card title |
| body-lg | 18px | 400 | Parágrafos principais |
| body | 16px | 400 | Body text |
| caption | 14px | 400 | Metadados |
| label | 12px | 500 / JetBrains Mono | Tags, badges, all-caps |

---

## Assets do produto

**Agentes visuais:**
- `img/aspira.png` — Aspira (Super Agente operação)
- `img/clovis.png` — Clóvis (Super Agente estrutura)
- `img/diego.png` + `img/diego-1.png` a `img/diego-11.png` — fotos do Diego

**Mockup de produto:** Telegram shell com conversa Aspira (ver sections.jsx HeroVis)

**Depoimentos com foto:**
- `img/denys.jpg` — Denys Buso / Conset Capital
- `img/arcanjo.jpg` — Arcanjo / Tráfego pago

---

## Estilo visual geral

**Referência visual:** Dark premium com acento laranja queimado. Tipografia bold e grande. Muito contraste. Fundo quase preto com elementos que "brilham" (glow laranja). Sem glassmorphism genérico. Sem gradiente roxo/azul de IA padrão.

**Estilo de fotografia:**
- [x] Fotografia real (Diego com telas ao fundo)
- [x] Mockups de produto (Telegram shell, terminal)
- [ ] Ilustração
- [x] Misto

**Atmosfera:** Premium técnico com acessibilidade — sério mas direto, nunca frio. Parece startup de produto real, não curso genérico de IA.

**DESIGN.md de referência:** `elevenlabs` (dark com acento vibrante, tipografia bold, produto técnico acessível)

**Design skill:** `bold` — tipografia enorme, contraste extremo, pouco texto, impacto máximo

---

## Notas de aplicação

**Social media (estáticos):**
- Fundo sempre escuro (#0a0a0a ou #111111)
- Headline em Syne 800, branco ou laranja (#E84000)
- Laranja como acento — não preencher tudo
- JetBrains Mono para tags, preços, dados técnicos
- Nunca fonte Syne em peso menor que 600 em título
- Logo versão V2 (símbolo isolado) para criativos quadrados
- Logo V1 (horizontal) para banners e stories

**Campanha perpétua Super Agente:**
- Paleta: laranja/preto (não azul/dourado institucional)
- Sempre incluir preço 6x R$16,50 em criativos de conversão
- Âncora R$997 riscada antes de mostrar preço real
- Garantia 7 dias sempre presente em peças de fundo de funil
