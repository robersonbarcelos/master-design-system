# PRD + SPECS — Sistema de Orquestração de Copy QA
> master-design-system · Camada de Produção de Social Media
> Versão 1.2.0 · Atualizado em 2026-07-14

---

## Sumário

1. [Requisitos de Produto (PRD)](#prd)
   - 1.1 Contexto e Problema
   - 1.2 Objetivos
   - 1.3 Fora do Escopo
   - 1.4 Histórias de Usuário
   - 1.5 Métricas de Sucesso
2. [Especificações Técnicas (SPECS)](#specs)
   - 2.1 Arquitetura do Sistema
   - 2.2 Mapa de Componentes
   - 2.3 Estrutura de Arquivos
   - 2.4 Protocolo de Invocação
   - 2.5 Especificações dos Gates
   - 2.6 Biblioteca de Padrões
   - 2.7 Detectores de Padrão Estrutural
   - 2.8 Pontos de Integração por Skill
   - 2.9 Casos de Borda e Fallbacks
3. [Diagrama de Workflow](#workflow)
   - 3.1 Fluxo Completo de Orquestração
   - 3.2 Fluxo Interno do copy-qa-sms
   - 3.3 Fluxo em Modo Standalone
4. [Changelog e Versionamento](#changelog)

---

## 1. Requisitos de Produto (PRD) {#prd}

### 1.1 Contexto e Problema

O master-design-system contém 7 skills de criação de social media (post-writer, thread-writer, caption-writer, hook-writer, carousel-writer, content-repurposer, video-script) que produzem copy para contas de clientes.

**O problema identificado na auditoria do sistema:**

Antes deste sistema, cada skill de criação gerenciava o controle de qualidade de forma independente e inconsistente:

| Problema | Impacto |
|---|---|
| Padrões de escrita IA (Tier 1/2/3) não eram detectados sistematicamente | Copy contendo "transformador", "seamless", "leverage" etc. era entregue aos clientes |
| Verificações de voz duplicadas em 6 skills com variações sutis | Inconsistência no que era capturado — skills diferentes verificavam coisas diferentes |
| Nenhuma fonte única de verdade para a biblioteca de padrões proibidos | Adicionar um novo padrão proibido exigia editar 7 arquivos |
| Sinais estruturais de IA (parágrafos uniformes, excesso de em-dash, bullets de substantivos) passavam sem verificação | Copy estruturalmente "legível como IA" aprovava o QA interno |
| Custo de manutenção alto | Atualizar a verificação de voz significava tocar cada skill de criação |
| Decisão de ângulo narrativo era tomada de forma invisível e inconsistente pelas skills de criação | Sempre resultava nas mesmas estruturas seguras (Hack List ou Value-Stack) — sem deliberação |

**Causa raiz:** O controle de qualidade estava descentralizado. Cada skill possuía sua própria lógica de QA, gerando divergência, lacunas e duplicação. A decisão de estrutura narrativa nunca havia sido externalizada para o usuário.

**Solução:**
1. Centralizar todas as verificações de qualidade pós-criação em uma única skill orquestradora (`copy-qa-sms`) pela qual toda skill de criação passa antes da entrega.
2. Externalizar a decisão de ângulo narrativo em uma skill upstream (`narrative-framework-sms`) que modela as 5 estruturas possíveis e entrega um briefing contratual para a skill de criação executar.

Uma fonte de verdade para QA. Uma fonte de verdade para narrativa. Cobertura universal.

---

### 1.2 Objetivos

**O1 — Zero entrega de padrão IA**
Nenhum copy produzido por qualquer skill de criação chega ao usuário se contiver um padrão de escrita Tier 1.

**O2 — Verificação de voz centralizada**
A verificação `production-rules.md → 00-B | PADRÕES DE AUSÊNCIA DE VOZ` roda de forma idêntica nas 7 skills de criação, originada de uma única definição de gate.

**O3 — Detecção de sinais estruturais**
Assinaturas estruturais de IA (comprimento uniforme de parágrafos, excesso de em-dash, bullets só com substantivos, atribuições vagas, contraste binário, fragmentação estacato) são capturadas antes da entrega, independentemente de qual skill produziu o copy.

**O4 — Ponto único de atualização**
Quando a biblioteca de padrões proibidos precisa ser atualizada (nova palavra Tier 1, novo sinal estrutural), apenas `copy-qa-sms/SKILL.md` é editado. As 7 skills de criação herdam a atualização automaticamente.

**O5 — Auditabilidade standalone**
Qualquer usuário pode invocar `copy-qa-sms` diretamente para auditar copy existente (rascunhos, copy de concorrentes, posts anteriores) sem passar por uma skill de criação.

**O6 — Operação silenciosa quando embutido**
Quando invocado como gate por outra skill, `copy-qa-sms` roda silenciosamente. O usuário vê apenas o copy final aprovado — não a lógica interna do gate nem o histórico de reescrita.

**O7 — Decisão narrativa deliberada**
Antes de qualquer criação de conteúdo com ângulo em aberto, o usuário vê os 5 frameworks narrativos modelados com hooks já escritos no tom do cliente, e escolhe conscientemente antes da execução.

---

### 1.3 Fora do Escopo

- NÃO substitui os QA Gates específicos de formato (cada skill mantém sua própria rubrica de pontuação — post: 90/100, carousel: 90/100, repurposer: 85/100)
- NÃO escreve copy do zero
- NÃO avalia estratégia de conteúdo, alinhamento de pilares ou agendamento de calendário
- NÃO analisa performance pós-publicação
- NÃO fornece conselhos sobre algoritmos de plataformas
- NÃO lida com assets visuais, imagens ou arquivos de vídeo

---

### 1.4 Histórias de Usuário

**Como operador de conteúdo:**
> "Quando peço ao post-writer para escrever um post no LinkedIn, quero que o copy final tenha sido automaticamente verificado quanto a padrões de IA — sem precisar rodar uma auditoria separada ou saber quais palavras observar."

**Como mantenedor do sistema:**
> "Quando os modelos da Anthropic ficarem melhores em evitar 'robusto' mas começarem a usar demais 'sutil', quero adicionar 'sutil' à lista de proibidos em um lugar e ter isso aplicado imediatamente a todas as skills de criação."

**Como revisor de cliente:**
> "Quero poder colar um texto no sistema e obter um relatório de auditoria estruturado mostrando exatamente quais padrões foram encontrados, o que foi alterado e a versão final aprovada."

**Como skill de criação (perspectiva interna):**
> "Depois de passar pelo meu próprio QA Gate específico de formato, repasso para o copy-qa-sms. Se voltar aprovado, entrego. Se voltar com reescritas, aplico silenciosamente e re-executo antes de entregar."

**Como estrategista de conteúdo:**
> "Quando tenho um tema mas não sei como entrar, quero ver os 5 ângulos possíveis com os hooks já escritos, para decidir qual direção tomar antes de qualquer copy ser produzido."

---

### 1.5 Métricas de Sucesso

| Métrica | Meta | Medição |
|---|---|---|
| Taxa de entrega de padrão Tier 1 | 0% | Auditoria manual do copy entregue por 30 dias |
| Estrutura uniforme de parágrafos nos outputs | < 5% dos outputs | Revisão estrutural de 50 posts de amostra |
| Ocorrências de em-dash por post (média) | ≤ 1 | Contagem em amostra de 50 posts de LinkedIn |
| Tempo para atualizar a biblioteca de padrões | < 2 min | Editar um arquivo, medir o tempo |
| Skills que requerem atualização individual após mudança na biblioteca | 0 | Contagem de arquivos tocados |
| Conteúdo produzido sem escolha de ângulo deliberada | 0% | Verificação de briefing na conversa antes de qualquer execução |

---

## 2. Especificações Técnicas (SPECS) {#specs}

### 2.1 Arquitetura do Sistema

```
┌─────────────────────────────────────────────────────────────────┐
│              CAMADA DE DECISÃO NARRATIVA (upstream)              │
│                                                                   │
│  narrative-framework-sms                                          │
│                                                                   │
│  Aciona quando: tema definido, ângulo em aberto                  │
│  Modela: 5 frameworks (Value-Stack, Problem-Proof, Hack List,    │
│          Rant Callout, Demo Walkthrough) × 4 formatos            │
│  Entrega: briefing contratual com hook aprovado + arco           │
│  Não aciona quando: ângulo explícito ou briefing já existe        │
└──────────────────────────────────────────────────────────────────┘
                              │ briefing
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  CAMADA DE CRIAÇÃO (7 skills)                    │
│                                                                   │
│  post-writer  thread-writer  caption-writer  hook-writer         │
│  carousel-writer  content-repurposer  video-script-sms           │
│                                                                   │
│  Cada skill:                                                      │
│  1. Lê o contexto (.agents/social-media-context-sms.md)          │
│  2. Lê o briefing do narrative-framework-sms (se existir)        │
│  3. Escreve copy específico para o formato                        │
│  4. Executa seu QA Gate específico (score ≥ 90 / ≥ 85)          │
│  5. ──── repassa para copy-qa-sms ────▶                         │
└──────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                copy-qa-sms (ORQUESTRADOR)                        │
│                                                                   │
│  PASSO 1: Gate de Voz                                            │
│    └─ production-rules.md → 00-B                                 │
│    └─ Padrões universais proibidos (8 categorias)                │
│                                                                   │
│  PASSO 2: Gate de Padrões IA                                     │
│    ├─ Tier 1: sempre reescrever (qualquer ocorrência)            │
│    ├─ Tier 2: reescrever se 2+ no mesmo parágrafo               │
│    ├─ Tier 3: revisar se 3+ por 200 palavras                     │
│    └─ Estrutural: 13 detectores de padrão                        │
│                                                                   │
│  PASSO 3: Decisão                                                │
│    ├─ APROVADO → retorna para skill → entrega silenciosa         │
│    └─ REPROVADO → reescrita automática → re-executa (máx 2x)    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                  COPY APROVADO → USUÁRIO
```

### 2.2 Mapa de Componentes

| Componente | Arquivo | Versão | Papel |
|---|---|---|---|
| **narrative-framework-sms** | `skills/social-media/narrative-framework-sms/SKILL.md` | 1.0.0 | Seletor de ângulo narrativo — upstream de todas as skills de criação; modela 5 frameworks e entrega briefing contratual |
| **copy-qa-sms** | `skills/social-media/copy-qa-sms/SKILL.md` | 1.1.0 | Orquestrador universal de QA — gate final antes de toda entrega de copy |
| **post-writer-sms** | `skills/social-media/post-writer-sms/SKILL.md` | 1.4.0 | Cria posts sociais standalone; invoca narrative-framework-sms + copy-qa-sms |
| **thread-writer-sms** | `skills/social-media/thread-writer-sms/SKILL.md` | 1.6.0 | Cria threads de múltiplos posts; invoca narrative-framework-sms + copy-qa-sms |
| **caption-writer-sms** | `skills/social-media/caption-writer-sms/SKILL.md` | 1.3.0 | Cria legendas visual-first; invoca copy-qa-sms |
| **hook-writer-sms** | `skills/social-media/hook-writer-sms/SKILL.md` | 1.3.0 | Cria linhas de abertura/hooks; invoca copy-qa-sms |
| **carousel-writer-sms** | `skills/social-media/carousel-writer-sms/SKILL.md` | 2.2.0 | Cria copy slide a slide para carrossel; invoca narrative-framework-sms + copy-qa-sms |
| **content-repurposer-sms** | `skills/social-media/content-repurposer-sms/SKILL.md` | 1.3.0 | Reaproveita conteúdo entre plataformas; invoca copy-qa-sms |
| **video-script-sms** | `skills/video-script-sms/SKILL.md` | 1.3.0 | Cria roteiros de vídeo; invoca narrative-framework-sms (MODO A) + copy-qa-sms |
| **production-rules.md** | `clients/[cliente]/production-rules.md` | Por cliente | Regras de voz específicas do cliente; lido pelo Passo 1 do copy-qa-sms |
| **social-media-context-sms.md** | `clients/[cliente]/.agents/social-media-context-sms.md` | Por cliente | Contexto de voz/plataforma; lido pelas skills de criação |

### 2.3 Estrutura de Arquivos

```
master-design-system/
├── skills/
│   ├── social-media/
│   │   ├── narrative-framework-sms/  ← NOVO (v1.0.0)
│   │   │   └── SKILL.md
│   │   ├── copy-qa-sms/              ← ATUALIZADO (v1.0 → v1.1)
│   │   │   └── SKILL.md
│   │   ├── post-writer-sms/          ← ATUALIZADO (v1.3 → v1.4)
│   │   │   └── SKILL.md
│   │   ├── thread-writer-sms/        ← ATUALIZADO (v1.5 → v1.6)
│   │   │   └── SKILL.md
│   │   ├── caption-writer-sms/       ← v1.3.0 (sem alteração)
│   │   │   └── SKILL.md
│   │   ├── hook-writer-sms/          ← v1.3.0 (sem alteração)
│   │   │   └── SKILL.md
│   │   ├── carousel-writer-sms/      ← ATUALIZADO (v2.1 → v2.2)
│   │   │   └── SKILL.md
│   │   └── content-repurposer-sms/   ← v1.3.0 (sem alteração)
│   │       └── SKILL.md
│   └── video-script-sms/             ← ATUALIZADO (v1.2 → v1.3)
│       └── SKILL.md
├── clients/
│   └── [nome-do-cliente]/
│       ├── production-rules.md       ← Lido pelo Passo 1 (seção 00-B)
│       └── .agents/
│           └── social-media-context-sms.md
└── docs/
    └── copy-qa-orchestration/
        ├── PRD-SPECS.md              ← Este arquivo
        └── PRD-SPECS.html            ← Versão visual
```

---

### 2.4 Protocolo de Invocação

#### Invocação do narrative-framework-sms (upstream)

Toda skill de criação verifica se o ângulo narrativo foi definido antes de escrever:

```
[Skill de criação ativada com tema]
  SE briefing do narrative-framework-sms já existe na conversa:
    → ler hook aprovado e arco de execução → executar sem desviar
  SE tema definido + ângulo em aberto (sem estrutura especificada):
    → invocar narrative-framework-sms com: {tema, formato}
    → aguardar escolha do usuário (A/B/C/D/E)
    → receber briefing estruturado → executar o arco
  SE ângulo especificado explicitamente pelo usuário:
    → executar diretamente (não acionar narrative-framework-sms)
```

**Exceção video-script-sms:** o gate de narrativa se aplica apenas ao MODO A (criação original). MODO B (reverse engineering de vídeo de referência) deriva o framework do vídeo analisado — não há escolha a fazer.

#### Invocação automática do copy-qa-sms (modo embutido)

Toda skill de criação chama `copy-qa-sms` após seu próprio QA Gate ser aprovado:

```
[Resultado do QA Gate da Skill de Criação]
  SE score >= limite (90 ou 85):
    → invocar copy-qa-sms com: {copy, plataforma, tipo_de_formato}
    → SE copy-qa-sms retornar APROVADO: entregar copy ao usuário (silenciosamente)
    → SE copy-qa-sms retornar REPROVADO: aplicar reescritas → re-invocar copy-qa-sms
       → SE segunda tentativa retornar APROVADO: entregar copy ao usuário
       → SE segunda tentativa ainda REPROVAR: mostrar trecho com falha ao usuário, pedir direcionamento
  CASO CONTRÁRIO (score < limite):
    → reescrever critérios reprovados → re-executar QA Gate → então invocar copy-qa-sms
```

**Modo silencioso:** Quando invocado por outra skill, `copy-qa-sms` NÃO exibe o resultado do gate ao usuário. O usuário vê apenas o copy final aprovado.

#### Invocação direta do copy-qa-sms (modo de auditoria)

Quando o usuário invoca `copy-qa-sms` diretamente:
- Entrada: texto de copy existente + plataforma (opcional)
- Saída: relatório completo de auditoria com antes/depois das reescritas + copy final aprovado
- Os 3 passos são executados por completo com resultados exibidos

---

### 2.5 Especificações dos Gates

#### Gate narrative-framework-sms

| Propriedade | Valor |
|---|---|
| **Gatilho** | Antes do processo de criação, quando ângulo não está definido |
| **Input mínimo** | Tema + formato (carrossel / thread / reel / post longo) |
| **Output** | 5 opções modeladas com hook escrito + arco resumido + melhor quando + risco |
| **Escolha** | Usuário escolhe A/B/C/D/E → skill gera briefing estruturado |
| **Contrato** | Hook aprovado é ponto de partida obrigatório — skill não substitui |
| **Não substitui** | Julgamento criativo da skill — apenas define o ângulo de entrada |

#### PASSO 1 — Gate de Voz

| Propriedade | Valor |
|---|---|
| **Gatilho** | Sempre executa primeiro, antes do Passo 2 |
| **Fonte primária** | `clients/[cliente-ativo]/production-rules.md` → seção `00-B \| PADRÕES DE AUSÊNCIA DE VOZ` |
| **Fallback** | Padrões universais proibidos (8 categorias, definidos no SKILL.md) |
| **Escopo** | Varredura completa do copy — não por parágrafo |
| **Ação em caso de falha** | Reescrever todo o trecho contendo a violação (não apenas a palavra) |
| **Limite** | Tolerância zero — qualquer violação bloqueia a entrega |

**Padrões universais proibidos (8 categorias):**

| # | Padrão | Regra de substituição |
|---|---|---|
| 1 | Adjetivo sem dado ("incrível", "robusto", "transformador") | Substituir por evidência concreta, número ou resultado específico |
| 2 | CTA vago ("saiba mais", "descubra", "clique aqui") | Especificar exatamente o que o leitor recebe |
| 3 | Abertura centrada na marca ("Nós somos" / "A [marca] é") | Reescrever em voz ativa, primeira pessoa, fato concreto |
| 4 | Tríade abstrata ("clareza, consistência e resultado") | Escolher um. Ser específico sobre ele. |
| 5 | Pergunta retórica sem resposta real | Converter em afirmação ou desenvolver a resposta no corpo |
| 6 | Prelúdio de anúncio ("Estamos animados em anunciar") | Começar direto com o anúncio |
| 7 | Jargão sem contexto técnico ("sinergia", "ecossistema") | Nomear o que concretamente acontece entre as partes |
| 8 | Fechamento motivacional genérico ("leve seu sucesso a sério") | Nomear a ação específica que produz o resultado prometido |

---

#### PASSO 2 — Gate de Padrões IA

**Arquitetura de tiers:**

| Tier | Condição de gatilho | Ação |
|---|---|---|
| **Tier 1** | Qualquer ocorrência isolada em qualquer parte do copy | Reescrever automaticamente a frase/sentença que contém |
| **Tier 2** | 2 ou mais palavras Tier 2 no mesmo parágrafo | Reescrever automaticamente o parágrafo inteiro |
| **Tier 3** | 3 ou mais palavras Tier 3 em qualquer janela de 200 palavras | Revisar a seção mais concentrada; reescrever se a densidade é semanticamente redundante |

**Unidade de varredura:**
- Tier 1: copy completo (output inteiro)
- Tier 2: por parágrafo (definido como bloco de texto separado por linha em branco)
- Tier 3: janela deslizante de 200 palavras

---

#### PASSO 3 — Gate de Decisão

| Condição | Ação | Visibilidade para o usuário |
|---|---|---|
| Todos os 3 passos APROVADOS | Entregar copy | Silencioso (embutido) / Relatório completo (standalone) |
| Qualquer passo REPROVADO (rodada 1) | Reescrever trecho com falha → re-executar os 3 passos | Reescrita silenciosa |
| Qualquer passo REPROVADO (rodada 2) | Entregar se aprovado; mostrar ao usuário se ainda falhar | Mostrar o trecho específico com falha + pedir direcionamento |

**Limite de reescrita:** Máximo 2 rodadas de reescrita automática por entrega. Evita loops infinitos em trechos genuinamente difíceis.

---

### 2.6 Biblioteca de Padrões

#### Tier 1 — Sempre reescrever

**Inglês:**
`delve` · `landscape` (metafórico) · `tapestry` · `realm` (metafórico) · `paradigm` · `embark` (metafórico) · `beacon` · `testament to` · `robust` · `comprehensive` · `cutting-edge` · `leverage` (como verbo) · `pivotal` · `meticulous` · `seamless` · `game-changer` · `utilize` · `groundbreaking` · `revolutionize` · `transformative` · `in conclusion` · `it's important to note` · `I need to emphasize` · `at the end of the day` · `think outside the box` · `move the needle` · `circle back` · `synergize` · `touch base` · `take it to the next level` · `deep dive` (como verbo) · `unpack` (como verbo) · `holistic approach` · `value-add` · `proactive` · `best-in-class` · `world-class` · `state-of-the-art` · `innovative solution` · `nuanced approach` · `foster growth` · `elevate your` · `deeply` · `truly` · `fundamentally` · `inherently` · `inevitably` · `simply` (como intensificador)

**Português:**
`transformador` · `revolucionário` · `robusto` · `abrangente` · `de ponta` · `alavancar` (como verbo) · `crucial importância` · `em conclusão` · `é importante ressaltar` · `é fundamental notar` · `sinergia` (sem contexto técnico) · `pensar fora da caixa` · `mergulho profundo` (como verbo) · `empoderar` · `potencializar` (quando há forma mais simples) · `solução inovadora` · `abordagem holística` · `fomentar o crescimento` · `elevar sua experiência` · `sem precedentes` (quando não há dado que comprove) · `profundamente` · `verdadeiramente` · `fundamentalmente` · `inerentemente` · `inevitavelmente` · `simplesmente` (como intensificador)

---

#### Tier 2 — Reescrever se 2+ no mesmo parágrafo

**Inglês:**
`harness` · `navigate` (metafórico) · `foster` · `elevate` · `unleash` · `streamline` · `empower` · `bolster` · `spearhead` · `resonate` · `nuanced` · `crucial` · `ensure` · `ecosystem` (não-técnico) · `journey` (metafórico) · `landscape` · `framework` (como buzzword) · `drive` (metáfora de negócio) · `unlock potential` · `leverage insights` · `really` · `just` · `honestly` · `actually` · `basically` · `literally` (quando não-literal)

**Português:**
`impulsionar` · `navegar` (metafórico) · `fomentar` · `elevar` · `desbloquear` · `otimizar` (sem contexto técnico) · `capacitar` · `fortalecer` · `liderar iniciativas` · `ressoar` · `sutil` (quando genérico) · `garantir` (sentido marketeiro) · `ecossistema` · `jornada` (metafórico) · `trilhar` · `desempenhar papel fundamental` · `catalisar` · `realmente` · `apenas` · `honestamente` · `basicamente` · `literalmente` · `genuinamente`

---

#### Tier 3 — Revisar se 3+ por 200 palavras

**Inglês:**
`significant` · `innovative` · `effective` · `dynamic` · `scalable` · `compelling` · `unprecedented` · `impactful` · `actionable` · `strategic` · `unique` · `powerful` · `engaging` · `exciting` · `essential` · `optimal` · `achieve` · `enhance` · `deliver` · `solution` · `expertise` · `commitment` · `dedicated` · `passionate` · `seamlessly`

**Português:**
`significativo` · `inovador` · `eficaz` · `dinâmico` · `escalável` · `impactante` · `sem precedentes` · `acionável` · `estratégico` · `único` · `poderoso` · `engajante` · `empolgante` · `essencial` · `ótimo` · `alcançar` · `aprimorar` · `entregar` · `solução` · `expertise` · `comprometimento` · `dedicado` · `apaixonado`

---

### 2.7 Detectores de Padrão Estrutural

13 padrões estruturais que sinalizam origem IA independentemente do vocabulário:

| # | Padrão | Limite de detecção | Correção |
|---|---|---|---|
| 1 | **Excesso de em-dash** (—) | > 2 no mesmo post/slide | Substituir por vírgula, dois-pontos ou reescrever a frase |
| 2 | **Excesso de negrito** | > 30% das frases em negrito | Remover negrito de frases não-críticas |
| 3 | **Comprimento uniforme de parágrafos** | Todos os parágrafos com 2-3 linhas exatas | Variar: misturar ritmo 1 linha, 3 linhas, 1 linha |
| 4 | **Bullets apenas com substantivos** | "• Eficiência • Inovação • Resultados" | Converter para frases de ação com verbo no início |
| 5 | **Atribuições vagas** | "Estudos mostram…", "Especialistas dizem…" | Citar a fonte específica ou remover a atribuição |
| 6 | **Aberturas com "Vamos…"** | No início de parágrafo ou seção | Substituir por imperativo direto ou afirmação |
| 7 | **Disclaimers de encerramento** | "Observe que isso é apenas…", "Sempre consulte…" | Remover — confiar no leitor |
| 8 | **Acumulação de hashtags** | 10+ hashtags idênticas em todos os posts | Variar ou reduzir à especificação da plataforma |
| 9 | **Emoji em títulos profissionais** | Qualquer emoji em título profissional | Remover do LinkedIn, decks e copy formal |
| 10 | **Contraste binário performático** | "Não é X. É Y." / "Not X. But Y." usado como gancho sem desenvolvimento | Afirmar o ponto diretamente sem o dispositivo binário |
| 11 | **Fragmentação estacato dramática** | Frases de 3–5 palavras acumuladas. Uma após a outra. Sem progressão. | Fundir em frase completa com subordinação lógica |
| 12 | **Parágrafo abrindo com "So" ou "Então"** | Parágrafo ou seção iniciando com "So," ou "Então," | Reescrever com afirmação direta sem a conjunção de transição |
| 13 | **Wh- openers performáticos** | "Why does this matter?" / "What does this mean?" sem resposta imediata | Substituir pela afirmação que a pergunta tentava construir |

---

### 2.8 Pontos de Integração por Skill

| Skill | Narrative-framework | Limite do QA Gate | Ponto de invocação do copy-qa-sms | Escopo da varredura | Modo silencioso |
|---|---|---|---|---|---|
| **post-writer-sms** | Sim — antes do processo de criação | ≥ 90/100 | Após aprovação do QA Gate | Post completo (unidade única) | Sim |
| **thread-writer-sms** | Sim — antes do processo de criação | ≥ 90/100 | Após aprovação do QA Gate | Cada post da thread independentemente | Sim |
| **caption-writer-sms** | Não | ≥ 90/100 | Após aprovação do QA Gate | Legenda completa (unidade única) | Sim |
| **hook-writer-sms** | Não | Checklist (sem pontuação) | Após aprovação do Checklist de entrega | Cada variante de hook independentemente | Sim |
| **carousel-writer-sms** | Sim — ETAPA 0 (oferta ao usuário) | ≥ 90/100 | Substitui o Bloco 3 — Verificação de voz; executa ANTES do QA Gate | Cada slide independentemente; estrutural no nível do script completo | Sim |
| **content-repurposer-sms** | Não | ≥ 85/100 | Após aprovação do QA Gate | Cada derivado por plataforma independentemente | Sim |
| **video-script-sms** | Sim — MODO A apenas; não se aplica ao MODO B | ≥ 90/100 | Após aprovação do QA Gate | Todos os blocos de fala (copy falado) do roteiro | Sim |

**Nota sobre carousel-writer-sms:** O copy-qa-sms é executado como Bloco 3 ANTES da pontuação do QA Gate, e não depois. Isso porque o carrossel tem um checklist mais complexo com 3 blocos que precedem o score do QA Gate.

**Nota sobre narrative-framework-sms no carousel:** A skill oferece o framework ao usuário no início (ETAPA 0), mas não obriga — se o usuário já tem ângulo definido, prossegue diretamente.

---

### 2.9 Casos de Borda e Fallbacks

| Cenário | Comportamento |
|---|---|
| `production-rules.md` não existe para o cliente ativo | Passo 1 roda apenas com os padrões universais proibidos; sem erro |
| Cliente não tem seção `00-B` no `production-rules.md` | Passo 1 roda com padrões universais; avança para o Passo 2 |
| Palavra Tier 1 faz parte de uma citação técnica ou nome próprio | Julgamento contextual: se citando fonte externa, sinalizar mas não reescrever automaticamente; mostrar ao usuário |
| Mesma palavra aparece no Tier 1 e Tier 2 | Tier 1 tem precedência — reescrita automática em qualquer ocorrência |
| Copy está em idioma não coberto pelas listas de padrões | Aplicar apenas detectores estruturais; registrar no relatório que a varredura de vocabulário foi parcial |
| Reescrita introduz novo padrão Tier 1 | Re-executar Passo 2 apenas na seção reescrita; corrigir antes de prosseguir |
| Modo standalone sem plataforma especificada | Executar todas as verificações; sinalizar padrões estruturais específicos de plataforma como "revisar se [plataforma]" |
| hook-writer invocado por outra skill (thread-writer, post-writer) | O gate copy-qa-sms já foi aplicado pela skill chamadora — não executar novamente |
| narrative-framework-sms: usuário especificou ângulo explicitamente | Não acionar o seletor — executar diretamente com o ângulo dado |
| narrative-framework-sms: briefing já existe na conversa | Não acionar novamente — ler o briefing existente e executar |
| narrative-framework-sms: video-script MODO B | Não acionar — o framework é derivado do vídeo analisado |

---

## 3. Diagrama de Workflow {#workflow}

### 3.1 Fluxo Completo de Orquestração

```
SOLICITAÇÃO DO USUÁRIO
    │
    ▼
SKILL DE CRIAÇÃO ativada
(post-writer / thread-writer / caption-writer /
 hook-writer / carousel-writer / content-repurposer /
 video-script)
    │
    ▼
┌─────────────────────────────────────┐
│  VERIFICAÇÃO DE CONTEXTO             │
│  Lê .agents/social-media-context    │
│  Se ausente → Context Gate           │
│  (avisar → continuar ou redirecionar │
│  para social-media-context-sms)     │
└─────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────┐
│  GATE DE NARRATIVA                   │
│  (post-writer / thread-writer /      │
│   carousel-writer / video-script     │
│   MODO A)                            │
│                                      │
│  Briefing existe? → usar             │
│  Ângulo explícito? → executar direto │
│  Tema sem ângulo? →                  │
│    invocar narrative-framework-sms   │
│    aguardar escolha A/B/C/D/E        │
│    receber briefing → executar arco  │
└─────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────┐
│  PROCESSO DE CRIAÇÃO                 │
│  (específico por formato: pesquisa, │
│   hook, rascunho, formatação)       │
│  Hook aprovado = ponto de partida   │
│  obrigatório quando briefing existe │
└─────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────┐
│  QA GATE ESPECÍFICO DE FORMATO      │
│  Rubrica de pontuação por skill:    │
│  • post / thread / caption /        │
│    carousel / vídeo: ≥ 90/100       │
│  • repurposer: ≥ 85/100            │
│  • hook: checklist (sem pontuação)  │
│                                     │
│  SE REPROVAR → reescrever → repontar│
└─────────────────────────────────────┘
    │ APROVADO
    ▼
┌─────────────────────────────────────────────────────┐
│  GATE copy-qa-sms (PASSO 1 → PASSO 2 → PASSO 3)   │
│                                                      │
│  PASSO 1 — Gate de Voz                              │
│  ├─ Carregar production-rules.md → 00-B             │
│  ├─ Varrer copy completo por cada padrão proibido   │
│  └─ REPROVAR? → reescrever trecho → re-executar P1  │
│                          │ APROVADO                 │
│  PASSO 2 — Gate de Padrões IA                      │
│  ├─ Tier 1: varrer copy completo                    │
│  │   REPROVAR? → reescrever frase → continuar       │
│  ├─ Tier 2: varrer por parágrafo                    │
│  │   REPROVAR (2+ no parágrafo)? → reescrever      │
│  ├─ Tier 3: janela deslizante de 200 palavras       │
│  │   REPROVAR (3+ na janela)? → revisar e revisar   │
│  └─ Estrutural: 13 detectores de padrão             │
│       REPROVAR? → aplicar correção estrutural        │
│                          │ APROVADO                 │
│  PASSO 3 — Decisão                                  │
│  ├─ Tudo aprovado? → ENTREGUE                       │
│  └─ Alguma falha? → reescrever → re-executar 3 P    │
│       2ª tentativa aprovada? → ENTREGUE             │
│       2ª tentativa reprovada? → mostrar ao usuário  │
└─────────────────────────────────────────────────────┘
    │ APROVADO
    ▼
COPY FINAL → USUÁRIO
(Entrega silenciosa — sem exibir output do gate)
```

---

### 3.2 Fluxo Interno do copy-qa-sms (detalhe do Passo 2)

```
PASSO 2 — GATE DE PADRÕES IA
│
├─ VARREDURA TIER 1 (copy completo)
│   │
│   ├─ Para cada palavra/frase da lista Tier 1 (PT + EN):
│   │   ├─ Encontrada? → marcar para reescrita
│   │   └─ Não encontrada? → continuar
│   │
│   ├─ Reescritas aplicadas a todos os trechos marcados
│   └─ Avançar para Tier 2 no copy reescrito
│
├─ VARREDURA TIER 2 (por parágrafo)
│   │
│   ├─ Dividir copy em parágrafos (por linha em branco)
│   ├─ Para cada parágrafo:
│   │   ├─ Contar palavras Tier 2 presentes
│   │   ├─ Contagem = 0 ou 1? → OK
│   │   └─ Contagem ≥ 2? → reescrever parágrafo inteiro
│   └─ Avançar para Tier 3 no copy reescrito
│
├─ VARREDURA TIER 3 (densidade)
│   │
│   ├─ Contar palavras Tier 3 no copy completo
│   ├─ Aplicar janela deslizante de 200 palavras
│   ├─ Janela com < 3 palavras Tier 3? → OK
│   └─ Janela com ≥ 3 palavras Tier 3? → revisar seção mais concentrada
│
└─ VARREDURA ESTRUTURAL (copy completo)
    │
    ├─ Contar em-dashes: > 2 no post/slide? → corrigir
    ├─ Densidade de negrito: > 30% das frases? → reduzir
    ├─ Uniformidade de parágrafos: todos iguais? → variar
    ├─ Conteúdo dos bullets: só substantivos? → converter para frases com verbo
    ├─ Frases de atribuição: vagas? → citar ou remover
    ├─ Aberturas "Vamos…": presentes? → reescrever
    ├─ Disclaimers de encerramento: presentes? → remover
    ├─ Contagem de hashtags: > 10 mesmo conjunto? → variar
    ├─ Emoji em títulos: presentes? → remover
    ├─ Contraste binário ("Não é X. É Y."): presente sem desenvolvimento? → afirmar direto
    ├─ Fragmentação estacato: frases curtas acumuladas sem progressão? → fundir
    ├─ "So" / "Então" abrindo parágrafo: presente? → reescrever com afirmação direta
    └─ Wh- opener sem resposta imediata: presente? → substituir pela afirmação
```

---

### 3.3 Fluxo em Modo Standalone

```
USUÁRIO invoca copy-qa-sms diretamente
    │
    ├─ Com texto de copy existente
    │   ├─ Plataforma especificada? → executar todas as verificações com contexto de plataforma
    │   └─ Plataforma não especificada? → executar verificações; sinalizar específicos como "revisar se [plataforma]"
    │
    └─ Sem texto de copy
        └─ Solicitar: "Qual o copy e a plataforma-alvo?"

            │
            ▼
    Executar Passo 1 → Passo 2 → Passo 3

            │
            ▼
    Apresentar relatório completo de auditoria:
    ┌────────────────────────────────────────┐
    │ RELATÓRIO COPY QA — [data]             │
    │ Plataforma: [X]  Cliente: [Y]          │
    │                                        │
    │ PASSO 1 — VOZ                          │
    │ [✓ Aprovado | ⚠️ N problemas + antes/depois] │
    │                                        │
    │ PASSO 2 — PADRÕES IA                   │
    │ Tier 1: [resultado]                    │
    │ Tier 2: [resultado]                    │
    │ Tier 3: [resultado]                    │
    │ Estrutural: [resultado]                │
    │                                        │
    │ RESULTADO                              │
    │ [✅ Aprovado | ⚠️ N ajustes]           │
    │                                        │
    │ COPY FINAL                             │
    │ [copy reescrito, pronto para publicar] │
    └────────────────────────────────────────┘
```

---

## 4. Changelog e Versionamento {#changelog}

### copy-qa-sms

| Versão | Data | Alterações |
|---|---|---|
| 1.1.0 | 2026-07-14 | Integração stop-slop: +6 palavras Tier 1 EN (AI intensifiers: deeply, truly, fundamentally, inherently, inevitably, simply); +6 PT equivalentes. +6 palavras Tier 2 EN (weak adverbs: really, just, honestly, actually, basically, literally); +6 PT. +4 detectores estruturais (#10 contraste binário, #11 fragmentação estacato, #12 So/Então openers, #13 Wh- openers). Total: 9 → 13 detectores estruturais. |
| 1.0.0 | 2026-07-09 | Lançamento inicial. Protocolo de 3 passos: Gate de Voz + Gate de Padrões IA (Tier 1/2/3 + estrutural) + Decisão. Modos embutido e standalone. |

### narrative-framework-sms

| Versão | Data | Alterações |
|---|---|---|
| 1.0.0 | 2026-07-14 | Lançamento inicial. 5 frameworks (Value-Stack, Problem-Proof, Hack List, Rant Callout, Demo Walkthrough). Arcos por formato para carrossel, thread, reel/vídeo curto, post longo/artigo. Output: apresentação de 5 opções com hooks + briefing estruturado após escolha. |

### Skills Atualizadas

| Skill | De | Para | Data | Alteração |
|---|---|---|---|---|
| post-writer-sms | 1.3.0 | 1.4.0 | 2026-07-14 | Adicionado gate de Framework Narrativo: invoca narrative-framework-sms quando ângulo não está definido; usa briefing existente quando disponível |
| thread-writer-sms | 1.5.0 | 1.6.0 | 2026-07-14 | Adicionado gate de Framework Narrativo: invoca narrative-framework-sms quando ângulo não está definido; hook aprovado = Post 1 obrigatório |
| carousel-writer-sms | 2.1.0 | 2.2.0 | 2026-07-14 | ETAPA 0 atualizada: substituiu proposta de "3 ângulos" por oferta de narrative-framework-sms com formato=carrossel |
| video-script-sms | 1.2.0 | 1.3.0 | 2026-07-14 | Adicionado gate de Framework Narrativo antes de "Detecção de modo": aplica apenas ao MODO A (criação original); hook aprovado = cena 1 obrigatória (primeiros 3s) |
| post-writer-sms | 1.2.0 | 1.3.0 | 2026-07-09 | Substituiu "Bloco 2 — Verificação de ausências" pela referência ao gate copy-qa-sms |
| thread-writer-sms | 1.4.0 | 1.5.0 | 2026-07-09 | Removeu seção standalone "Verificação de Voz"; gate copy-qa-sms adicionado após QA Gate |
| caption-writer-sms | 1.2.0 | 1.3.0 | 2026-07-09 | Removeu Passo 8 do Processo de Escrita (verificação inline de voz); gate copy-qa-sms adicionado após QA Gate |
| hook-writer-sms | 1.2.0 | 1.3.0 | 2026-07-09 | Gate copy-qa-sms adicionado após Checklist de entrega; hooks apresentados apenas após aprovação do gate |
| carousel-writer-sms | 2.0.0 | 2.1.0 | 2026-07-09 | Bloco 3 reescrito como gate copy-qa-sms (executa antes do QA Gate, integrado ao checklist de 3 blocos) |
| content-repurposer-sms | 1.2.0 | 1.3.0 | 2026-07-09 | Seção "Verificação de Voz e QA Gate" fundida; gate copy-qa-sms adicionado após QA Gate ≥ 85 |
| video-script-sms | 1.1.0 | 1.2.0 | 2026-07-09 | Gate copy-qa-sms adicionado após QA Gate ≥ 90; cobre todos os blocos de fala (copy falado) |

---

### Decisões de Design

**Por que não embutir a lista Tier 1 em cada skill de criação?**
As listas de padrões são documentos vivos. Se "sutil" precisar ser promovido do Tier 2 para o Tier 1, uma única edição em `copy-qa-sms/SKILL.md` se propaga para todas as 7 skills. Embutir exigiria 7 edições síncronas com risco de divergência ao longo do tempo.

**Por que manter QA Gates específicos de formato em cada skill?**
Os critérios de formato são intrinsecamente diferentes. Um gate de carrossel pontua "virada ao slide correto" — sem sentido para um tweet. Um gate de thread pontua "ritmo entre posts" — irrelevante para uma legenda. Os gates específicos codificam conhecimento de craft que não se generaliza. O `copy-qa-sms` cuida do que se generaliza: voz, vocabulário de IA e estrutura.

**Por que modo silencioso quando embutido?**
O modelo mental do usuário é: "pedi um post e recebi um post." Mostrar a ele um output interno do gate — mesmo que verde — quebra esse modelo mental e gera sobrecarga cognitiva. O gate é infraestrutura, não interface.

**Por que o limite de 2 rodadas de reescrita?**
Loops infinitos são possíveis se um trecho é semanticamente difícil e cada reescrita introduz um novo padrão. O limite de 2 rodadas expõe o impasse ao usuário — que tem contexto de domínio que o modelo não tem — em vez de loopar silenciosamente ou entregar copy ruim.

**Por que o carrossel executa copy-qa-sms ANTES do QA Gate (enquanto todos os outros executam depois)?**
O Bloco 3 do carrossel (verificação de voz) já estava posicionado antes do QA Gate no fluxo original do checklist de 3 blocos. Substituí-lo pelo copy-qa-sms manteve a ordem arquitetural sem quebrar o fluxo existente. Para todas as outras skills, o copy-qa-sms segue o QA Gate de formato porque a integridade de formato é verificada primeiro, depois a integridade de voz/padrão IA.

**Por que o narrative-framework-sms é uma skill separada e não embutido em cada skill de criação?**
A decisão de ângulo narrativo é independente do formato. Os mesmos 5 frameworks se aplicam ao carrossel, thread, reel e post longo — apenas a unidade de execução muda (slide vs post vs cena vs parágrafo). Uma skill central garante que a modelagem seja idêntica independentemente de qual skill de criação a invoca, e que atualizações nos frameworks (novo framework, nova regra de calibração) se propaguem automaticamente para todas.

**Por que o narrative-framework-sms não decide — apenas apresenta?**
A escolha de ângulo é uma decisão estratégica, não operacional. O modelo tem a capacidade de modelar todos os 5 frameworks, mas não tem o contexto completo de audiência, timing, relacionamento do cliente com a marca e objetivos de curto prazo. O usuário tem. A skill apresenta as opções com hooks escritos (para que a escolha seja informada), mas a decisão final fica com quem tem contexto completo.

---

*Documento mantido em: `master-design-system/docs/copy-qa-orchestration/PRD-SPECS.md`*
*Versão visual: `master-design-system/docs/copy-qa-orchestration/PRD-SPECS.html`*
