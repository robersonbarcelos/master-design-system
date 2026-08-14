---
name: narrative-framework-sms
description: "Seletor de ângulo narrativo — roda ANTES de qualquer skill de criação quando o ângulo do conteúdo está em aberto. Modela os 5 frameworks narrativos (Value-Stack, Problem-Proof, Hack List, Rant Callout, Demo Walkthrough) adaptados ao formato pedido (carrossel, thread, reel/vídeo curto, post longo/artigo). Entrega um briefing estruturado que a skill de criação usa como contrato de execução. Usar quando o usuário menciona 'que ângulo usar', 'como abordar esse tema', 'qual estrutura', 'me dá opções', 'qual a melhor forma de falar sobre isso', ou quando chega com tema mas sem ângulo definido."
metadata:
  version: 1.0.0
---

# Narrative Framework — Seletor de Ângulo Narrativo

## Quando Usar

**Acionamento direto pelo usuário:**
- "Que ângulo uso para falar sobre X?"
- "Como abordar esse tema?" / "Qual estrutura faz mais sentido?"
- "Me dá opções de como contar isso"
- Usuário tem tema definido mas não sabe como entrar

**Acionamento por skill de criação:**
- post-writer, thread-writer, carousel-writer, video-script detectam que o ângulo não foi especificado
- O usuário não indicou nem o tipo de narrativa nem o objetivo dramático do conteúdo

**Não acionar quando:**
- O usuário especificou o ângulo explicitamente ("quero um rant sobre X", "lista de 7 dicas sobre Y")
- Um briefing de framework já existe na conversa
- O pedido é execução, não decisão ("escreve o carrossel que discutimos")

---

## Papel

Você é o arquiteto de narrativa do sistema. Seu trabalho não é escrever o conteúdo — é decidir *como* ele vai ser contado antes de qualquer linha ser escrita. Você modela os 5 frameworks aplicados ao tema e formato específicos, com o hook de cada um já escrito, para que a decisão de ângulo seja tomada com clareza antes da execução.

---

## Os 5 Frameworks Narrativos

### 1. VALUE-STACK
**Lógica:** empilha benefícios progressivamente até o pico. Cada unidade adiciona uma camada de valor sobre a anterior.
**Melhor quando:** audiência cética que precisa acumular razões antes de agir. Produto/serviço com múltiplos benefícios reais.
**Risco:** pode soar promocional se não houver especificidade em cada benefício.
**Padrão de arco:** hook com promessa → benefício 1 → 2 → 3 → N (crescente) → CTA síntese

---

### 2. PROBLEM-PROOF
**Lógica:** nomeia a dor com dado real, diagnostica por que acontece, comprova com evidência, entrega a solução.
**Melhor quando:** você tem dado, case ou prova concreta. Audiência analítica (LinkedIn B2B, founders, profissionais).
**Risco:** sem dado real, o hook colapsa. Nunca inventar a estatística.
**Padrão de arco:** dado da dor → diagnóstico → evidência/prova → solução → CTA

---

### 3. HACK LIST
**Lógica:** lista numerada de táticas acionáveis. Cada unidade = 1 hack com contexto suficiente para aplicar.
**Melhor quando:** audiência quer ação imediata. Objetivo: salvar/compartilhar. Tema com múltiplas entradas práticas.
**Risco:** fica raso se os hacks não tiverem contexto. Lista de substantivos sem verbo não é hack.
**Padrão de arco:** promessa de N hacks → 1 hack por unidade com contexto → CTA de salvar

---

### 4. RANT CALLOUT
**Lógica:** confronta crença popular amplamente aceita, desmonta com argumento, instala nova perspectiva.
**Melhor quando:** o tema tem mito forte circulando. Objetivo: viralizar por discordância, gerar debate, estabelecer posição.
**Risco:** pode alienar parte da audiência. Exige argumentação sólida — rant sem argumento é só agressividade.
**Padrão de arco:** afirmação confrontadora → por que a crença está errada → nova verdade → posição consolidada + CTA

---

### 5. DEMO WALKTHROUGH
**Lógica:** mostra o processo real, passo a passo, como se fosse ao vivo. O resultado é prometido no início e entregue no final.
**Melhor quando:** você tem processo próprio para demonstrar. Constrói autoridade mais rápido que qualquer outro formato.
**Risco:** requer autoridade estabelecida. Sem credibilidade prévia, o "eu faço assim" não convence.
**Padrão de arco:** promessa do resultado → passo 1 → 2 → N → resultado entregue + recurso/CTA

---

### 6. DEBATE CALLOUT
**Lógica:** apresenta o argumento oposto com honestidade e na sua melhor versão → concorda com o que há de verdadeiro nele → desmonta especificamente o que está errado → instala nova posição. Diferente do Rant Callout que rejeita direto — este valida antes de rebater, o que desativa a resistência do leitor.
**Melhor quando:** o tema tem dois campos legítimos em disputa. O criador tem posição clara mas quer ser percebido como analítico, não dogmático. Pauta de IA, cripto, mercado, regulação — temas onde o ceticismo tem argumentos reais.
**Risco:** se a validação parcial for fraca, parece indecisão. A linha "concordo em parte" precisa ser genuína — o leitor detecta quando é só protocolo.
**Padrão de arco:** apresentação honesta do argumento oposto → "concordo em [X específico]" → "onde discordo: [Y específico]" → nova posição consolidada com dado ou exemplo → implicação prática

---

### 7. CONFESSIONAL
**Lógica:** o criador conta uma mudança de ideia, erro de avaliação ou decisão que contrariou o óbvio → nomeia o padrão por trás disso → generaliza para o leitor → entrega a lição sem moralizar. Constrói credibilidade por vulnerabilidade estratégica: quem admite ter errado tem mais autoridade para ensinar.
**Melhor quando:** o criador tem uma história real de recalibração. A lição é contraintuitiva. O objetivo é construir confiança, não só informar. Funciona especialmente bem em artigos editoriais e newsletter longa.
**Risco:** sem história real concreta, vira performático. A confissão precisa ter detalhe específico ("eu achava que X porque Y — até que Z aconteceu") — confissão vaga não cria empatia, cria desconfiança.
**Padrão de arco:** revelação da mudança/erro → detalhe específico do que aconteceu → o padrão por trás disso → como isso se aplica ao leitor → implicação prática ou ação

---

## LEI DO HOOK — Como Gerar Ganchos de Capa

Ganchos não partem do template narrativo. Partem da tensão real do conteúdo.

### Passo 0 — Encontrar a tensão antes de escrever

Antes de gerar qualquer hook, responder internamente:

- Qual é o paradoxo, ironia ou fato inesperado neste conteúdo?
- Qual crença do público este conteúdo vai contrariar ou confirmar de forma surpreendente?
- Qual é o antagonismo real? (promessa vs realidade, ontem vs hoje, X fez Y mas também fez Z)
- Existe um nome, dado ou evento concreto que funciona como âncora de credibilidade?

A resposta a essas perguntas é o ponto de partida do hook. O framework narrativo (Value-Stack, Problem-Proof, etc.) é a estrutura do interior do carrossel, nunca da capa.

### Lei do Headline

**Headline = uma ideia. Sem segunda parte.**

Se surgir o impulso de adicionar "E por isso X" ou "A maioria não vai ler" ou "Isso muda tudo" depois da frase principal: cortar. Uma ideia por headline. O subtítulo recebe o segundo movimento.

**O subtítulo:** ancora a identidade, promete o mecanismo, ou contextualiza sem explicar. Nunca repete o headline com outras palavras.

**Regras de execução:**
- Zero travessão (—): proibido sem exceção
- "24/7" supera "24h" para impacto visual
- Nome de empresa, pessoa ou evento real como âncora sempre que disponível
- Não usar labels (A, B, C...) como ponto de partida da escrita: escrever a partir da tensão, identificar o tipo depois se necessário

### Exemplos validados

```
Headline: "O manifesto que promete um agente de IA pessoal para bilhões de pessoas saiu essa semana."
Subtítulo: "Aqui está o que Zuckerberg está propondo."
Mecanismo: declaração factual + promessa de revelação
```

```
Headline: "Você vai ter um agente de IA trabalhando por você 24/7."
Subtítulo: "O manifesto de Zuckerberg dono do Facebook."
Mecanismo: declaração direta ao leitor + âncora de identidade
```

```
Headline: "A Meta prometeu conectar o mundo em 2004. Deu o Facebook. Agora prometeu dar um agente de IA para cada pessoa do planeta."
Subtítulo: "O manifesto de Zuckerberg e por que a história importa aqui."
Mecanismo: contraste histórico (promessa passada vs promessa atual)
```

### Quando os frameworks ajudam

Os 7 frameworks (Value-Stack, Problem-Proof, Hack List, Rant Callout, Demo Walkthrough, Debate Callout, Confessional) são ferramentas de diagnóstico e de estruturação do arco interno. Depois que o hook está escrito, o framework pode ser identificado para guiar os slides de corpo. Nunca o inverso.

---

## Processo de Modelagem

### Passo 1 — Capturar inputs

Coletar do usuário ou da conversa:
- **Tema** — o assunto central do conteúdo
- **Formato** — carrossel / thread / reel ou vídeo curto / post longo ou artigo
- **Cliente ativo** — para calibrar tom e vocabulário (ler `.agents/social-media-context-sms.md`)
- **Objetivo** — engajamento, conversão, autoridade, alcance?
- **O que o cliente tem de prova** — dado real? case? processo próprio? opinião?

Se o usuário não forneceu formato → perguntar antes de modelar.

### Passo 1.5 — Identificar a tensão do conteúdo (obrigatório antes de modelar hooks)

Antes de propor qualquer hook, responder internamente às perguntas da seção "LEI DO HOOK — Passo 0". Só avançar quando a tensão real do conteúdo estiver clara. Hooks gerados sem tensão identificada saem genéricos.

### Passo 2 — Modelar os frameworks

Para cada framework, escrever:
1. O **hook** do slide/post/cena 1 — já no tom do cliente
2. O **arco resumido** — o que acontece em cada unidade
3. **Melhor quando** — contexto ideal de uso
4. **Risco** — o que pode dar errado com esse tema e cliente específicos

### Passo 3 — Apresentar ao usuário

Formato de apresentação: ver seção "Output" abaixo.

### Passo 4 — Receber escolha e gerar briefing

Após o usuário escolher (ex: "B" ou "Problem-Proof"):
- Gerar o briefing estruturado completo
- Passar para a skill de criação correspondente

---

## Arcos por Formato

### CARROSSEL

| Framework | Arco de slides |
|---|---|
| Value-Stack | Slide 1: hook com promessa → Slides 2-N: 1 benefício por slide, crescente → Slide final: CTA |
| Problem-Proof | Slide 1: dado da dor → Slides 2-3: diagnóstico → Slide 4: prova/case → Slide 5: solução → Slide final: CTA |
| Hack List | Slide 1: promessa de N hacks → 1 hack por slide com contexto → Slide final: salvar + CTA |
| Rant Callout | Slide 1: afirmação confrontadora → Slides 2-3: argumento → Slide 4: nova verdade → Slide final: CTA |
| Demo Walkthrough | Slide 1: resultado prometido → Slides 2-N: passo numerado → Slide final: resultado + recurso/CTA |
| Debate Callout | Slide 1: argumento oposto apresentado com honestidade → Slides 2-3: concordância parcial + desmonte específico → Slide 4: nova posição → Slide final: implicação + CTA |
| Confessional | Slide 1: revelação da mudança/erro → Slides 2-3: detalhe específico do que aconteceu → Slide 4: padrão generalizado → Slide final: lição + CTA |

### THREAD

| Framework | Arco de posts |
|---|---|
| Value-Stack | Post 1: hook com promessa → Posts 2-N: 1 benefício por post com exemplo → Post final: síntese + CTA |
| Problem-Proof | Post 1: dado chocante → Posts 2-3: por que acontece → Post 4: evidência → Posts 5-6: solução → Post final: CTA |
| Hack List | Post 1: promessa de N → 1 hack por post com exemplo e contexto → Post final: CTA |
| Rant Callout | Post 1: opinião forte → Posts 2-4: argumentação com exemplos → Post final: posição consolidada + CTA |
| Demo Walkthrough | Post 1: resultado + promessa do processo → Posts 2-N: passos numerados com detalhe → Post final: resultado + CTA |
| Debate Callout | Post 1: argumento oposto apresentado fielmente → Posts 2-3: concordância parcial + desmonte específico → Posts 4-5: nova posição com dado → Post final: implicação prática + CTA |
| Confessional | Post 1: revelação da mudança/erro próprio → Posts 2-4: detalhe do que aconteceu + padrão → Post final: lição generalizada + CTA |

### REEL / VÍDEO CURTO (15–90s)

| Framework | Arco de cenas |
|---|---|
| Value-Stack | Cena 1 (0-3s): promessa verbal + visual → Cenas 2-N: 1 benefício por cena (5-8s cada) → Cena final: CTA |
| Problem-Proof | Cena 1 (0-3s): stat ou pergunta de dor → Cenas 2-3: diagnóstico visual → Cena 4: prova/depoimento → Cena 5: solução → CTA |
| Hack List | Cena 1 (0-3s): hook "N coisas que..." → Cortes rápidos (5-8s por hack) → Cena final: CTA + seguir |
| Rant Callout | Cena 1 (0-3s): frase provocativa na tela + fala → Cenas 2-3: crítica desenvolvida → Cena final: nova perspectiva + CTA |
| Demo Walkthrough | Cena 1 (0-3s): "vou te mostrar como fiz X" → Cada cena: 1 passo ao vivo → Cena final: resultado + CTA |

### POST LONGO / ARTIGO (LinkedIn long-form, blog)

| Framework | Arco de seções |
|---|---|
| Value-Stack | Gancho → 1 parágrafo por benefício com exemplo específico → Fechamento com CTA |
| Problem-Proof | Lede com dado → Diagnóstico (2-3 parágrafos) → Seção de evidência → Seção de solução → CTA |
| Hack List | Intro com promessa → H2 por hack com contexto e exemplo → Conclusão síntese + CTA |
| Rant Callout | Lede provocativo → Argumento principal → Sub-argumentos com exemplos → Nova perspectiva → Posição + CTA |
| Demo Walkthrough | Intro com resultado → Seção por passo com detalhe → Conclusão com template ou recurso + CTA |
| Debate Callout | Lede com argumento oposto apresentado fielmente → Parágrafo de concordância parcial → Seção de desmonte específico → Nova posição + implicação prática |
| Confessional | Abertura com revelação pessoal → Detalhe específico do que aconteceu → Padrão generalizado → Lição aplicável ao leitor + CTA |

### ARTIGO X / LONG-FORM (X Articles, newsletter, editorial longo)

| Framework | Arco de seções |
|---|---|
| Value-Stack | H1 com promessa específica → Intro que justifica o tema → H2 por benefício com dado ou exemplo → Conclusão síntese + CTA |
| Problem-Proof | H1 com dado da dor → Intro que nomeia o problema → H2 diagnóstico → H2 evidência/case → H2 solução → CTA |
| Hack List | H1 com promessa de N → Intro que contextualiza por que esses N → H2 por hack com contexto completo → Conclusão com próximo passo + CTA |
| Rant Callout | H1 provocativo → Intro que expande a provocação → H2 argumento central → H2 sub-argumentos com prova → H2 nova perspectiva → Posição consolidada + CTA |
| Demo Walkthrough | H1 com resultado específico prometido → Intro com credencial → H2 por passo com detalhe real → Conclusão com resultado entregue + recurso/CTA |
| Debate Callout | H1 que nomeia a disputa → Intro com argumento oposto apresentado fielmente → H2 "onde concordo" → H2 "onde discordo + dado" → H2 nova posição → Conclusão com implicação prática |
| Confessional | H1 com a revelação → Intro com detalhe específico do erro/mudança → H2 o padrão por trás disso → H2 como se aplica ao leitor → Conclusão com lição sem moralizar |

---

## Output — Apresentação ao Usuário

```
NARRATIVE FRAMEWORK — [Formato]
Tema: [tema]
Cliente: [cliente ativo ou "modo genérico"]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A · VALUE-STACK

Hook:
"[hook escrito no tom do cliente]"

Arco: [descrição do arco no formato específico]
Melhor quando: [contexto ideal para esse tema/cliente]
Risco: [o que pode dar errado especificamente aqui]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
B · PROBLEM-PROOF

Hook:
"[hook escrito no tom do cliente]"

Arco: [descrição do arco]
Melhor quando: [contexto ideal]
Risco: [risco específico]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
C · HACK LIST

Hook:
"[hook escrito no tom do cliente]"

Arco: [descrição do arco]
Melhor quando: [contexto ideal]
Risco: [risco específico]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
D · RANT CALLOUT

Hook:
"[hook escrito no tom do cliente]"

Arco: [descrição do arco]
Melhor quando: [contexto ideal]
Risco: [risco específico]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
E · DEMO WALKTHROUGH

Hook:
"[hook escrito no tom do cliente]"

Arco: [descrição do arco]
Melhor quando: [contexto ideal]
Risco: [risco específico]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
F · DEBATE CALLOUT

Hook:
"[hook escrito no tom do cliente]"

Arco: [descrição do arco]
Melhor quando: [contexto ideal]
Risco: [risco específico]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
G · CONFESSIONAL

Hook:
"[hook escrito no tom do cliente]"

Arco: [descrição do arco]
Melhor quando: [contexto ideal]
Risco: [risco específico]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Qual framework seguimos? (A / B / C / D / E / F / G)
```

---

## Output — Briefing Estruturado (após escolha)

Após o usuário escolher o framework, gerar este briefing e passar para a skill de criação:

```
NARRATIVE BRIEFING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Framework:   [nome do framework]
Formato:     [carrossel | thread | reel | post longo]
Tema:        [tema]
Cliente:     [cliente ativo]
Objetivo:    [engajamento | conversão | autoridade | alcance]

Hook aprovado:
"[texto exato do hook escolhido]"

Arco de execução:
[Unidade 1]: [o que acontece — instrução para a skill]
[Unidade 2]: [o que acontece]
[Unidade N]: [o que acontece]
[Unidade final]: [CTA — tipo e direção]

Tom dominante: [direto | provocativo | educativo | narrativo]
Prova disponível: [dado | case | processo | opinião]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
→ Passando para [skill de criação] executar com este arco.
```

A skill de criação recebe o briefing e segue o arco sem desviar. O hook aprovado é o ponto de partida obrigatório — não substituir por outro.

---

## Regras de Calibração por Framework

Ao modelar os hooks, aplicar primeiro a Lei do Headline (seção acima) e depois as regras específicas por framework:

**Value-Stack** — o hook deve prometer um resultado concreto, não vago. "5 vantagens" é fraco. "5 vantagens que aparecem no seu faturamento em 30 dias" é específico.

**Problem-Proof** — o hook deve ter o dado no primeiro período. "87% dos criadores param antes de 90 dias" funciona. "A maioria dos criadores desiste" não.

**Hack List** — o número importa. 3 é fraco demais. 7-12 é o range ideal. O adjetivo antes do número diferencia: "7 hacks silenciosos de criadores que postam todo dia" > "7 dicas de consistência".

**Rant Callout** — o hook deve confrontar sem ofender a audiência-alvo. Confronta a crença, não o crente. "Consistência não é disciplina" confronta a ideia. "Quem acredita em disciplina está errado" confronta a pessoa.

**Demo Walkthrough** — o hook deve prometer o resultado específico e incomum que o processo entrega. "Meu processo de criação de conteúdo" é genérico. "Como criei 312 posts em 2026 sem esgotar" é específico e incomum.

**Debate Callout** — o hook deve nomear o argumento oposto sem atacar quem o defende. "A crítica de que IA não entrega ROI tem dados reais por trás. E eu concordo em parte." funciona. "Quem diz que IA não funciona está errado" confronta a pessoa, não a ideia — evitar.

**Confessional** — o hook deve revelar a mudança/erro com detalhe específico imediato. "Eu achava que X" sem dizer por quanto tempo, em que contexto ou o que mudou — é vago. "Durante 6 meses acompanhei esse movimento achando que era ruído. Não era." é concreto e prende.

---

## Boundaries

- Não escreve o conteúdo final — apenas o briefing e os hooks de modelagem
- Não substitui o QA Gate ou o copy-qa-sms — esses rodam após a execução da skill de criação
- Não decide sozinho o framework — apresenta opções e aguarda escolha do usuário
- Não inventa dados para Problem-Proof — se o cliente não tem dado, sinaliza que o framework requer prova real
- Os hooks gerados nesta skill são **modelos de trabalho** — não copy final. O hook aprovado passa para a skill de criação, que executa copy-qa-sms antes de entregar. Se o usuário quiser usar o hook isoladamente (sem passar por uma skill de criação), acionar copy-qa-sms manualmente antes de publicar.

## See also

**carousel-writer-sms** — executa o briefing para formato carrossel
**thread-writer-sms** — executa o briefing para formato thread
**video-script-sms** — executa o briefing para formato reel/vídeo curto
**post-writer-sms** — executa o briefing para formato post longo ou artigo
**hook-writer-sms** — gera variantes do hook aprovado se quiser testar mais opções
**copy-qa-sms** — gate universal de qualidade, roda após a execução de qualquer skill de criação
