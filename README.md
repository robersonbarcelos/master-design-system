# Master Social Design System

**Orquestrador de produção de design e conteúdo para Claude Code**

> Um sistema de skills que detecta o contexto de trabalho automaticamente e conduz o fluxo completo de produção — landing pages, social media, roteiros de vídeo, campanhas de lançamento e interfaces de produto — sem que você precise especificar cada etapa.

---

## O que é

O **Master Social Design System** é um orquestrador de skills para [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Você descreve o que precisa fazer em linguagem natural. O sistema detecta o contexto, carrega o perfil do cliente correto, aciona as skills necessárias na ordem certa e aplica gates de qualidade antes de entregar.

**5 contextos suportados:**

| # | Contexto | Quando acionar |
|---|---|---|
| 1 | **Landing Page** | LP, página de vendas, página de captura, site |
| 2 | **Social Media** | carrossel, post, feed, Instagram, TikTok, LinkedIn, legenda |
| 3 | **Roteiro de Vídeo** | roteiro, reel, vídeo, script, shorts, YouTube |
| 4 | **Lançamento de Infoproduto** | lançamento, campanha, infoproduto, abertura de carrinho |
| 5 | **Interface Design** | dashboard, SaaS, área de membros, ferramenta interna, portal |

**~32 skills integradas:**

- 14 Social Media Skills (`blacktwist/social-media-skills`)
- 2 skills próprias: `landing-page-guide-v2`, `card-news-generator-v2`
- 4 skills de visual critique + 5 de UI/UX design (`Owl-Listener/designer-skills`)
- `huashu-design` (assets de marca, motion, slides, infográficos)
- `impeccable` (arquitetura de LP, craft, polish, audit)
- `taste-skill` (execução React/Tailwind anti-slop)
- `web-design-guidelines` (compliance técnico granular)
- `interface-design` (design de produto, dashboards, SaaS)
- `video-script-sms` (roteiros de vídeo — incluída neste repositório)
- `json-prompt-generator` (JSONs estruturados de imagem para geradores de IA)

---

## Como funciona — visão geral

```
Você escreve:  "preciso fazer 3 carrosseis para essa semana"
                              ↓
Orquestrador:  detecta CONTEXTO 2 (Social Media)
                              ↓
               lê .agents/social-media-context-sms.md do cliente
                              ↓
               propõe 3 ângulos → aguarda sua escolha
                              ↓
               aciona: hook-writer → carousel-writer → auto-gera capas + legendas
                              ↓
               aciona: json-prompt-generator → card-news-generator → caption-writer
                              ↓
               salva artefatos em runs/[data]/
```

O orquestrador **pausa apenas** para:
- Aprovação de direção visual
- Escolha de ângulo de carrossel
- Confirmação do cliente

Tudo mais é executado automaticamente.

---

## Instalação

### Pré-requisitos

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) instalado
- Node.js 18+

### 1 — Clone este repositório

```bash
git clone https://github.com/robersonbarcelos/master-design-system-v270726.git
cd master-design-system-v270726
```

### 2 — Instale o orquestrador principal

```bash
# Via npx skills (recomendado)
npx skills add ./

# Ou manualmente
cp SKILL.md ~/.claude/skills/production-orchestrator/SKILL.md
```

### 3 — Instale a skill de roteiro de vídeo (incluída neste repo)

```bash
cp -r skills/video-script-sms ~/.claude/skills/
```

### 4 — Instale as Social Media Skills

```bash
npx skills add blacktwist/social-media-skills
```

Ou pelo Claude Code: `Cowork > Customize > Skills > +` e faça upload de cada zip.

### 5 — Instale as demais skills

```bash
# huashu-design — assets de marca, motion design, slides
npx skills add alchaincyf/huashu-design

# taste-skill — execução React/Tailwind anti-slop
npx skills add leonxlnx/taste-skill@taste-skill

# web-design-guidelines — compliance técnico granular
npx skills add vercel-labs/agent-skills@web-design-guidelines

# interface-design — dashboards, SaaS, área de membros
npx skills add dammyjay93/interface-design@interface-design

# impeccable — arquitetura LP, craft, audit
# Baixe de: https://github.com/impeccable-io/impeccable
# Copie a pasta .agents/skills/impeccable para ~/.claude/skills/

# designer-skills — 3 plugins: visual-critique, ui-design, ux-strategy
/plugin marketplace add Owl-Listener/designer-skills
```

### 6 — Verifique

No Claude Code, abra uma pasta de cliente e escreva:

```
preciso criar uma landing page para um cliente
```

O orquestrador detecta o contexto e inicia o fluxo.

---

## Estrutura do repositório

```
master-social-design-system/
├── SKILL.md                          ← Orquestrador mestre (lido pelo Claude Code)
├── README.md                         ← Este arquivo
├── PRD.md                            ← Documentação técnica completa
│
├── skills/
│   ├── video-script-sms/
│   │   └── SKILL.md                  ← Skill de roteiro de vídeo (nova)
│   ├── social-media/                 ← 14 social media skills
│   ├── design/                       ← Skills de design (visual critique, ui-design, ux-strategy)
│   ├── huashu-design/                ← huashu-design completo
│   └── impeccable/                   ← impeccable completo
│
├── workflows/
│   ├── 01-landing-page.md            ← Fluxo detalhado LP com taste-skill + web-design-guidelines
│   ├── 02-social-media.md            ← Fluxo detalhado social media
│   ├── 03-video-script.md            ← Fluxo detalhado roteiro de vídeo
│   ├── 04-launch-campaign.md         ← Fluxo detalhado campanha de lançamento
│   └── 05-interface-design.md        ← Fluxo detalhado interface de produto
│
├── reference/
│   └── design-md-guide.md            ← Guia para escolher DESIGN.md por projeto
│
└── clients/
    ├── _template/                    ← Template para novos clientes
    │   ├── .agents/
    │   │   ├── social-media-context-sms.md
    │   │   ├── paid-ads-onboarding.md
    │   │   └── ads-context.md
    │   ├── CLAUDE.md
    │   ├── DESIGN.md
    │   ├── brand-spec.md
    │   ├── content-system.md
    │   ├── production-rules.md
    │   ├── visual-system.md
    │   └── references/
    │       ├── copies-aprovadas.md
    │       ├── dados-ancora.md
    │       └── temas.md
    └── [nome-cliente]/               ← Pasta por cliente (versionada completa, incluindo runs/)
```

> **Clientes ativos neste repositório:** `Carol`, `ESENCA`, `aurum-lingerie`, `intus-hub`, `mercurius`, `michele-fara`, `motofacil`, `novadax`, `super-agente-ia`, `white-label`. Todas as pastas de cliente — incluindo contexto, referências e histórico de produção em `runs/` — são versionadas neste repositório.

---

## Sistema de contexto de cliente

Cada cliente tem uma pasta com arquivos de contexto persistentes. As skills leem esses arquivos automaticamente a cada sessão — você **nunca re-explica** o cliente.

### Arquivos por cliente

| Arquivo | Lido por | Conteúdo |
|---|---|---|
| `.agents/social-media-context-sms.md` | Todas as social media skills | Nicho, voz, pilares, plataformas, restrições |
| `brand-spec.md` | huashu-design | Logo, cores, tipografia, assets |
| `DESIGN.md` | impeccable, landing-page-guide-v2 | Referência visual do projeto |
| `visual-system.md` | json-prompt-generator | Sistema visual para geração de imagens |
| `content-system.md` | carousel-writer, post-writer | Regras de copy específicas |
| `production-rules.md` | Orquestrador | Regras de produção do cliente |

### Criar um novo cliente

```bash
# Opção 1 — Script automatizado
./setup-client.sh nome-do-cliente        # Linux/macOS
./setup-client.ps1 nome-do-cliente       # Windows

# Opção 2 — Manual
mkdir -p clients/nome-do-cliente/.agents
cp clients/_template/.agents/social-media-context-sms.md clients/nome-do-cliente/.agents/
cp clients/_template/brand-spec.md clients/nome-do-cliente/
cp clients/_template/DESIGN.md clients/nome-do-cliente/
cp clients/_template/visual-system.md clients/nome-do-cliente/
```

Depois, abra a pasta no Claude Code e escreva qualquer coisa — o sistema detecta que não há contexto e inicia o onboarding automaticamente.

---

## Fluxo de acionamento — passo a passo

### PASSO 0 — Detecção automática

Ao receber qualquer mensagem, o orquestrador:

1. **Identifica o contexto** pelo vocabulário da mensagem
2. **Localiza o cliente** — lê `.agents/social-media-context-sms.md` se existir
3. **Verifica os arquivos de marca** — `brand-spec.md` e `DESIGN.md`
4. **Aciona o gate de entrada** — se algo está faltando, para e resolve antes de prosseguir

### CONTEXTO 1 — Landing Page

```
[GATE 0] brand-spec.md + DESIGN.md existem?
    ↓ NÃO → Core Asset Protocol + Direction Advisor (huashu)
    ↓ SIM →

FASE 1 — FUNDAÇÃO
├── huashu: Core Asset Protocol → extrai assets de marca
├── huashu: Direction Advisor → 3 direções visuais (usuário escolhe 1)
├── designer-skills: color-palette → fecha paleta
└── Benchmark de mercado (3 concorrentes)

[GATE 1] Shape aprovado? Paleta fechada? Nenhuma fonte rejeitada?

FASE 2 — CONSTRUÇÃO
├── impeccable Shape → define estrutura + 11 elementos + copy por seção
├── taste-skill + impeccable Craft → executa React/Tailwind
│   ├── DESIGN_VARIANCE: 8 (assimétrico, sem 3 cards iguais)
│   ├── MOTION_INTENSITY: 6 (Framer Motion spring physics)
│   └── VISUAL_DENSITY: 4 (espaçamento generoso)
└── impeccable Polish → animações + microinterações + meta tags

[GATE 2] Todos os componentes prontos?

FASE 3 — VALIDAÇÃO
├── huashu: critique 5D → coerência, hierarquia, técnica, funcionalidade, inovação
├── impeccable: audit → WCAG AA + performance + responsivo + anti-patterns
└── web-design-guidelines → compliance granular (14 categorias técnicas)

[GATE 3] Todos os audits passaram? → ENTREGA FINAL
```

**Os 11 elementos obrigatórios de uma LP:**
1. Headline com proposta de valor clara
2. Subheadline de suporte
3. Hero visual (imagem, vídeo ou mockup)
4. Benefícios (transformação, não features)
5. Prova social (depoimentos, números, logos)
6. Como funciona (processo em 3 etapas)
7. Sobre o criador/autoridade
8. CTA principal (acima do fold e repetido)
9. Garantia e objeções
10. FAQ
11. Urgência/escassez (se aplicável)

---

### CONTEXTO 2 — Social Media

**Fluxo de carrossel:**

```
ETAPA 1 — PRÉ-PRODUÇÃO: 3 ÂNGULOS DISTINTOS
  Cada ângulo entrega:
  - Nome (ex: Provocação, Educativo Direto, Contrarian, Dado Chocante)
  - Gancho de capa — 1-2 linhas impactantes
  - Linha narrativa — o que o carrossel vai contar

[GATE 4.5] Ângulo aprovado pelo usuário (1, 2 ou 3)?

ETAPA 2 — PRODUÇÃO DO CARROSSEL
├── hook-writer-sms → aprofunda variações do gancho
└── carousel-writer-sms → script 9-12 slides
    ├── Slides CERNE: 100% do espaço, dados, máx 8 linhas, até 4 bullets
    └── Slides SECUNDÁRIOS: máx 4 linhas, sem indicar [espaço para imagem]

ETAPA 3 — AUTO-GERAÇÃO (sem precisar solicitar)
├── 5 variações de capa:
│   V1: Dado chocante / número em destaque
│   V2: Contraste visual / dois mundos opostos
│   V3: Personagem / storytelling humano
│   V4: Minimalista / tipografia forte
│   V5: Metáfora visual / conceitual
└── 3 variações de legenda:
    L1: Storytelling — narrativa que acompanha os slides
    L2: Provocação/Dado — abre com número ou fato chocante
    L3: Educativa/Direta — explica o valor objetivamente

ETAPA 4 — JSON DE IMAGEM
└── json-prompt-generator → JSON completo da capa escolhida
    (scene / style / technical / materials / composition / quality include+avoid)

[GATE 4] Script aprovado?

ETAPA 5 — CARDS E DISTRIBUIÇÃO
├── card-news-generator-v2 → cards visuais com brand-spec.md
└── caption-writer-sms → legenda final otimizada por plataforma
```

---

### CONTEXTO 3 — Roteiro de Vídeo

```
BRIEFING (5 perguntas)
├── Plataforma e formato (Reel 15s/30s/60s, TikTok, YouTube)
├── Objetivo (educativo, venda, autoridade, bastidor)
├── Tema e mensagem central
├── Estilo (talking head, animado, narração off, misto)
└── CTA ao final

FASE 2 — ROTEIRO (via video-script-sms)
  Entrega:
  - Hook dos primeiros 3 segundos
  - Roteiro cena a cena (fala + descrição visual + duração + B-roll)
  - CTA final
  - Caption otimizada por plataforma

FASE 3 — PRODUÇÃO VISUAL (se animado)
└── huashu-design → motion design MP4/GIF + BGM

FASE 4 — DISTRIBUIÇÃO
├── caption-writer-sms → legenda + hashtags
└── content-repurposer-sms → adapta para outros formatos
```

---

### CONTEXTO 4 — Lançamento de Infoproduto

```
FASE 1 — BASE DA CAMPANHA
├── huashu: Core Asset Protocol → assets do produto
├── huashu: Direction Advisor → direção visual da campanha
├── content-strategy-sms → pilares (educação→autoridade→desejo→prova→urgência)
├── content-calendar-sms → cronograma pré/lançamento/pós
└── Benchmark de 3 lançamentos similares

FASE 2 — LANDING PAGE DE VENDAS
└── Execute CONTEXTO 1 completo (com todos os gates)

FASE 3 — CONTEÚDO DE AQUECIMENTO
├── Semana 1: carrosseis sobre a dor + posts de autoridade
├── Semana 2: carrosseis de método/solução + thread de bastidor
└── Semana 3: depoimentos + carrossel de transformações + antecipação
  Para cada peça: hook → carousel → json-prompt → card → caption → repurpose

FASE 4 — PRODUÇÃO DO LANÇAMENTO
├── huashu → animação de abertura de carrinho (MP4 + BGM)
├── huashu → deck de vendas para live (HTML + PPTX editável)
├── hook-writer → hooks de abertura de carrinho
├── post-writer → posts de urgência, depoimento, last call
├── thread-writer → thread de lançamento
└── video-script → roteiros de vídeo da campanha

FASE 5 — ANÁLISE PÓS-LANÇAMENTO
├── performance-analyzer-sms → o que converteu mais
├── content-pattern-analyzer-sms → padrões de performance
├── audience-growth-tracker-sms → crescimento durante a campanha
└── optimization-advisor-sms → o que replicar no próximo lançamento
```

---

### CONTEXTO 5 — Interface Design

```
FASE 1 — INTENT FIRST (via interface-design)
  Responder obrigatoriamente antes de qualquer wireframe:
  1. Quem é esse usuário? (pessoa real, contexto de uso)
  2. O que ele precisa fazer? (verbo preciso: aprovar, revisar, criar)
  3. Como isso deve parecer? (frio como terminal? denso como trading floor?)

[GATE 5] Intent respondido com especificidade?

FASE 2 — DOMAIN EXPLORATION (via interface-design)
  4 outputs obrigatórios:
  ├── Domínio: conceitos, metáforas, vocabulário do produto (mín. 5)
  ├── Mundo de cores: cores do domínio físico (mín. 5 — não "quente/frio")
  ├── Assinatura: elemento visual que só existe para ESTE produto
  └── Defaults a evitar: 3 escolhas óbvias para esse tipo de interface

FASE 3 — EXECUÇÃO (via taste-skill + interface-design)
  Stack: React / Next.js + Tailwind + Framer Motion
  Dials: DESIGN_VARIANCE: 6 / MOTION_INTENSITY: 4 / VISUAL_DENSITY: 7-9 ou 3-5
  Craft foundations:
  ├── Surface Elevation: camadas com mínima diferença de lightness
  ├── Borders: rgba de baixa opacidade, sistema de 4 níveis
  └── Token names semânticos: --vault-surface, --terminal-ink (nunca --gray-700)

FASE 4 — VALIDAÇÃO
├── Swap Test: troque pelos choices mais comuns — ficou diferente?
├── Squint Test: desfoque os olhos — hierarquia ainda legível?
├── Signature Test: 5 elementos onde a assinatura aparece
├── Token Test: leia os CSS variables — soam como este produto?
└── web-design-guidelines → compliance técnico granular
```

---

## Gates obrigatórios

| Gate | Contexto | Condição | Consequência se falhar |
|---|---|---|---|
| GATE 0 | Todos | `brand-spec.md` + `DESIGN.md` existem? | STOP: execute Core Asset Protocol |
| GATE 1 | LP | Shape aprovado? Paleta fechada? | STOP: não gera código |
| GATE 2 | LP | Componentes React completos? | STOP: não audita |
| GATE 3 | LP | 5D Critique + Audit + web-design-guidelines executados? | STOP: não entrega |
| GATE 4 | Social | Script aprovado? brand-spec.md carregado? | STOP: não gera visual |
| GATE 4.5 | Carrossel | 3 ângulos propostos? Ângulo aprovado? | STOP: não escreve script |
| GATE 5 | Interface | Intent respondido? Domain Exploration com 4 outputs? | STOP: não executa |

---

## Salvamento automático de artefatos

Após cada etapa aprovada, o sistema salva em `runs/[data-de-hoje]/`:

| Artefato | Nome do arquivo |
|---|---|
| 3 ângulos propostos | `angulos-[tema].md` |
| Script de carrossel | `carrossel-[tema].md` |
| 5 variações de capa | `capas-[tema].md` |
| 3 variações de legenda | `legendas-[tema].md` |
| JSON de capa (carrossel) | `json-capas-[tema].md` |
| JSON de post estático | `json-estatico-[tema].md` |
| JSON de stories | `json-stories-[tema].md` |
| JSON de lançamento | `json-lancamento-[tipo].md` |
| Roteiro de vídeo | `roteiro-[tema].md` |

---

## Regras de qualidade — o que o sistema nunca aceita

**Fontes rejeitadas:**
Inter, DM Sans, Playfair Display, Fraunces, Space Grotesk, Outfit, Plus Jakarta Sans, Instrument Sans, Instrument Serif, Cormorant, Lora, Syne

**Estéticas rejeitadas:**
Gradiente roxo/azul genérico, ícones emoji como ilustração, glassmorphism sem propósito, layout de template, hero centrado com texto sobre imagem escura, 3 cards iguais em linha horizontal

**AI Tells proibidos (taste-skill):**
- Sem neon/glow externo
- Sem `#000000` puro
- Sem `h-screen` (use `min-h-[100dvh]`)
- Sem `transition: all`
- Sem Inter font

---

## Exemplos de uso no dia a dia

```
# Social media
"preciso fazer 3 carrosseis para essa semana para o cliente João"
→ Carrega perfil do João → Contexto 2 → 3 ângulos → script → capas → cards

# Landing page
"quero criar uma landing page de vendas para o curso de X"
→ Contexto 1 → fundação → shape → craft → validação → entrega

# Vídeo
"me ajuda a escrever o roteiro do reel de terça"
→ Contexto 3 → briefing (5 perguntas) → video-script-sms

# Lançamento
"vamos planejar a campanha de lançamento do produto Y"
→ Contexto 4 → base → LP → aquecimento → produção → análise

# Interface
"preciso criar o dashboard de admin da plataforma"
→ Contexto 5 → intent first → domain exploration → execução → validação
```

---

## Mapa completo de skills

| Skill | Origem | Contextos | Fase |
|---|---|---|---|
| production-orchestrator | Este repo | Todos | Orquestração |
| video-script-sms | Este repo | 3, 4 | Produção |
| social-media-context-sms | blacktwist | 2, 4 | Setup |
| content-strategy-sms | blacktwist | 2, 4 | Estratégia |
| content-calendar-sms | blacktwist | 2, 4 | Calendário |
| platform-strategy-sms | blacktwist | 2, 4 | Estratégia |
| hook-writer-sms | blacktwist | 2, 3, 4 | Produção |
| carousel-writer-sms | blacktwist | 2, 4 | Produção |
| caption-writer-sms | blacktwist | 2, 3, 4 | Produção |
| post-writer-sms | blacktwist | 2, 4 | Produção |
| thread-writer-sms | blacktwist | 2, 4 | Produção |
| content-repurposer-sms | blacktwist | Todos | Distribuição |
| performance-analyzer-sms | blacktwist | 2, 4 | Análise |
| audience-growth-tracker-sms | blacktwist | 2, 4 | Análise |
| content-pattern-analyzer-sms | blacktwist | 2, 4 | Análise |
| optimization-advisor-sms | blacktwist | 2, 4 | Análise |
| landing-page-guide-v2 | my-skills | 1 | Construção |
| card-news-generator-v2 | my-skills | 2 | Produção visual |
| json-prompt-generator | my-skills | 2, 4 | Produção visual |
| visual-critique (4x) | designer-skills | 1, 2 | Validação |
| ui-design (5x) | designer-skills | 1, 5 | Fundação |
| ux-strategy | designer-skills | 1, 4 | Fundação |
| huashu-design | alchaincyf | 1, 2, 3, 4, 5 | Foundation + Produção + Validação |
| impeccable | impeccable-io | 1 | Construção + Validação |
| taste-skill | leonxlnx | 1, 5 | Construção |
| web-design-guidelines | vercel-labs | 1, 5 | Validação |
| interface-design | dammyjay93 | 5 | Todas as fases |

---

## Atualização

```bash
git pull origin main
# Re-copie os SKILL.md atualizados para ~/.claude/skills/
```

---

## Versão

**v1.3.0** — 2026-07-27

Veja o [PRD.md](PRD.md) para documentação técnica completa, decisões de arquitetura, roadmap e limitações conhecidas.

---

## Licença

MIT
