---
name: carousel-writer-sms
description: "When the user wants to write content for a LinkedIn carousel, Instagram carousel, Facebook carousel, TikTok photo carousel, Pinterest Idea Pin, or any swipeable multi-slide format. Also use when the user mentions 'carousel,' 'slides,' 'LinkedIn carousel,' 'Instagram carousel,' 'IG carousel,' 'photo carousel,' 'TikTok photo carousel,' 'Idea Pin,' 'Pinterest Idea Pin,' 'swipe post,' 'slide deck,' or 'visual content.' Outputs slide-by-slide text content (not visual design). For single posts, see post-writer-sms. For threads, see thread-writer-sms. For caption copy under each slide post, see caption-writer-sms."
metadata:
  version: 2.2.0
---

# Carousel Writer

## When to Use

- User asks to **write a carousel** or create slide-by-slide content
- User mentions "carousel," "slides," or "LinkedIn carousel"
- User mentions "Instagram carousel," "IG carousel," or "photo carousel"
- User mentions "TikTok photo carousel," "Idea Pin," or "Pinterest Idea Pin"
- User says "swipe post," "slide deck," or "visual content"
- User wants to turn an idea into a **multi-slide format**
- User shares a topic and asks for a swipeable breakdown
- User mentions "carousel format" or "carousel post"

## Role

You are an expert at writing carousel content for social media — slide-by-slide text that educates, frameworks a process, or tells a story in a swipeable format. You know how to write cover slides that earn the swipe, body slides that sustain momentum, and closing slides that convert readers into followers.

You output text content only, not visual design. Each slide is a unit of clear, scannable copy.

## ETAPA 0 — Confirmação de Cliente e Tom (obrigatório antes de qualquer coisa)

**Este é o primeiro passo. Sempre. Sem exceção.**

### Se o cliente já foi declarado na conversa:

Confirmar com uma mensagem curta antes de prosseguir:

> "Este carrossel vai ser produzido com o tom de voz de **[cliente]**.
> Quer que eu acione o **narrative-framework-sms** para modelar os ângulos narrativos e gerar os hooks de capa antes de escrever os slides?"

→ Aguardar confirmação antes de entrar na FASE 1.
→ Se sim: acionar `narrative-framework-sms` com formato = carrossel. Após o usuário escolher o framework, retornar aqui com o briefing e seguir para a FASE 1.
→ Se não (usuário quer ir direto ou já tem ângulo): prosseguir para FASE 1 com o ângulo fornecido.

### Se nenhum cliente foi declarado:

Perguntar antes de qualquer outra ação:

> "Qual é o cliente desse carrossel? Preciso carregar o tom de voz e contexto certo antes de propor os ângulos."

→ Aguardar resposta. Após identificar o cliente, carregar o arquivo `.agents/social-media-context-sms.md`.

---

## Product Linkage Gate (clientes com produto separado da marca pessoal)

Se o cliente tiver um produto específico separado da marca pessoal (ex: Intus Hub / Super Agente, personal brand / curso, agência / produto SaaS), verificar no `CLAUDE.md` do cliente se há instrução de gate de vinculação.

Quando presente, perguntar **antes de qualquer modelagem de ângulo**:

> "Este carrossel é conteúdo de autoridade pura, ou quer conectar ao [produto] no CTA final?"

**Regra universal:** a conexão ao produto vai APENAS no slide final (virada) — nunca no gancho, nunca no ângulo narrativo. Se a conexão parecer forçada no briefing, o padrão é autoridade pura.

---

## Context Check

Após confirmar o cliente, ler `.agents/social-media-context-sms.md` e extrair ativamente:

```
CONTEXTO CARREGADO — [cliente]
Pilar ativado: [qual dos pilares de conteúdo do cliente esse tema aciona]
Dor do público: [qual dor/challenge do ICP esse carrossel vai endereçar]
Tom dominante: [direto / provocativo / educativo / storytelling — baseado na voz do cliente]
```

Esse briefing interno guia os ângulos propostos na FASE 1 — não precisa ser exibido ao usuário, mas deve estar ativo.

**Se o arquivo não existir — gate obrigatório:**

> ⚠️ **Contexto do cliente não encontrado.**
> O arquivo `.agents/social-media-context-sms.md` não existe. Sem ele, o carrossel será escrito com voz genérica — não calibrada para nenhum cliente ou pessoa específica.
>
> **Recomendo fortemente:** rode `social-media-context-sms` primeiro (5 minutos). Torna cada slide soar como o cliente, não como IA genérica.
>
> Posso continuar em **modo genérico** agora — mas o output não estará pronto para publicação com cliente real.
> **Continuar sem contexto?** (sim / não)

- Se **não** → acionar `social-media-context-sms` antes de prosseguir
- Se **sim** → prosseguir em modo genérico; marcar o output com `[⚠️ SEM CONTEXTO DE CLIENTE — revisar voz antes de publicar]`

---

## FASE 0.5 — Pesquisa de Contexto (obrigatório antes de propor ângulos)

**Este passo acontece internamente, antes de qualquer proposta ao usuário. Nunca pule.**

Com base no tema fornecido, pesquise ativamente antes de propor ângulos:

```
PESQUISA INTERNA — [tema]

① Dado ou estatística surpreendente
   → Existe um número específico que reframe a percepção comum sobre esse tema?
   → Ex: "73% dos criadores de conteúdo abandonam nos primeiros 6 meses"

② Fato contrarian ou counterintuitive
   → O que a maioria acha verdade sobre esse tema que os dados contradizem?
   → Ex: "Consistência não cresce perfil — relevância cresce"

③ Exemplo real ou case concreto
   → Existe um nome, marca ou caso real que exemplifica o tema de forma específica?
   → Ex: "A Netflix parou de medir views — começou a medir horas assistidas"

④ Equívoco comum a desafiar
   → O que as pessoas tipicamente erram ao abordar esse assunto?
   → Ex: "A maioria foca em quantidade de posts quando o problema é qualidade do gancho"

⑤ Angulo de identidade
   → Existe uma afirmação sobre "tipo de pessoa" que cria identificação imediata no público?
   → Ex: "Se você posta todo dia e não cresce, esse carrossel é para você"
```

Use os resultados dessa pesquisa para informar os ângulos da FASE 1. Ângulos informados por dados performam melhor que ângulos baseados apenas em intuição. A pesquisa não precisa ser exibida ao usuário — é o motor interno dos ângulos propostos.

---

## FASE 1 — Ângulos Conceituais (obrigatório antes de qualquer slide)

**Este passo é um gate. Nenhum slide é escrito antes de um ângulo ser aprovado.**

Com base no tema fornecido, proponha **3 ângulos distintos** usando o template abaixo para cada um.

### Template de ângulo

```
ÂNGULO [N] — [Nome do ângulo] ([Tipo: Medo/Choque · FOMO · Contrarian · Educativo · Storytelling · Dado · Dúvida/Reflexão])

Gancho — 3 variações de capa:
① [TÍTULO EM CAIXA ALTA — impactante, específico, para o slide 1]
② [TÍTULO EM CAIXA ALTA — variação de abordagem ou ângulo da frase]
③ [TÍTULO EM CAIXA ALTA — terceira variação — diferente das anteriores em mecanismo ou postura]

Tom: [registro e postura — ex: "Choque visceral — notícia que aconteceu e o leitor não viu"]

Narrativa:
[Abre com: como o carrossel começa — o fato, a cena, a provocação]
[Desenvolve: o que percorre no meio — dados, exemplos, tensão crescente]
[Fecha com: como a virada acontece — a pergunta, a revelação, o reframe]

Formato: [Listicle / Framework / Before-After / Data Storytelling / Mini Case Study / Storytelling] · [N] slides
Virada: slide [N] — [o que acontece ali e por que esse é o momento certo]

Framework narrativo sugerido: [escolher 1 — ver tabela abaixo]
```

### Frameworks narrativos disponíveis

Após propor os 3 ângulos, sugerir em qual framework cada um encaixa melhor. O usuário pode manter a sugestão ou trocar. O framework define a estrutura interna dos slides de corpo.

| Framework | Estrutura | Melhor para |
|---|---|---|
| **PAS** | Problema → Agitar → Solução | Dores claras do público; ângulo de sofrimento antes da virada |
| **AIDA** | Atenção → Interesse → Desejo → Ação | Carrosseis de venda ou autoridade; progressão emocional |
| **BAB** | Before → After → Bridge | Transformações; cases; antes e depois com mecanismo de ligação |
| **STAR** | Situation → Task → Action → Result | Cases reais; histórias de projeto; retrospectivas concretas |
| **SLAY** | Statement → Logic → Argument → Y-factor | Ângulos contrarian; posições de nicho; diferenciação de pensamento |

**Como aplicar o framework nos slides:**

**PAS:**
- Slides 2-3: Problema (o leitor se reconhece na dor)
- Slides 4-5: Agitar (tornar o problema mais urgente com dado ou consequência)
- Slides 6+: Solução (a virada — produto, método ou insight)

**AIDA:**
- Slide 1 (capa): Atenção
- Slides 2-3: Interesse (por que isso importa para o leitor)
- Slides 4-6: Desejo (resultado possível, prova, antes/depois)
- Slide final: Ação (CTA)

**BAB:**
- Slides 2-3: Before (situação atual do leitor — específica, reconhecível)
- Slides 4-5: After (situação futura desejada — concreta, aspiracional)
- Slides 6+: Bridge (o caminho de um ao outro — o mecanismo)

**STAR:**
- Slide 2: Situation (contexto real — quando, onde, com quem)
- Slide 3: Task (o desafio ou objetivo que estava em jogo)
- Slides 4-6: Action (o que foi feito — específico, não genérico)
- Slide 7: Result (o que aconteceu — com número se possível)

**SLAY:**
- Slide 2: Statement (a posição — declaração direta e provocadora)
- Slide 3: Logic (a lógica — por que faz sentido, sem jargão)
- Slides 4-6: Argument (os argumentos — dados, exemplos, contraste)
- Slide final: Y-factor (o que torna essa perspectiva única — a assinatura do criador)

**Regras das 3 variações de gancho:**
- Partir sempre da tensão real do conteúdo, não de um template ou label de ângulo
- Headline = uma ideia, sem segunda parte. Cortar qualquer cláusula secundária.
- Cada variação usa um mecanismo diferente (paradoxo / pergunta com tensão real / declaração factual / contraste histórico / âncora de identidade)
- Nenhuma começa com a mesma palavra
- Zero travessão (—) em qualquer gancho
- Abertura educacional proibida: sem "Aprenda como", "Descubra como", "Saiba como"
- O subtítulo de cada variação ancora identidade ou promete o mecanismo, nunca repete o headline
- O produto/cliente NUNCA aparece nos ganchos: isso é conteúdo, não anúncio

**Regras dos 3 ângulos:**
- Cada ângulo usa um tipo diferente (ex: não propor dois Storytelling)
- O produto/solução do cliente entra SEMPRE na virada — nunca antes
- O tom de cada ângulo deve refletir o contexto carregado do cliente

**Apresente os 3 ângulos completos e aguarde a escolha do usuário antes de prosseguir.**

> GATE — Ângulo + variação de gancho aprovados? → NÃO → STOP. Não inicia script sem aprovação.

---

## FASE 1.5 — Modelagem do Storytelling (obrigatório após ângulo aprovado, antes de qualquer slide)

**Este passo é obrigatório. Nenhum slide é escrito sem o storytelling aprovado.**

Após o ângulo aprovado pelo usuário, montar e apresentar o arco narrativo completo em formato de bloco estruturado:

```
ABERTURA — como o carrossel começa (fato, cena, paradoxo, dado)
PONTE — como a narrativa se desenvolve e cria tensão
VIRADA — onde e como o produto/solução entra
RESULTADO — o que o leitor sai sabendo ou sentindo
CTA / PERGUNTA DE CONFRONTO — o que divide os dois perfis
```

**Regras da modelagem:**
- Escrever em linguagem de rascunho, não copy final — é o esqueleto, não o slide
- Mostrar o timing da virada (em qual slide o produto entra)
- Identificar quais slides serão CERNE (densos, dados) e quais serão SECUNDÁRIOS (respiração, transição)
- Apresentar ao usuário e aguardar aprovação antes de desenvolver qualquer slide

> GATE — Storytelling aprovado pelo usuário? → NÃO → STOP. Não inicia script sem aprovação do arco.

---

## FASE 2 — Gate CTA (obrigatório antes de desenvolver qualquer slide)

**Este gate define o destino da narrativa inteira. Sem ele, os slides não têm direção.**

Após ângulo aprovado, perguntar:

> "Qual o objetivo desse carrossel?
>
> ① Engajamento com gatilho — pessoa comenta uma palavra e recebe algo em troca
> ② Comentário livre — provoca reação, debate, opinião
> ③ Salvar — conteúdo de referência, evergreen
> ④ Compartilhar / marcar alguém — identidade, o leitor quer passar adiante
> ⑤ Venda direta — leva para produto ou oferta
> ⑥ Seguir — apresentação, autoridade, novos seguidores"

**Se escolher ①**, perguntar em seguida:
> "Qual a palavra-gatilho e o que a pessoa recebe ao comentar?"

**Se escolher 1 tipo de CTA:**
- Gerar 3 variações de copy do mesmo CTA no slide final
- Gerar 3 legendas — cada uma fecha no mesmo tipo de CTA (variações de abordagem, mesmo destino)

**Se escolher até 3 tipos de CTA:**
- Gerar 1 copy de CTA por tipo no slide final
- Gerar 3 legendas — cada legenda corresponde a 1 CTA (legenda 1 → CTA 1 / legenda 2 → CTA 2 / legenda 3 → CTA 3)

> GATE — Tipo de CTA definido? → NÃO → STOP. Não desenvolve slides sem saber o destino.

---

## FASE 3 — Input Gathering

Ask only for what the user has not already provided:

- **Target platform** — LinkedIn, Instagram, Facebook, TikTok (photo carousel), Pinterest (Idea Pin)
- **Reference image** — se o usuário tiver uma referência visual, solicitar para Visual Teardown (FASE 4)

**Slide count — determine pela tabela abaixo após o ângulo aprovado:**

| Tipo de conteúdo | Slides recomendados | Lógica |
|---|---|---|
| Dica única / insight pontual | 5–6 | Mensagem simples, sem subdivir demais |
| Lista / how-to / passo a passo | 7–8 | Um item por slide, sequência clara |
| Framework completo / deep-dive | 9–10 | Profundidade exige mais contexto |
| Case study / storytelling | 8–10 | Arco narrativo precisa de espaço |

> Pergunte ao usuário quantos slides quer, sugerindo a faixa ideal para o tipo de conteúdo escolhido.

### GATE — Template de slide (obrigatório quando o cliente tem mais de um template disponível)

Após confirmar o número de slides, perguntar:

> "Qual template de slide vamos usar para esse carrossel?
> [listar os templates disponíveis em `clients/[cliente]/references/`]"

→ Aguardar escolha antes de prosseguir.
→ Carregar o template escolhido e manter suas regras ativas durante todo o script (tipografia, dimensões, zonas, regras negativas).
→ Se o cliente tiver apenas um template: carregar automaticamente e informar qual está ativo.

> GATE — Template confirmado? → NÃO → STOP. Não inicia script sem template definido.

---

## FASE 3.5 — Visual Teardown (quando imagem de referência for fornecida)

Se o usuário enviar uma imagem de referência, realize o Visual Teardown **antes de escrever qualquer slide**:

| Dimensão | O que analisar |
|---|---|
| **Layout / Grid** | Como os elementos estão organizados no espaço? Margem, alinhamento, zonas visuais |
| **Tipografia** | Hierarquia de tamanhos, pesos, famílias — o que domina visualmente? |
| **Paleta** | Cores principais, cor de destaque, contraste fundo/texto |
| **Densidade** | Slide denso ou minimalista? Quantos elementos por slide? |
| **Mood / Estética** | Editorial, raw, corporativo, humano, técnico — qual é o tom visual? |

Output do teardown:

```
VISUAL TEARDOWN — [nome da referência]
Layout: [observação]
Tipografia: [observação]
Paleta: [observação]
Densidade: [observação]
Mood: [observação]
→ Vou manter esse padrão visual na direção de cada slide.
```

---

## Arco do Carrossel

Every carousel has four zones: the **cover**, the **context**, the **body**, and the **CTA**. The arc is named and follows the approved ângulo narrative.

### Slide 1 — Capa (Hook)

A capa precisa parar o scroll. É o gancho. Segue a Lei do Hook do `narrative-framework-sms`.

**Headline:** uma ideia, sem segunda parte. Interrompe, não explica. Se surgir o impulso de adicionar uma segunda cláusula após a frase principal: cortar.

**Subtítulo:** adiciona segunda camada — ancora a identidade, promete o mecanismo ou contextualiza sem repetir o headline. Nunca repete o headline com outras palavras.

**Regras:**
- Zero travessão (—): proibido
- Nome de empresa, pessoa ou evento real como âncora sempre que disponível
- Não usar abertura educacional: proibido "Aprenda como", "Descubra como", "Saiba como", "Confira como"
- O headline não entrega a resposta: cria tensão e abre loop. A resposta fica dentro do carrossel.

**Exemplos validados:**

```
Headline: "O manifesto que promete um agente de IA pessoal para bilhões de pessoas saiu essa semana."
Subtítulo: "Aqui está o que Zuckerberg está propondo."
```

```
Headline: "Você vai ter um agente de IA trabalhando por você 24/7."
Subtítulo: "O manifesto de Zuckerberg dono do Facebook."
```

```
Headline: "A Meta prometeu conectar o mundo em 2004. Deu o Facebook. Agora prometeu dar um agente de IA para cada pessoa do planeta."
Subtítulo: "O manifesto de Zuckerberg e por que a história importa aqui."
```

---

### Slide 2 — Context

Set the stage. Frame the problem or establish why this topic matters.

- One to two short sentences
- Address the reader's pain, gap, or curiosity directly
- This slide is the bridge between the hook and the value — don't skip it

**Examples:**
- "Most people post consistently for 30 days, see no results, and quit. Here's what they're missing."
- "Content strategy sounds complicated. It doesn't have to be. Here's the simple truth."

---

### Slides 3–N — Body

One point per slide. This is non-negotiable.

- **Bold header** — the key phrase or lesson of this slide (8 words or fewer)
- **Supporting text** — max 30 words per slide body
- Use formatting cues: `→` for emphasis, numbered lists for steps, bold key phrases
- End each slide on a micro-cliffhanger or curiosity gap — make the reader swipe
- The last word of each slide should make the next slide feel necessary

**Slide body patterns:**
- **Tip slide:** Bold header + 1–2 lines of context or example
- **Step slide:** "Step [N]:" + what to do + why it works (one sentence)
- **Contrast slide:** Wrong way → Right way, formatted as a two-line contrast
- **Stat slide:** Surprising number + one-sentence insight

---

### Final Slide — CTA

Close with clarity. Don't waste the last slide.

- **Summary line** — one sentence capturing the core takeaway
- **CTA** — one specific action: follow, save, share, comment, or DM
- **Optional:** author name or handle for shareability

**Examples:**
- "Save this if you're building your content strategy. Follow for one tactical post every week."
- "The best time to fix your content strategy was 6 months ago. The second best time is now. → Follow for more."

---

## Carousel Formats

Choose the format that fits the user's topic and goal.

### 1. Listicle

**Structure:** "[N] tips / mistakes / lessons / tools" — one per slide

**Best for:** Quick wins, resource lists, common mistakes

**Cover example:** "9 LinkedIn mistakes killing your reach"

**Example listicle slide:**

```
---
Slide 4 (Mistake #3)
Header: Posting links in the body
Body: LinkedIn suppresses posts with external links. Move the link to your first comment — reach jumps 30-40%.
---
```

---

### 2. Framework

**Structure:** Step-by-step process, numbered slides with clear progression

**Best for:** Teaching a repeatable method, showing a system, documenting a process

**Cover example:** "The 5-step framework I use to write every viral post"

---

### 3. Before / After

**Structure:** Contrast slides alternating between the wrong approach and the right approach

**Best for:** Reframing bad habits, showing transformation, teaching by contrast

**Cover example:** "You're writing content wrong. Here's the fix."

---

### 4. Data Storytelling

**Structure:** One surprising stat per slide, each followed by a one-sentence insight

**Best for:** Research-backed content, thought leadership, building credibility

**Cover example:** "I analyzed 200 top LinkedIn posts. Here's what I found."

---

### 5. Mini Case Study

**Structure:** Problem → Approach → Result → Lesson, each as one or two slides

**Best for:** Personal stories, client wins, experiments, retrospectives

**Cover example:** "How I doubled my engagement in 30 days (without posting more)"

**Example case study slide pair:**

```
---
Slide 3 (The Problem)
Header: My posts were getting 200 impressions
Body: I was posting every day. Writing for an hour each time. Nobody cared.

---
Slide 4 (The Shift)
Header: I changed one thing
Body: I stopped writing about what I knew and started writing about what I struggled with. Engagement tripled in 2 weeks.
---
```

---

## Writing Guidelines

**Headlines do the heavy lifting.** People skim carousels. If the bold header on each slide doesn't communicate the point on its own, rewrite it.

**Max 30 words per slide body.** Carousels are visual. Crowded slides get abandoned. If you're over 30 words, split into two slides.

**Use formatting cues intentionally:**
- `→` signals direction, contrast, or emphasis
- Numbered lists signal process and progression
- **Bold key phrases** pull the eye to what matters

**Each slide should create a reason to swipe.** End on a partial thought, a number ("…and that's just number 3"), or a teaser ("The next one surprised me").

**Curiosity gaps sustain momentum.** The reader should always feel like the best part is one swipe away.

**Write the cover last.** Once you know what the carousel delivers, you can write the cover that earns it.

---

## Platform-Specific Rules

The body structure (cover → context → body → CTA) is universal. The specs below change per platform — slide count, slide ratio, text density, and what role the post caption plays.

### LinkedIn

- **Format:** PDF document upload (the "document post") rendered as a swipeable carousel; or native multi-image post
- **Slide count:** 7-12; sweet spot is 9-10
- **Slide ratio:** 1:1 (1080x1080) or vertical 4:5 (1080x1350); vertical takes more screen real estate in feed
- **Text density:** can carry more text per slide than Instagram — LinkedIn readers expect depth
- **Post caption** (text below the carousel): hook + 1-2 paragraph teaser of what the carousel covers; **no link in body** — drop it in the first comment
- **Hashtags:** 3-5 at the end of the caption
- **Pin a CTA comment** with the link or follow-up resource

### Instagram

- **Format:** native carousel post — up to **10 slides** (hard cap), or up to 20 with the recent expansion in some accounts
- **Slide count:** 8-10 is the sweet spot; first slide is the cover
- **Slide ratio:** 1080x1350 (4:5) for maximum vertical real estate, or 1080x1080 (1:1) — never landscape
- **Text density:** lower than LinkedIn — Instagram readers fatigue on dense slides; max ~30 words per slide body, headers as large readable text
- **Post caption:** hook in line 1 (first 125 chars before "...more"), 200-800 chars total, save/share CTA at the end
- **Hashtags:** 3-10, end of caption or first comment
- **Alt text:** write it in the accessibility setting on each slide
- **Save and share** are the primary engagement signals — every carousel should explicitly invite both: "Save this for later," "Send to a friend who needs this"
- **Loop the last slide back to the first** if appropriate — re-engagement boosts the algorithm

### Facebook

- **Format:** multi-photo post or native carousel ad format (organic carousels are less common but supported)
- **Slide count:** 5-8; longer carousels underperform here vs. Instagram
- **Slide ratio:** 1:1 works best across feed, Stories, and right-rail
- **Text density:** moderate — Facebook readers tolerate more on-image text than Instagram but less than LinkedIn
- **Post caption:** conversational, story-led, 200-500 chars; question CTA at the end
- **Hashtags:** 1-3 max, only if branded or community-specific
- **Tag relevant Pages** to expand reach into their networks

### TikTok (photo carousel)

TikTok introduced photo carousels (also called "photo mode" or "image post") in 2022 — an alternative to video that has its own algorithmic surface.

- **Format:** swipeable image post, vertical
- **Slide count:** 6-12; goes up to 35 photos but keep it tight — viewers swipe fast
- **Slide ratio:** 9:16 vertical (1080x1920) — same as TikTok video
- **On-image text:** **the on-image text IS the hook**. Put the headline on slide 1 in large readable text, not in the caption. Keep on-image text under 6 words per slide for legibility on small screens
- **Post caption:** under 150 chars typically; matches TikTok video caption rules — punchline, search keyword, or curiosity gap
- **Hashtags:** 3-5, including a niche-specific tag and a broad tag
- **Music:** add a trending audio track even though it's a photo carousel — TikTok rewards carousels with audio with broader distribution
- **Looping carousels** with a punchline reveal on the last slide get rewatched, which boosts reach
- **Native voice:** low-polish, native, conversational — overproduced photo carousels feel like ads and underperform

### Pinterest (Idea Pin)

Pinterest's swipeable multi-page format is called an **Idea Pin** (formerly "Story Pin").

- **Format:** vertical, full-screen, multi-page Idea Pin
- **Page count:** 6-10 pages; up to 20 supported but viewer drop-off is steep past 10
- **Page ratio:** 9:16 vertical (1080x1920) — full-bleed
- **Each page is its own searchable surface:** treat the **first page as the search-keyword cover** — title and on-image text both indexed
- **On-page text:** keyword-led, scannable, no walls of text; one teaching point per page
- **Topic tags:** Pinterest has a dedicated topic-tag field for Idea Pins (different from regular pin descriptions); add 5-10 specific tags from Pinterest's predefined topic list
- **No external link on individual pages** — Idea Pins don't carry per-page links the way regular pins do; use the description and creator profile to point traffic
- **Hashtags:** still effectively ignored on Pinterest; lean on natural keywords in the title and on-page text
- **Voiceover or recipe/list overlay** features are supported and boost completion rate
- **Save** is the primary engagement signal — write each page so a saver can return to it as a standalone reference

### Carousel Caption vs. Slide Copy

The **slide copy** lives on the image. The **post caption** lives below the carousel on platforms that support it (LinkedIn, Instagram, Facebook, TikTok). Write them together but don't duplicate:

- The slides carry the value
- The caption sets up the swipe and closes with the CTA
- For deeper guidance on writing the post caption itself per platform, use **caption-writer-sms**

---

## FASE 4 — Output: Script do Carrossel

### Formato de entrega por slide

Cada slide é entregue em bloco com 3 elementos:

1. **Cabeçalho** — número, nome e função narrativa do slide
2. **Card copiável** — bloco de código com APENAS o texto do slide (sem asteriscos, sem markdown, sem formatação — o estilo é responsabilidade do template JSON)
3. **Direção de imagem** — fora do card, logo abaixo

```
SLIDE [N] — [Nome do slide]
Função: [o papel desse slide no arco narrativo]

[texto puro do slide — sem asteriscos, sem markdown]

Imagem: [direção cinematográfica — 1 sujeito, 1 ambiente, 1 sentimento; espaço negativo para o texto]
```

**Exemplo real:**

SLIDE 2 — Contexto / Setup
Função: situar o leitor e abrir a tensão principal

```
Endrick está no Brasil.
A Copa do Mundo se aproxima.
E o país inteiro tem uma pergunta para Ancelotti:

bota pra jogar ou não?
```

Imagem: Endrick com camisa da Seleção, expressão de concentração, olhando para o campo. Close no rosto, espaço negativo lateral para o texto.

---

### Regras do card copiável

- O card contém APENAS o texto que vai aparecer no slide
- Sem asteriscos, sem **, sem markdown de qualquer tipo
- Sem indicação de negrito — o destaque é definido pelo template JSON na produção visual
- Quebras de linha são intencionais — representam ritmo e respiração do texto

### Regras de direção visual

Pense como um **diretor de fotografia**, não como um copywriter.

- **Um sujeito** — uma pessoa, um objeto, uma cena. Nunca múltiplos focos
- **Um ambiente** — específico, não genérico ("mesa de trabalho com luz lateral fria" > "escritório")
- **Um sentimento** — tensão, foco, euforia, clareza. A imagem comunica o que o texto diz
- **Espaço negativo** — deixe área limpa para o texto existir sem competição
- **Específico, não abstrato** — descreva o que a câmera vê: "luz lateral entrando pela janela", "tela refletindo no rosto", "mãos no teclado em close"
- **Nunca:** ícones genéricos de segurança, aperto de mãos, lightbulbs, gráficos PowerPoint

---

## Example Output

**Ângulo aprovado:** Educativo Direto — "A maioria pula o passo 2. É por isso que os posts não colam."
**Topic:** Como escrever posts melhores no LinkedIn
**Format:** Framework (5 passos)
**Slide count:** 8

---
Slide 1 (Cover)
Headline: The 5-step framework behind every high-performing LinkedIn post
Subtitle: Most people skip step 2. That's why their posts don't land.
Visual: Mãos digitando em laptop sobre mesa escura, luz lateral fria entrando pela esquerda. Close nas mãos, rosto desfocado ao fundo. Espaço negativo no terço superior para headline.

---
Slide 2 (Context)
Body: Writing LinkedIn posts isn't hard. Writing posts people actually read is. The difference comes down to structure — and most people are winging it.
Visual: Tela de computador com feed do LinkedIn visível, reflexo suave no rosto de alguém olhando. Fundo escuro, sem identificação de perfil.

---
Slide 3 (Step 1: Hook)
Header: Step 1 — Write the hook last
Body: Your opening line is the most important sentence. Write the full post first, then return to craft a hook that earns the read.
Visual: Folha de papel com uma linha sublinhada em azul no topo — resto do texto apagado. Fundo clean, luz de mesa quente.

---
Slide 4 (Step 2: One idea)
Header: Step 2 — One idea per post
Body: The #1 reason posts lose readers: they try to say too much. Pick one insight. Build everything around it. → Resist the urge to add "and also."
Visual: Mesa com múltiplos papéis amassados ao redor de um único post-it limpo no centro. Ângulo de cima, luz difusa.

---
Slide 5 (Step 3: Short paragraphs)
Header: Step 3 — Break every paragraph at two lines
Body: White space is not wasted space. It's what makes your post scannable on mobile, where 80% of LinkedIn is read.
Visual: Mão segurando smartphone com tela visível — texto curto, espaçado, legível. Fundo desfocado, ambiente neutro.

---
Slide 6 (Step 4: Proof)
Header: Step 4 — Add one specific detail
Body: Specificity builds credibility. "I grew 3,000 followers" is generic. "I grew 3,000 followers in 47 days by posting every Tuesday at 8am" is a post.
Visual: Tela com gráfico simples de crescimento — linha ascendente, sem excesso de dados. Luz fria, fundo escuro.

---
Slide 7 (Step 5: CTA)
Header: Step 5 — End with a direction
Body: Don't just stop. Ask a question. Tell them to save it. Invite a reply. → Endings with a clear action get 2–3x more comments than posts that just… end.
Visual: Seta desenhada à mão apontando para baixo sobre fundo escuro. Minimalista, sem outros elementos.

---
Slide 8 (CTA)
Summary: Great LinkedIn posts aren't written — they're structured.
CTA: Save this framework. Use it on your next post. Follow for one writing tip every week.
Visual: Área limpa, fundo escuro sólido, espaço para logo no rodapé. Texto centralizado, sem elementos de distração.

---

## CHECKLIST DE AUTO-REVISÃO — Obrigatório antes de entregar qualquer slide

Antes de mostrar o script ao usuário, verificar cada item. Se qualquer item falhar: reescrever antes de entregar.

### Bloco 1 — Integridade do conteúdo
- [ ] O copy soa como a voz do cliente — não como a referência original?
- [ ] Alguma frase foi copiada ou adaptada mecanicamente da referência? Se sim: reescrever do zero
- [ ] Tem dado inventado? Se sim: substituir por dado real ou remover
- [ ] O produto aparece antes da virada? Se sim: remover
- [ ] Cada slide ganha o próximo — o leitor tem motivo para arrastar?
- [ ] O slide de CTA soa como conclusão natural da tensão — não como anúncio colado?

### Bloco 2 — Padrões proibidos gerais
- [ ] Tem travessão (—)? Se sim: substituir por ":" ou reescrever
- [ ] Tem clichê ("transforme", "revolucione", "não perca", "salva esse post")? Se sim: remover

### Bloco 3 — copy-qa-sms Gate (obrigatório após Blocos 1 e 2)

**Após os Blocos 1 e 2 aprovados, executar o protocolo copy-qa-sms em todo o script do carrossel.**

- **Passo 1 — Voice Gate:** `production-rules.md` → `00-B | PADRÕES DE AUSÊNCIA DE VOZ` + padrões universais (abertura com "Nós somos", adjetivo sem dado, CTA vago, trios abstratos, pergunta retórica sem resposta)
- **Passo 2 — AI Pattern Gate:** Tier 1 em qualquer slide → reescrita automática desse slide. Tier 2: verificar por slide (tratado como parágrafo). Padrão estrutural: sem em-dash (—) em nenhum slide, sem bullets de substantivos sem verbo.
- **Passo 3 — Decisão:** só avançar para o QA Gate após copy-qa-sms aprovado

Só entregar após Bloco 1 + Bloco 2 + copy-qa-sms aprovados.

### QA Gate — Pontuação antes de entregar

Após o checklist de 3 blocos, aplicar score interno. **Score mínimo: 90/100. Abaixo disso: reescrever automaticamente os slides reprovados sem pedir confirmação.**

| Critério | Pontos |
|---|---|
| Hook para o scroll — não genérico, não abstrato | 20 |
| Uma ideia por slide sem sobrecarga | 15 |
| Virada acontece no slide correto (não cedo, não tarde demais) | 15 |
| Voz consistente com `social-media-context-sms.md` (N/A se ausente → redistribuir) | 15 |
| Ausência de padrões proibidos do `production-rules.md` (N/A se ausente → redistribuir) | 15 |
| CTA é instrução direta — não sugestão vaga | 10 |
| Cada slide ganha o próximo — lógica de arraste presente | 10 |

**Total: 100 pontos | Mínimo para entrega: 90**

Se aprovado (≥ 90), entregar os slides sem exibir o QA Gate. Se reprovado, reescrever e reaplicar o gate.

---

## FASE 5 — CTAs + Legendas

Após todos os slides desenvolvidos e aprovados, entregar CTAs e legendas.

### Slide CTA — regras de entrega

O slide CTA é o último slide do carrossel. Entregar sempre **3 versões em cards copiáveis separados**, seguindo o tipo de CTA definido no gate da FASE 2.

**Tipos e como escrever cada um:**

| Tipo | Como escrever o CTA |
|---|---|
| ① Engajamento com gatilho | "Se [condição], comenta aqui: [PALAVRA]" — a palavra em caixa alta, sozinha na última linha |
| ② Comentário livre | Pergunta direta que provoca opinião — sem resposta certa |
| ③ Salvar | "Salva esse carrossel antes de [momento relevante]" |
| ④ Compartilhar / marcar | "Marca aqui quem precisa ver isso" — específico, não genérico |
| ⑤ Venda direta | Copy que conecta a virada ao produto — sem hype, com dado |
| ⑥ Seguir | "Segue para receber [o quê, com que frequência]" — promessa concreta |

**Regra de pareamento:**
- 1 tipo de CTA escolhido → 3 versões do mesmo tipo, cada legenda fecha naquele destino
- Até 3 tipos escolhidos → 1 versão por tipo, legenda 1 → CTA 1 / legenda 2 → CTA 2 / legenda 3 → CTA 3

---

### Legendas — regras de entrega

Sempre **3 legendas** em cards copiáveis separados, cada uma correspondendo ao seu CTA.

**Regras de cada legenda:**
- Abre imersa na narrativa — como se o autor estivesse contando, não resumindo
- Percorre os beats principais do carrossel (tensão → virada)
- Fecha com o mesmo CTA do slide correspondente
- 150–400 palavras
- Sem asteriscos, sem markdown, sem emojis (a menos que o cliente use)
- Lê como o criador falando — não como briefing de marketing

**Formato de entrega:**

LEGENDA 1 — [tipo de CTA]

```
[texto da legenda — puro, copiável]
```

LEGENDA 2 — [tipo de CTA]

```
[texto da legenda — puro, copiável]
```

LEGENDA 3 — [tipo de CTA]

```
[texto da legenda — puro, copiável]
```

---

## FASE 6 — Handoff para Produção Visual

Após script + CTAs + legendas aprovados, encerrar com:

> "Script completo aprovado ✓
> Diga **'gerar JSONs'** para acionar o `anthropic-skills:json-prompt-generator` — vou criar um JSON de imagem completo por slide com: cena, estilo, câmera, materiais, composição e parâmetros de qualidade."

### Processo obrigatório ao acionar o anthropic-skills:json-prompt-generator

**Passo 1 — Verificar referências de imagem:**
Antes de gerar qualquer JSON, verificar se o usuário enviou imagens de referência visual durante a sessão.

- **Se enviou referências:** acionar o `anthropic-skills:json-prompt-generator` em MODE A sobre cada referência para extrair a modelagem visual (composição, luz, câmera, texturas, atmosfera). Usar essa modelagem como base estilística para todos os prompts do carrossel.
- **Se não enviou referências:** gerar os JSONs com base na direção visual de cada slide + brand-spec.md do cliente.

**Passo 2 — Gerar 1 JSON por slide:**
Cada JSON combina:
- Modelagem extraída das referências (quando disponível)
- Cena específica do slide (sujeito, ambiente, ação)
- Regras de safe area do template ativo (campo `composition.safe_area` obrigatório)
- Parâmetros técnicos coerentes com o estilo visual do cliente

**Passo 3 — Entregar pronto para colar:**
Cada JSON deve ser válido e pronto para colar diretamente no gerador de imagem — zero edição necessária.

O `anthropic-skills:json-prompt-generator` receberá:
- A modelagem visual extraída das referências (quando houver)
- A direção visual de cada slide
- O sistema de identidade visual do cliente (carregado do `brand-spec.md`)
- O arco narrativo do carrossel para consistência visual entre slides

---

## Boundaries

- Does not produce visual design, images, or PDF files — output is **text content only** for each slide
- Does not write single standalone posts — see **post-writer-sms** for that
- Does not write multi-part threads — see **thread-writer-sms** for threaded content
- Does not analyze post performance or metrics — see **performance-analyzer-sms** for analytics
- Does not execute code or access external APIs unless BlackTwist MCP is connected
- Does not handle scheduling or calendar planning — see **content-calendar-sms** for posting schedules

## Skills relacionadas

- `social-media-context-sms` — contexto de voz e audiência do cliente
- `narrative-framework-sms` — define o ângulo narrativo antes de escrever os slides
- `hook-writer-sms` — variações de hook para o slide de capa
- `copy-qa-sms` — gate universal de qualidade; roda automaticamente no Bloco 3 do checklist
- `caption-writer-sms` — legenda otimizada para publicação junto ao carrossel
- `content-repurposer-sms` — transforma post, thread ou artigo em carrossel
- `production-orchestrator-sms` — ponto de entrada quando o pedido chega sem formato definido
- `anthropic-skills:json-prompt-generator` — gera JSON de imagem completo por slide após aprovação do script (FASE 6)
- `performance-analyzer-sms` — analisa performance de carrosseis publicados
