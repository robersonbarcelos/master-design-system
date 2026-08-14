# PRD — Master Social Design System

**Versão:** 1.3.0
**Data:** 2026-07-27
**Repositório:** https://github.com/robersonbarcelos/master-design-system-v270726
**Tipo:** Sistema de orquestração de skills para produção de design e conteúdo no Claude Code

---

## 1. Visão geral

### 1.1 Problema

Profissionais de social media, criação de conteúdo e landing pages que trabalham com múltiplos clientes enfrentam:

- **Retrabalho de contexto**: configurar o perfil de cada cliente do zero a cada nova sessão
- **Atrito no fluxo**: lembrar qual skill chamar em qual momento, em qual ordem
- **Inconsistência**: dificuldade de manter voz e identidade visual coerentes entre peças do mesmo cliente
- **Desperdício de tokens**: carregar skills desnecessárias para o contexto em execução
- **Qualidade variável**: ausência de gates de validação estruturados que garantam entrega profissional

### 1.2 Solução

Um orquestrador de skills que:

1. **Detecta automaticamente** o contexto de trabalho (LP / social media / vídeo / lançamento / interface de produto) pela linguagem natural da mensagem
2. **Carrega o perfil do cliente** via arquivos de contexto persistentes — sem que o usuário precise re-explicar
3. **Conduz o fluxo completo de produção** acionando as skills certas na ordem certa
4. **Usa apenas as skills necessárias** para o contexto detectado
5. **Executa gates obrigatórios** e valida critérios de pronto antes de avançar entre fases

### 1.3 Princípio de operação

O sistema opera em **linguagem natural**. Você não invoca skills explicitamente — você descreve o que precisa produzir. O orquestrador é o único ponto de entrada; ele resolve internamente qual skill acionar, em qual fase, com qual contexto.

---

## 2. Perfil do usuário

**Perfil principal:** Social media manager / criador de conteúdo / infoprodutor solo ou em agência pequena

**Contexto de trabalho:**
- Múltiplos clientes ativos (até ~10 simultaneamente)
- Produz: landing pages, carrosseis, posts, stories, roteiros, campanhas de lançamento
- Ambiente principal: Claude Code

**O que o usuário NÃO quer fazer:**
- Especificar qual skill chamar a cada tarefa
- Re-explicar o cliente a cada sessão
- Montar fluxos manualmente
- Validar qualidade peça por peça sem critério estruturado

---

## 3. Arquitetura do sistema

### 3.1 Estrutura de arquivos

```
master-social-design-system/
│
├── SKILL.md                    ← ORQUESTRADOR MESTRE
│                                 Contém: detecção de contexto, fluxos dos 5 contextos,
│                                 mapa de orquestração, gates, critérios de pronto,
│                                 regras de qualidade, salvamento de artefatos
│
├── skills/
│   ├── video-script-sms/       ← Skill incluída: roteiros de vídeo
│   ├── social-media/           ← 14 social media skills
│   ├── design/                 ← Skills de design (visual critique, ui-design, ux-strategy)
│   │   ├── card-news-generator-v2/
│   │   ├── json-prompt-generator/
│   │   ├── landing-page-guide-v2/
│   │   ├── ui-design/          ← color-system, layout-grid, typography-scale, visual-hierarchy
│   │   ├── ux-strategy/        ← competitive-analysis
│   │   └── visual-critique/    ← critique-brand, critique-composition, critique-typography, critique-visual-hierarchy
│   ├── huashu-design/          ← huashu-design completo
│   └── impeccable/             ← impeccable completo
│
├── workflows/                  ← Documentação dos fluxos por contexto
│   ├── 01-landing-page.md
│   ├── 02-social-media.md
│   ├── 03-video-script.md
│   ├── 04-launch-campaign.md
│   └── 05-interface-design.md
│
├── reference/
│   └── design-md-guide.md      ← Como selecionar DESIGN.md por tipo de projeto
│
└── clients/
    └── _template/              ← Template de onboarding (único versionado)
        ├── .agents/
        │   ├── social-media-context-sms.md
        │   ├── paid-ads-onboarding.md
        │   └── ads-context.md
        ├── CLAUDE.md
        ├── DESIGN.md
        ├── brand-spec.md
        ├── content-system.md
        ├── production-rules.md
        ├── visual-system.md
        └── references/
            ├── copies-aprovadas.md
            ├── dados-ancora.md
            └── temas.md
```

### 3.2 Skills integradas — tabela completa

#### Skills deste repositório

| Skill | Arquivo | Versão | Função |
|---|---|---|---|
| production-orchestrator | `SKILL.md` | 1.1.0 | Orquestrador mestre |
| video-script-sms | `skills/video-script-sms/SKILL.md` | 1.0.0 | Roteiros de vídeo falados |

#### Social Media Skills (blacktwist/social-media-skills)

| Skill | Versão | Acionado em |
|---|---|---|
| social-media-context-sms | 1.0.0 | Setup + todos os contextos |
| content-strategy-sms | 1.0.0 | Contextos 2 e 4 |
| content-calendar-sms | 1.0.0 | Contextos 2 e 4 |
| platform-strategy-sms | 1.0.0 | Contextos 2 e 4 |
| hook-writer-sms | 1.1.0 | Contextos 2, 3 e 4 |
| carousel-writer-sms | 1.1.0 | Contextos 2 e 4 |
| caption-writer-sms | 1.1.0 | Contextos 2, 3 e 4 |
| post-writer-sms | 1.2.0 | Contextos 2 e 4 |
| thread-writer-sms | 1.3.0 | Contextos 2 e 4 |
| content-repurposer-sms | 1.1.0 | Todos os contextos |
| performance-analyzer-sms | 1.0.0 | Contextos 2 e 4 (análise) |
| audience-growth-tracker-sms | 1.0.0 | Contextos 2 e 4 (análise) |
| content-pattern-analyzer-sms | 1.0.0 | Contextos 2 e 4 (análise) |
| optimization-advisor-sms | 1.0.0 | Contextos 2 e 4 (análise) |

#### My-skills

| Skill | Acionado em |
|---|---|
| landing-page-guide-v2 | Contexto 1 (alternativa ao impeccable) |
| card-news-generator-v2 | Contexto 2 — visuais de carrossel |
| json-prompt-generator | Contextos 2 e 4 — JSON estruturado de imagem |

#### Designer-skills (Owl-Listener — 3 plugins)

| Plugin / Skill | Acionado em |
|---|---|
| visual-critique: critique-brand-consistency | Contextos 1 e 2 |
| visual-critique: critique-composition | Contextos 1 e 2 |
| visual-critique: critique-typography | Contextos 1 e 2 |
| visual-critique: critique-visual-hierarchy | Contextos 1 e 2 |
| ui-design: color-palette | Contextos 1 e 4 |
| ui-design: type-system | Contextos 1 e 4 |
| ui-design: visual-hierarchy | Contextos 1 e 2 |
| ui-design: layout-grid | Contexto 1 |
| ux-strategy: competitive-analysis | Contextos 1 e 4 |

#### huashu-design (alchaincyf)

| Capacidade | Acionado em |
|---|---|
| Core Asset Protocol | Setup de cliente, Contextos 1 e 4 |
| Design Direction Advisor | Contextos 1, 4 e 5 |
| 5-dimension critique | Contextos 1 e 4 (validação) |
| Motion design MP4/GIF | Contextos 2, 3 e 4 |
| Slide deck HTML + PPTX | Contexto 4 |
| Interactive prototype | Contextos 1 e 4 |
| Infographic | Contextos 2 e 4 |

#### impeccable (impeccable-io)

| Capacidade | Fase | Acionado em |
|---|---|---|
| Shape | Fase 2 início | Contexto 1 |
| Craft | Fase 2 meio | Contexto 1 |
| Polish | Fase 2 fim | Contexto 1 |
| Audit | Fase 3 | Contextos 1 e 4 |
| Brand | Contexto 1 | Fundação |

#### taste-skill (leonxlnx)

| Capacidade | Acionado em |
|---|---|
| Execução React/Tailwind anti-slop | Contextos 1 (Fase 2 Craft) e 5 (Fase 3) |
| Creative Arsenal: Bento, Masonry, Curtain, Parallax | Contexto 1 |
| Framer Motion spring physics | Contextos 1 e 5 |
| Dials DESIGN_VARIANCE / MOTION_INTENSITY / VISUAL_DENSITY | Contextos 1 e 5 |

#### web-design-guidelines (vercel-labs)

| Capacidade | Acionado em |
|---|---|
| Compliance técnico granular (14 categorias) | Contextos 1 (Fase 3) e 5 (Fase 4) |
| focus-visible, aria-label, autocomplete | LP + Interface |
| prefers-reduced-motion, touch-action | LP + Interface |
| tabular-nums, overscroll-behavior, hydration | LP + Interface |
| Output: lista de violações file:line | LP + Interface |

#### interface-design (dammyjay93)

| Capacidade | Acionado em |
|---|---|
| Intent First methodology | Contexto 5, Fase 1 |
| Domain Exploration | Contexto 5, Fase 2 |
| Craft Foundations (surface elevation, borders, tokens) | Contexto 5, Fase 3 |
| Swap / Squint / Signature / Token Tests | Contexto 5, Fase 4 |
| Infinite Expression mandate | Contexto 5 |

---

## 4. Sistema de contexto de cliente

### 4.1 Arquivos de contexto

| Arquivo | Conteúdo | Lido por |
|---|---|---|
| `.agents/social-media-context-sms.md` | Nicho, público, voz, pilares, plataformas, restrições | Todas as social-media-skills |
| `.agents/paid-ads-onboarding.md` | Estratégia de anúncios pagos | Skills de ads |
| `.agents/ads-context.md` | Contexto de campanhas pagas | Skills de ads |
| `brand-spec.md` | Logo, cores hex, tipografia, assets | huashu-design |
| `DESIGN.md` | Referência visual do projeto | impeccable, landing-page-guide-v2 |
| `visual-system.md` | Sistema visual para geração de imagens | json-prompt-generator |
| `content-system.md` | Regras de copy específicas do cliente | carousel-writer, post-writer |
| `production-rules.md` | Regras de produção do cliente | Orquestrador |
| `references/copies-aprovadas.md` | Copies aprovados anteriores | hook-writer, carousel-writer |
| `references/dados-ancora.md` | Dados, números e fatos do nicho | Produção de conteúdo |
| `references/temas.md` | Banco de temas e pautas | content-calendar-sms |

### 4.2 Ciclo de vida do contexto

1. **Criação (uma vez):** onboarding estruturado de 30-40 min por cliente
2. **Uso recorrente:** todas as skills leem automaticamente a cada sessão
3. **Atualização:** re-execução parcial de `social-media-context-sms` quando necessário
4. **Garantia:** o usuário nunca re-explica o cliente em sessões subsequentes

### 4.3 Onboarding de novo cliente

O orquestrador detecta ausência de contexto e executa automaticamente:

**Etapa A — Contexto de social media**
Coleta sequencial (uma pergunta por vez):
1. Nome, nicho e produto/serviço principal
2. Público-alvo: quem é, dor principal, desejo
3. Voz e tom: 3-5 adjetivos
4. Pilares de conteúdo: 3-5 temas fixos
5. Plataformas ativas e frequência
6. O que a marca NUNCA deve dizer ou parecer
7. Exemplo de post referência (opcional)

Salva em `.agents/social-media-context-sms.md`.

**Etapa B — Marca visual**
1. Logo (arquivo ou URL)
2. Cores da marca (hex ou referência)
3. Fontes
4. Screenshots do produto/serviço
5. Material de referência visual

Se não tiver → aplica Design Direction Advisor (3 direções para escolher).

Salva em `brand-spec.md`.

**Etapa C — Referência visual**
Seleciona 1 `DESIGN.md` do guia `reference/design-md-guide.md` com base no posicionamento do cliente.

---

## 5. Fluxo completo de detecção e orquestração

### 5.1 Detecção de contexto

```
Mensagem do usuário
       ↓
Extração de palavras-chave
       ↓
┌─────────────────────────────────────────────────────────┐
│ "landing page, LP, página de vendas, site"              │ → CONTEXTO 1
│ "carrossel, post, Instagram, TikTok, feed, legenda"     │ → CONTEXTO 2
│ "roteiro, reel, vídeo, script, shorts, YouTube"         │ → CONTEXTO 3
│ "lançamento, campanha, infoproduto, carrinho"           │ → CONTEXTO 4
│ "dashboard, SaaS, área de membros, ferramenta, portal"  │ → CONTEXTO 5
└─────────────────────────────────────────────────────────┘
       ↓
Ambíguo? → pergunta em uma linha
       ↓
Verifica .agents/social-media-context-sms.md
       ↓
Verifica brand-spec.md e DESIGN.md
       ↓
GATE 0 → Executa contexto detectado
```

### 5.2 CONTEXTO 1 — Landing Page

```
GATE 0: brand-spec.md + DESIGN.md existem?
  └── NÃO → Core Asset Protocol + Direction Advisor (huashu) → STOP até concluir

FASE 1 — FUNDAÇÃO
├── huashu: Core Asset Protocol
│     Input: logo, cores, fontes, screenshots, referências
│     Output: brand-spec.md completo
├── huashu: Direction Advisor (se cliente sem identidade definida)
│     Output: 3 direções visuais com demos → usuário escolhe 1
├── designer-skills: color-palette
│     Output: paleta principal + verificação de contraste AA
└── Benchmark: análise de 3 concorrentes
      Output: oportunidade de diferenciação identificada

GATE 1: Shape aprovado? Paleta fechada? Nenhuma fonte rejeitada?

FASE 2 — CONSTRUÇÃO
├── impeccable: Shape
│     Input: brand-spec.md + DESIGN.md + benchmark + paleta
│     Output: estrutura HTML comentada + copy por seção + 11 elementos definidos
│     Gate interno: Shape aprovado pelo usuário antes de codar
├── taste-skill + impeccable: Craft (simultâneos)
│     taste-skill recebe: estrutura do Shape + copy + paleta + tipografia
│     taste-skill entrega: componentes React/Tailwind com:
│       - DESIGN_VARIANCE: 8 (assimétrico, sem 3 cards iguais)
│       - MOTION_INTENSITY: 6 (Framer Motion spring physics em CTAs)
│       - VISUAL_DENSITY: 4 (espaçamento generoso)
│       - Creative Arsenal para seções com POV único
│     impeccable Craft: qualidade de agência, copy final
└── impeccable: Polish
      Output: animações scroll-triggered + microinterações + meta tags + OG image

GATE 2: Todos os componentes React entregues?

FASE 3 — VALIDAÇÃO
├── huashu: 5-dimension critique
│     Dimensões: coerência filosófica, hierarquia visual, execução técnica,
│                funcionalidade, inovação
│     Output: radar + lista de ajustes visuais priorizados
├── impeccable: audit
│     Verifica: WCAG AA, performance (LCP < 2.5s), responsivo, anti-patterns de IA
│     Output: lista de fixes por prioridade
└── web-design-guidelines: compliance técnico
      14 categorias verificadas:
      focus-visible | aria-label | autocomplete | prefers-reduced-motion
      touch-action | overscroll-behavior | tabular-nums | min-w-0
      dimensões de imagem | hydration safety | translate="no" | i18n
      Output: lista de violações no formato file:line → todas devem ser resolvidas

GATE 3: 5D Critique + Audit + web-design-guidelines executados e sem violações críticas?

ENTREGA FINAL: LP publicável + checklist completo
```

### 5.3 CONTEXTO 2 — Social Media

```
FASE 1 — ESTRATÉGIA (executar uma vez por cliente)
├── content-strategy-sms → pilares, posicionamento, voz consistente
└── platform-strategy-sms → o que vai em cada plataforma e com qual abordagem

FASE 2 — PRODUÇÃO DE CARROSSEL

  ETAPA 1 — PRÉ-PRODUÇÃO: 3 ÂNGULOS
    Cada ângulo entrega:
    - Nome do ângulo (Provocação, Educativo Direto, Contrarian, Dado Chocante, Storytelling)
    - Gancho de capa (1-2 linhas impactantes)
    - Linha narrativa (o que o carrossel vai contar)

  [GATE 4.5] Ângulo aprovado? (1, 2 ou 3)

  ETAPA 2 — PRODUÇÃO DO SCRIPT
    hook-writer-sms:
      Input: ângulo escolhido + gancho de capa aprovado
      Output: variações aprofundadas do gancho
    carousel-writer-sms:
      Input: hook aprofundado + ângulo + linha narrativa
      Output: script 9-12 slides estruturado
        - Slides CERNE: 100% do slide, max 8 linhas, até 4 bullets com descrição
        - Slides SECUNDÁRIOS: max 4 linhas, sem indicar [espaço para imagem]
        Estrutura: CAPA → GANCHO → CONTEXTO → ANÁLISE → IMPLICAÇÕES → AÇÃO → CTA

  ETAPA 3 — AUTO-GERAÇÃO (imediata, sem solicitar)
    5 variações de capa:
      V1: Dado chocante / número impactante em destaque
      V2: Contraste visual / dois mundos opostos
      V3: Personagem / storytelling humano
      V4: Minimalista / tipografia forte dominante
      V5: Metáfora visual / conceitual
    3 variações de legenda:
      L1: Storytelling (narrativa que acompanha a jornada)
      L2: Provocação/Dado (abre com número ou fato chocante)
      L3: Educativa/Direta (explica o valor objetivamente)
    Formato de cada legenda: 150-300 palavras + CTA final
    Restrição: legenda complementa (não repete) os slides

  ETAPA 4 — JSON DE IMAGEM
    json-prompt-generator:
      Input: capa escolhida (V1-V5) + visual-system.md + brand-spec.md
      Output: JSON completo {
        scene, style, technical (camera/aperture/depth),
        materials, composition, quality: {include, avoid}
      }
      Salvo em: json-capas-[tema].md

  [GATE 4] Script aprovado + brand-spec.md carregado?

  ETAPA 5 — CARDS E DISTRIBUIÇÃO
    card-news-generator-v2:
      Input: script aprovado + JSON de capa + brand-spec.md
      Output: cards visuais com identidade do cliente
    caption-writer-sms:
      Input: cards prontos + copy dos slides
      Output: legenda final otimizada por plataforma

FASE 3 — CALENDÁRIO (se solicitado planejamento mensal)
└── content-calendar-sms → cronograma com cadência, temas e datas

FASE 4 — ANÁLISE (quando tiver dados de performance)
├── performance-analyzer-sms → interpreta métricas, gera insights
├── content-pattern-analyzer-sms → identifica padrões de performance
├── optimization-advisor-sms → recomendações específicas de melhoria
└── audience-growth-tracker-sms → tendência de crescimento
```

### 5.3.1 Gates Obrigatórios embutidos na skill orquestradora (production-orchestrator-sms v1.1.0)

Desde 2026-07-27, o gate de skill de criação definido no `CLAUDE.md` raiz (seção "Gate de Skill de Criação") também está **embutido diretamente** em `skills/social-media/production-orchestrator-sms/SKILL.md`, para que valha em toda produção — carrossel, artigo, post, thread, hook, roteiro de vídeo — sem depender de releitura externa do `CLAUDE.md`.

| Gate | Verificação | Ação se falhar |
|---|---|---|
| GATE A | Formato do pedido tem skill de criação correspondente na tabela? (carrossel → carousel-writer-sms, artigo → article-writer-sms, post → post-writer-sms, thread → thread-writer-sms, legenda → caption-writer-sms, hook → hook-writer-sms, roteiro → video-script-sms, ilustração → illustration-writer-sms, repurpose → content-repurposer-sms, publicação de artigo → x-article-publisher) | STOP: pergunta ao usuário qual skill usar; nunca escreve copy "por fora" de uma skill |
| GATE B | Ângulo/framework narrativo já definido pelo usuário? | NÃO → aciona `narrative-framework-sms` antes de prosseguir, independente do formato |
| GATE C | `copy-qa-sms` (Voice Gate + AI Pattern Gate + padrões estruturais) executado antes da entrega? | STOP: orquestrador aciona `copy-qa-sms` manualmente antes de entregar, mesmo que a skill de criação tenha falhado em embuti-lo |
| GATE D | Artefato final salvo em `clients/[cliente]/runs/[data]/`? | Empacotamento final — não substitui os gates A, B e C |

**Exceção única (válida para os 4 gates):** o usuário pede explicitamente um rascunho sem passar pela skill/framework/QA — nesse caso o orquestrador sinaliza de forma visível: `[⚠️ COPY SEM GATE — não passou por narrative-framework-sms e/ou copy-qa-sms]`.

**Por que embutido na skill (e não só no CLAUDE.md):** em 2026-07-21 um carrossel foi produzido escrevendo ângulos manualmente, pulando o gate de framework narrativo e o QA. O `CLAUDE.md` descreve a regra em nível de sistema; esta seção a torna operacional dentro do próprio fluxo de roteamento, garantindo que ela dispare mesmo se o `CLAUDE.md` não for relido na sessão.

### 5.4 CONTEXTO 3 — Roteiro de Vídeo

```
FASE 1 — BRIEFING (5 perguntas, sequencial)
  1. Plataforma e formato (Reel 15s/30s/60s, TikTok, YouTube Shorts, YouTube longo)
  2. Objetivo (educativo, venda, autoridade, entretenimento, bastidor)
  3. Tema e mensagem central
  4. Estilo (talking head, animado, narração off, misto)
  5. CTA desejado ao final

FASE 2 — ROTEIRO (via video-script-sms)
  Input: briefing completo
  Output estruturado:
  - Hook dos primeiros 3 segundos (obrigatório parar scroll)
  - Roteiro cena a cena:
      [CENA N] Duração: Xs
      Fala: "..."
      Visual: (o que a câmera mostra)
      B-roll: (se aplicável)
      Corte: (tipo de transição)
  - CTA final com texto exato
  - Caption otimizada para a plataforma alvo

FASE 3 — PRODUÇÃO VISUAL (se animado ou motion)
└── huashu-design: motion design MP4/GIF + BGM

  Se talking head → entrega o script para gravação manual

FASE 4 — DISTRIBUIÇÃO
├── caption-writer-sms → legenda + hashtags por plataforma
└── content-repurposer-sms → adapta para outros formatos e plataformas
```

### 5.5 CONTEXTO 4 — Lançamento de Infoproduto

```
FASE 1 — BASE DA CAMPANHA
├── huashu: Core Asset Protocol → assets do produto
├── huashu: Direction Advisor → direção visual de toda a campanha
├── Fecha paleta e tipografia da campanha
├── content-strategy-sms → pilares (educação→autoridade→desejo→prova→urgência)
├── content-calendar-sms → cronograma pré/lançamento/pós-lançamento
└── Benchmark de 3 lançamentos similares no mercado

FASE 2 — LANDING PAGE DE VENDAS
└── Executa CONTEXTO 1 completo com foco em:
    - Copy orientado à transformação (não ao produto)
    - Prova social desde o wireframe (sem placeholder)
    - Urgência real (data de fechamento ou bônus limitado)
    - Garantia proeminente
    - Critique 5D obrigatório antes de publicar

FASE 3 — CONTEÚDO DE AQUECIMENTO (por semana)
  Para cada semana de pré-lançamento:
    Semana 1 — Educação e problema:
      - 2-3 carrosseis educativos sobre a dor
      - 1-2 posts de autoridade
    Semana 2 — Autoridade e método:
      - 2 carrosseis de método/solução
      - 1 thread de bastidor/processo
    Semana 3 — Desejo e prova:
      - Depoimentos formatados
      - Carrossel de transformações/resultados
      - Post de antecipação
  Para cada peça:
    hook-writer → carousel-writer → json-prompt-generator → card-news → caption → repurpose
  Artefatos: json-lancamento-semana[N]-[tema].md

FASE 4 — PRODUÇÃO DO LANÇAMENTO
├── Assets de alto impacto (huashu):
│   - Animação de abertura de carrinho (MP4 + BGM)
│   - Deck de vendas para live (HTML + PPTX editável)
│   - Protótipo clicável da área de membros (device frame)
├── Copy de lançamento:
│   - hook-writer → hooks de abertura de carrinho
│   - post-writer → posts de urgência, depoimento, last call
│   - thread-writer → thread de lançamento
│   - caption-writer → legendas de cada peça
│   - json-prompt-generator → JSON de imagem por post estático
│     Artefatos: json-lancamento-urgencia.md, json-lancamento-lastcall.md
└── Roteiros de vídeo → CONTEXTO 3 para cada vídeo da campanha

FASE 5 — ANÁLISE PÓS-LANÇAMENTO
├── performance-analyzer-sms → o que converteu mais
├── content-pattern-analyzer-sms → padrões de conteúdo que performaram
├── audience-growth-tracker-sms → crescimento durante a campanha
└── optimization-advisor-sms → o que replicar no próximo lançamento
```

### 5.6 CONTEXTO 5 — Interface Design

```
FASE 1 — INTENT FIRST (via interface-design)
  Responder com especificidade antes de qualquer wireframe:
  1. Quem é esse usuário?
     Não: "usuários em geral"
     Sim: "gestora financeira que abre o painel às 9h depois de checar email"
  2. O que ele precisa fazer?
     Não: "ver dados"
     Sim: "aprovar pagamento em menos de 3 cliques"
  3. Como isso deve parecer?
     Não: "limpo e moderno"
     Sim: "frio como terminal de trading, sem distrações"

[GATE 5] Intent respondido com especificidade? → NÃO: volta à Fase 1

FASE 2 — DOMAIN EXPLORATION (via interface-design)
  4 outputs obrigatórios antes de qualquer componente:
  ├── Domínio: conceitos, metáforas e vocabulário do mundo do produto (mínimo 5)
  ├── Mundo de cores: cores do domínio físico (mínimo 5 — não "quente/frio", vá ao mundo real)
  ├── Assinatura: elemento visual/estrutural/de interação que só existe para ESTE produto
  └── Defaults a evitar: 3 escolhas óbvias (visual + estrutural) para esse tipo de interface

  Teste obrigatório: leia a proposta sem o nome do produto.
  Alguém identificaria para que serve? → NÃO: explore mais fundo

FASE 3 — EXECUÇÃO (via taste-skill + interface-design)
  Stack: React / Next.js + Tailwind CSS + Framer Motion
  Dials:
    - DESIGN_VARIANCE: 6 (offset, estruturado mas não genérico)
    - MOTION_INTENSITY: 4 (transições funcionais, sem cinema)
    - VISUAL_DENSITY: 7-9 (dashboards densos) ou 3-5 (apps simples)
  Craft foundations obrigatórias:
    - Surface Elevation: camadas com mínima diferença de lightness
      inputs levemente mais escuros (receptores de conteúdo)
      sidebar mesma cor do canvas + borda sutil
      dropdowns um nível acima da superfície pai
    - Borders: rgba de baixa opacidade (não hex sólido)
      Sistema de 4 níveis: padrão → suave → ênfase → focus ring
    - Token names semânticos do domínio do produto:
      --vault-surface, --terminal-ink, --flow-muted
      NUNCA: --gray-700, --primary, --bg-light
    - Infinite Expression: se você pode trocar sua escolha pela padrão sem diferença → refaça
  AI Tells proibidos:
    - Sidebar diferente do canvas (fragmenta o espaço visual)
    - 3 metric boxes com ícone-esquerda + número-grande + label-pequeno em sequência
    - Inter font
    - #000000 puro (use Zinc-950 ou off-black)
    - transition: all

FASE 4 — VALIDAÇÃO (via interface-design + web-design-guidelines)
  Swap Test: troque seus choices pelos mais comuns → ficou diferente? → NÃO: refaça
  Squint Test: desfoque os olhos → hierarquia legível? Sem linhas duras?
  Signature Test: aponte 5 elementos onde a assinatura do produto aparece
  Token Test: leia os CSS variables em voz alta → soam como este produto?
  web-design-guidelines: zero violações em focus-visible, aria-label,
    touch-action, prefers-reduced-motion, autocomplete, tabular-nums (obrigatório em dados)
```

---

## 6. Mapa de orquestração

### 6.1 Tabela mestra de ativação

| Skill | Contexto | Fase | Trigger de ativação |
|---|---|---|---|
| `huashu` (Core Asset Protocol) | 1, 2, 4, 5 | Fundação | brand-spec.md ausente ou incompleto |
| `huashu` (Direction Advisor) | 1, 4, 5 | Fundação | cliente sem identidade visual definida |
| `huashu` (5D Critique) | 1, 4 | Validação | toda LP antes de publicar |
| `huashu` (motion/infográfico) | 2, 3, 4 | Produção | post rico, asset animado, MP4/BGM |
| `impeccable` (Shape) | 1 | Fase 2 início | após Foundation, antes de codar |
| `impeccable` (Craft) | 1 | Fase 2 meio | após Shape aprovado |
| `impeccable` (Polish) | 1 | Fase 2 fim | componentes prontos |
| `impeccable` (Audit) | 1, 4 | Fase 3 | LP completa |
| `taste-skill` | 1 | Fase 2 Craft | simultâneo com impeccable Craft |
| `taste-skill` | 5 | Fase 3 | execução de código de produto |
| `web-design-guidelines` | 1, 5 | Fase 3 Audit | após código pronto |
| `interface-design` | 5 | Todas as fases | qualquer interface de produto |
| `json-prompt-generator` | 2, 4 | Fase 2 Produção visual | após direção visual definida |
| `card-news-generator-v2` | 2 | Fase 2 Carrossel | após JSON de capa gerado |
| `visual-critique` | 1, 2 | Validação | revisão visual antes de entregar |
| `landing-page-guide-v2` | 1 | Fase 1 | benchmark de estrutura (prazo curto) |

### 6.2 Escopos por skill — o que FAZ e NÃO FAZ

**`impeccable`**
- FAZ: arquitetura de LP (Shape), construção com qualidade (Craft), refinamento (Polish), audit anti-patterns e responsivo
- NÃO FAZ: execução React com Framer Motion, compliance técnico granular, critique visual 5D

**`taste-skill`**
- FAZ: execução React/Tailwind anti-slop, Creative Arsenal (Bento, Masonry, Curtain, Parallax, Glassmorphism), Framer Motion physics, dials de variance/motion/density
- NÃO FAZ: estrutura de conversão da LP, copy, critique visual, compliance a11y granular

**`web-design-guidelines`**
- FAZ: compliance técnico granular (14 categorias): focus-visible, aria, touch-action, prefers-reduced-motion, autocomplete, tabular-nums, hydration safety, i18n
- NÃO FAZ: design visual, copy, estrutura de conversão, critique, geração de componente

**`huashu-design`**
- FAZ: Core Asset Protocol (extração de marca), Direction Advisor (3 direções), 5D Critique, motion design MP4/GIF, infográfico print-quality
- NÃO FAZ: geração de código React, compliance técnico, copy de LP

**`interface-design`**
- FAZ: design de produto (dashboards, admin panels, SaaS, ferramentas), intent-first, domain exploration, signature visual, craft foundations
- NÃO FAZ: landing pages de marketing, posts de social media

**`json-prompt-generator`**
- FAZ: gera JSON estruturado de imagem por peça (scene / style / technical / materials / composition / quality include+avoid)
- Recebe: direção visual + visual-system.md + brand-spec.md
- Alimenta: Freepik, Midjourney ou qualquer gerador de imagem
- NÃO FAZ: escreve copy, cria cards, publica, gera a imagem diretamente

**`card-news-generator-v2`**
- FAZ: geração de cards visuais para carrossel com brand-spec aplicado
- Recebe: script aprovado + JSON de capa
- NÃO FAZ: estratégia, copy, legenda, análise de performance

### 6.3 Handoffs por contexto

**CONTEXTO 1 — Landing Page**

| De | Para | O que passa no handoff |
|---|---|---|
| Fase 1 Foundation | impeccable Shape | brand-spec.md + DESIGN.md + benchmark + paleta fechada |
| impeccable Shape | taste-skill Craft | Estrutura HTML comentada + copy por seção + paleta + tipografia |
| taste-skill Craft | impeccable Polish | Componentes React prontos + lista de animações pendentes |
| impeccable Polish | Fase 3 Validação | LP completa + checklist de polish aplicado |
| huashu 5D Critique | impeccable Audit | Lista de ajustes visuais priorizados |
| impeccable Audit | web-design-guidelines | Código após fixes visuais |
| web-design-guidelines | Entrega final | Lista de violações técnicas resolvidas + LP aprovada |

**CONTEXTO 2 — Social Media**

| De | Para | O que passa no handoff |
|---|---|---|
| content-strategy-sms | Pré-produção (3 ângulos) | Pilares + voz + tema da peça |
| Pré-produção (3 ângulos) | hook-writer-sms | Ângulo escolhido + gancho de capa aprovado |
| hook-writer-sms | carousel-writer-sms | Hook aprofundado + ângulo + linha narrativa |
| carousel-writer-sms | Auto-geração | Script completo CERNE/SECUNDÁRIO + brand-spec |
| Auto-geração | json-prompt-generator | Capa escolhida (V1–V5) + visual-system.md + brand-spec.md |
| json-prompt-generator | card-news-generator-v2 | JSON completo da capa + script aprovado + brand-spec.md |
| card-news-generator-v2 | caption-writer-sms | Cards visuais prontos + copy dos slides |

**CONTEXTO 5 — Interface Design**

| De | Para | O que passa no handoff |
|---|---|---|
| Fase 1 Intent First | Fase 2 Domain Exploration | 3 respostas de intent + contexto do usuário real |
| Domain Exploration | taste-skill Execução | Domínio + mundo de cores + assinatura + defaults a evitar |
| taste-skill Execução | Fase 4 Validação | Código completo + token names definidos |
| Validação (4 testes) | web-design-guidelines | Código após ajustes visuais |

---

## 7. Gates obrigatórios — especificação completa

### GATE 0 — Entrada de qualquer contexto

| Verificação | Ação se falhar |
|---|---|
| `brand-spec.md` existe? | STOP: execute Core Asset Protocol (huashu) |
| `DESIGN.md` existe? | STOP: execute Design Direction Advisor |
| Perfil de cliente existe? | Execute Onboarding antes de continuar |

### GATE 1 — CONTEXTO 1, antes da Fase 2 Craft

| Verificação | Ação se falhar |
|---|---|
| Shape aprovado pelo usuário? | STOP: não gera código sem aprovação da arquitetura |
| Paleta e tipografia fechadas no brand-spec? | STOP: define antes de codar |
| Alguma fonte da lista rejeitada presente? | STOP: substitua antes de continuar |

### GATE 2 — CONTEXTO 1, antes da Fase 3 Validação

| Verificação | Ação se falhar |
|---|---|
| Todos os componentes React entregues? | STOP: complete a execução antes de auditar |

### GATE 3 — CONTEXTO 1, antes da Entrega Final

| Verificação | Ação se falhar |
|---|---|
| Critique 5D executado (huashu)? | STOP |
| Audit impeccable executado? | STOP |
| web-design-guidelines executado? | STOP |

### GATE 4 — CONTEXTO 2, antes de gerar cards

| Verificação | Ação se falhar |
|---|---|
| Script aprovado pelo usuário? | STOP: não gera visual sem script aprovado |
| brand-spec.md carregado? | STOP |

### GATE 4.5 — CONTEXTO 2, antes do script de carrossel

| Verificação | Ação se falhar |
|---|---|
| 3 ângulos foram apresentados? | STOP: gere os ângulos primeiro |
| Ângulo aprovado pelo usuário? | STOP: não inicia script sem aprovação |

### GATE 5 — CONTEXTO 5, antes da Fase 3 Execução

| Verificação | Ação se falhar |
|---|---|
| Intent respondido com especificidade? | STOP: volta à Fase 1 |
| Domain Exploration com 4 outputs? | STOP: não executa sem domínio explorado |

---

## 8. Critérios de pronto por entregável

### LP completa (CONTEXTO 1)
- [ ] 11 elementos obrigatórios presentes
- [ ] Critique 5D sem pendências críticas
- [ ] Audit impeccable: WCAG AA, performance, responsivo, zero anti-patterns de IA
- [ ] web-design-guidelines: zero violações em focus-visible, touch-action, prefers-reduced-motion, autocomplete
- [ ] Nenhuma fonte rejeitada
- [ ] Meta tags e OG image gerados
- [ ] CTAs acima do fold e repetidos
- [ ] LCP < 2.5s

### Carrossel Social Media (CONTEXTO 2)
- [ ] 3 ângulos propostos e 1 aprovado antes de qualquer slide (GATE 4.5)
- [ ] Script 9-12 slides com tipologia CERNE vs SECUNDÁRIO aplicada
- [ ] Slides CERNE: 100% do espaço, dados quantificados, máx 8 linhas
- [ ] Slides SECUNDÁRIOS: máx 4 linhas, sem `[espaço para imagem]` no copy
- [ ] 5 variações de capa geradas automaticamente
- [ ] 3 variações de legenda geradas automaticamente (Storytelling / Provocação / Educativa)
- [ ] JSON de imagem gerado via json-prompt-generator para a capa escolhida
- [ ] brand-spec.md aplicado nos cards
- [ ] Caption final otimizada por plataforma
- [ ] Legenda revisada contra voz do cliente no brand-spec

### Interface de Produto (CONTEXTO 5)
- [ ] Intent respondido com especificidade (quem, o quê, como sente)
- [ ] Assinatura identificável em 5 elementos concretos
- [ ] Surface elevation system implementado
- [ ] Zero fonts rejeitadas
- [ ] Token names semânticos do domínio do produto
- [ ] Estados loading, empty e error em todas as views
- [ ] web-design-guidelines sem violações críticas

---

## 9. Regras de qualidade globais

### Fontes rejeitadas (todos os contextos)
Inter, DM Sans, Playfair Display, Fraunces, Space Grotesk, Outfit, Plus Jakarta Sans, Instrument Sans, Instrument Serif, Cormorant, Lora, Syne

### Estéticas rejeitadas
Gradiente roxo/azul genérico, ícones emoji como ilustração, glassmorphism sem propósito, layout de template, hero centrado com texto sobre imagem escura, 3 cards iguais em linha horizontal

### AI Tells proibidos
- Sem neon/glow externo
- Sem `#000000` puro (use Zinc-950 ou equivalente)
- Sem `h-screen` (use `min-h-[100dvh]`)
- Sem `transition: all`
- Sem layout de template reconhecível

### Salvamento automático de artefatos

| Artefato | Quando salvar | Arquivo |
|---|---|---|
| 3 ângulos propostos | Após propor, antes da escolha | `runs/[data]/angulos-[tema].md` |
| Script de carrossel | Após gerar o script completo | `runs/[data]/carrossel-[tema].md` |
| Variações de capa | Após auto-gerar as 5 capas | `runs/[data]/capas-[tema].md` |
| Variações de legenda | Junto com as capas | `runs/[data]/legendas-[tema].md` |
| JSON de capa (carrossel) | Após json-prompt-generator | `runs/[data]/json-capas-[tema].md` |
| JSON de post estático | Após json-prompt-generator | `runs/[data]/json-estatico-[tema].md` |
| JSON de stories | Após json-prompt-generator | `runs/[data]/json-stories-[tema].md` |
| JSON de lançamento | Após json-prompt-generator | `runs/[data]/json-lancamento-[tipo].md` |
| Roteiro de vídeo | Após gerar o roteiro | `runs/[data]/roteiro-[tema].md` |

Tema em kebab-case. Ex: `halvng-bitcoin`, `ethereum-staking`, `lancamento-agosto`.
Pasta `runs/[data]/` criada automaticamente se não existir.

---

## 10. Decisões de arquitetura

### 10.1 Por que impeccable é o padrão para LPs

O usuário definiu "sempre a entrega mais impecável possível" para páginas. O impeccable é o único que tem gates de qualidade embutidos: tipografia, anti-slop, acessibilidade, auditoria técnica. O custo de tokens é real mas justificado pelo padrão de entrega.

### 10.2 Por que taste-skill entra na Fase 2 Craft (não substitui impeccable)

impeccable é o arquiteto: define estrutura, os 11 elementos, copy por seção, regras de conversão. taste-skill é o executor: pega essa estrutura e gera componentes React/Tailwind com anti-slop rules, Framer Motion physics, Creative Arsenal. São responsabilidades diferentes na mesma fase.

### 10.3 Por que web-design-guidelines complementa (não substitui) o audit do impeccable

O audit do impeccable cobre WCAG AA macro, performance e responsividade. web-design-guidelines cobre 14 categorias de compliance granular que o impeccable não verifica: `focus-visible`, `touch-action`, `prefers-reduced-motion`, `autocomplete`, `tabular-nums`, hydration safety, i18n. São camadas ortogonais, não redundantes.

### 10.4 Por que landing-page-guide-v2 permanece

Alternativa legítima quando: prazo curto, cliente de entrada, primeira versão para validação. O orquestrador pergunta ao usuário qual situação se aplica quando detecta ambiguidade.

| Situação | Use |
|---|---|
| Cliente high-ticket, entrega premium, tem tempo | impeccable + taste-skill |
| Prazo curto, produto de entrada, LP simples | landing-page-guide-v2 |
| Primeiro rascunho para validar com cliente | landing-page-guide-v2 → depois impeccable para versão final |

### 10.5 Por que apenas 3 plugins do designer-skills

Os outros 6 plugins cobrem: pesquisa qualitativa com usuários, gestão de sprint de design, handoff de equipe, design de interação técnico, prototipagem formal, estratégia de UX corporativa. Nenhum se aplica ao perfil de social media / infoprodutor / LP solo.

### 10.6 Por que video-script-sms é nova (não existia)

Nenhuma das skills existentes cobria roteiro de vídeo falado. As skills disponíveis cobrem hook (hook-writer-sms), legenda (caption-writer-sms), animação (huashu). O miolo do roteiro — cenas, fala, visual, timing — estava sem cobertura.

### 10.7 Por que interface-design ficou no Contexto 5 (separado dos outros)

A skill declara explicitamente em seu escopo: "Not for: landing pages, marketing sites, campaigns." Aplicá-la em LPs violaria sua metodologia de Domain Exploration (que pressupõe interface de produto com usuário recorrente, não visitante de LP). O Contexto 5 cria o espaço correto para seu uso.

### 10.8 Mapa de orquestração extraído do mestre-squad-builder

A metodologia do mestre-squad-builder (o que NÃO faz por agente, handoffs formalizados, gates explícitos, critérios de pronto) foi incorporada como seção MAPA DE ORQUESTRAÇÃO no SKILL.md. Isso resolve sobreposição de responsabilidades entre skills e processos que avançavam sem informação suficiente.

---

## 11. Limitações conhecidas

| Limitação | Impacto | Workaround |
|---|---|---|
| Skills não invocam outras skills via código | O orquestrador instrui o Claude sobre o fluxo — não executa chamadas programáticas | Orquestrador gerencia o fluxo em linguagem natural |
| No Claude.ai chat (não Code) | Skills não funcionam nativamente | Use o SKILL.md do orquestrador como instrução customizada de um Project |
| Roteiros de vídeo falados | O sistema entrega o script, não o vídeo | Gravação manual pelo criador |
| huashu-design em PT-BR | Prompts internos em chinês — pode ter variações ocasionais | Funciona em PT-BR mas resultados podem variar |
| Clientes com pouca referência visual | Direction Advisor gera 3 direções mas o refinamento é manual | Executar onboarding visual completo com o cliente antes |

---

## 12. Roadmap

### v1.1 ✅ Concluído (2026-05-21)
- [x] taste-skill integrada ao CONTEXTO 1 Fase 2 Craft
- [x] web-design-guidelines integrada ao CONTEXTO 1 Fase 3 Audit
- [x] CONTEXTO 5 — Interface Design (dashboard, SaaS, produto digital)
- [x] MAPA DE ORQUESTRAÇÃO: tabela de ativação, escopos, handoffs, gates, critérios de pronto
- [x] README e PRD atualizados
- [x] workflow 01-landing-page.md atualizado
- [x] workflow 05-interface-design.md criado

### v1.2 ✅ Concluído (2026-07-27)
- [x] Todas as pastas de cliente (incluindo `runs/`) versionadas neste repositório, sem exclusão via `.gitignore`
- [x] Repositório republicado em `master-design-system-v270726`
- [x] Restauração do conteúdo real de 23 skills que estavam substituídas por stubs "moved" com caminho absoluto de máquina
- [x] Regra canônica no `CLAUDE.md`: repositório é a única fonte de verdade de skills, nunca a pasta global do usuário
- [x] `production-orchestrator-sms` v1.1.0 — Gates Obrigatórios (A/B/C/D) embutidos diretamente na skill (ver seção 5.3.1)
- [x] `workflows/02-social-media.md` atualizado com os 4 gates por tipo de peça, incluindo fluxo de artigo (article-writer-sms → illustration-writer-sms → x-article-publisher)
- [ ] Integração com BlackTwist MCP para publicação direta nas plataformas
- [ ] Template de proposta comercial para clientes
- [ ] Skill de briefing estruturado para novos projetos
- [ ] Template de relatório mensal de cliente

### v1.3
- [ ] Guia de meta ads (criativo de anúncio) — ads-create, ads-meta, ads-plan já instalados, falta mapear no orquestrador

### v2.0
- [ ] Skill de análise de concorrentes com web scraping
- [ ] Sistema de versionamento de conteúdo por cliente
- [ ] Dashboard de KPIs integrado com performance dos clientes
