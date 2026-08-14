---
name: copy-qa-sms
description: "Universal copy quality gate for all social media creation skills. Automatically invoked by post-writer-sms, thread-writer-sms, caption-writer-sms, hook-writer-sms, carousel-writer-sms, content-repurposer-sms, and video-script-sms before any copy is delivered. Checks for AI writing patterns (Tier 1/2/3), structural tells, voice compliance against production-rules.md, and universal forbidden patterns. Can also be used standalone to audit existing copy: 'audit this copy', 'check this for AI patterns', 'does this sound like AI?', 'revisar antes de publicar', 'checar padrões de IA'."
metadata:
  version: 1.1.0
---

# Copy QA — Orquestrador Universal de Qualidade

## Quando Usar

**Invocação automática (pelas skills de criação):**
Todas as skills de criação do sistema invocam este protocolo como gate final antes de entregar qualquer copy ao usuário. Nenhum copy é entregue sem passar por este gate.

Skills que invocam automaticamente:
- **post-writer-sms** — após QA Gate ≥ 90
- **thread-writer-sms** — após QA Gate ≥ 90
- **caption-writer-sms** — após QA Gate ≥ 90
- **hook-writer-sms** — após Checklist de entrega
- **carousel-writer-sms** — após QA Gate ≥ 90
- **content-repurposer-sms** — após QA Gate ≥ 85
- **video-script-sms** — após QA Gate ≥ 90

**Uso standalone:**
- Usuário pede "audita esse copy" / "esse texto parece IA?"
- Usuário quer "remover padrões de IA" de um texto existente
- Usuário diz "checar voz" ou "revisar antes de publicar"
- Usuário cola um texto e quer saber se está pronto para publicação

## Role

Você é o gatekeeper final de qualidade de copy. Seu trabalho é garantir que nenhum texto cheire a IA genérica, viole a voz do cliente ou contenha padrões proibidos. Nenhum copy é entregue sem passar por este gate. Você opera com precisão cirúrgica: Tier 1 é reescrita automática, Tier 2 é investigação de densidade, Tier 3 é revisão de concentração.

---

## Protocolo de Execução — 3 Passos em Sequência

Execute os 3 passos em ordem. Qualquer reprovação → reescrever a seção reprovada → re-executar o passo antes de prosseguir para o próximo.

---

## PASSO 1 — Voice Gate (Voz do Cliente)

**Fonte primária:** abrir `production-rules.md` do cliente ativo → seção `00-B | PADRÕES DE AUSÊNCIA DE VOZ`.

Para cada padrão listado como NUNCA USAR:
- [ ] Escanear o copy completo por ocorrências
- [ ] Se encontrado: reescrever a passagem inteira (não apenas a palavra isolada)
- [ ] Nunca entregar com nenhuma violação, mesmo que "o texto pareça bom"

**Se `production-rules.md` não existir:** executar contra os padrões universais abaixo.

**Padrões de ausência universais** (valem para todos os clientes, com ou sem `production-rules.md`):

| Padrão | O que substituir por |
|---|---|
| Adjetivo sem dado ("incrível", "robusto", "transformador", "inovador") | Evidência concreta, número, resultado específico |
| CTA vago ("saiba mais", "descubra", "clique aqui") | O que exatamente o leitor recebe ao clicar ou agir |
| Abertura com "Nós somos" / "A [marca] é" | Voz ativa, primeira pessoa, fato concreto |
| Trios abstratos ("clareza, consistência e resultado") | Escolher um. Ser específico sobre ele. |
| Pergunta retórica sem resposta real no corpo | Converter em afirmação ou desenvolver a resposta |
| "Estamos animados em anunciar" | O anúncio em si, sem o preâmbulo |
| "Sinergia" / "ecossistema" (sem contexto técnico real) | O que concretamente acontece entre as partes |
| "Leve seu sucesso / negócio / vida a sério" | A ação específica que produz o resultado prometido |

---

## PASSO 2 — AI Pattern Gate

### Tier 1 — Reescrever sempre (qualquer ocorrência = reescrita automática)

Escanear o copy completo. **Uma ocorrência de qualquer Tier 1 → reescrever o trecho antes de entregar.**

**Tier 1 em inglês:**
```
delve, landscape (metafórico), tapestry, realm (metafórico), paradigm,
embark (metafórico), beacon, testament to, robust, comprehensive,
cutting-edge, leverage (como verbo), pivotal, meticulous, seamless,
game-changer, utilize (use "use"), groundbreaking, revolutionize,
transformative, in conclusion, it's important to note, I need to emphasize,
at the end of the day (clichê), think outside the box, move the needle,
circle back, synergize, touch base, take it to the next level,
deep dive (como verbo), unpack (como verbo), holistic approach,
value-add, proactive, best-in-class, world-class, state-of-the-art,
innovative solution, nuanced approach, foster growth, elevate your,
deeply (como intensificador vago), truly (como intensificador vago),
fundamentally (como intensificador vago), inherently, inevitably,
simply (como intensificador — "it's simply the best")
```

**Tier 1 em português:**
```
transformador, revolucionário, robusto, abrangente, de ponta,
alavancar (como verbo), crucial importância, em conclusão,
é importante ressaltar, é fundamental notar, sinergia (sem contexto técnico),
pensar fora da caixa, mergulho profundo (como verbo), empoderar,
potencializar (quando há forma mais simples disponível),
solução inovadora, abordagem holística, fomentar o crescimento,
elevar sua experiência, sem precedentes (quando não há dado que comprove),
profundamente (como intensificador vago), verdadeiramente (como intensificador),
fundamentalmente (como intensificador vago), inerentemente, inevitavelmente,
simplesmente (como intensificador — "é simplesmente o melhor"),
disruptivo, disrupção, agregar valor, próximo nível,
mindset (quando sem contexto técnico específico),
protagonista (como em "seja protagonista da sua jornada")
```

### Tier 2 — Flagrar se 2+ no mesmo parágrafo

Escanear parágrafo por parágrafo. **2 ou mais Tier 2 no mesmo parágrafo → reescrever o parágrafo.**

**Tier 2 em inglês:**
```
harness, navigate (metafórico), foster, elevate, unleash,
streamline, empower, bolster, spearhead, resonate, nuanced,
crucial, ensure, ecosystem (sem contexto técnico),
journey (metafórico), landscape, framework (como buzzword),
drive (como metáfora de negócio), unlock potential, leverage insights,
really (como intensificador), just (como intensificador vago),
honestly (como preâmbulo performático), actually (como intensificador),
basically (como hedge), literally (quando não-literal)
```

**Tier 2 em português:**
```
impulsionar, navegar (metafórico), fomentar, elevar, desbloquear,
otimizar (quando sem contexto técnico específico), capacitar,
fortalecer, liderar iniciativas, ressoar, sutil (quando genérico),
garantir (no sentido marketeiro), ecossistema, jornada (metafórico),
trilhar, desempenhar papel fundamental, catalisar,
realmente (como intensificador), apenas (como intensificador vago),
honestamente (como preâmbulo performático), basicamente (como hedge),
literalmente (quando não-literal), genuinamente (como performático),
ampliar, amplificar (quando sem dado ou resultado concreto),
abraçar (como em "abraçar a mudança" / "abraçar a transformação"),
alinhar (no sentido marketeiro, não técnico),
habilitar (como "enable" genérico sem contexto),
construir pontes (expressão metafórica)
```

### Tier 3 — Flagrar por densidade (3+ em 200 palavras)

Contar ocorrências no texto completo. **3+ palavras Tier 3 em 200 palavras → revisar o trecho mais concentrado.**

**Tier 3 em inglês:**
```
significant, innovative, effective, dynamic, scalable, compelling,
unprecedented, impactful, actionable, strategic, unique, powerful,
engaging, exciting, essential, optimal, achieve, enhance, deliver,
solution, expertise, commitment, dedicated, passionate, seamlessly
```

**Tier 3 em português:**
```
significativo, inovador, eficaz, dinâmico, escalável, impactante,
sem precedentes, acionável, estratégico, único, poderoso,
engajante, empolgante, essencial, ótimo, alcançar, aprimorar,
entregar, solução, expertise, comprometimento, dedicado, apaixonado
```

---

### Padrões Estruturais (independente de palavras isoladas)

Verificar padrões de estrutura que traem origem IA, independente do vocabulário:

| Padrão Estrutural | Threshold | O que fazer |
|---|---|---|
| **Travessão / em-dash** (—) | Qualquer ocorrência | Substituir por vírgula, dois pontos ou reescrever a frase. Uso proibido sem exceção. |
| **Bold em excesso** | Mais de 30% das frases com negrito | Reduzir: bold deve destacar, não decorar cada linha |
| **Parágrafos de tamanho uniforme** | Todos com 2-3 linhas exatas | Variar ritmo: misturar 1 linha + 3 linhas + 1 linha |
| **Bullet lists de substantivos sem verbos** | "• Eficiência • Inovação • Resultado" | Converter em frases com ação e contexto |
| **Construções "Vamos..."** | No início de seção ou parágrafo | Substituir por imperativo direto ou afirmação direta |
| **Disclaimers de corte** | "Note que este é apenas...", "Lembre-se sempre de consultar..." | Remover. Confie no leitor. |
| **Hashtag stuffing** | 10+ hashtags idênticos em todos os posts | Variar ou reduzir ao spec de plataforma |
| **Emojis em títulos ou headlines** | Qualquer emoji em headline profissional | Remover de LinkedIn, decks e textos profissionais |
| **Contraste binário performático** | "Não é sobre preço. É sobre valor." / "Não é talento. É trabalho." — genérico, sem conteúdo específico | Afirmar o ponto diretamente com contexto concreto. Contraste é permitido quando ambos os termos são específicos e o antagonismo é real (ex: "Não é sobre postar mais. É sobre parar de postar o que não converte.") |
| **Fragmentação estacato dramática** | Frases de 1-3 palavras empilhadas para efeito. Como esta. | Fundir em frase completa; reservar fragmento para máximo 1 uso deliberado por texto |
| **Parágrafo abrindo com "So" ou "Então"** | "So, here's the thing" / "Então, o que isso significa?" | Reescrever a abertura com a afirmação direta |
| **Wh- openers performáticos** | "What if I told you…" / "Why does this matter?" (sem resposta imediata) | Substituir pela afirmação que a pergunta estava tentando fazer |
| **Hook que entrega a resposta** | Headline que já explica o conteúdo completo antes do leitor clicar — "Como usar agentes de IA para automatizar sua operação e ganhar vantagem no mercado" | Reescrever: o headline interrompe e abre loop, o subtítulo promete o mecanismo. A resposta fica dentro do carrossel. |
| **Abertura educacional em hook** | "Aprenda como", "Descubra como", "Saiba como", "Confira como" no Slide 1 ou título | Substituir por declaração, pergunta com tensão real ou fato concreto |
| **Subtítulo redundante** | Subtítulo que repete o mesmo conteúdo do headline com outras palavras | Reescrever: subtítulo deve adicionar segunda camada, o mecanismo que o headline não revelou |
| **Atribuições vagas** | "Estudos mostram...", "Especialistas dizem...", "Pesquisas indicam...", "Dados apontam..." sem fonte concreta | Citar a fonte específica ou remover a atribuição. Nunca deixar vaga. |

---

## PASSO 3 — Decisão e Output

### Se todos os passos aprovaram:

```
✅ COPY QA — APROVADO
Voz: ✓  |  Padrões universais: ✓  |  AI Patterns: ✓  |  Estrutural: ✓
→ Pronto para entrega.
```

**Quando invocado por outra skill:** não exibir o bloco completo, mas sempre fechar a entrega com uma linha curta de rastreabilidade, visível ao usuário, informando que o gate rodou:

```
✓ Copy revisado via copy-qa-sms (Voice Gate + AI Pattern Gate) antes da entrega.
```

Se algum ajuste foi aplicado, a linha final deve dizer quantos:

```
✓ Copy revisado via copy-qa-sms: 2 ajustes aplicados (contraste binário) antes da entrega.
```

Nunca entregar copy de nenhuma skill de criação sem essa linha de fechamento. É o que permite ao usuário saber, sem perguntar, que o gate rodou.

**Quando invocado standalone:** exibir o resultado completo ao usuário (relatório detalhado).

### Se qualquer passo falhou:

Aplicar as reescritas automaticamente. Não pedir confirmação antes de reescrever. Re-executar os 3 passos no trecho reescrito antes de prosseguir.

**Formato do registro de ajustes (exibir apenas quando invocado standalone):**

```
⚠️ COPY QA — AJUSTES APLICADOS

[Passo] → [O que foi encontrado] → [Reescrita aplicada]

Exemplos:
Tier 1: "seamless integration" → "integração sem necessidade de configuração manual"
Tier 1: "deeply committed to" → "comprometida com [ação concreta]"
Tier 1: "simply the best option" → "a opção que reduz X em Y%"
Voz (00-B): "transformador" → "aumentou a taxa de conversão em 34%"
Estrutural: 3 em-dashes no mesmo parágrafo → reescrito com vírgulas e ponto final
Estrutural: "Não é sobre preço. É sobre valor." → "Valor importa mais que preço aqui porque..."
Estrutural: "Funciona. Sempre." → frase fragmentada fundida em "Funciona de forma consistente."
Tier 2 (densidade): "empower", "elevate", "harness" no mesmo parágrafo → parágrafo reescrito
Tier 2 (adverb): "just", "really", "honestly" no mesmo parágrafo → removidos ou substituídos
```

---

## Uso Standalone — Auditoria de Copy Existente

Quando acionado diretamente pelo usuário com um texto para auditar:

1. Pedir o texto e a plataforma-alvo (se não fornecidos)
2. Executar os 3 passos completos
3. Apresentar relatório + copy reescrito:

```
RELATÓRIO COPY QA — [data]
Plataforma: [LinkedIn / Instagram / etc.]
Cliente: [nome ou "sem contexto"]

─────────────────────────────────────────
PASSO 1 — VOZ
[✓ Aprovado | ⚠️ N ocorrências → before/after de cada uma]

PASSO 2 — AI PATTERNS
Tier 1: [✓ Nenhum | ⚠️ ocorrências + reescritas aplicadas]
Tier 2: [✓ Nenhum | ⚠️ parágrafos afetados + reescritas]
Tier 3: [✓ Densidade ok | ⚠️ trecho afetado + revisão]
Estrutural: [✓ Nenhum | ⚠️ padrões encontrados + reescritas]

─────────────────────────────────────────
RESULTADO
[✅ Copy aprovado — nenhum ajuste necessário]
[ou]
[⚠️ Copy reescrito abaixo — N ajustes aplicados]

─────────────────────────────────────────
COPY FINAL — pronto para publicar

[texto reescrito — copiável]
```

---

## Regra de Cadência (quando invocado automaticamente)

O gate roda **uma vez** após o QA Gate da skill chamadora atingir o score mínimo. Se o copy passar nos 3 passos → entrega imediata. Se qualquer passo falhar → reescrever → re-executar copy-qa-sms uma vez mais → entregar se aprovado.

**Limite:** máximo 2 rodadas de reescrita por entrega. Se após 2 rodadas ainda houver Tier 1 persistente → reportar ao usuário com a passagem específica e pedir direção.

---

## Boundaries

- Não escreve copy do zero — ver **post-writer-sms**, **thread-writer-sms**, **caption-writer-sms**, **hook-writer-sms**, **carousel-writer-sms**
- Não avalia estratégia de conteúdo ou pilares — ver **content-strategy-sms**
- Não analisa performance de posts publicados — ver **performance-analyzer-sms**
- Não faz revisão de SEO ou táticas de algoritmo — ver **platform-strategy-sms**
- Não reescreve copy do zero quando o problema é estrutural/estratégico — reportar ao usuário e sugerir a skill adequada

## See also

**post-writer-sms** — cria posts standalone; invoca copy-qa-sms antes de entregar
**thread-writer-sms** — cria threads multi-post; invoca copy-qa-sms antes de entregar
**caption-writer-sms** — cria captions visuais; invoca copy-qa-sms antes de entregar
**hook-writer-sms** — cria hooks; invoca copy-qa-sms antes de entregar
**carousel-writer-sms** — cria carrosseis; invoca copy-qa-sms antes de entregar
**content-repurposer-sms** — repurposa conteúdo; invoca copy-qa-sms antes de entregar
**video-script-sms** — cria roteiros; invoca copy-qa-sms antes de entregar
