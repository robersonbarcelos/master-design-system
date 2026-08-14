---
name: workflow-producao-lp
description: Workflow orquestrado de produção de landing page com gates obrigatórios. Acionar quando Diego disser "quero produzir uma página", "nova LP", "criar página de vendas" ou similar. Nunca pular etapas. Nunca começar código sem aprovação do Gate 3.
---

# Workflow de Produção de Landing Page — INTUS HUB

## Trigger

Qualquer variação de: "quero produzir uma página", "nova LP", "criar página de vendas", "criar página de produto", "quero uma landing page".

Ao detectar o trigger: **não comece a codificar**. Inicie a Etapa 1.

---

## ETAPA 1 — BRIEFING COMPLETO

**Skill:** nenhuma — conversa direta com Diego.

Coletar obrigatoriamente:

- **Produto/serviço:** o que é, qual a promessa principal
- **Público-alvo:** quem é, cargo, dor principal, nível de consciência
- **Tipo de página:** vendas (PAS + oferta direta) ou produto (features/benefícios)
- **Tom/voz:** direto, consultivo, técnico, aspiracional?
- **Stack:** HTML puro, React/Next.js, intushub-template, outro?
- **Referências visuais:** mínimo 3 sites/marcas que Diego quer como referência
- **Anti-objetivos:** o que NÃO deve parecer, direção errada, o que evitar
- **Conteúdo disponível:** imagens reais, vídeo, copy existente, depoimentos

### 🔒 GATE 1

**Não avança sem:**
- Tipo de página definido (vendas ou produto)
- Mínimo 3 referências visuais fornecidas
- Anti-objetivos declarados (mesmo que seja "não parece genérico de SaaS")

---

## ETAPA 2 — ANÁLISE COMPETITIVA

**Skill:** `competitive-analysis`

Executar sobre os concorrentes diretos + referências fornecidas no briefing:

1. Abrir cada referência no Chrome e analisar visualmente
2. Mapear: IA/UX patterns, estrutura de seções, copy approach, CTAs, provas sociais
3. Identificar: o que todos fazem igual (table stakes), o que ninguém faz (gap)
4. Produzir tabela comparativa com pontos fortes, fracos e oportunidade

**Entregável:** mapa de oportunidade de diferenciação — onde a página do Diego se destaca.

### 🔒 GATE 2

**Diego valida:**
- A oportunidade de diferenciação faz sentido?
- Há algum padrão competitivo que ele quer adotar ou rejeitar?

Sem direção clara de diferenciação → revisitar referências antes de avançar.

---

## ETAPA 3 — DIREÇÃO ESTÉTICA + DESIGN SYSTEM + NARRATIVA

**Skills:**
- `impeccable → shape` (direção visual, scene sentence, design system)
- `ui-design/color-system` (paleta completa com tokens CSS e contraste verificado)
- `ui-design/typography-scale` (escala tipográfica modular como CSS vars)
- `references/catalogo-narrativa-lp.md` (estrutura de seções)
- `references/copy-conversao-lp.md` (framework PAS, 7 dimensões CRO)

### 3A — Direção Estética + Tokens (impeccable shape + color-system + typography-scale)

Definir e documentar:
- **Direção:** Minimalista Refinado / Bold Maximalist / Editorial / Retro-Futurista / Orgânico
- **Scene sentence:** quem usa, onde, que luz, que estado de espírito (força dark vs light)
- **Color strategy:** Restrained / Committed / Full palette / Drenched
- **Âncoras nomeadas:** 2-3 referências específicas (não adjetivos)
- **Tipografia:** display font + body font (nunca Inter/Roboto/Arial genérico)
- **Motion strategy:** entrada, scroll, hover
- **Layout approach:** centralizado simétrico? assimétrico? grid-breaking?

Após a direção aprovada, acionar **obrigatoriamente**:

`ui-design/color-system` → gerar paleta completa com tonal scales, semantic tokens (success/warning/error), verificar contraste WCAG AA em todas as combinações texto/fundo. Entregar como CSS custom properties prontas para colar no `:root`.

`ui-design/typography-scale` → gerar escala modular (caption 12px → display 48-64px), pesos, line-heights, letter-spacing. Entregar como CSS vars tipográficas prontas.

**Por que aqui e não na Etapa 5:** O problema de contraste insuficiente (ex: mentoria.html — cards `#0F0E1A` sobre `#07070D`) acontece quando a paleta é definida ao codificar, ad hoc. Tendo tokens verificados antes do Gate 3, o código da Etapa 5 usa variáveis já aprovadas e nenhum problema de contraste chega à auditoria.

### 3B — Estrutura de Seções + Narrativa

Definir sequência de seções baseada no tipo:

**Vendas (PAS):** Hero → Problema → Agitação → Solução → Prova → Especialização → VSL → Resultados → Oferta → Garantia → FAQ → Form/CTA → Footer

**Produto/Serviço:** Hero → Problema (leve) → Solução/Como funciona → Especialização → VSL → Casos de uso → Form/CTA → Footer

### 3C — Copy Framework

Para cada seção definir:
- Headline (sem travessão, sem cara de IA)
- Framework PAS aplicado: Problema → Agitação → Solução
- CTAs com verbo + resultado (não "Enviar", não "Saiba mais")
- Tom da voz: direto, humano, específico

### 🔒 GATE 3 — GATE MAIS CRÍTICO

**Diego aprova TUDO antes de qualquer código:**
- Brief visual escrito e confirmado
- Direção estética nomeada (não genérica)
- Sequência de seções aprovada
- Copy framework ou pelo menos headlines das seções principais

**Nunca começar código sem aprovação explícita do Gate 3.**

---

## ETAPA 4 — PROTOTIPAÇÃO DE SEÇÕES COMPLEXAS

**Skill:** `huashu-design`

Usar apenas para seções que envolvem:
- Hero com motion design (animação, dashboard, terminal, 3D)
- Interações não-triviais (carrossel, tabs, transições)
- Elementos visuais experimentais

Protocolo:
1. Gerar 3 variações visuais (HTML) da hero/seção complexa
2. Abrir no Chrome para review visual
3. Diego escolhe 1 direção ou hibridiza 2

### 🔒 GATE 4

- Diego aprova o protótipo visual da hero antes de avançar para implementação completa
- Se não há seções complexas → Gate 4 é pulado, avançar direto para Etapa 5

---

## ETAPA 5 — IMPLEMENTAÇÃO

**Skill:** `landing-page-guide-v2` (checklist dos 11 elementos)

Regras de implementação:

- Código fiel ao brief aprovado — desvios de direção precisam de aviso + aprovação
- Design system como CSS custom properties no `:root` antes de qualquer componente
- 11 elementos obrigatórios (ver `references/11-essential-elements.md`)
- Nunca usar Inter/Roboto/Arial sem justificativa de projeto
- Nunca usar gradiente roxo em fundo branco
- Nunca usar card grid genérico com ícone + título + texto idênticos
- Nunca usar travessão (—) no copy
- Reveal on scroll via IntersectionObserver
- Fontes self-hosted (woff2)
- Imagens: webp, fetchpriority="high" no hero, lazy abaixo da dobra

### 🔒 GATE 5

- Preview no Chrome confirmado (não apenas servidor local)
- Screenshot capturado e examinado seção por seção
- Nenhum erro de console

---

## ETAPA 6 — AUDITORIA + POLISH

**Skills (nesta ordem):**

1. `critique-screen` → auditoria das 4 dimensões:
   - `critique-visual-hierarchy` (entry point, eye flow, peso, ênfase)
   - `critique-brand-consistency` (mood, voz, tokens)
   - `critique-composition` (balanço, whitespace, ritmo, gestalt)
   - `critique-typography` (escala, legibilidade, consistência)

2. `impeccable → clarify` → copy: sem cara de IA, sem travessão, sem jargão empilhado

3. `impeccable → polish` → micro-detalhes de qualidade final

4. `impeccable → audit` → performance, acessibilidade, responsivo, Lighthouse

5. **PageSpeed Audit** (URL de produção real — nunca localhost):
   - Abrir `pagespeed.web.dev` com a URL publicada
   - Rodar Mobile + Desktop, capturar: Performance, LCP, TBT, CLS
   - Atacar top 3 oportunidades de alto impacto na ordem do relatório
   - Critério mínimo de aprovação: **Score Mobile >= 85, LCP < 2.5s, CLS < 0.1**
   - Referência de score alcançável: 96/97 (Super Agente LP)
   - Registrar scores antes/depois de qualquer correção

**Entregável:** lista priorizada de correções (P1 crítico / P2 importante / P3 polish) + scores PageSpeed Mobile e Desktop documentados.

Aplicar correções P1 e P2 antes de declarar a página pronta. Score Mobile < 85 bloqueia aprovação final.

---

## Resumo dos Gates

| Gate | Quando | O que bloqueia |
|------|--------|----------------|
| 🔒 Gate 1 | Após briefing | Sem referências ou tipo → não avança |
| 🔒 Gate 2 | Após análise competitiva | Sem oportunidade clara → revisitar |
| 🔒 Gate 3 | Após direção estética | Sem aprovação → nunca começa código |
| 🔒 Gate 4 | Após protótipo hero | Sem aprovação visual → não implementa |
| 🔒 Gate 5 | Após implementação | Sem preview no Chrome → não audita |

---

## Regras Permanentes de Copy (todas as páginas)

- **Nunca usar travessão (—)**. Substituir por ":" ou reescrever a frase.
- Sem frases "não X, é Y" (clichê de copy de IA saturado)
- CTAs com verbo + resultado: "Quero meu diagnóstico" não "Enviar"
- Headlines específicas com resultado/transformação — nunca genéricas
- Prova social específica: nome, resultado numérico, contexto — nunca vaga
- Urgência real apenas — nunca falsa/abusiva

---

## Skills por Etapa (referência rápida)

| Etapa | Skill principal | Skills auxiliares |
|-------|----------------|-------------------|
| 1 Briefing | — (conversa) | — |
| 2 Competitiva | competitive-analysis | Chrome extension |
| 3 Direção | impeccable → shape | web-design-conversao.md, catalogo-secoes |
| 4 Protótipo | huashu-design | Chrome extension |
| 5 Implementação | landing-page-guide-v2 | 11-essential-elements.md |
| 6 Auditoria | critique-screen | impeccable → polish, audit, clarify |
