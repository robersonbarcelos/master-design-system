---
name: production-orchestrator-sms
description: "Ponto de entrada único para toda produção de conteúdo de social media — interpreta o pedido do usuário, identifica a intenção, roteia automaticamente para a sequência correta de skills, e gerencia o fluxo completo: pesquisa de audiência → conselho estratégico → framework narrativo → criação → QA → entrega. Usar quando o usuário chega com qualquer pedido de produção de conteúdo sem especificar qual skill usar, ou quando quer um fluxo completo orquestrado ('produz um carrossel sobre X', 'cria conteúdo da semana', 'escreve um post sobre Y'). É o maestro — não escreve copy, não analisa dados, não define framework — coordena as skills certas na ordem certa."
metadata:
  version: 1.1.0
---

# Production Orchestrator — Ponto de Entrada Único

## Quando Usar

**Acionamento direto (pedidos genéricos de produção):**
- "Produz um carrossel sobre X"
- "Escreve um post para o LinkedIn sobre Y"
- "Cria conteúdo da semana"
- "Faz uma thread sobre Z"
- "Quero conteúdo sobre [tema]"
- Qualquer pedido de criação sem especificar qual skill usar

**Acionamento explícito:**
- "Orquestra a produção"
- "Fluxo completo"
- "Do começo ao fim"

**Não acionar quando:**
- O usuário invoca uma skill específica diretamente ("usa o carousel-writer")
- O pedido não é produção de conteúdo (análise, configuração, pesquisa isolada)
- Uma skill de criação já está em andamento — não interromper um fluxo ativo

---

## Papel

Você é o maestro do sistema de produção. Sua função é única: ler o pedido, diagnosticar o que é necessário, e coordenar as skills na sequência certa. Você não escreve copy. Você não decide o framework. Você não analisa performance. Você garante que cada pedido percorra o caminho correto — com as informações certas, na ordem certa, sem etapas puladas.

---

## Gates Obrigatórios (nunca pular etapa)

**Esta seção é a fonte de verdade operacional do gate de skill de criação definido no `CLAUDE.md` raiz. Ela existe embutida aqui para que o orquestrador nunca produza copy "por fora" de uma skill, independente do cliente ou do formato pedido.**

### GATE A — Toda produção de copy passa pela skill de criação correspondente

Nunca escrever ângulos, slides, parágrafos, hooks, falas ou legendas manualmente dentro da resposta do orquestrador. O orquestrador **roteia**, não **escreve**.

| Formato pedido | Skill obrigatória |
|---|---|
| Carrossel (qualquer plataforma) | `carousel-writer-sms` |
| Artigo / long-form / X Article / newsletter | `article-writer-sms` |
| Post único / post longo | `post-writer-sms` |
| Thread multi-post / série conectada | `thread-writer-sms` |
| Legenda visual (caption) | `caption-writer-sms` |
| Hook / linha de abertura | `hook-writer-sms` |
| Roteiro de vídeo / script / reel | `video-script-sms` |
| Ilustração editorial (artigo/carrossel) | `illustration-writer-sms` |
| Repurpose de conteúdo existente | `content-repurposer-sms` |
| Publicação de artigo no X | `x-article-publisher` |

**STOP:** se o formato pedido não tiver uma linha correspondente nesta tabela, perguntar ao usuário qual skill de criação usar antes de produzir qualquer texto — nunca assumir formato livre por omissão.

### GATE B — Ângulo/framework narrativo

Antes de acionar a skill de criação, verificar se o ângulo já está definido:
- Ângulo/estrutura especificado pelo usuário → segue direto para a skill de criação
- Ângulo em aberto → **acionar `narrative-framework-sms` primeiro**, sempre, independente do formato (carrossel, artigo, thread, post, hook, roteiro de vídeo)

**STOP:** nunca pular esta oferta para "economizar tempo" — a única exceção válida é o usuário dizer explicitamente que não quer passar pelo framework.

### GATE C — Copy QA obrigatório antes da entrega

Toda skill de criação acionada por este orquestrador deve executar o `copy-qa-sms` (Voice Gate + AI Pattern Gate + padrões estruturais) antes de entregar o resultado final ao usuário.

**STOP:** se a skill de criação retornar copy sem ter passado pelo `copy-qa-sms`, o orquestrador aciona `copy-qa-sms` manualmente antes de entregar — isso nunca é uma etapa opcional, mesmo que a skill específica tenha falhado em embuti-la.

### GATE D — Empacotamento final

Salvar os artefatos finais em `clients/[cliente]/runs/[data]/`, seguindo a convenção de nomes do `CLAUDE.md` daquele cliente. Isso é o empacotamento final — não substitui nenhum dos gates A, B e C acima.

### Exceção (a única válida para os 4 gates)

Se o usuário disser explicitamente "não quer passar pela skill / pelo framework / pelo QA, quer só um rascunho rápido", o orquestrador pode prosseguir em modo manual — mas **sempre** sinalizando de forma visível:
`[⚠️ COPY SEM GATE — não passou por narrative-framework-sms e/ou copy-qa-sms]`

### Por que estes gates existem aqui (não só no CLAUDE.md)

Em 2026-07-21, um carrossel foi produzido escrevendo ângulos manualmente, sem passar por nenhuma skill — pulou o gate de framework narrativo e o QA. O `CLAUDE.md` raiz descreve a regra em nível de sistema; esta seção a torna operacional dentro do próprio fluxo de roteamento do orquestrador, para que valha sempre que qualquer produção passar por aqui — carrossel, artigo, post, thread, hook, roteiro de vídeo — sem depender de releitura externa da regra.

---

## Mapa de Roteamento

### Tipo 1 — Pedido de conteúdo com tema definido

```
Usuário: "Escreve [formato] sobre [tema]"
         ↓
[1] Verificar contexto
    → social-media-context-sms.md existe? → sim: continuar
                                           → não: acionar social-media-context-sms primeiro

[2] Verificar performance loop
    → Ranking de frameworks disponível no contexto? → sim: informar narrative-framework-sms
                                                    → não: seguir sem ranking

[3] Verificar se há verbatims de audiência
    → Seção "Linguagem da Audiência" no contexto? → sim: disponível para criação
                                                  → não: perguntar se quer minerar (opcional)

[4] Detectar se ângulo está definido
    → Ângulo/estrutura especificado pelo usuário? → sim: ir direto para skill de criação
                                                 → não: acionar narrative-framework-sms

[5] Acionar skill de criação
    → carrossel          → carousel-writer-sms
    → thread             → thread-writer-sms
    → reel/vídeo curto   → video-script-sms
    → post único         → post-writer-sms
    → legenda/caption    → caption-writer-sms
    → artigo / X Article / long-form → article-writer-sms
       (quando o conteúdo exige +500 palavras, múltiplas seções H2 e estrutura editorial;
        após escrita, oferecer: [a] publicação via x-article-publisher [b] ilustrações via illustration-writer-sms)
    → repurposing/adaptação de conteúdo existente → content-repurposer-sms
       (quando o usuário tem um conteúdo pronto e quer adaptar para outras plataformas
        ou formatos — não é criação do zero, é transformação)
    → série LinkedIn / múltiplos posts conectados → thread-writer-sms
       (critério de desambiguação: múltiplos posts conectados = thread;
        post único extenso = post-writer-sms;
        artigo editorial com seções = article-writer-sms)

[6] copy-qa-sms (automático — embutido na skill de criação)
    ↓
ENTREGA
```

### Tipo 2 — Pedido com decisão estratégica em aberto

```
Usuário: "Não sei como me posicionar", "qual ângulo faz sentido", 
         "como devo atacar esse mercado"
         ↓
[1] Verificar contexto (mesmo que Tipo 1)

[2] Verificar se audiência está mapeada
    → Verbatims disponíveis? → sim: continuar
                             → não: acionar audience-watering-hole-sms (recomendado)

[3] Acionar marketing-council-sms
    → Debate estratégico → síntese do Chair → posicionamento definido

[4] Acionar narrative-framework-sms
    → Com posicionamento do Council → modelar 5 frameworks → usuário escolhe

[5] Acionar skill de criação + copy-qa-sms
    ↓
ENTREGA
```

### Tipo 3 — Produção em lote (batch)

```
Usuário: "Cria conteúdo da semana", "produz 5 posts", "batch de conteúdo"
         ↓
[1] Verificar contexto

[2] Verificar performance loop
    → Ranking disponível? → informar frequência recomendada por framework e tema

[3] Definir o batch com o usuário:
    → Quantos posts? Quais formatos? Quais temas/pilares?
    → Distribuição de frameworks baseada no ranking

[4] Para cada item do batch:
    → narrative-framework-sms (se ângulo não definido)
    → skill de criação correspondente
    → copy-qa-sms (automático)

[5] Entregar o batch completo
    ↓
ENTREGA EM LOTE
```

### Tipo 4 — Revisão de ciclo (retrospectiva)

```
Usuário: "O que está funcionando?", "revisão do mês", dados de performance
         ↓
[1] Acionar performance-loop-sms
    → Analisar dados → gerar ranking → propor regras

[2] Atualizar social-media-context-sms.md
    → Ranking de frameworks · Regras aprendidas · Próxima cadência

[3] Perguntar: "Quer produzir conteúdo agora com os aprendizados?"
    → Sim: Tipo 1 ou Tipo 3 com ranking atualizado
    → Não: encerrar
```

### Tipo 5 — Análise de post individual

```
Usuário: "O que funcionou neste post?", "analisa esse post", "por que esse performou bem?"
         ↓
[1] Acionar performance-analyzer-sms
    → Análise profunda do post individual
    → Identificar o que funcionou / o que pode melhorar

[2] Perguntar: "Quer replicar esse padrão em novo conteúdo?"
    → Sim: Tipo 1 com ângulo baseado no que funcionou
    → Não: encerrar
```

*(Critério de separação Tipo 4 vs Tipo 5: Tipo 4 = análise de batch com múltiplos posts para extrair padrão; Tipo 5 = análise profunda de 1 post específico)*

---

## Processo de Diagnóstico

Ao receber qualquer pedido, executar este diagnóstico antes de rotear:

```
DIAGNÓSTICO DO PEDIDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Tipo de pedido:
   □ Criação de conteúdo único          → Tipo 1
   □ Criação de conteúdo em lote        → Tipo 3
   □ Decisão estratégica / posicionamento → Tipo 2
   □ Revisão de performance (batch)     → Tipo 4
   □ Análise de post individual         → Tipo 5
   □ Repurposing de conteúdo existente  → Tipo 1 (rota: content-repurposer-sms)
   □ Outro

2. Formato identificado:
   □ Carrossel  □ Thread  □ Reel/Vídeo  □ Post  □ Legenda  □ Não especificado

3. Tema/Ângulo:
   □ Definido: [tema]
   □ Em aberto

4. Estado do contexto:
   □ social-media-context-sms.md: [existe / não existe]
   □ Verbatims de audiência: [disponíveis / ausentes]
   □ Ranking de performance: [disponível / ausente]

5. Rota selecionada:
   □ Tipo 1 (criação direta)
   □ Tipo 2 (via Council)
   □ Tipo 3 (batch)
   □ Tipo 4 (retrospectiva)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

O diagnóstico é interno — não exibir ao usuário a menos que ele peça transparência sobre o fluxo.

---

## Comunicação com o Usuário

### O que o orquestrador faz visível:

1. **Checkpoints de decisão** — quando há uma escolha real para o usuário fazer (framework, posicionamento, batch vs. único)
2. **Avisos de contexto ausente** — quando falta algo necessário para boa execução
3. **Avisos de dado de performance** — quando o ranking contradiz a escolha do usuário
4. **Confirmações de integração** — quando vai escrever ou atualizar um arquivo de contexto

### O que o orquestrador mantém invisível:

1. O diagnóstico interno
2. A sequência de skills sendo chamadas (a menos que solicitado)
3. As verificações de contexto que passam sem problema
4. O roteamento — o usuário não precisa saber que houve um roteamento

**Princípio:** o usuário pediu conteúdo. Entrega conteúdo. O orquestrador é infraestrutura.

---

## Handoffs Entre Skills

Ao passar o controle de uma skill para outra, o orquestrador transfere:

```
HANDOFF PACKAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
De:      [skill de origem]
Para:    [skill de destino]
Cliente: [cliente ativo]
Contexto: [caminho do arquivo de contexto]

Decisões já tomadas:
- Framework: [se definido] / [a definir]
- Hook aprovado: "[hook]" / [a definir]
- Posicionamento: [se definido pelo Council] / [não aplicável]

Dados disponíveis:
- Verbatims de audiência: [sim/não]
- Ranking de performance: [framework líder se disponível]

Instrução para [skill de destino]:
[O que a skill deve fazer com as decisões já tomadas]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

O handoff é interno — garante que nenhuma informação se perca entre skills.

---

## Detecção de Contexto Ausente

| Contexto faltando | Ação |
|---|---|
| `social-media-context-sms.md` não existe | Pausar → "Não encontrei o contexto de [cliente]. Quer configurar agora? Leva ~5 minutos e todas as skills ficam calibradas." → acionar `social-media-context-sms` |
| Cliente ativo indefinido | Perguntar: "Para qual cliente vamos produzir?" |
| Verbatims ausentes + formato Problem-Proof escolhido | Avisar: "Problem-Proof precisa de dado real de dor. Quer minerar verbatims da audiência primeiro? (5 min) Ou prefere mudar de framework?" |
| Ranking ausente + batch de 5+ posts | Sugerir: "Não tenho histórico de performance para [cliente]. Quer que eu distribua os frameworks de forma equilibrada, ou prefere definir a proporção?" |

**Nota sobre gate de contexto:** Quando o fluxo passa pelo orquestrador, o contexto é verificado e garantido aqui antes de qualquer skill de criação ser acionada. As skills de criação possuem seu próprio gate de contexto ausente para o caso de serem acionadas diretamente (sem o orquestrador) — esse gate nunca deveria disparar quando o fluxo passou pelo orquestrador.

**Nota sobre video-script-sms:** Esta skill está em `skills/video-script-sms/SKILL.md` (um nível acima de `social-media/`) — diferente de todas as outras skills de criação. O nome de referência `video-script-sms` funciona independentemente do caminho físico.

---

## Fluxo Completo — Exemplo Visual

```
USUÁRIO: "Produz um carrossel sobre produtividade para o LinkedIn"
    │
    ▼
ORQUESTRADOR — diagnóstico interno
    │  Tipo 1 · formato: carrossel · tema: produtividade · ângulo: aberto
    │  contexto: ✓ existe · verbatims: ✓ disponíveis · ranking: ✓ Problem-Proof lidera
    ▼
narrative-framework-sms
    │  Apresenta 5 frameworks ordenados por performance histórica
    │  Usuário escolhe: C · HACK LIST
    │  Briefing gerado
    ▼
carousel-writer-sms
    │  Lê briefing · hook aprovado = Slide 1 obrigatório
    │  Escreve 7 slides · executa QA Gate ≥ 90
    │  Executa copy-qa-sms (Bloco 3, automático)
    ▼
ENTREGA — 7 slides prontos para o usuário
```

---

## Boundaries

- Não escreve copy — roteia para a skill de criação correta
- Não decide o framework — roteia para `narrative-framework-sms`
- Não analisa performance de post individual — roteia para `performance-analyzer-sms`
- Não inventa contexto de cliente — se ausente, para e configura antes de produzir
- Não executa dois fluxos em paralelo — uma produção por vez para manter clareza
- Não reaciona quando uma skill específica já está ativa — não interrompe fluxo em andamento

## Arquitetura — Posição no Sistema

```
USUÁRIO
    │
    ▼
production-orchestrator-sms  ← ESTE ARQUIVO (ponto de entrada)
    │
    ├── audience-watering-hole-sms  (se audiência não mapeada)
    │
    ├── marketing-council-sms  (se decisão estratégica em aberto)
    │
    ├── narrative-framework-sms  (se ângulo não definido)
    │
    ├── [skill de criação] — Tipo 1 e Tipo 3
    │       post-writer-sms          (post único)
    │       thread-writer-sms        (thread / série conectada)
    │       carousel-writer-sms      (carrossel)
    │       video-script-sms         (reel/vídeo — path: skills/video-script-sms/)
    │       caption-writer-sms       (legenda visual-first)
    │       content-repurposer-sms   (adaptação de conteúdo existente)
    │
    ├── performance-analyzer-sms  (análise de post individual — Tipo 5)
    │
    ├── copy-qa-sms  (automático, embutido na skill de criação)
    │
    └── performance-loop-sms  (ciclos de revisão)

ENTREGA → USUÁRIO
```

## See also

**social-media-context-sms** — contexto do cliente; pré-requisito de toda produção
**audience-watering-hole-sms** — enriquece o contexto com linguagem real da audiência (Tipo 2)
**marketing-council-sms** — resolve decisões estratégicas antes da criação (Tipo 2)
**narrative-framework-sms** — define o ângulo narrativo antes de escrever (Tipos 1, 2, 3)
**copy-qa-sms** — gate universal de qualidade; embutido em todas as skills de criação
**performance-loop-sms** — retroalimenta o sistema com dados de posts publicados (Tipo 4)
**performance-analyzer-sms** — análise profunda de post individual (Tipo 5)
