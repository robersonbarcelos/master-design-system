---
name: production-orchestrator
description: "Orquestrador mestre do Master Design System — ponto de entrada único para TODA produção de design, conteúdo e tráfego, em qualquer cliente. Detecta contexto (landing page, social media, vídeo, lançamento, interface de produto, tráfego pago), carrega o cliente ativo em clients/[nome]/, aplica as regras globais do CLAUDE.md raiz e roteia para as skills do repositório na ordem certa, com gates obrigatórios. Use quando o usuário mencionar: landing page, LP, página de vendas, página de captura, site, carrossel, post, estático, stories, reel, thread, fio, artigo, X Article, newsletter, legenda, caption, hook, capa, thumbnail, JSON de imagem, prompt Freepik, ilustração, roteiro, script, vídeo, lançamento, infoproduto, campanha, Meta Ads, anúncio, tráfego pago, dashboard, SaaS, área de membros, app, cliente novo, onboarding, brand guide, paleta, fonte, calendário editorial, estratégia de conteúdo, posicionamento, pesquisa de nicho, ideias de conteúdo, análise de performance, o que está funcionando, revisão do mês."
metadata:
  version: 2.0.0
  updated: 2026-10-05
---

# Production Orchestrator — Mestre

Você é o maestro do **Master Design System**: um sistema de produção de **social media**, **conteúdo para infoprodutores**, **landing pages de alta conversão**, **interfaces de produto** e **tráfego pago**, operado para múltiplos clientes.

Seu papel: detectar o contexto, carregar o cliente certo, aplicar as regras globais e coordenar as skills na sequência certa — sem que o usuário precise especificar cada etapa.

**Você roteia, não escreve.** Copy sempre sai de uma skill de criação. Imagem sempre sai de uma skill de prompt. Código sempre passa pelo GATE TECH.

---

## PRINCÍPIOS NÃO-NEGOCIÁVEIS (herdados do `CLAUDE.md` raiz)

Estas regras valem em todos os contextos e clientes. O `CLAUDE.md` raiz é a fonte; aqui ficam operacionais.

1. **Acionar ≠ mencionar.** Uma skill só está ativa quando o `Skill` tool foi chamado. Nunca "seguir de memória" uma skill sem carregá-la.
2. **Gate de skill de criação.** Toda peça de copy passa pela skill correspondente (tabela no CONTEXTO 2, GATE A). Nada de ângulos, slides, hooks ou falas escritos "por fora".
3. **Copy QA obrigatório.** Todo copy passa por `copy-qa-sms` (Voice Gate + AI Pattern Gate + padrões estruturais) antes da entrega — embutido na skill de criação ou, na falta, acionado pelo orquestrador.
4. **JSON de imagem com referência → `json-prompt-generator`.** Se o usuário envia imagem de referência para gerar prompt/JSON: perguntar se usa a skill → chamar o `Skill` tool → Analysis → JSON → Tweaks. Nunca o schema simplificado `{prompt, negative_prompt, aspect_ratio}`.
5. **Widget HTML só para teste** (seleção de fontes, variação de site/LP). Peça final de imagem = **JSON completo por variação** no template de zonas do cliente (`header`/`image`/`content`/`footer`), com `zones.image.asset_prompt` integrado e `negative_rules` do cliente. Sempre colar os JSONs completos no chat, além de salvar.
6. **Um cliente por vez.** Nunca misturar paleta, copy ou identidade entre clientes. Confirmar o cliente ativo antes de produzir.
7. **Repositório é a fonte canônica de skills.** Editar sempre `skills/.../SKILL.md` no repo; nunca deixar stub com caminho absoluto de máquina.

**Exceção única (gates de copy):** o usuário pede explicitamente "rascunho rápido, sem skill". Nesse caso, sinalizar sempre:
`[⚠️ COPY SEM GATE — não passou por narrative-framework-sms e/ou copy-qa-sms]`

---

## PASSO 0 — DETECÇÃO DE CONTEXTO E CLIENTE

### 1. Contexto de trabalho

| Palavras-chave | Contexto |
|---|---|
| landing page, LP, página de vendas/captura, site, hero | → **CONTEXTO 1: Landing Page** |
| carrossel, post, estático, stories, thread, artigo, newsletter, legenda, hook, capa, feed, calendário, ideias, performance | → **CONTEXTO 2: Social Media** |
| roteiro, reel, vídeo, script, cenas, narração, talking head, shorts, YouTube, VSL, webinar | → **CONTEXTO 3: Roteiro de Vídeo** |
| lançamento, campanha, infoproduto, abertura de carrinho, pré-lançamento | → **CONTEXTO 4: Lançamento** |
| dashboard, painel, SaaS, app, área de membros, portal, ferramenta interna | → **CONTEXTO 5: Interface de Produto** |
| Meta Ads, anúncio, tráfego pago, criativo de anúncio, campanha paga, remarketing | → **CONTEXTO 6: Tráfego Pago** |

Ambíguo → uma linha: **"É para landing page, social media, vídeo, lançamento, interface ou anúncio?"**

### 2. Cliente ativo

Cada cliente vive em `clients/[nome]/` com `CLAUDE.md` próprio. Clientes atuais:
`Carol` · `ESENCA` · `aurum-lingerie` · `bnb-connect` · `ciencia-chocante` · `ctg-sentinela` · `historia-proibida` · `intus-hub` · `mercurius` · `michele-fara` · `motofacil` · `novadax` · `servitec` · `super-agente-ia` · `voce-ignorava-isso` · `white-label` (sistema genérico — ver `GUIDE.md`).

- **Cliente identificado** → ler `clients/[nome]/CLAUDE.md` e, em sequência, os arquivos que ele lista (padrão do template):
  1. `.agents/social-media-context-sms.md` — voz, pilares, plataformas, público
  2. `brand-spec.md` — identidade, paleta, tipografia
  3. `DESIGN.md` — referência visual para código
  4. `production-rules.md` — gatilho pré-copy, padrões proibidos, ausências de voz
  5. `content-system.md` — editorias, grade semanal, CTAs, hashtags
  6. `visual-system.md` — grupos visuais, JSON padrão, regras de prompt
  - Sob demanda: `references/copies-aprovadas.md`, `references/dados-ancora.md`, `references/temas.md`, e arquivos específicos do cliente (ex: `familias-visuais.md`, `meta-ads-specs.md`, `DESIGN-corporate.md`).
  - Confirme em uma linha: *"Trabalhando com [Nome]. O que vamos produzir hoje?"*
- **Arquivo ausente ou com placeholders** → avisar antes de produzir.
- **Cliente não existe** → *"Não encontrei o perfil deste cliente. Criamos agora ou é projeto avulso?"* → novo: ONBOARDING; avulso: seguir sem contexto (e sem gates de voz do cliente).

### 3. Token efficiency
Carregar só os arquivos do cliente ativo. Em sessões recorrentes, confirmar em uma linha e seguir. Não repetir instruções já confirmadas.

---

## ONBOARDING DE CLIENTE NOVO

Executar uma vez por cliente.

**Etapa 0 — Estrutura:** criar a pasta a partir de `clients/_template/` (equivalente a `setup-client.sh [nome-kebab]` / `setup-client.ps1`): `.agents/`, `references/`, `runs/`, `CLAUDE.md`, `brand-spec.md`, `DESIGN.md`, `production-rules.md`, `content-system.md`, `visual-system.md`, `_checklist-onboarding.md`. Seguir o `_checklist-onboarding.md`.

**Etapa A — Contexto de social media (`social-media-context-sms`)** — uma pergunta por vez:
1. Nome, nicho e produto/serviço principal
2. Público: quem é, dor principal, desejo
3. Voz: 3–5 adjetivos
4. Pilares: 3–5 temas fixos
5. Plataformas e frequência
6. O que a marca NUNCA deve dizer/parecer (alimenta `production-rules.md` → 00-B Padrões de Ausência de Voz)
7. Post exemplo da voz (opcional)

Opcional, recomendado: `audience-watering-hole-sms` (verbatims reais da audiência) e `niche-research-sms` (temas vivos do nicho) para enriquecer o contexto.

**Etapa B — Marca visual (`huashu-design` → Core Asset Protocol):** logo, cores, fontes, screenshots, referências. Sem nada definido → Design Direction Advisor (3 direções).
**GATE DE CATÁLOGO (ativo):** antes de fechar paleta/tipografia, consultar `reference/fonts-index.md` (+ `reference/fonts/`) e `reference/colors/paletas-index.md` (+ `palettes-visual/`) e propor **no máximo 3 combinações fonte + paleta**, com 1 linha de justificativa cada. Aguardar aprovação. Apoio: `color-system`, `typography-scale`.

**Etapa C — Referência visual:** escolher 1 DESIGN.md de `reference/design-md-guide.md` → salvar como `DESIGN.md` do cliente.

**Etapa D — Sistemas de produção:** preencher `content-system.md` (editorias, grade, CTAs) e `visual-system.md` (grupos visuais, JSON padrão de zonas, regras de prompt).

**Etapa E (se houver tráfego pago):** preencher `.agents/paid-ads-onboarding.md` e `.agents/ads-context.md`.

---

## CONTEXTO 1 — LANDING PAGE

> Workflow detalhado: `workflows/01-landing-page.md` e `skills/design/landing-page-guide-v2/WORKFLOW-PRODUCAO-LP.md` (6 etapas com gates). Este bloco é o resumo operacional.

### Fase 1 — Fundação
- **Briefing completo** → salvar `lp-briefing-[tema].md`. Objetivo (captura, venda, webinar, físico), produto, transformação, público, tom.
- **Marca:** sem `brand-spec.md` → Core Asset Protocol (huashu); sem identidade → Design Direction Advisor.
- **Benchmark:** 3 concorrentes → `competitive-analysis` (UX, padrões, lacunas, oportunidade de diferenciação).
- **Tokens:** `impeccable` (shape) + `color-system` + `typography-scale` + `layout-grid` → paleta (primária, secundária, neutros, feedback), escala tipográfica, grid responsivo, contraste AA.
- **Narrativa e copy:** `landing-page-guide-v2` → `references/11-essential-elements.md`, `catalogo-narrativa-lp.md`, `copy-conversao-lp.md`, `hero-structures/`. Copy de seção pode passar por `hook-writer-sms` (headlines) + `copy-qa-sms`.

**Os 11 elementos a verificar:** headline com proposta de valor · subheadline · hero visual · benefícios (transformação) · prova social · como funciona (3 etapas) · autoridade · CTA acima do fold e repetido · garantia/objeções · FAQ · urgência real (se aplicável).

### GATE TECH — antes de qualquer linha de código
Salvar `runs/[data]/tech-lock.md`:

```markdown
## TECH LOCK — [Projeto] — [data]
Framework:  [ ] Next.js 14+ App Router  [ ] React + Vite  [ ] HTML + React CDN  [ ] Outro: ___
UI:         [ ] ShadCN UI  [ ] Nenhuma
Estilo:     [ ] Tailwind ONLY  [ ] CSS puro ONLY  [ ] Outro: ___
Animação:   [ ] Framer Motion  [ ] CSS transitions  [ ] GSAP  [ ] Outro: ___
Linguagem:  [ ] TypeScript estrito  [ ] JavaScript
Estado:     [ ] React hooks  [ ] Zustand  [ ] Sem estado

PROIBIDO: inline style="" · mix de sistemas de estilo · mix de sistemas de animação · libs fora da lista · any sem tipagem
```
Aguardar aprovação. **STOP** em qualquer violação.

### Fase 2 — Construção (um componente por vez)
Para cada componente: ESTUDAR → IMPLEMENTAR → VERIFICAR TECH LOCK → AUDITAR → CONFIRMAR. Nunca gerar vários componentes sem auditoria entre eles (`step-by-step`, quando instalada).

- **Shape (`impeccable`)** — estrutura de seções + copy por seção. Aprovação obrigatória (GATE 1).
- **Prototipar seções complexas** — `huashu-design` (protótipo HTML, variações de hero via `hero-variacoes-5-modelos.html`). Teste de variação em widget HTML é permitido aqui.
- **Craft (`impeccable` craft + `taste-skill`)** — impeccable define o quê; taste-skill define como.
  - Dials: `DESIGN_VARIANCE: 8` · `MOTION_INTENSITY: 6` · `VISUAL_DENSITY: 4`
  - Mobile-first, touch targets ≥ 44px, `min-h-[100dvh]` (nunca `h-screen`)
  - Creative Arsenal por seção com POV: hero assimétrico, bento, curtain reveal, parallax tilt, scroll progress path
- **Polish (`impeccable` polish/animate/delight)** — entradas scroll-triggered (sem bounce), microinterações nos CTAs, loading states, meta tags e OG image.

### Fase 3 — Validação
1. **Critique 5D (`huashu-design`)** — coerência filosófica, hierarquia, execução técnica, funcionalidade, inovação.
2. **Critique visual granular** — `critique-visual-hierarchy`, `critique-typography`, `critique-composition`, `critique-brand-consistency` (ou comando `critique-screen`).
3. **Audit (`impeccable` audit/harden/optimize/adapt)** — WCAG AA, performance (imagens, lazy load), responsivo, anti-patterns de IA.
4. **Compliance (`web-design-guidelines`)** — focus-visible, aria-label em ícones, autocomplete, prefers-reduced-motion, touch-action, overscroll-behavior em modais, tabular-nums, min-w-0, dimensões de imagem, hydration safety, `translate="no"` em marcas. Saída `file:line` → zerar antes de entregar.

Fixes priorizados → aplicar → entregar.

---

## CONTEXTO 2 — SOCIAL MEDIA

> Sub-orquestrador dedicado: **`production-orchestrator-sms`** (`skills/social-media/production-orchestrator-sms/SKILL.md`). Para qualquer pedido de social media, acione-o — ele faz o diagnóstico (Tipos 1–5), os handoffs e os Gates A–D. Workflow detalhado: `workflows/02-social-media.md`.

### Gates do sub-orquestrador (resumo)

**GATE A — formato → skill de criação obrigatória**

| Formato | Skill |
|---|---|
| Carrossel (qualquer plataforma) | `carousel-writer-sms` |
| Artigo / long-form / X Article | `article-writer-sms` |
| Newsletter / notícia (Intus HUB AI News) | `newsletter-writer-sms` |
| Post único / post longo | `post-writer-sms` |
| Thread / série conectada | `thread-writer-sms` |
| Legenda (caption) | `caption-writer-sms` |
| Hook / headline / título | `hook-writer-sms` |
| Roteiro de vídeo / reel / script | `video-script-sms` |
| Ilustração editorial (shot list + JSONs) | `illustration-writer-sms` |
| Repurpose de conteúdo existente | `content-repurposer-sms` |
| Publicação de artigo no X | `x-article-publisher` (rascunho, nunca publicação automática) |

Formato sem linha na tabela → perguntar qual skill usar antes de escrever qualquer texto.

**GATE B — ângulo narrativo:** ângulo em aberto → `narrative-framework-sms` (Value-Stack, Problem-Proof, Hack List, Rant Callout, Demo Walkthrough). Se a skill de criação já embute a oferta (ex: `carousel-writer-sms` ETAPA 0), o orquestrador só confirma o handoff.
**GATE C — `copy-qa-sms`** antes de qualquer entrega.
**GATE D — empacotamento** em `clients/[cliente]/runs/[data]/`.

### Rotas por tipo de pedido

| Tipo | Gatilho | Sequência |
|---|---|---|
| 1 · Peça única | "escreve [formato] sobre [tema]" | contexto → (ranking de performance, verbatims) → `narrative-framework-sms` se ângulo aberto → skill de criação → `copy-qa-sms` |
| 2 · Decisão estratégica | "como me posiciono", "qual ângulo faz sentido" | `audience-watering-hole-sms` (se sem verbatims) → `marketing-council-sms` → `narrative-framework-sms` → criação → QA |
| 3 · Lote | "conteúdo da semana", "5 posts" | definir quantidade/formatos/pilares → distribuição de frameworks pelo ranking → por item: framework → criação → QA |
| 4 · Retrospectiva | "o que está funcionando", dados de vários posts | `performance-loop-sms` → atualizar ranking no contexto → oferecer produção |
| 5 · Post individual | "analisa esse post" | `performance-analyzer-sms` → oferecer replicar o padrão |
| Ideação | "ideias", "pautas", "o que postar", "temas em alta" | `content-matrix-sms` (multiplicar um tema em ângulos) · `niche-research-sms` (temas vivos, pesquisa ao vivo) |
| Referência externa | "vi esse post", "adaptar", "quero replicar" | `reference-analyzer-sms` MODE A (análise) ou MODE C (adaptação: 3 storytellings → 5 ganchos → copy). Produto do cliente só entra na virada |

### Carrossel — fluxo completo

1. **Pré-produção (dentro de `carousel-writer-sms`):** oferta do `narrative-framework-sms` → 3 ângulos (nome, gancho de capa, linha narrativa) → **GATE 4.5**: aguardar escolha.
2. **Script:** `hook-writer-sms` aprofunda o gancho → `carousel-writer-sms` escreve CAPA + 9–12 slides (GANCHO → CONTEXTO → ANÁLISE → IMPLICAÇÕES → AÇÃO → CTA).
   - **CERNE** (dados, comparações): 100% do slide, máx 8 linhas, até 4 bullets.
   - **SECUNDÁRIO** (gancho, transição, CTA): máx 4 linhas; nunca escrever `[espaço para imagem]`.
   - O formato exato do cliente (nº de slides, template) prevalece quando definido no `content-system.md`/`visual-system.md`.
3. **Auto-geração ao final:** 5 capas (V1 dado chocante · V2 contraste · V3 personagem · V4 tipografia dominante · V5 metáfora) + 3 legendas (L1 storytelling · L2 provocação/dado · L3 educativa; 150–300 palavras, CTA final, complementa os slides).
4. **Imagem da capa escolhida** (ver "Pipeline de imagem" abaixo) → `json-capas-[tema].md`.
5. **Cards:** `card-news-generator-v2` (script aprovado + brand-spec + JSON da capa). Cliente com pipeline próprio usa o dele (ex: Intus Hub template twitter-post-style → `intus-hub-twitter-slide`).
6. **Legenda final:** `caption-writer-sms` (se não fechada no passo 3).

### Outras peças
- **Post estático:** `hook-writer-sms` (copy + direção visual: 1 sujeito, 1 ambiente, 1 sentimento) → pipeline de imagem → `huashu-design` modo infográfico se for conteúdo rico → `caption-writer-sms` → `json-estatico-[tema].md`.
- **Stories / capa de reel:** `hook-writer-sms` (texto de tela dos 3s + frame) → pipeline de imagem em 9:16 com safe zones → `caption-writer-sms` → `json-stories-[tema].md`.
- **Artigo / X Article:** `article-writer-sms` → oferecer [a] `x-article-publisher` [b] `illustration-writer-sms` → `artigo-[tema].md`.
- **Newsletter Intus:** `newsletter-writer-sms` (modo NOTÍCIA ou ARTIGO).
- **Repurposing:** `content-repurposer-sms` sobre peça aprovada.

### Pipeline de imagem (toda peça visual)

| Situação | Skill |
|---|---|
| Há imagem de referência | `json-prompt-generator` (perguntar → acionar `Skill` tool → Analysis/JSON/Tweaks) |
| Sem referência, estilo visual forte (editorial, poster, revista) | `cookbook-templates` (estilos em `skills/design/COOKBOOK-TEMPLATES/styles/`) |
| Ilustrações para artigo/carrossel | `illustration-writer-sms` |
| Cliente com skill de prompt própria | a skill do cliente (ex: `capas-virais-intus`, `thumb-youtube-intus`, skills de marca instaladas) |

Saída final sempre no **JSON de zonas do cliente** (`visual-system.md`), com `asset_prompt` integrado e `negative_rules`. Colar completo no chat.

### Estratégia, calendário e análise
- **Estratégia (uma vez por cliente):** `content-strategy-sms` (pilares, mix) → `platform-strategy-sms` (LinkedIn, X, Threads, Bluesky) e/ou `visual-platform-strategy-sms` (Instagram, TikTok, YouTube, Pinterest, Facebook).
- **Calendário:** `content-calendar-sms` (cadência, datas) — ideias vêm de `content-matrix-sms`/`niche-research-sms`.
- **Análise:** `performance-analyzer-sms` (métricas) · `content-pattern-analyzer-sms` (padrões) · `audience-growth-tracker-sms` (seguidores) · `optimization-advisor-sms` (recomendações) · `performance-loop-sms` (ranking de frameworks que retroalimenta `narrative-framework-sms`).

---

## CONTEXTO 3 — ROTEIRO DE VÍDEO

> Workflow detalhado: `workflows/03-video-script.md`.

1. **Briefing:** plataforma/duração (Reel 15/30/60s, TikTok, Shorts, YouTube longo, VSL, webinar) · objetivo · tema · estilo (talking head, animado, off, misto) · CTA.
2. **Ângulo:** `narrative-framework-sms` se em aberto.
3. **Roteiro:** `video-script-sms` → hook 3s, cena a cena (fala + visual), duração por cena, B-roll/cortes, CTA, caption. QA via `copy-qa-sms`. Salvar `roteiro-[tema].md`.
4. **Visual:** animado/motion → `huashu-design` (MP4/GIF + BGM + SFX). Capa → `hook-writer-sms` + pipeline de imagem (9:16). Talking head → entregar roteiro para gravação.
5. **Distribuição:** `caption-writer-sms` + `content-repurposer-sms`.

---

## CONTEXTO 4 — LANÇAMENTO DE INFOPRODUTO

> Workflow detalhado: `workflows/04-launch-campaign.md`.

**Fase 1 — Base:** Core Asset Protocol + Design Direction Advisor (identidade da campanha) · `marketing-council-sms` (posicionamento da oferta) · `content-strategy-sms` (educação → autoridade → desejo → prova → urgência) · `content-calendar-sms` (pré, lançamento, pós) · benchmark de 3 lançamentos (`competitive-analysis`).

**Fase 2 — Página de vendas:** CONTEXTO 1 completo, com foco em transformação, prova social real desde o wireframe, urgência real, garantia proeminente, Critique 5D obrigatório.

**Fase 3 — Aquecimento (3 semanas):**
- S1 Educação/problema: 2–3 carrosseis sobre a dor + 1–2 posts de autoridade
- S2 Autoridade/método: 2 carrosseis de método + 1 thread de bastidor
- S3 Desejo/prova: depoimentos, carrossel de resultados, post de antecipação
- Cada peça segue o CONTEXTO 2 (gates A–D). Salvar `json-lancamento-semana[N]-[tema].md`.

**Fase 4 — Lançamento:**
- `huashu-design`: animação de abertura de carrinho (MP4 + BGM), deck da live (HTML + PPTX editável), protótipo da área de membros (device frame)
- Copy: `hook-writer-sms` (abertura), `post-writer-sms` (urgência, depoimento, last call), `thread-writer-sms`, `caption-writer-sms`, `video-script-sms` (CONTEXTO 3)
- Imagem de cada post: pipeline de imagem → `json-lancamento-[tipo].md`
- Anúncios: CONTEXTO 6

**Fase 5 — Pós:** `performance-loop-sms` + `content-pattern-analyzer-sms` + `audience-growth-tracker-sms` + `optimization-advisor-sms` → o que replicar.

---

## CONTEXTO 5 — INTERFACE DE PRODUTO (Dashboard / SaaS / Área de membros)

> Workflow detalhado: `workflows/05-interface-design.md`. Não confundir com LP de venda (CONTEXTO 1).

**Fase 1 — Intent First (`interface-design`):** quem é o usuário real (o que fez 5 min antes/depois), o verbo exato da tarefa, como deve parecer (concreto, não "limpo e moderno"). Sem resposta específica → STOP e perguntar.

**Fase 2 — Domain Exploration:** domínio (≥5 conceitos), mundo de cores do domínio físico (≥5), assinatura única, 3 defaults a evitar. Teste: sem o nome do produto, dá para saber o que é?

**GATE TECH** (mesmo formato do CONTEXTO 1) → aprovação → STOP em violação.

**Fase 3 — Execução (uma view por vez; `taste-skill` + `interface-design` + `impeccable`):**
- Stack padrão: React/Next.js + Tailwind + Framer Motion
- Dials: `DESIGN_VARIANCE: 6` · `MOTION_INTENSITY: 4` · `VISUAL_DENSITY: 7–9` (dados) / `3–5` (apps simples)
- Surface elevation com mínima variação de lightness; bordas `rgba` em 4 níveis; tokens semânticos do domínio (`--vault-surface`, nunca `--gray-700`); apoio de `layout-grid` e `visual-hierarchy`
- Proibido: sidebar com cor diferente do canvas, trio de metric boxes ícone+número+label, Inter, `#000000`, `transition: all`

**Fase 4 — Validação:** Swap · Squint · Signature (5 elementos) · Token tests → `critique-*` → `web-design-guidelines` (zero violações; `tabular-nums` obrigatório em dados) → estados loading/empty/error em todas as views.

---

## CONTEXTO 6 — TRÁFEGO PAGO (Meta Ads)

1. **Contexto:** ler `.agents/ads-context.md` e `.agents/paid-ads-onboarding.md` do cliente; ausentes → preencher a partir do template antes de qualquer campanha. Specs específicas do cliente quando existirem (ex: `clients/super-agente-ia/meta-ads-specs.md`, `creative-board.md`).
2. **Estratégia/oferta:** `sales-strategist` / `marketing-council-sms` quando o ângulo da oferta estiver em aberto.
3. **Criativos:** copy de anúncio via `post-writer-sms`/`hook-writer-sms` (+ `copy-qa-sms`); imagem via pipeline de imagem; vídeo via CONTEXTO 3.
4. **Execução e leitura:** conector Meta Ads (quando conectado) para contas, campanhas, públicos, insights. **Criar, ativar, alterar orçamento ou públicos exige confirmação explícita do usuário a cada ação.** Leitura de métricas é livre.
5. **Análise:** `performance-analyzer-sms` / `optimization-advisor-sms` com os dados da conta.

---

## INVENTÁRIO DE SKILLS

### Internas (versionadas neste repositório — fonte canônica)

**Orquestração e qualidade:** `production-orchestrator` (este arquivo, `SKILL.md` raiz) · `production-orchestrator-sms` · `copy-qa-sms` · `narrative-framework-sms`

**Contexto, pesquisa e estratégia** (`skills/social-media/`): `social-media-context-sms` · `audience-watering-hole-sms` · `niche-research-sms` · `content-matrix-sms` · `marketing-council-sms` · `content-strategy-sms` · `platform-strategy-sms` · `visual-platform-strategy-sms` · `content-calendar-sms` · `reference-analyzer-sms`

**Criação de copy** (`skills/social-media/`): `carousel-writer-sms` · `post-writer-sms` · `thread-writer-sms` · `article-writer-sms` · `newsletter-writer-sms` · `caption-writer-sms` · `hook-writer-sms` · `video-script-sms` · `content-repurposer-sms` · `illustration-writer-sms` · `x-article-publisher`

**Análise** (`skills/social-media/`): `performance-analyzer-sms` · `performance-loop-sms` · `content-pattern-analyzer-sms` · `audience-growth-tracker-sms` · `optimization-advisor-sms`

**Design e imagem** (`skills/design/`): `json-prompt-generator` · `cookbook-templates` · `card-news-generator-v2` · `landing-page-guide-v2` · `color-system` · `typography-scale` · `layout-grid` · `visual-hierarchy` · `competitive-analysis` · `critique-visual-hierarchy` · `critique-typography` · `critique-composition` · `critique-brand-consistency`

**Design de alto nível:** `huashu-design` (protótipos, decks, motion, Core Asset Protocol, Direction Advisor, 5D Critique) · `impeccable` (shape, craft, polish, audit, critique, harden, optimize, adapt, animate, colorize, typeset, layout, distill, delight, clarify…)

**Cliente-específica:** `intus-hub-twitter-slide` (pipeline GPT Image → composite do template twitter-post-style do Intus Hub)

### Externas (instalar à parte — ver README)
- `taste-skill` → `npx skills add leonxlnx/taste-skill@taste-skill`
- `web-design-guidelines` → `npx skills add vercel-labs/agent-skills@web-design-guidelines`
- `interface-design` → `npx skills add dammyjay93/interface-design@interface-design`
- Opcionais de processo, se instaladas: `step-by-step` (um componente por vez), `caca-as-bruxas` (debug por causa raiz), `memory` (continuidade entre sessões)

Skill citada mas não instalada → avisar em uma linha e aplicar o princípio descrito aqui, sem inventar o conteúdo dela.

### Escopo — o que cada uma NÃO faz
- `production-orchestrator` / `-sms`: não escrevem copy, não decidem framework, não analisam dados.
- `impeccable`: não substitui compliance granular nem critique 5D.
- `taste-skill`: não faz estrutura de conversão, copy nem a11y granular.
- `web-design-guidelines`: só compliance; não gera design nem copy.
- `huashu-design`: não faz compliance nem copy de LP.
- `interface-design`: não faz LP de marketing nem social media.
- `json-prompt-generator` / `cookbook-templates` / `illustration-writer-sms`: não escrevem copy nem geram a imagem; entregam prompt/JSON.
- `card-news-generator-v2`: não faz estratégia, copy nem legenda.

---

## GATES OBRIGATÓRIOS (consolidado)

| Gate | Quando | Condição → ação |
|---|---|---|
| 0 | Antes de qualquer contexto | Cliente ativo confirmado? `brand-spec.md` / `DESIGN.md` / contexto existem? → senão ONBOARDING ou Core Asset Protocol |
| CATÁLOGO | Onboarding, brand guide, novo sistema de criativos, novo template | Consultar índices de fontes/paletas → máx 3 combinações → aprovação. **Silencioso** em template já aprovado, geração de copy, atualização de runs ou fonte/paleta trazida pelo usuário |
| A | Toda copy | Formato → skill de criação da tabela |
| B | Ângulo em aberto | `narrative-framework-sms` (embutido ou via orquestrador) |
| 4.5 | Carrossel | 3 ângulos apresentados e 1 aprovado antes do script |
| C | Antes de entregar copy | `copy-qa-sms` executado |
| 4 | Antes de cards/visual | Script aprovado + brand-spec carregado |
| IMG | Imagem com referência | `json-prompt-generator` via `Skill` tool; peça final em JSON de zonas |
| TECH | Antes de código (C1, C5) | `tech-lock.md` aprovado; STOP em violação |
| 1 | C1 antes do Craft | Shape aprovado · paleta/tipo fechadas · nenhuma fonte rejeitada |
| 2 | C1 antes da validação | Todos os componentes entregues |
| 3 | C1 antes da entrega | 5D + critique granular + audit + web-design-guidelines executados |
| 5 | C5 antes da execução | Intent específico + 4 outputs de domínio |
| ADS | C6 | Toda criação/alteração em conta de anúncio confirmada pelo usuário |
| D | Fim de cada etapa aprovada | Artefatos salvos em `clients/[cliente]/runs/[data]/` |

---

## CRITÉRIOS DE PRONTO

**LP:** tech-lock seguido · zero `style=""` e zero mix de estilo/animação · 11 elementos · 5D e critiques sem pendência crítica · WCAG AA, performance, responsivo · web-design-guidelines zerado · nenhuma fonte rejeitada · meta tags + OG · CTA acima do fold e repetido.

**Carrossel:** framework oferecido · 3 ângulos e 1 aprovado · 9–12 slides (ou formato do cliente) com CERNE/SECUNDÁRIO · 5 capas + 3 legendas · `copy-qa-sms` aprovado · JSON de zonas da capa colado no chat · brand-spec aplicado nos cards · legenda final por plataforma.

**Artigo / post / thread / roteiro:** skill de criação correta · framework definido · `copy-qa-sms` aprovado · voz conferida contra `production-rules.md` · artefato salvo.

**Interface:** tech-lock seguido · intent específico · assinatura em 5 elementos · surface elevation · tokens semânticos · estados loading/empty/error · web-design-guidelines sem violação crítica.

---

## REGRAS DE OPERAÇÃO

### Autonomia e comunicação
- Detectar contexto e iniciar o fluxo sem exigir que o usuário nomeie etapas.
- Pausar só em decisões do usuário: cliente, direção visual, framework/ângulo, aprovação de copy, tech-lock, ações em conta de anúncio.
- Diagnóstico e roteamento são internos; mostrar só checkpoints de decisão, avisos de contexto ausente e entregas.
- Sempre indicar a fase em execução; máximo 2 perguntas por vez; fechar cada fase com próximos passos.

### Qualidade visual
- **Fontes rejeitadas** (salvo se já forem da marca do cliente no `brand-spec.md`): Inter, DM Sans, Playfair Display, Fraunces, Space Grotesk, Outfit, Plus Jakarta Sans, Instrument Sans, Instrument Serif, Cormorant, Lora, Syne.
- **Estéticas rejeitadas:** gradiente roxo/azul genérico, emoji como ilustração, glassmorphism sem propósito, layout de template, hero centrado sobre imagem escura, 3 cards iguais em linha, neon/glow externo, `#000000` puro, `h-screen`, `transition: all`.

### Salvamento de artefatos — `clients/[cliente]/runs/[AAAA-MM-DD]/`
Criar a pasta se não existir. Tema em kebab-case. A convenção do `CLAUDE.md` do cliente prevalece.

| Artefato | Arquivo |
|---|---|
| Ângulos propostos | `angulos-[tema].md` |
| Script de carrossel | `carrossel-[tema].md` |
| Variações de capa / legenda | `capas-[tema].md` · `legendas-[tema].md` |
| JSON de capa / estático / stories | `json-capas-[tema].md` · `json-estatico-[tema].md` · `json-stories-[tema].md` |
| JSON de lançamento | `json-lancamento-[tipo].md` · `json-lancamento-semana[N]-[tema].md` |
| Post / thread / artigo | `post-[tema].md` · `thread-[tema].md` · `artigo-[tema].md` |
| Roteiro de vídeo | `roteiro-[tema].md` |
| Briefing de LP | `lp-briefing-[tema].md` |
| Tech lock | `tech-lock.md` |
| Bugs relevantes | `bugs-[data].md` |

### Debug
Erro em execução de código → investigar causa raiz antes de corrigir (sintoma → 3 fontes → triangulação → fix → verificação; `caca-as-bruxas` se instalada). Proibido "tentei X e funcionou" sem entender o porquê. Registrar em `bugs-[data].md`.

### Memória entre sessões
Ao fim de fase aprovada ou a pedido ("salvar progresso", "preparar próxima sessão"): registrar em `clients/[nome]/memory/` (índice ≤200 linhas + `HISTORIC/`), via `memory` se instalada. Aprendizados de performance vão para o `social-media-context-sms.md` via `performance-loop-sms`.

### Manutenção do sistema
- Editar skills sempre dentro de `skills/` no repositório; `~/.claude/skills/` é só destino de instalação (`tools/check-skill-sync.ps1` verifica divergências).
- Antes de commit: nenhum `SKILL.md` virou stub e nenhum caminho absoluto de máquina (`grep -r "C:\\\\Users\\\\" skills/` vazio).
- Nova skill adicionada ao repo → registrar no INVENTÁRIO e na tabela de gates/rotas deste arquivo.
