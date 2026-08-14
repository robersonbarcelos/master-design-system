---
name: Intus IA Corporate
description: Consultoria B2B de IA implementada de verdade na operação do cliente — landing page institucional premium
colors:
  intus-blue: "#0033AA"
  electric-blue: "#0055FF"
  light-blue: "#3399FF"
  bright-gold: "#F0B429"
  signal-gold: "#FFD700"
  hub-gold: "#C8960A"
  hub-night: "#050D1F"
  surface-alt: "#0A1330"
  white-ice: "#F0F4FF"
typography:
  display:
    fontFamily: "Inter, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: "clamp(2.75rem, 5vw, 4.5rem)"
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Inter, 'Helvetica Neue', system-ui, sans-serif"
    fontSize: "clamp(1.75rem, 3vw, 2.5rem)"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Space Grotesk, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: "normal"
  label:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: "0.75rem"
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0.08em"
rounded:
  sm: "6px"
  md: "10px"
  lg: "16px"
spacing:
  sm: "8px"
  md: "16px"
  lg: "32px"
  xl: "64px"
  xxl: "120px"
components:
  button-primary:
    backgroundColor: "{colors.electric-blue}"
    textColor: "{colors.white-ice}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
  button-primary-hover:
    backgroundColor: "{colors.intus-blue}"
    textColor: "{colors.white-ice}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.white-ice}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "16px 32px"
  badge-scarcity:
    backgroundColor: "transparent"
    textColor: "{colors.bright-gold}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
  card-proof:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.white-ice}"
    rounded: "{rounded.md}"
    padding: "32px"
---

# Design System: Intus IA Corporate

## 1. Overview

**Creative North Star: "A Sala de Operações"**

Não é a vitrine de uma agência, é a sala onde o trabalho de verdade acontece — mapas de arquitetura, monitores escuros, dados reais rodando. A página não precisa convencer com brilho, precisa convencer com prova: cada seção mostra algo que já está funcionando, não promete algo que vai funcionar. O tom é institucional e contido, nunca frio — sério do jeito que um sócio técnico é sério numa reunião de decisão, não do jeito burocrático de um banco.

Rejeita explicitamente: hero centrado com headline gigante seguido de 3 cards idênticos (padrão repetido em Epic Labs, Flowgrammers e KapexIA — os três concorrentes diretos mais próximos usam essa mesma estrutura), gradiente roxo/azul genérico de produto de IA, qualquer resquício da paleta laranja/preto de campanha do Super Agente, e o verniz institucional vazio do Templo (acabamento premium sobre um produto que é só treinamento raso).

**Key Characteristics:**
- Assimétrico por princípio — nunca hero/seção centralizada como padrão
- Prova visual anexada a cada claim forte (nenhuma alegação "solta" sem elemento de apoio ao lado)
- Azul como estrutura (70% da superfície), dourado como pontuação rara (20%), branco como respiro (10%)
- Motion contido — reforça seriedade, nunca decorativo

## 2. Colors

Paleta de dois acentos com papéis fixos: azul constrói a estrutura da página inteira, dourado é reservado só para o momento em que algo precisa parecer "prova" ou "escassez real".

### Primary
- **Intus Blue** (#0033AA): cor estrutural — divisores, bordas de seção, fundo de blocos de conteúdo técnico (arquitetura, segurança). É a cor que "constrói" a página.
- **Electric Blue** (#0055FF): reservada exclusivamente para CTAs e estados interativos (hover, foco). Nunca usada como cor decorativa de fundo.

### Secondary
- **Bright Gold** (#F0B429): o "momento" — usada em no máximo 1 elemento por dobra (número de escassez, palavra-chave da headline, selo de prova). Sua raridade é o que a torna eficaz.
- **Signal Gold** (#FFD700): variante de maior impacto, reservada só para o núcleo do CTA final de escassez — nunca repetida em outra seção.

### Neutral
- **Hub Night** (#050D1F): fundo principal de toda a página.
- **Surface Alt** (#0A1330): fundo de seções que precisam se diferenciar levemente do hero (prova social, segurança, cards) sem quebrar o dark base.
- **White Ice** (#F0F4FF): texto principal, headlines.
- **Light Blue** (#3399FF): texto secundário, labels, metadados — nunca corpo de parágrafo longo.

### Named Rules
**The One Gold Rule.** Bright Gold ou Signal Gold aparecem no máximo uma vez por dobra de tela. Se duas seções adjacentes usam dourado, uma delas está errada — dourado é o sinal raro de "preste atenção aqui", não decoração recorrente.

## 3. Typography

**Display Font:** Inter (com fallback Helvetica Neue / sans-serif do sistema) — esta é a fonte de display real do site institucional em produção (mentoria.intushub.com.br), não a Syne usada nos materiais de social media.
**Body Font:** Space Grotesk (com fallback sans-serif do sistema)
**Label/Mono Font:** JetBrains Mono (com fallback monospace do sistema)

**Character:** Inter em peso 900/700 carrega o peso institucional da marca no site — geométrica, direta, sem o traço "editorial/display de IA genérica" que a Syne carrega; Space Grotesk no corpo mantém legibilidade técnica sem parecer frio; JetBrains Mono sinaliza "dado real" sempre que aparece (fases do processo, tags de categoria, badges de segurança).

### Hierarchy
- **Display** (800, clamp(2.75rem, 5vw, 4.5rem), 1.05): headline do hero — a única headline em peso 800 na página inteira.
- **Headline** (700, clamp(1.75rem, 3vw, 2.5rem), 1.15): título de cada seção (Prova, Segurança, Processo, Escassez).
- **Body** (400, 1rem, 1.6): parágrafos — máximo 65-75ch por linha.
- **Label** (500, 0.75rem, letter-spacing 0.08em, uppercase): badges de fase (01/02/03/04), tag de categoria do produto, metadados de prova social.

### Named Rules
**The No-Inter-Tight Rule.** Inter Tight (variante compacta) é exclusiva da campanha Super Agente — não confundir com Inter padrão, que é a fonte de display oficial do site institucional. Nenhum peso, nenhuma variante de Inter Tight aparece nesta linha de produto.

**The No-Syne Rule.** Syne está proibida em qualquer peça deste produto (Intus IA Corporate / site institucional). Syne tem assinatura visual de "gerado por IA/template genérico de landing page" — não é a fonte usada no site real da Intus Hub. Display font aqui é sempre Inter (700/900).

## 4. Elevation

Sistema flat por padrão — sem sombras decorativas. Profundidade é comunicada por variação de fundo (Hub Night → Surface Alt) e por glow pontual em elementos de destaque, nunca por `box-shadow` estrutural em cards comuns.

### Shadow Vocabulary
- **Glow azul** (`box-shadow: 0 0 40px rgba(0,85,255,0.2)`): usado apenas no CTA primário e em bordas de card ativo/selecionado.
- **Glow dourado** (`box-shadow: 0 0 32px rgba(240,180,41,0.18)`): reservado ao elemento único de "momento" por dobra (número de escassez, selo de prova) — respeita a One Gold Rule.

### Named Rules
**The Flat-By-Default Rule.** Superfícies são planas em repouso. Glow só aparece como resposta a estado (hover, foco) ou para marcar o único elemento de destaque dourado permitido por dobra.

## 5. Components

### Buttons
- **Shape:** cantos levemente arredondados (6px) — nunca pill/totalmente arredondado, nunca esquadro 0px.
- **Primary:** fundo Electric Blue (#0055FF), texto White Ice, padding 16px 32px, tipografia Label (JetBrains Mono, uppercase, tracking 0.08em). Label sempre "Aplicar" / "Quero ser avaliado" — nunca "Comprar" ou "Assinar".
- **Hover / Focus:** fundo escurece para Intus Blue (#0033AA) + glow azul; foco visível com outline 2px Electric Blue offset 2px (nunca `outline: none`).
- **Ghost (CTA secundário):** transparente, borda 1px White Ice a 30% opacidade, texto White Ice — usado para "Ver como funciona" ao lado do CTA primário.

### Badges / Tags
- **Estilo:** fundo transparente, texto Bright Gold, JetBrains Mono uppercase — usado em badges de fase e no número de escassez.
- **Regra:** segue a One Gold Rule — nunca mais de um badge dourado visível por dobra.

### Cards / Containers
- **Corner Style:** 10px (rounded.md).
- **Background:** Surface Alt (#0A1330) sobre fundo Hub Night.
- **Shadow Strategy:** flat por padrão (ver Elevation); glow azul apenas se o card for interativo/selecionável.
- **Border:** 1px solid rgba(51,153,255,0.2) como padrão; variante rgba(240,180,41,0.3) reservada ao card de escassez/prova central.
- **Internal Padding:** 32px (spacing.lg).
- **Regra:** nunca 3 cards idênticos lado a lado como bloco de "como funciona" — usar lista editorial numerada (número + título + descrição, separados por linha fina) em vez de grid de cards repetidos, seguindo o benchmark de processo do Epic Labs.

### Inputs / Fields (formulário de aplicação)
- **Style:** fundo Surface Alt, borda 1px rgba(51,153,255,0.2), texto White Ice, radius 6px.
- **Focus:** borda muda para Electric Blue sólido + glow azul sutil — nunca borda laranja (herança proibida da paleta antiga).
- **Error / Disabled:** erro em vermelho funcional (não pertence à paleta de marca, é só semântico) com mensagem inline; disabled reduz opacidade para 40%.

### Navigation
- Logo (V1 horizontal) à esquerda, CTA "Aplicar" sempre visível à direita mesmo em scroll (sticky), fundo Hub Night com blur sutil ao rolar. Mobile: menu colapsa, CTA permanece fixo.

## 6. Do's and Don'ts

### Do:
- **Do** usar Intus Blue como cor estrutural em 70% da superfície, Bright Gold como pontuação em 20%, branco como respiro em 10% — proporção institucional oficial da marca.
- **Do** anexar prova visual a cada claim forte (skin in the game, segurança, escassez) — nenhuma alegação sozinha em texto.
- **Do** usar Inter 700/900 em toda headline, nunca abaixo de 700.
- **Do** manter layout assimétrico, sem hero centrado.

### Don't:
- **Don't** usar a fonte Syne em nenhuma peça — não é a fonte do site real, tem assinatura de template genérico de IA. Display font é sempre Inter.
- **Don't** usar hero centrado seguido de grid de 3 cards idênticos — é o padrão repetido em Epic Labs, Flowgrammers e KapexIA; essa página precisa ser visivelmente diferente disso.
- **Don't** usar gradiente roxo/azul genérico de produto de IA.
- **Don't** usar qualquer valor da paleta de campanha do Super Agente (#E84000, #FF6020, Inter Tight) — pertence só ao produto B2C.
- **Don't** usar o hero-metric template (número grande + label pequeno + stats de apoio) — é clichê de SaaS.
- **Don't** usar linguagem de compra ("Comprar", "Assinar", "Checkout") em nenhum CTA — o funil é de aplicação, não de venda direta.
- **Don't** usar mais de um elemento com glow/badge dourado por dobra de tela.
