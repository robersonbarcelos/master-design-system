# Shape — Variação B (Homepage Premium) — Intus IA Corporate

> Fase: impeccable Shape. Status: aguardando confirmação do usuário antes do craft (React/Tailwind + taste-skill).
> Register: brand. Contexto: PRODUCT.md + DESIGN.md em `corporate-lp/`.

---

## 1 | Feature Summary

Landing page institucional (Variação B) do Intus IA Corporate — homepage premium multi-seção pra decisores de empresa que estão comparando fornecedores de consultoria de IA B2B (Epic Labs, Templo, Flowgrammers, ibe.IA, KapexIA, DORPA) e decidindo se aplicam pro processo seletivo. A página não vende — qualifica, gera desejo e escassez real, e converte em clique no CTA "Aplicar", que abre o popup de formulário já existente (Supabase + disparo Telegram).

## 2 | Primary User Action

Clicar em "Aplicar" / "Quero ser avaliado" — repetido em pelo menos 4 pontos da página (hero, pós-prova, pós-segurança, CTA final de escassez) — abrindo o popup de formulário existente.

## 3 | Design Direction

- **Color strategy:** Full palette (já fechada em DESIGN.md) — Intus Blue estrutural, Bright Gold como pontuação rara (One Gold Rule: 1x por dobra), White Ice/Hub Night como base neutra. Proporção 70/20/10.
- **Theme (scene sentence):** um decisor de empresa, sozinho no notebook, à noite ou de manhã cedo antes de uma reunião, com 3-4 abas de concorrentes abertas, cético, procurando o motivo real pra confiar em mais um fornecedor de "IA para empresas" — isso força dark, sóbrio, sem grito visual, com prova fazendo o trabalho pesado.
- **Anchor references:** Epic Labs (metáfora simples de processo + escassez real e comunicada), Templo (nível de acabamento institucional) — evitando explicitamente a estrutura hero-centrado + 3 cards idênticos que Epic Labs, Flowgrammers e KapexIA compartilham.

## 4 | Scope

- **Fidelidade:** shape completo (estrutura + copy) agora; craft (componentes React/Tailwind) só depois de aprovação.
- **Amplitude:** página inteira — todas as seções da Variação B.
- **Interatividade:** estática nesta fase. Popup de formulário, scroll-reveals e hover states entram no craft.
- **Intenção de tempo:** sem prazo apertado — foco em qualidade e aprovação de estrutura antes de gerar qualquer componente.

## 5 | Layout Strategy

Assimétrico do primeiro ao último bloco — nenhuma seção usa hero centrado ou grid de 3 cards iguais. Hierarquia de "gravidade crescente": a página abre séria (hero técnico, split 60/40) e vai empilhando peso de prova (skin in the game → segurança → interface → autoridade) até o momento de escassez no fim, que é o único bloco autorizado a usar o glow dourado com mais intensidade. O "Como Funciona" usa lista editorial numerada (padrão Epic Labs) em vez de cards, quebrando o padrão repetido nos concorrentes diretos.

## 6 | Key States

- **Default (scroll):** estado padrão, todas as seções visíveis em sequência.
- **Popup aberto:** overlay do formulário existente sobre a página (dimming do fundo, sem literal necessidade de construir — só o trigger).
- **Popup fechado / retorno:** usuário volta pro ponto de scroll onde estava.
- **Mobile:** nav colapsa, CTA "Aplicar" permanece fixo (sticky) no rodapé ou topo.
- **Reduced motion:** todas as animações de scroll-reveal viram fade instantâneo ou removidas.
- **Estado de escassez esgotada (futuro/opcional):** se o número de vagas do mês zerar, o card de escassez deve poder trocar pra "Lista de espera" sem quebrar layout — deixar isso previsto na estrutura, mesmo que não implementado agora.

## 7 | Interaction Model

Clique em qualquer CTA "Aplicar"/"Quero ser avaliado" dispara o popup de formulário já existente (Supabase + Telegram) — este shape não desenha o formulário, só define os pontos de gatilho. Scroll-triggered reveals sutis por seção (opacity + translateY pequeno, sem bounce, easing ease-out-quart), respeitando `prefers-reduced-motion`. Header sticky com CTA sempre visível após o hero. Sem modais além do popup de aplicação — nada de "modal como primeiro pensamento" pra outras interações (FAQ usa accordion inline, não modal).

## 8 | Content Requirements

Ver seção completa de copy abaixo (item 11). Assets necessários:
- **Mockup do painel/interface:** gerar novo, via `json-prompt-generator`, na paleta institucional (decisão do usuário — não reaproveitar o mockup laranja do site atual).
- **Foto do Diego:** asset já existente (`img/diego.png` + variantes).
- **Aspira/Clóvis:** assets já existentes (`img/aspira.png`, `img/clovis.png`).
- **Prova de clientes corporativos reais:** deferred pelo usuário ("entra depois") — layout precisa reservar espaço para isso sem ficar vazio/quebrado até lá (usar placeholder de peso visual equivalente, não bloco vazio).
- **Ícones de segurança:** line style, monocromático — a gerar/escolher no craft, nunca cadeado genérico de stock.

## 9 | Recommended References (para o craft)

`spatial-design.md` (layout assimétrico sem cards repetidos), `motion-design.md` (scroll-reveals contidos), `typography.md` (hierarquia Inter/Space Grotesk/JetBrains Mono), `interaction-design.md` (trigger de popup, accordion do FAQ), `color-and-contrast.md` (aplicação da One Gold Rule e WCAG AA sobre Hub Night).

## 10 | Open Questions

Nenhuma pendência bloqueante — defaults assumidos: fase 4 do processo (Treinar equipe) entra na lista "Como Funciona" mesmo não tendo entregável visual próprio; espaço de prova de clientes reais usa placeholder editorial (não card vazio) até vocês enviarem os cases.

---

## 11 | Estrutura completa de seções + copy (Variação B)

Mapeamento dos 11 elementos obrigatórios de LP (produção-system) + os diferenciais específicos do Intus IA Corporate.

### 01 — Header (sticky)
- Logo Intus Hub (V1 horizontal, versão light/dourado institucional)
- Nav: Como Funciona · Segurança · Prova · FAQ
- CTA topo direita: **"Aplicar"** (sempre visível, mesmo peso do resto da página)

### 02 — Hero *(elementos 1, 2, 3, 8)*
**Headline (Display, Inter 900):**
> Eu uso os agentes que construo. Sua empresa também vai.

**Subheadline:**
> Intus IA Corporate — implementação de IA sob medida para empresas. Não é curso. É a gente entrando na sua operação e construindo junto.

**Corpo de apoio:**
> Sua empresa não precisa de 10 ferramentas de IA. Precisa de um agente desenhado pro seu processo, com alguém treinado pra operar.

**Hero visual:** mockup do painel/interface (a gerar) num split assimétrico 60/40 — texto à esquerda, painel escuro com dados reais à direita, levemente rotacionado/sobreposto (não um retângulo centralizado).

**CTAs:** "Aplicar" (primário, Electric Blue) + "Ver como funciona" (ghost, âncora scroll pra seção 05)

### 03 — O Problema *(contexto/tensão antes da prova)*
**Headline:**
> Sua empresa está travada, e você já sabe disso.

Lista numerada 01/02/03 (reaproveitando a lógica já validada no site atual, adaptada ao tom institucional):
1. Seu time refaz a mesma tarefa manual todo dia — enquanto o concorrente já automatizou.
2. O relatório chega depois que a decisão já foi tomada.
3. Toda semana empurra pra próxima o que devia estar rodando sozinho.

### 04 — Prova operacional / Skin in the game *(elemento 5 + elemento 7, combinados)*
**Headline:**
> Somos o nosso próprio caso de uso.

**Corpo:**
> Aspira e Clóvis não são demo. São os agentes que rodam a operação do Diego todos os dias — antes de qualquer empresa contratar, o método já estava em produção na própria Intus Hub. Hoje, empresas reais já usam a mesma base.

- Bloco com foto do Diego + citação curta em 1ª pessoa (formato "Por que confiar" do Epic Labs, adaptado)
- Placeholder editorial reservado pra logos/nomes de clientes corporativos reais (layout pronto, populado depois)

### 05 — Como Funciona *(elemento 6 — processo, lista editorial, NUNCA cards)*
**Headline:**
> Do diagnóstico ao agente rodando. Sua equipe sai treinada pra continuar sozinha.

Lista numerada 01→04 (número grande em JetBrains Mono + título + descrição curta, separados por linha fina — sem ícones, sem cards):
1. **Identificar** — Mapeamos sua operação, seus gargalos reais e onde a IA gera ganho de verdade.
2. **Desenhar** — Arquitetura do agente, integrações, e o desenho de segurança e interface específicos pro seu negócio.
3. **Implementar** — Equipe técnica constrói e testa com dados reais da sua operação — não é entrega empacotada, é construção supervisionada.
4. **Treinar equipe** — Seu time aprende a operar, ajustar e expandir os agentes sem depender da gente.

### 06 — Segurança & Dados Sensíveis *(diferencial de mercado — nenhum concorrente tem)*
**Headline:**
> Dados sensíveis fazem parte do desenho, não são um detalhe técnico depois.

**Corpo:**
> Classificação do que é dado sensível na sua empresa, controle de acesso, adequação à LGPD quando aplicável, e definição clara de onde tudo fica armazenado — isso é parte da Fase 2, antes de qualquer linha de código.

Bloco visualmente mais "sóbrio" da página (regra do DESIGN.md) — ícones line-style monocromáticos, sem foto, sem glow dourado.

### 07 — Interface dedicada *(elemento 3 reforçado — prova visual tangível)*
**Headline:**
> Sua empresa opera o agente. Não decora comandos de terminal.

**Corpo:**
> Construímos um painel adequado pro uso corporativo — não um bot solto no Telegram. Você decide quem acessa, o que cada pessoa vê, e o que cada ação faz.

Segundo mockup do painel (ou zoom em detalhe do mesmo asset da seção 02) — prova visual de "produto real entregue".

### 08 — Escassez / CTA central *(elemento 11 — urgência real)*
**Headline:**
> Vagas de [mês] limitadas pela capacidade real da equipe técnica.

**Corpo:**
> Não é gatilho de marketing — é agenda física. Diego e a equipe técnica acompanham cada empresa de perto, o que limita quantas conseguimos atender ao mesmo tempo sem perder qualidade.

Card único com número de vagas em JetBrains Mono + Bright Gold (único uso de glow dourado mais intenso da página, respeitando a One Gold Rule).

**CTA:** "Aplicar para uma das [N] vagas"

### 09 — Garantia *(elemento 9 — objeção principal: "vou ficar dependente do fornecedor pra sempre")*
**Headline:**
> Garantia por marco, não por prazo genérico.

**Corpo:**
> Se o Relatório de Oportunidades da Fase 1 não apontar ganho viável pro seu negócio, você não avança — e recebe reembolso da Fase 1. Sem letra miúda.

### 10 — FAQ *(elemento 10)*
Accordion, reaproveitando e expandindo as perguntas já validadas no site atual:
- Minha empresa precisa de que tamanho pra fazer sentido?
- Quanto tempo até os primeiros resultados?
- Preciso ter equipe de TI própria?
- Isso substitui minha equipe atual?
- Quais áreas do negócio vocês cobrem?
- Como meus dados ficam protegidos durante o processo? *(nova — reforça a seção 06)*
- Minha equipe fica dependente de vocês depois? *(nova — reforça a garantia/Fase 4)*
- Como começar?

### 11 — CTA final + Rodapé
**Headline:**
> Quanto custa mais um mês de trabalho sem IA rodando de verdade?

CTA: "Aplicar" (repetido, mesmo peso do hero)
Rodapé: logo, links institucionais, sem redes sociais genéricas em destaque (mantém tom institucional).

---

**Próximo passo:** aguardando sua confirmação pra seguir pro craft (taste-skill + impeccable Craft/Polish) desta estrutura, ou ajustes antes disso.
