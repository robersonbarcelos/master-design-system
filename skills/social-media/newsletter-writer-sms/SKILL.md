---
name: newsletter-writer-sms
description: "Skill de escrita editorial para Intus HUB AI News (Diego Spanevello). Dois modos via gate obrigatório: NOTÍCIA (item de newsletter Ghost — 2 parágrafos por notícia, seguindo o estilo editorial da Intus) e ARTIGO (editorial long-form Ghost com estrutura completa, ângulo narrativo via narrative-framework-sms, e os 15 mecanismos narrativos como camada de execução). Integra com o fluxo Ghost da skill intus-newsletter. copy-qa-sms obrigatório antes de qualquer entrega. Usar quando o usuário pede 'escreve a notícia', 'redige o artigo', 'texto da newsletter', 'copy do artigo Ghost', ou quando a skill intus-newsletter delegar a escrita."
metadata:
  version: 1.0.0
  client: intus-hub
  canal: Intus HUB AI News
---

# Newsletter Writer — Intus HUB AI News

## Quando Usar

- Usuário pede texto para item de newsletter (notícia individual)
- Usuário pede escrita de artigo editorial completo para o Ghost
- Usuário diz "redige", "escreve a notícia", "texto do artigo", "copy da newsletter"
- skill `intus-newsletter` delega a etapa de escrita

**Não acionar quando:**
- O pedido é de carrossel ou post de Instagram → `carousel-writer-sms` / `post-writer-sms`
- O pedido é de thread ou X Article → `thread-writer-sms` / `article-writer-sms`
- O pedido é só de imagens ou deploy Ghost → skill `intus-newsletter`

---

## GATE OBRIGATÓRIO — Modo de Escrita

**Se o usuário não especificou o modo, perguntar antes de qualquer produção:**

> "É uma **notícia** (item da newsletter — 2 parágrafos) ou um **artigo** (editorial completo)?"

**Exceções — detectar automaticamente e não perguntar:**
- Usuário colou um link ou pauta com "newsletter", "notícia", "item" → modo NOTÍCIA
- Usuário disse "artigo", "long-form", "análise aprofundada", "editorial" → modo ARTIGO
- Contexto da conversa já deixa claro (ex: está no meio da produção de uma newsletter)

---

## IDENTIDADE E VOZ

| Campo | Valor |
|---|---|
| Canal | Intus HUB AI News |
| Fundador | Diego Spanevello |
| Público | Interessados em IA: técnicos, criadores, founders, investidores — nível intermediário/avançado |
| Tom | Analítico, direto, causa-efeito, sem clickbait, sem euforia de hype |
| Idioma | Português brasileiro |
| Frequência | Semanal |

**Vocabulário preservado (nunca traduzir):**
`token, prompt, fine-tuning, reasoning model, benchmark, inference, context window, RAG, agent, LLM, open-source, API, yield, funding rate, stake, TVL, front-run`

**Proibições absolutas:**
- Travessão (—) em qualquer posição → substituir por ":" ou reformular a frase
- "É importante ressaltar", "nesse contexto podemos observar", "especialistas apontam"
- Adjetivos sem dado ("revolucionário", "inovador", "transformador")
- Trio de adjetivos ("rápido, seguro e escalável")
- Abertura com "Nós somos" / "A [marca] é"
- Pergunta retórica sem resposta na frase seguinte

---

## MODO NOTÍCIA

### Quando usar
Produzir o texto de uma ou mais notícias individuais para o corpo de uma edição da newsletter Ghost. Cada notícia = 2 parágrafos + título.

### Estrutura por notícia

```
[EMOJI] TÍTULO — curto, específico, sem travessão

PARÁGRAFO 1 — Contexto + o que aconteceu
→ Primeira frase: abertura paradoxal OU dado surpreendente (max 1 frase)
→ O que foi anunciado/acontecido com dado concreto
→ Âncora de autoridade: quem disse, onde, quando (nome real + contexto)

PARÁGRAFO 2 — Implicação + perspectiva
→ O que muda a partir disso
→ "A variável decisiva é..." OU contraste com dois casos reais
→ Fechamento: variável a monitorar ou ação prática mínima
```

### Emojis por categoria

| Emoji | Categoria |
|---|---|
| 🤖 | IA / Modelos / Tecnologia |
| ⚡ | Bitcoin / Macro |
| 🔷 | Ethereum / Protocolo |
| 🏛️ | RWA / Finanças Tradicionais |
| ⚖️ | Regulação |
| ⚠️ | Riscos / Segurança |
| 🇧🇷 | Brasil |
| 💵 | Stablecoins |
| 🏦 | DeFi / Protocolos |
| 📈 | Mercado positivo |
| 📉 | Quedas |
| 🔍 | Auditoria / Pesquisa |

### QA Gate — Notícia (score mínimo: 90/100)

| Critério | Pontos |
|---|---|
| Primeira frase cria fricção ou dado surpreendente — não começa com "A empresa anunciou" | 20 |
| Âncora de autoridade concreta presente (nome real, não "especialistas") | 20 |
| Parágrafo 2 entrega implicação real — não repete o fato do parágrafo 1 | 20 |
| Pelo menos um número concreto (%, valor, data, unidade) | 15 |
| Ritmo varia — não dois parágrafos com exatamente o mesmo tamanho | 10 |
| Nenhuma proibição absoluta violada | 15 |

---

## MODO ARTIGO

### Quando usar
Produzir um artigo editorial completo para o Ghost. Leitura longa, análise aprofundada, estrutura com seções.

### Passo 0 — Gate de CTA (obrigatório antes de qualquer escrita)

Perguntar antes de começar o artigo:

> "Este artigo vai ter um **CTA de produto** no final?
> - **Sim** → qual produto? (ex: Super Agente de IA, outro) e qual o link do botão?
> - **Não** → seguir sem bloco de CTA"

- Se **sim**: registrar produto + link e reservar `[IMAGEM_5]` + bloco CTA na estrutura
- Se **não**: estrutura termina no disclaimer; nenhum `[IMAGEM_5]`
- Nunca escrever CTA sem o link confirmado pelo usuário

### Passo 1 — Definir o ângulo narrativo

**Se `narrative-framework-sms` já rodou e gerou briefing:**
→ Usar o hook aprovado como abertura
→ Seguir o arco de execução como estrutura das seções
→ Pular para Passo 2

**Se tema definido mas ângulo em aberto:**
→ Acionar `narrative-framework-sms` com `formato = artigo editorial`
→ Apresentar os 7 frameworks (A a G) com hooks escritos no tom da Intus
→ Aguardar escolha antes de escrever

**Se o usuário especificou o ângulo diretamente:**
→ Executar diretamente no Passo 2

### Passo 2 — Apresentar o arco antes de escrever

Nunca desenvolver o artigo sem validar o arco primeiro:

```
ARCO DO ARTIGO — [Tema]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Framework: [nome]
Título (H1): [proposta — específico, não genérico]
Hook (abertura): [primeira frase ou parágrafo]

Seções:
H2 · [nome] — [o que acontece aqui]
H2 · [nome] — [o que acontece aqui]
H2 · [nome — RISCOS] — obrigatório em todo artigo
H2 · [nome — PALAVRAS FINAIS] — síntese + variável/ação

Virada: seção [N] — [onde o argumento central se resolve]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Arco aprovado? → NÃO → STOP. Não desenvolver sem aprovação.
```

### Passo 3 — Escrever o artigo

Com arco aprovado, desenvolver aplicando obrigatoriamente a **Camada de Execução** abaixo.

**Regras de conteúdo:**
- Uma tese por seção — cada H2 desenvolve um único ponto
- Parágrafo máximo 4-5 linhas
- Cada seção termina com gancho para a próxima
- Seção de RISCOS obrigatória em todo artigo — mínimo 2 riscos reais, nunca amenizar
- Seção de PALAVRAS FINAIS: fundo claro com borda escura (não fundo escuro — quebra em dark mode)

### Estrutura obrigatória do artigo

```
1. GANCHO (sem título de seção)
   5-8 linhas. Abertura paradoxal OU confissão OU dado incomum. Cria imagem antes de qualquer dado técnico.

2. [IMAGEM_1] — logo após o gancho

3. CONTEXTO — Por que isso importa agora
   Dado de abertura + "Tradução: [o que significa na prática]"

4. ANÁLISE PRINCIPAL (pode ter sub-tópicos H3)
   Núcleo. Dados + o que significam. Cada dado seguido de explicação.
   Incluir analogia cotidiana antes de qualquer conceito técnico novo.

5. [IMAGEM_2]

6. DESDOBRAMENTOS — O que muda a partir disso
   Cenários. A variável decisiva. Contraste com dois casos reais quando possível.

7. [IMAGEM_3]

8. ⚠️ RISCOS — obrigatório, sempre presente
   Bloco laranja. Mínimo 2 riscos, máximo 4. Nunca amenizar.

9. 🎯 PALAVRAS FINAIS
   Síntese + Oportunidade / Risco + variável ou ação específica para o leitor.
   NUNCA frase motivacional vaga. NUNCA fundo escuro no bloco.

10. DISCLAIMER (fixo do template Ghost — não alterar)
```

---

## CAMADA DE EXECUÇÃO — Os 15 Mecanismos Narrativos

Estes mecanismos se aplicam à escrita de cada parágrafo, em ambos os modos. Não são opcionais — são o que diferencia a voz editorial da Intus de um texto genérico de IA.

### Mecanismos de ABERTURA (aplicar na primeira frase / primeiro parágrafo)

**M1 — Abertura Paradoxal**
A primeira frase contradiz o óbvio. O leitor para e pensa: "espera, como assim?"
> Errado: "O DeepSeek anunciou um aumento de preços nesta semana."
> Certo: "O DeepSeek ficou mais caro. E isso é exatamente a notícia que o mercado não queria ouvir."

**M2 — Âncora de Autoridade Concreta**
Nome real + contexto de onde veio a informação. Nunca "especialistas", "estudos", "analistas".
> Errado: "Especialistas apontam que os custos de inferência vão cair."
> Certo: "Dario Amodei disse isso numa entrevista à Bloomberg na quinta-feira."

**M3 — Promessa Antecipada** *(Modo ARTIGO — aplicar na abertura)*
O leitor sabe o que vai ganhar antes de começar. Máximo 3 pontos prometidos.
> "Neste artigo: por que o aumento de preços do DeepSeek é o sinal que o mercado ignorava, o que a saída da liderança do Google DeepMind revela sobre a corrida interna, e qual o risco que ninguém está calculando."

### Mecanismos de CREDIBILIDADE (aplicar na construção dos parágrafos)

**M4 — Espelho do Leitor**
Descreve o estado atual do leitor com precisão antes de apresentar o novo ângulo. Sem julgamento.
> "A maioria das pessoas que testou os modelos open-source chegou na mesma conclusão: funciona bem para coisas simples. O que está acontecendo agora é diferente."

**M5 — Dado Específico Sem Arredondamento**
Preferir sempre o número exato ao arredondado. A especificidade sinaliza que você foi à fonte.
> Errado: "cresceu muito" / "a maioria das empresas"
> Certo: "cresceu 900% em cinco anos" / "36% das empresas do portfólio da Carta"

**M6 — Confissão Pessoal como Âncora** *(Modo ARTIGO — aplicar no gancho ou intro)*
Uma linha de recalibração própria antes do conselho. Não diminui autoridade — aumenta confiança.
> "Acompanhei esse movimento por meses achando que era ruído. Não era."

### Mecanismos de CLAREZA (aplicar na explicação de conceitos)

**M7 — Analogia Cotidiana Antes do Conceito Técnico**
Toda vez que aparecer um conceito técnico novo, criar primeiro uma imagem familiar.
> Antes de explicar "critério de sucesso de loop": a máquina de lavar que para quando a roupa está limpa, não quando o ciclo de uma hora acaba.

**M8 — Nomeação do Problema**
Dar nome ao padrão identificado. O nome cria âncora que o leitor carrega.
> "Isso tem um nome: dependência de API única."
> "O que está acontecendo é o que eu chamo de comoditização silenciosa."

**M9 — Tradução Explícita Após Dado**
Cada dado técnico seguido de "Tradução: [o que significa na prática]".
> "O modelo R2 custa 60% mais por token que o R1. Tradução: quem construiu produto sobre a API do DeepSeek acreditando no preço baixo como dado permanente vai precisar repensar a margem."

### Mecanismos de PERSUASÃO (aplicar na construção do argumento)

**M10 — Debate Estruturado** *(ativar especialmente no Framework Debate Callout)*
Apresentar o argumento oposto fielmente antes de rebater. "Concordo em parte" antes de "mas discordo em".
> "O ceticismo faz sentido — e tem dados reais por trás. O que mudou não é a posição, é o patamar de comparação."

**M11 — Classificação com Nome Próprio**
Nomear categorias e padrões em vez de só descrevê-los.
> "ateus de IA" vs "crentes de IA"
> "o padrão do modelo Frankenstein: muitas partes, nenhuma coerência"

**M12 — Contraste com Dois Casos Reais**
Nunca abstrato vs abstrato. Dois nomes reais como representantes de cada lado.
> "OpenAI cobra por output. Anthropic cobra por capacidade de raciocínio. São modelos de negócio diferentes."

### Mecanismos de RITMO (aplicar no nível da frase)

**M13 — Virada Dupla**
Validar o ponto de vista oposto antes de apresentar o argumento. Desativa resistência.
> "Os céticos estão certos nos problemas. Podem estar errados na conclusão."

**M14 — Ritmo Telegráfico nos Momentos de Impacto**
Frases curtas (5-8 palavras) após parágrafo longo para marcar impacto. Nunca empilhar mais de 3 seguidas.
> "[parágrafo longo de análise] A Anthropic não mudou uma política. Ela sinalizou uma postura."

**M15 — Humor Seco e Autoirônico** *(máximo 1 ocorrência por peça)*
Uma frase irônica ou observacional no momento em que o texto ficou pesado. Nunca apelativo.
> "O argumento de que 'ninguém usa modelos open-source em produção' sobreviveu até o momento em que todo mundo começou a usar modelos open-source em produção."

---

## QA Gate — Artigo (score mínimo: 90/100)

| Critério | Pontos |
|---|---|
| Abertura paradoxal ou dado incomum na primeira frase — não começa com "A empresa anunciou" | 15 |
| Âncora de autoridade concreta presente (nome real + contexto) | 15 |
| Pelo menos uma analogia cotidiana antes de conceito técnico | 10 |
| Dados específicos sem arredondamento em pelo menos 3 momentos | 10 |
| Ritmo varia — parágrafos longos misturados com frases curtas de impacto | 10 |
| Seção de RISCOS presente e não amenizada | 15 |
| PALAVRAS FINAIS entrega variável/ação específica — não frase motivacional vaga | 10 |
| Nenhuma proibição absoluta violada (travessão, adjetivos sem dado, trio de adjetivos) | 15 |

**Total: 100 pontos | Mínimo para entrega: 90**

---

## copy-qa-sms Gate — Obrigatório após QA Gate ≥ 90

Executar `copy-qa-sms` em todo o corpo do texto antes de entregar:

- **Passo 1 — Voice Gate:** varrer proibições absolutas listadas nesta skill + padrões universais
- **Passo 2 — AI Pattern Gate:** Tier 1 → reescrita automática. Tier 2: por parágrafo. Estrutural: varrer todos os padrões (em-dash, bold excessivo, parágrafos uniformes, atribuições vagas, "Vamos...", fragmentação estacato, wh-openers performáticos)
- **Passo 3 — Decisão:** reprovação → reescrever → re-executar. Máximo 2 rodadas

Fechar a entrega com rastreabilidade:
```
✓ Copy revisado via copy-qa-sms (Voice Gate + AI Pattern Gate) antes da entrega.
```
Se ajustes: `✓ Copy revisado via copy-qa-sms — N ajustes aplicados antes da entrega.`

---

## Output — Modo Notícia

Entregar as notícias no formato do corpo da newsletter Ghost:

```
NOTÍCIAS — [N] itens · Edição [data]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[EMOJI] TÍTULO DA NOTÍCIA 1

Parágrafo 1...

Parágrafo 2...

---

[EMOJI] TÍTULO DA NOTÍCIA 2

Parágrafo 1...

Parágrafo 2...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Copy revisado via copy-qa-sms antes da entrega.
```

## Output — Modo Artigo

Entregar o artigo completo em HTML seguindo o template Ghost da skill `intus-newsletter`, com placeholders `[IMAGEM_N]` para upload posterior.

Após entrega:
> "Artigo pronto ✓
> Quer que eu gere o `artigo_topicos.json` com os prompts de imagem agora?"

---

## Boundaries

- Não faz deploy Ghost — para isso usar a skill `intus-newsletter`
- Não gera imagens — gera prompts via `artigo_topicos.json` ou `topicos.json`
- Não define estratégia de conteúdo — ver `content-strategy-sms`
- Não escreve carrossel, post ou thread — ver as skills correspondentes

## Skills relacionadas

- `narrative-framework-sms` — define o ângulo narrativo (7 frameworks) antes do artigo
- `intus-newsletter` — fluxo completo Ghost: imagens, upload, deploy
- `copy-qa-sms` — gate universal de qualidade; roda automaticamente após QA Gate interno
- `carousel-writer-sms` — quando o conteúdo vai para carrossel IG em vez de newsletter
- `hook-writer-sms` — variações de abertura se o hook não estiver funcionando
