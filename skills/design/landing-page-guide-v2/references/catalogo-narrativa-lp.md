---
name: catalogo-narrativa-lp
description: Catálogo de seções para landing pages com narrativa de conversão. Define sequência, papel de cada seção e quando usar. Adaptado do plugin intushub-plugin para HTML puro. Usar na Etapa 3 do workflow de produção.
---

# Catálogo de Seções — Narrativas de LP

## Tipo 1: Vendas (PAS + Oferta Direta)

Sequência recomendada para produto ou serviço com preço e CTA de compra/contato direto.

| # | Seção | Papel | Obrigatório |
|---|-------|-------|-------------|
| 1 | NAV | Logo + CTA principal fixo no topo | Sim |
| 2 | HERO | Promessa principal, headline, sub, 2 CTAs | Sim |
| 3 | SOCIAL PROOF | Números, logos, contador de clientes | Recomendado |
| 4 | PROBLEMA (DOR) | Nomeia a dor com especificidade | Sim |
| 5 | AGITAÇÃO | Custo de não resolver — tempo, dinheiro, risco | Sim |
| 6 | SOLUÇÃO | Como funciona, 3 passos, o que entrega | Sim |
| 7 | ESPECIALIZAÇÃO | Diferenciais ou módulos específicos | Recomendado |
| 8 | VSL | Vídeo talking head do Diego ou produto | Se disponível |
| 9 | RESULTADOS | Cases reais com número + setor + contexto | Sim |
| 10 | DEPOIMENTOS | Carrossel ou cards com nome + foto + resultado | Recomendado |
| 11 | OFERTA | Preço, ancoragem, o que está incluído | Sim (se tem preço) |
| 12 | GARANTIA | Remove o risco da decisão | Recomendado |
| 13 | FAQ | 5-8 objeções respondidas | Sim |
| 14 | FORM / CTA FINAL | Última chamada, máxima urgência | Sim |
| 15 | FOOTER | Links, legal, copyright | Sim |

**Narrativa resumida:** Hero (promessa) → Dor → Agitação → Solução → Prova → Oferta → Sem risco → Ação

---

## Tipo 2: Serviço/Mentoria (Alto Ticket, Sem Preço Público)

Para serviços consultivos, mentoria, high-ticket sem preço visível. CTA é diagnóstico/contato.

| # | Seção | Papel | Obrigatório |
|---|-------|-------|-------------|
| 1 | NAV | Logo + CTA "Solicitar diagnóstico" | Sim |
| 2 | HERO | Problema + o que fazemos + 2 CTAs | Sim |
| 3 | PROBLEMA (DOR) | 3 dores específicas do público | Sim |
| 4 | SOLUÇÃO | Como resolvemos, metodologia, 3 etapas | Sim |
| 5 | ESPECIALIZAÇÃO | 2-3 áreas de atuação com detalhes | Sim |
| 6 | VSL | Talking head do especialista | Se disponível |
| 7 | RESULTADOS | 3 cases: setor + número + descrição | Sim |
| 8 | SOBRE (opcional) | Credenciais do especialista, sem ego | Opcional |
| 9 | FAQ | 5-6 objeções de alto ticket | Recomendado |
| 10 | FORM MULTI-STEP | Form 4-5 etapas com progress tracker | Sim |
| 11 | FOOTER | Links, legal | Sim |

**Narrativa resumida:** Problema → Como resolvemos → Prova → Diagnóstico gratuito

---

## Tipo 3: Produto Digital (Curso/Infoproduto)

| # | Seção | Papel | Obrigatório |
|---|-------|-------|-------------|
| 1 | NAV | Logo + preço + CTA compra | Sim |
| 2 | HERO | Transformação prometida + CTA | Sim |
| 3 | STATS BAR | Alunos, avaliação, horas de conteúdo | Recomendado |
| 4 | PARA QUEM É | Persona com identificação | Sim |
| 5 | MÓDULOS | Conteúdo com accordion | Sim |
| 6 | RESULTADOS | Cases de alunos | Sim |
| 7 | DEPOIMENTOS | Com foto e resultado específico | Sim |
| 8 | OFERTA | Preço, ancoragem, bônus, parcelamento | Sim |
| 9 | GARANTIA | 7/14/30 dias | Sim |
| 10 | FAQ | Objeções de compra | Sim |
| 11 | CTA FINAL | Última chamada com urgência real | Sim |
| 12 | FOOTER | Links, legal | Sim |

---

## Regras de Seção

### Hero

- Headline: promessa específica com resultado (não genérica)
- Sub: amplia a promessa e antecipa objeção principal
- CTA primário: verbo + resultado ("Solicitar diagnóstico gratuito")
- CTA secundário: social proof ou "Ver como funciona"
- Elemento visual: motion design / imagem real / dashboard — nunca stock photo genérica
- Sem: travessão no copy, adjetivos sem substância

### DOR (Problema)

- Nomear a dor antes de falar da solução
- 3 dores específicas do público, não genéricas
- Cada dor: título concreto + descrição em 2-3 linhas
- Ícones: mínimos e sem cara de template SaaS
- Alternativa sem ícones: usar número (01/02/03) com tipografia maior

### SOLUÇÃO

- 3 etapas numeradas com nome e descrição
- Foco em resultado de cada etapa, não em feature
- Depois: 2 cartões de especialização com bullets específicos

### RESULTADOS / USE CASES

- Sempre: número de resultado + setor + contexto real
- Formato: métrica grande (destaque) → descrição do caso → setor
- Mínimo 3, máximo 5
- Placeholder aceitável se deixar claro que é exemplo a substituir

### FORM

- Alto ticket → form multi-step com 4-5 etapas
- Progress indicator no topo (Etapa 1 de 4)
- Form modal (clica no CTA, abre flutuando) ou inline?
  - **Modal:** melhor para páginas narrativas longas (não quebra o fluxo)
  - **Inline:** melhor para páginas curtas e diretas
- Etapas sugeridas para serviço/mentoria:
  1. Nome + WhatsApp
  2. Empresa + Segmento + Cargo
  3. Principal desafio (textarea)
  4. Confirmação + resumo do que foi preenchido

### FAQ

- 5-8 perguntas que respondem as objeções reais
- Não inventar objeções genéricas — pensar nas reais do público
- Accordion com animação suave
- Última pergunta sempre: "Como começo?" com resposta que leva ao CTA

---

## O que nunca fazer em seção nenhuma

- Card grid 3x com ícone SVG genérico + título + texto idênticos em peso (AI slop visual)
- Gradiente roxo/azul em fundo branco
- Testimunho sem nome, foto ou número real
- CTA enterrado abaixo de muito conteúdo sem repetição
- Seção de "sobre" longa antes das provas
- Countdown timer falso
