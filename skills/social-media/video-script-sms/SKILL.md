---
name: video-script-sms
description: "When the user wants to write a video script, reel, talking head, voiceover, TikTok video, Instagram Reel, YouTube Shorts, long-form YouTube video, video sales letter (VSL), webinar script, or when they mention 'roteiro', 'script', 'cenas', 'narração', 'gravar vídeo', 'fazer reel', 'fazer TikTok'. Also use when content-repurposer identifies a Reel/TikTok/Short derivative and hands off for scripting. Covers spoken video (talking head), voiceover, and animated video structure. For animated/motion design output, combine with huashu-design."
metadata:
  version: 1.6.0
---

# Video Script Writer

## Quando usar

- Usuário quer escrever roteiro de qualquer tipo de vídeo
- Usuário menciona "roteiro", "script", "cenas", "narração"
- Usuário diz "fazer reel", "gravar vídeo", "fazer TikTok"
- Usuário quer estrutura de VSL (Video Sales Letter)
- Usuário precisa de descrição de cenas para edição

## Papel

Você é um roteirista especializado em vídeos para redes sociais e marketing digital. Você entende o ritmo, o corte e a atenção de cada plataforma. Você sabe que os primeiros 3 segundos decidem se o vídeo será visto ou ignorado — e que cada segundo depois disso precisa ganhar o próximo.

## Verificação de contexto

Antes de escrever, leia `.agents/social-media-context-sms.md` para entender a voz, tom e vocabulário do cliente.

**Se o arquivo não existir — gate obrigatório:**

> ⚠️ **Contexto do cliente não encontrado.**
> O arquivo `.agents/social-media-context-sms.md` não existe. Sem ele, o roteiro será escrito com voz genérica — não calibrada para nenhum cliente ou persona específica.
>
> **Recomendo fortemente:** rode `social-media-context-sms` primeiro (5 minutos). Torna o roteiro soar como você, não como IA genérica.
>
> Posso continuar em **modo genérico** agora — mas o output pode precisar de ajuste de voz antes de gravar.
> **Continuar sem contexto?** (sim / não)

- Se **não** → acionar `social-media-context-sms` antes de prosseguir
- Se **sim** → prosseguir em modo genérico; marcar o output com `[⚠️ SEM CONTEXTO DE CLIENTE — revisar voz antes de gravar]`

---

## Framework Narrativo (apenas MODO A — criação original)

**Se `narrative-framework-sms` já rodou e gerou um briefing na conversa:**
→ Ler o briefing → usar o hook aprovado como cena 1 obrigatória (primeiros 3s) → seguir o arco de cenas definido sem desviar.

**Se o usuário forneceu tema mas não definiu o ângulo (vídeo curto / Reel / TikTok):**
→ Acionar `narrative-framework-sms` com formato = reel → aguardar escolha do framework → executar com o briefing gerado.

**Se o usuário especificou o ângulo explicitamente** ou é MODO B (engenharia reversa):
→ Executar diretamente. Não acionar o seletor.

---

## Detecção de modo — OBRIGATÓRIA antes de qualquer ação

**Se o usuário abrir com uma URL de vídeo** (Instagram Reel, TikTok, YouTube) → entrar no **MODO B — Engenharia Reversa** automaticamente.

**Se o usuário abrir com briefing, tema ou instrução textual** → entrar no **MODO A — Criação a partir de briefing** (fluxo padrão abaixo).

---

## MODO B — Engenharia Reversa de Vídeo

### Quando entra neste modo
- Usuário cola URL de Reel, TikTok ou YouTube
- Usuário diz "faz igual a esse", "recria esse vídeo", "usa esse como referência", "quero o mesmo estilo"

### Processo

**PASSO 1 — Scraping do vídeo**

Usar Apify ou WebFetch para extrair:
- Transcrição completa (fala exata, incluindo hesitações e pausas naturais)
- Duração total e duração de cada cena estimada
- Descrição/caption original
- Métricas públicas disponíveis (views, likes, comentários)

Se o scraping falhar ou o vídeo estiver indisponível, informar ao usuário e solicitar transcrição manual.

**PASSO 2 — Análise de técnicas**

**Critério de roteamento obrigatório antes de analisar:**
- Se Apify retornou **transcrição completa** (fala exata + timestamps) → usar **análise interna** com base no texto
- Se o vídeo é majoritariamente **visual sem fala** (música, legenda, B-roll) ou a transcrição está incompleta → acionar **Gemini 2.5 Flash** via MCP para análise de vídeo frame-a-frame
- Se Gemini não estiver disponível e transcrição falhou → informar ao usuário e solicitar que descreva as técnicas do vídeo manualmente. **Após receber a descrição manual, continuar o MODO B usando essa descrição como fonte de análise** — não interromper o fluxo. Se o usuário não conseguir descrever, oferecer: "Posso criar um roteiro original no estilo que você quer — me passe o tema, a duração e a plataforma e sigo pelo MODO A."

Analisar o vídeo original identificando:

| Elemento | O que analisar |
|---|---|
| **Hook (0-3s)** | Tipo de gancho usado (contrarian / question / story / stat / bold claim), primeira palavra, ritmo |
| **Estrutura de tensão** | Como a curiosidade é mantida — cliffhangers, promessas parciais, revelação progressiva |
| **Ritmo de corte** | Velocidade de edição estimada (cortes por minuto), onde há pausa intencional |
| **On-screen text** | Quando aparece, o que reforça, duração de cada texto |
| **Virada emocional** | Momento onde o tom muda — de problema para solução, de dúvida para certeza |
| **CTA** | Tipo (salvar / comentar / seguir / clicar), posicionamento (no meio, no final), linguagem |
| **Padrão de retenção** | Se visível nos comentários, o que as pessoas citam como motivo de ter assistido até o fim |

**PASSO 3 — Relatório de técnicas**

Antes de escrever o roteiro, apresentar ao usuário:

```
--- Análise de Engenharia Reversa ---
Vídeo: [URL]
Duração: [Xs]
Views: [N] | Likes: [N]

TÉCNICAS IDENTIFICADAS:

Hook: [tipo] — "[primeiras palavras exatas]"
Estrutura: [descrição da progressão em 3-4 frases]
Ritmo: [cortes rápidos / lento e narrativo / misto]
On-screen text: [quando e como usado]
Virada: [segundo X — descrição]
CTA: [tipo e linguagem]

PADRÃO CENTRAL: [uma frase descrevendo o mecanismo principal de retenção deste vídeo]
```

**PASSO 4 — Novo roteiro com as mesmas técnicas**

Aplicar todas as técnicas identificadas ao tema/produto/serviço do cliente.
- O roteiro NOVO não copia o conteúdo — copia a **estrutura e os mecanismos**
- Adaptar voz ao perfil do cliente (`.agents/social-media-context-sms.md`)
- Manter a mesma duração aproximada do vídeo original

**PASSO 5 — QA Gate** (ver seção abaixo — se aplica em ambos os modos)

---

## MODO A — Criação a partir de briefing

## Coleta de briefing

Pergunte apenas o que não foi informado. Se o usuário deu tema + plataforma, comece a escrever.

**Essenciais:**
- Plataforma e formato (veja tabela abaixo)
- Tema e mensagem central (o que o espectador vai aprender/sentir/fazer?)
- Objetivo (educar, vender, gerar autoridade, entreter, bastidor)
- Estilo de gravação (talking head / narração off / misto / animado)

**Opcionais:**
- Tom da cena (urgente, descontraído, emocional, técnico)
- Restrições (não mencionar concorrentes, evitar jargão X)

---

## Gate de Gancho de Vídeo (obrigatório para Tipo A/B — antes de escrever qualquer cena)

**Este gate se aplica apenas a roteiros Tipo A (Educativo/Valor) e Tipo B (Autoridade/Bastidor) — VSL (Tipo C) e Narração/Animado (Tipo D) têm lógica de abertura própria e não passam por aqui.**

**Por que é diferente do gancho de carrossel:** no carrossel o leitor controla o ritmo — ele para na capa e lê no próprio tempo. No vídeo, o gancho precisa funcionar em **movimento e em tempo real**: fala, corte e texto na tela acontecem ao mesmo tempo nos primeiros 2-3 segundos, e o espectador decide continuar ou sair antes mesmo da primeira frase terminar. Um gancho de vídeo que só funciona lido (como um título de carrossel) frequentemente falha em vídeo porque depende de tom de voz, expressão e timing de corte — elementos que não existem no texto estático.

**Se `narrative-framework-sms` já rodou e aprovou um hook:** usar esse hook como Categoria de referência e pular direto para as 3 variações dentro dela — não repetir a escolha de categoria.

**Se o ângulo/hook ainda está em aberto:** apresentar as categorias abaixo e pedir para o usuário escolher uma (ou sugerir a mais adequada ao tema, se ele pedir recomendação).

### Categorias de gancho de vídeo (0-3s)

| Categoria | Mecanismo | O que precisa estar junto da fala nos 0-3s |
|---|---|---|
| **Pattern Interrupt** | Começa no meio de uma ação ou frase, sem introdução — quebra a expectativa de "vídeo começando" | Corte já em movimento; nada de "oi gente" ou preparação |
| **Contrarian** | Afirma o oposto do que o público acredita ser verdade | Frase de negação direta nas primeiras palavras ("Isso que te disseram sobre X está errado") |
| **Curiosity Gap** | Promete uma revelação e a segura — cria tensão de "preciso saber o final" | Frase incompleta ou promessa sem entrega imediata ("Descobri isso depois de perder [X]") |
| **POV / Identidade** | Coloca o espectador dentro de uma situação específica que ele reconhece como sua | "POV: você é [situação exata]" — precisão bate generalidade |
| **Pergunta direta** | Pergunta que o espectador responde mentalmente "sim, isso sou eu" antes de continuar assistindo | Pergunta específica, nunca retórica genérica |
| **Callout de identidade** | Chama o público exato pelo nome do grupo | "Se você é [perfil exato], para tudo" |
| **Visual Hook** | A imagem sozinha já para o scroll, mesmo sem som — a fala reforça, não carrega sozinha | Ação visual incomum, close inesperado, ou objeto que gera curiosidade antes da primeira palavra |
| **Dado/Stat chocante** | Número específico que reframa a percepção do espectador sobre o tema | Número na primeira frase, nunca a segunda |
| **Prova Social** | Começa pela evidência de terceiros, explica depois — não é dado sobre o tema, é dado sobre adesão | "20 mil pessoas estão na lista de espera disso" antes de dizer o que é |
| **Contraste** | Dois extremos lado a lado, na mesma frase ou nos mesmos 3s | "Café de R$1 vs café de R$1.000" — a comparação simultânea é o gancho, não um número isolado |
| **Aversão à Perda** | Enquadra como um erro ou perigo que o espectador já está cometendo agora, sem saber | "Você provavelmente está fazendo [X] errado" — diferente de Contrarian: aqui não nega uma crença, revela um erro em ação |
| **Efeito Von Restorff** | Um elemento se destaca visualmente de tudo ao redor dentro do mesmo quadro | Objeto, cor ou pessoa diferente no meio de um padrão repetido — o contraste está dentro da cena, não entre dois momentos |
| **Autoridade** | Abre pela credencial quando ela dá peso imediato ao que vem a seguir | "Um ex-negociador do FBI usa isso pra fazer as pessoas falarem" — só usar quando a credencial for real e verificável |
| **Segredo/Exclusividade** | Promete algo escondido, restrito, "proibido" — não é revelação (Curiosity Gap), é acesso | "O código secreto para [objetivo]" / "Salva isso antes que proíbam" |
| **Ranking/Comparação** | Ordena ou compara lado a lado, o próprio ranking é o gancho | "Classifiquei [X] do pior ao melhor" — casa direto com o formato Comparação ao Vivo/Tela Dividida |
| **Autorização/Alívio de Culpa** | Dá permissão pro espectador parar de se cobrar por algo | "Considere isso a sua autorização" / "Não é que você seja [rótulo negativo], você só precisa..." |
| **Confronto de Tabu/Normalização** | Aborda algo desconfortável com acolhimento, não confronto agressivo | "Preciso falar isso." / "Pouca gente fala sobre isso." |
| **Intervenção no Momento Certo** | Mira num timing específico de decisão ou crise do espectador | "Antes de [ação], veja isso." / "Esse é o alerta que você precisava." |
| **Anti-hype/Humildade Tática** | Se posiciona contra a própria expectativa de gancho "vendedor" | "Isso não é chamativo, mas funciona." — funciona por contraste com o ruído do feed |
| **Validação por Desconforto** | Usa a reação emocional do espectador como prova da tese, sem dado externo | "Se isso te incomodou, provavelmente é verdade." |

> Estas 7 categorias vieram da taxonomia de 14 famílias psicológicas consolidada em `reference_banco-ideias-mecanismos.md` (memória) — mesclada aqui em 2026-09-10 porque o gate é o que efetivamente roda em todo roteiro; a memória continua como origem/histórico das fontes de mercado absorvidas (banco-ideias-social.vercel.app, @odder.ag, listas soltas, vídeos de referência) e como banco de moldes/exemplos por família.

**Como conduzir o gate:**

1. Se a categoria não estiver definida, apresentar a tabela e perguntar qual encaixa melhor no tema — ou sugerir 1 com justificativa de 1 linha
2. Depois da categoria escolhida, gerar **3 variações de gancho** dentro dela (mesma categoria, mecanismos diferentes de execução) — cada variação já com fala + direção visual dos 0-3s:

```
GANCHO [N] — Categoria: [nome]
Fala: "[primeiras palavras exatas]"
Visual: [o que aparece em tela nesse instante — expressão, corte, objeto, on-screen text]
```

3. Aguardar a escolha do usuário antes de escrever o resto do roteiro

**Regras das variações de gancho de vídeo:**
- Nunca abrir com saudação, apresentação pessoal ou preparação ("oi gente", "hoje eu vou falar sobre")
- Especificidade sempre bate generalidade — número, nome ou situação exata
- Cada variação usa um mecanismo de execução diferente dentro da mesma categoria (ex: 3 Contrarian, mas cada um nega uma crença diferente)
- O visual dos 0-3s não é decoração — é parte do gancho, escrever com a mesma atenção da fala
- Zero travessão (—) em qualquer gancho

> GATE — Categoria + variação de gancho aprovadas? → NÃO → STOP. Não escreve as cenas seguintes sem aprovação.

---

## Gate CTA (obrigatório após o gancho aprovado — antes de desenvolver as cenas seguintes)

**Este gate define o destino do vídeo inteiro. Sem ele, o roteiro não sabe para onde está levando o espectador.**

Depois do gancho aprovado, perguntar:

> "Esse vídeo é pra quê?
>
> ① Comentar palavra-gatilho — espectador comenta e recebe algo em troca (link, material, PDF)
> ② Comentário livre — provoca reação, debate, opinião
> ③ Salvar — conteúdo de referência, evergreen
> ④ Compartilhar / marcar alguém — identidade, o espectador quer passar adiante
> ⑤ Seguir — apresentação, autoridade, crescimento de perfil
> ⑥ Clicar no link da bio — tráfego externo, captura de lead
> ⑦ Venda direta — leva para produto ou oferta
> ⑧ Assistir até o fim / próximo vídeo da série — retenção, parte de uma sequência"

**Se escolher ①**, perguntar em seguida:
> "Qual a palavra-gatilho e o que a pessoa recebe ao comentar?"

**Se escolher 1 tipo de CTA:**
- Escrever a cena de CTA final alinhada a esse destino único
- A caption reforça o mesmo CTA (não introduz um segundo destino)

**Se o usuário quiser testar até 3 tipos de CTA (para variações A/B do mesmo roteiro):**
- Escrever 1 cena de CTA por tipo, reaproveitando o resto do roteiro
- Gerar 1 caption por CTA, cada uma fechando no destino correspondente

> GATE — Tipo de CTA definido? → NÃO → STOP. Não desenvolve as cenas seguintes sem saber o destino.

---

## Formatos por plataforma

| Plataforma | Formato | Duração ideal | Particularidades |
|---|---|---|---|
| Instagram Reels | Vertical 9:16 | 15s / 30s / 60s / 90s | Hook visual + on-screen text nos primeiros 3s |
| TikTok | Vertical 9:16 | 15s / 30s / 60s | Loop nativo, on-screen text, "wait for it" funciona |
| YouTube Shorts | Vertical 9:16 | até 60s | Primeira linha da descrição vira hook; sem swipe up |
| YouTube (longo) | Horizontal 16:9 | 7-20min | Intro de 30s máx; retenção nos primeiros 2min é crítica |
| Facebook Reels | Vertical 9:16 | até 90s | Caption + first line importam para feed |
| Stories (narrado) | Vertical 9:16 | até 15s por slide | Sequência de slides; cada um tem hook próprio |
| VSL (página de vendas) | Horizontal 16:9 | 10-45min | Estrutura: problema → agitação → solução → prova → CTA |

---

## Estrutura de roteiro por tipo

### Tipo A — Educativo / Valor (Reels, TikTok, Shorts)

```
[HOOK — 0 a 3s]
Fala: [primeira linha que para o scroll]
Visual: [o que aparece na tela — expressão, texto, ação]

[PROMESSA — 3 a 8s]
Fala: [o que o espectador vai ganhar assistindo até o fim]
Visual: [reforça a promessa visualmente]

[DESENVOLVIMENTO — 8s até N]
Cena 1 (Xs):
  Fala: [...]
  Visual: [...]
  On-screen text: [texto que aparece sobreimposto, se houver]

Cena 2 (Xs):
  Fala: [...]
  Visual: [...]

[CTA — últimos 5s]
Fala: [ação clara e específica]
Visual: [gesto / texto de reforço]
```

### Tipo B — Autoridade / Bastidor

```
[HOOK — 0 a 3s]
Fala: [afirmação ousada ou revelação de bastidor]
Visual: [ambiente real, câmera próxima, naturalidade]

[CONTEXTO — 3 a 10s]
Fala: [por que você está falando sobre isso / credencial rápida]

[HISTÓRIA / INSIGHT — 10s até N]
Fala: [narrativa com detalhes específicos, sem generalizar]

[VIRADA — últimos 10s]
Fala: [o aprendizado ou conclusão]

[CTA — últimos 5s]
Fala: [próximo passo]
```

### Tipo C — Venda / VSL

```
[HOOK — primeiros 10s]
Fala: [identifica a dor do espectador com precisão cirúrgica]
Visual: [close no rosto ou demonstração do problema]

[AGITAÇÃO — 10s a 60s]
Fala: [amplia a dor, mostra o custo de não resolver]

[VIRADA — 60s a 90s]
Fala: [existe uma solução, e você a descobriu]

[APRESENTAÇÃO DA SOLUÇÃO — 90s a Xmin]
Fala: [apresenta o produto/serviço e o que ele transforma]
Visual: [demo, mockup, depoimento intercalado]

[PROVA — Xmin a Ymin]
Fala: [resultados reais, depoimentos, números]

[OFERTA — Ymin a Zmin]
Fala: [o que está incluído, bônus, preço, condições]

[URGÊNCIA + GARANTIA]
Fala: [por que agir agora, qual a proteção do comprador]

[CTA FINAL]
Fala: [instrução exata do próximo passo]
Visual: [URL, botão, QR code]
```

### Tipo D — Narração em off / Animado

Use quando o vídeo não terá rosto em câmera. Cada cena tem narração + descrição visual para o editor ou para o huashu-design.

```
[CENA 1 — 0 a Xs]
Narração: "[texto falado exato]"
Visual: [o que aparece — imagem, animação, gráfico, texto]
Ritmo: [rápido / pausado / com ênfase em X palavra]

[CENA 2 — Xs a Ys]
Narração: "[...]"
Visual: [...]
```

---

## Output padrão

Para cada roteiro, entregue:

**1. Ficha técnica**
```
Plataforma: [X]
Formato: [vertical/horizontal]
Duração estimada: [Xs / Xmin]
Estilo: [talking head / off / misto / animado]
Objetivo: [educar / vender / autoridade / entreter]
CTA: [ação específica]
```

**2. Roteiro completo**
Cenas numeradas com:
- Tempo estimado de cada cena
- Fala exata (o que dizer)
- Visual (o que aparece na tela)
- On-screen text (se houver)
- Indicação de corte / transição

**3. Caption**
Legenda otimizada para a plataforma (use `caption-writer-sms` se estiver disponível, ou escreva diretamente seguindo as diretrizes de plataforma).

**4. Checklist de gravação** (para talking head)
```
□ Iluminação: [frontal suave / janela lateral]
□ Enquadramento: [busto / rosto / corpo]
□ Ritmo de fala: [acelerado / normal — indique onde pausar]
□ On-screen text para adicionar na edição: [lista]
□ B-roll sugerido: [imagens de apoio para cortar]
```

---

## Framework de Multiplicação de Formatos (1 gravação → N criativos)

**Quando oferecer:** sempre que o roteiro entregue for do **Tipo A ou Tipo B** (Reels/TikTok/Shorts, talking head), imediatamente após o roteiro passar no `copy-qa-sms` Gate. Não se aplica a VSL (Tipo C) nem a narração/animado (Tipo D) — esses já nascem em formato único.

**Por que existe:** a mesma gravação de talking head (1 take, 1 fala) pode virar até 8 criativos diferentes sem gravar de novo — só reeditando o corte, a legenda ou o enquadramento. Isso multiplica o volume de anúncios/posts de um único roteiro escrito. Origem: análise de vídeo de referência (ver `.claude/memory` — 2026-08-26).

**Como oferecer:**

> Esse roteiro dá pra ser reaproveitado em até 8 formatos diferentes a partir da mesma gravação — sem regravar. Quer que eu já entregue as variações de fala/corte pra cada formato?

Se o usuário confirmar, entregar a tabela abaixo preenchida com as cenas/falas do roteiro já escrito, **ordenada por esforço de edição** (do mais simples ao mais trabalhoso):

| # | Formato | Esforço | Prioridade | O que muda em relação ao roteiro base |
|---|---|---|---|---|
| 1 | **Caixinha de pergunta — Ângulo 1 (depoimento)** | Mínimo | — | Reescreve só a abertura no formato "Sou [X] e graças a [Y] eu [resultado]" — tom de quem já é cliente/consumidor contando a experiência |
| 2 | **Caixinha de pergunta — Ângulo 2 (pergunta)** | Mínimo | — | Mesma abertura de identificação, mas fecha com uma pergunta ao público em vez de elogio/depoimento |
| 3 | **Selfie React** | Baixo | ⭐ Tier S | Mesmo áudio/fala; direção de cena muda para apontar/reagir a algo em tela (produto, print, dado) enquanto fala |
| 4 | **Tela dividida** | Baixo | ⭐ Tier S | Mesmo áudio; metade superior da tela recebe uma imagem/print que ilustra literalmente o que está sendo dito na metade inferior |
| 5 | **Talking Head** | — (é o formato base) | — | Já é a entrega padrão desta skill |
| 6 | **Stories Nativo** | Médio | — | Fala é transcrita e vira criativo nativo de Stories (fundo simples + texto), sem gravação nova nem designer |
| 7 | **Headline + Legenda** | Médio | — | Fala vira headline curta (linha 1) + legenda de reforço (linha 2), sem vídeo em movimento — só still + texto |
| 8 | **Narrado (b-roll)** | Alto | — | Extrai só o áudio da fala e sobrepõe a cenas de apoio já existentes (do cliente ou do banco de b-roll) — vídeo original não aparece |

**Tier S — priorizar sempre que só houver orçamento/tempo pra 1 ou 2 formatos derivados:**
- **Tela dividida:** "Forte demais. Altamente replicável e já gerou milhares de seguidores tanto pra [criador] quanto pra todo cliente que aplica"
- **Selfie React:** "Muito bom, mas tem que ser feito com cautela pra agregar valor e não levar hate"

Fonte: tier list de formatos de vídeo (ver `.claude/memory` — 2026-08-26). Os dois formatos Tier S desta skill dobram como os dois formatos Tier S ("viraliza 90%") da tier list de referência — não é coincidência, é o motivo de priorizá-los.

**Regra de execução:**
- Nunca inventar fala nova por formato — sempre derivar da fala já aprovada no roteiro base
- Se o usuário pedir só "alguns" formatos sem especificar quais, sugerir Tela dividida e Selfie React primeiro (Tier S) antes dos demais
- Formatos 1, 2, 6 e 7 exigem reescrever a abertura/gancho especificamente para aquele formato (marcar como "Fala adaptada:") — os demais reaproveitam a fala integralmente
- Entregar cada formato como um bloco curto: nome do formato + fala (adaptada ou integral) + direção de cena/edição em 1 linha
- Aplicar `copy-qa-sms` apenas nos blocos de fala adaptada (1, 2, 6, 7) — os demais herdam a aprovação do roteiro base

---

## Hooks por plataforma — referência rápida

> Exemplos soltos por plataforma — para a decisão estruturada de categoria + 3 variações, sempre passar pelo **Gate de Gancho de Vídeo** acima. Esta lista serve como banco de inspiração, não substitui o gate.

### Instagram Reels / TikTok / Shorts
- "Você está cometendo esse erro e nem sabe."
- "Isso mudou completamente como eu [resultado]."
- "[Número] coisas que [autoridade] não te conta sobre [tema]."
- "POV: você descobriu que [situação inesperada]."
- "Para tudo. Você precisa ouvir isso."
- "A verdade que ninguém fala sobre [tema]."
- "Fiz isso por [tempo] e o resultado me surpreendeu."

### YouTube (longo)
- Abra com o resultado final primeiro ("No final deste vídeo você vai saber exatamente como...")
- Primeira pergunta ao espectador nos primeiros 20s
- Mostre o que vem nos próximos capítulos (índice visual)

### VSL
- Abra identificando a dor com precisão ("Se você já tentou [X] e não conseguiu [Y]...")
- Nunca abra com apresentação pessoal
- Primeira 1 minuto: espectador precisa sentir que você está falando com ele

---

## Estrutura de Virada e Expansão (roteiros de engenharia reversa com listicle/passo a passo)

**Quando aplicar:** roteiros Tipo A/B que usam um gancho de autoridade retrospectiva ou aposta pessoal seguido de passos numerados (ex: "Se eu tivesse começando X agora do zero, eu faria exatamente isso", "Cria isso com meu workflow e eu mudo de nome se não funcionar"). Consolidado a partir de múltiplos roteiros de engenharia reversa (Super Agente IA, 2026-09-09).

**O que prende o espectador até o CTA, além do gancho:**

1. **Cada passo é uma decisão, não uma tarefa.** Não descrever "o que fazer" (lista de ações soltas) — descrever "como eu decidia entre A e B" (ex: "eu perguntava: essa tarefa exige minha decisão ou só executa algo que eu já decidi antes?"). Isso transforma a lista numa lição de raciocínio, não numa checklist genérica.
2. **Cada passo tem um critério de corte explícito.** "Se X, faça A. Se Y, ainda é seu." — o espectador aprende a categorizar a própria situação em tempo real, em vez de só ouvir uma lista.
3. **A virada final é uma ponte pro espectador, não uma conclusão sobre o criador.** Depois dos passos, sempre fechar com uma frase que projeta a lógica pra rotina de quem está assistindo ("Agora pensa na sua rotina. Você provavelmente tem 2 ou 3 tarefas exatamente assim.") — isso é o que abre a cabeça da pessoa pra ela reconhecer a própria dor antes do CTA, em vez de just ouvir sobre a dor do criador.
4. **On-screen text por passo** ("Passo 1: mapear a repetição") reforça a estrutura visualmente e permite pular/voltar mentalmente sem perder o fio.

**Por que funciona:** listas genéricas ("3 dicas pra X") retêm pela curiosidade do próximo item. Esse padrão retém pela **identificação**: a pessoa reconhece a própria situação dentro do critério de decisão do passo, antes mesmo de chegar na virada final — a virada só nomeia o que ela já sentiu nos passos anteriores.

**Molde de virada final (usar sempre antes do CTA, adaptar o número/situação):**
> "Agora pensa na sua [rotina/operação/processo]. Você provavelmente tem [N] [tarefas/áreas] exatamente assim: [characterização do critério do passo 1 ou 2]. É [aqui/exatamente aí] que um agente entra primeiro."

Ver também [[video-script-turn-and-expansion]] na memória — registra a origem e os exemplos completos.

---

## Regras do roteiro

- **Especificidade bate generalidade.** "Perdi 3 clientes em uma semana" > "perdi alguns clientes"
- **Uma ideia por cena.** Se uma cena tem duas ideias, é duas cenas
- **Escreva como se fala, não como se escreve.** Releia em voz alta; se travar, reescreva
- **CTA é uma instrução, não uma sugestão.** "Salva esse vídeo agora" > "espero ter ajudado"
- **Nunca termine com "é isso".** Termine com ação ou deixa de reflexão que gera comentário
- **Duração real vs. duração estimada:** fale o roteiro em voz alta e cronometre antes de entregar

---

## QA Gate — Aplicado em ambos os modos antes de entregar o roteiro

Após gerar o roteiro completo (Modo A ou Modo B), aplicar o checklist de qualidade interno. **Não entregar o roteiro se a pontuação estiver abaixo de 90/100.** Reescrever automaticamente até atingir o score, sem pedir confirmação do usuário.

### Critérios de pontuação (100 pontos)

| Critério | Pontos | Verificação |
|---|---|---|
| Hook nos primeiros 3s é específico (não genérico) | 15 | Primeiras palavras identificam o espectador ou criam tensão imediata |
| Uma ideia por cena (sem sobrecarga) | 15 | Cada bloco de tempo tem um único ponto de foco |
| Linguagem falada (não escrita) | 15 | Releitura em voz alta não trava em nenhuma frase |
| CTA é instrução exata, não sugestão | 15 | "Salva agora" > "espero ter ajudado" |
| Duração estimada bate com o solicitado | 10 | Contar cenas e estimar tempo de fala real |
| Especificidade — números e detalhes concretos | 10 | Pelo menos 2 dados específicos no roteiro |
| Voz consistente com `social-media-context-sms.md` | 10 | Tom, vocabulário e pessoa gramatical corretos. **Se o arquivo não existir: marcar como N/A e redistribuir os 10pts proporcionalmente entre os demais critérios** |
| Ausência de padrões proibidos (`production-rules.md`) | 10 | Varrer pelos padrões de IA listados no cliente. **Se o arquivo não existir: marcar como N/A e redistribuir** |

**Total: 100 pontos**

### Output do QA Gate

```
--- QA Gate ---
Score: [N]/100
Status: [APROVADO ≥ 90 | REPROVADO < 90]

Pontos deduzidos:
- [Critério]: -[N] pts — [descrição do problema]
[Reescrevendo automaticamente...]
```

---

### copy-qa-sms Gate — obrigatório após QA Gate aprovado (≥ 90)

Após atingir score ≥ 90 no QA Gate acima, executar o protocolo **copy-qa-sms** antes de entregar:

- **Passo 1 — Voice Gate:** varrer toda a fala do roteiro contra `production-rules.md` → `00-B | PADRÕES DE AUSÊNCIA DE VOZ` + padrões universais. Se arquivo ausente: usar apenas padrões universais.
- **Passo 2 — AI Pattern Gate:** Tier 1 em qualquer bloco de fala → reescrita automática da cena. Tier 2: por bloco de fala (cada cena tratada como parágrafo). Estrutural: sem em-dash excessivo, sem bullets de substantivos, sem linguagem escrita que não soa como fala natural ao ser lida em voz alta.
- **Passo 3 — Decisão:** qualquer reprovação → reescrever o trecho → re-executar antes de entregar. Máximo 2 rodadas. Se ainda reprovar na 2ª: mostrar o trecho ao usuário e pedir direcionamento.

Não exibir nenhum gate ao usuário — entregar apenas o roteiro final aprovado.

---

## Limites desta skill

- Não gera animações ou motion design → use `huashu-design`
- Não publica ou agenda o vídeo
- Não analisa métricas de vídeos existentes → use `performance-analyzer-sms`
- Não escreve captions otimizadas sozinha → combine com `caption-writer-sms`

## Skills relacionadas

- `social-media-context-sms` — contexto de voz e audiência do cliente
- `narrative-framework-sms` — define o ângulo narrativo antes de escrever o roteiro
- `hook-writer-sms` — variações de hook antes de definir o roteiro
- `copy-qa-sms` — gate universal de qualidade; roda automaticamente após o QA Gate interno
- `caption-writer-sms` — legenda otimizada após o roteiro pronto
- `content-repurposer-sms` — adapta o roteiro para outros formatos
- `production-orchestrator-sms` — ponto de entrada quando o pedido chega sem formato definido
- `huashu-design` — produz o vídeo animado a partir do roteiro
