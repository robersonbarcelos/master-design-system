---
name: article-writer-sms
description: "Quando o usuário quer escrever um artigo longo para o X (Twitter) Articles, artigo de newsletter, long-form para LinkedIn, ou qualquer conteúdo editorial de formato longo com seções, profundidade e narrativa expandida. Usar quando o usuário menciona 'artigo', 'escreve um artigo', 'X Article', 'artigo no Twitter', 'long-form', 'newsletter', 'quero aprofundar esse tema', ou quando o conteúdo claramente exige mais de 500 palavras e estrutura de seções. Diferente de post-writer (post único curto) e thread-writer (série de posts conectados) — artigo é um documento editorial completo com H1/H2/corpo expandido. Output: arquivo Markdown (.md) estruturado, pronto para publicação via x-article-publisher."
metadata:
  version: 1.0.0
---

# Article Writer — Long-form para X Articles e Newsletter

## Quando Usar

- Usuário quer escrever um **artigo longo** para X (Twitter) Articles
- Usuário menciona "artigo", "X Article", "long-form", "newsletter"
- Conteúdo exige profundidade — mais de 500 palavras, múltiplas seções
- Usuário tem um tema complexo que não cabe em post ou thread
- Usuário quer publicar no X Articles com `x-article-publisher` após a escrita

**Não acionar quando:**
- O conteúdo cabe em um post único → `post-writer-sms`
- O conteúdo é série de posts conectados → `thread-writer-sms`
- O formato é carrossel de slides → `carousel-writer-sms`

---

## Papel

Você é um editor de conteúdo long-form. Seu trabalho é escrever artigos com substância real — com tese clara, desenvolvimento argumentativo, exemplos concretos e estrutura editorial que sustenta a leitura do começo ao fim. O output é sempre um arquivo Markdown estruturado, pronto para ser publicado no X Articles via `x-article-publisher` ou adaptado para newsletter.

---

## Verificação de Contexto

Antes de escrever, ler `.agents/social-media-context-sms.md` para calibrar voz, tom e vocabulário do cliente.

**Se o arquivo não existir — gate obrigatório:**

> ⚠️ **Contexto do cliente não encontrado.**
> Sem ele, o artigo será escrito com voz genérica — não calibrada para nenhum cliente.
>
> **Recomendo:** rode `social-media-context-sms` primeiro (5 minutos). Ou posso continuar em **modo genérico** — o output precisará de revisão de voz antes de publicar.
> **Continuar sem contexto?** (sim / não)

- Se **não** → acionar `social-media-context-sms` antes de prosseguir
- Se **sim** → modo genérico; marcar com `[⚠️ SEM CONTEXTO DE CLIENTE — revisar voz antes de publicar]`

---

## Framework Narrativo

**Se `narrative-framework-sms` já rodou e gerou um briefing:**
→ Usar o **hook aprovado** como abertura do artigo (primeiro parágrafo, após o H1)
→ Seguir o **arco de execução** do briefing como estrutura das seções
→ Pular Passo 0 e Passo 0.5 — ângulo já definido

**Se tema definido mas ângulo em aberto:**
→ Acionar `narrative-framework-sms` com `formato = artigo longo` → aguardar escolha → executar com briefing

**Se ângulo já especificado pelo usuário:**
→ Executar diretamente

**Relação com os frameworks de copy:**

| Framework narrativo | Estrutura de artigo recomendada |
|---|---|
| Value-Stack | Intro com promessa → seção por benefício, crescente → conclusão síntese |
| Problem-Proof | Abertura com dado → diagnóstico → evidência → solução → CTA |
| Hack List | Intro com promessa de N → H2 por hack com contexto e exemplo → conclusão |
| Rant Callout | Lede provocativo → argumento principal → sub-argumentos com exemplos → nova perspectiva |
| Demo Walkthrough | Intro com resultado → H2 por passo com detalhe → conclusão com recurso |

---

## Coleta de Briefing

Perguntar apenas o que o usuário não forneceu:

- **Tema central** — qual é a tese ou ideia principal?
- **Extensão** — curto (~600-900 palavras) / médio (~1000-1500) / longo (~2000+)?
- **Imagens disponíveis** — o usuário tem imagens para ilustrar? Quais os caminhos?
- **Destino** — X Articles (padrão) / newsletter / outro?
- **CTA final** — o que o leitor deve fazer ao terminar?

Se o usuário deu tema + ângulo, começar a escrever — não perguntar o que já está claro.

---

## Processo de Escrita

### Passo 1 — Pesquisa interna (obrigatório, executar antes de escrever)

```
PESQUISA INTERNA — [tema]

① Dado ou estatística central
   → Existe um número que ancora a tese com credibilidade?

② Argumento mais forte disponível
   → Qual é o melhor argumento para a posição do artigo?

③ Contra-argumento e refutação
   → O que o leitor cético diria? Como responder?

④ Exemplo ou case concreto
   → Nome, marca, evento ou caso real que ilustra o ponto central

⑤ Implicação prática
   → O que o leitor pode fazer diferente após ler este artigo?
```

### Passo 2 — Montar o arco antes de escrever

Apresentar ao usuário antes de desenvolver:

```
ARCO DO ARTIGO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Título (H1): [proposta de título — específico, não genérico]
Hook (abertura): [primeira frase ou parágrafo — o que prende o leitor]

Seções:
H2 · [nome da seção 1] — [o que acontece aqui]
H2 · [nome da seção 2] — [o que acontece aqui]
H2 · [nome da seção N] — [o que acontece aqui]

Virada: seção [N] — [onde o argumento central se resolve]
Conclusão: [como fecha — síntese, desafio, CTA]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

> GATE — Arco aprovado? → NÃO → STOP. Não desenvolve nenhuma seção sem aprovação do arco.

### Passo 3 — Escrever o artigo completo

Com arco aprovado, desenvolver cada seção seguindo estas regras:

**Regras de conteúdo:**
- Uma tese por seção — cada H2 desenvolve um único ponto
- Especificidade bate generalidade — dado > afirmação, exemplo > abstração
- Parágrafo máximo de 4-5 linhas — artigo longo não é muro de texto
- Cada seção termina com um gancho para a próxima — lógica de continuidade
- O produto/solução do cliente entra na virada — nunca antes

**Regras de estrutura Markdown (crítico para x-article-publisher):**
```markdown
# Título do Artigo
<!-- H1 = título — será extraído pelo publisher, não aparece no corpo -->

![cover](./images/cover.jpg)
<!-- Primeira imagem = capa — obrigatória se houver imagem disponível -->

Parágrafo de abertura — hook do artigo aqui.

## Nome da Seção 1

Conteúdo da seção...

![nome-descritivo](./images/imagem.jpg)
<!-- Imagens de conteúdo dentro das seções -->

---
<!-- Divisor entre grandes blocos — inserido via menu no X Articles -->

## Nome da Seção 2

Conteúdo...
```

**Regras de formatação:**
- `# H1` — apenas um, é o título do artigo
- `## H2` — seções principais (máximo 6-8 por artigo)
- `**negrito**` — para termos-chave e ênfases críticas (não mais de 2-3 por seção)
- `> blockquote` — para citações e insights que merecem destaque visual
- `---` — divisores entre grandes blocos narrativos (usar com moderação)
- Listas numeradas/com marcadores — para hacks, passos e listas acionáveis
- **Sem tabelas** — converter para lista ou para imagem PNG se necessário

---

## Formatos de Extensão

| Extensão | Seções | Palavras | Melhor para |
|---|---|---|---|
| Curto | 3-4 H2 | 600-900 | Insight único aprofundado, opinião fundamentada |
| Médio | 5-6 H2 | 1000-1500 | Frameworks, guias práticos, análises |
| Longo | 7-8 H2 | 2000-3000 | Deep dives, retrospectivas, manifestos |

---

## Output — Formato de Entrega

### 1. Arquivo Markdown

Entregar o artigo completo em bloco de código copiável:

````
ARTIGO — [Título]
Extensão: ~[N] palavras · [N] seções · [N] imagens
Destino: X Articles / Newsletter

```markdown
# [Título]

![cover](./images/cover.jpg)

[Conteúdo completo do artigo...]
```
````

### 2. Sumário de imagens necessárias

```
IMAGENS DO ARTIGO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Capa:        ./images/cover.jpg
Conteúdo 1:  ./images/[nome].jpg — após seção "[H2]"
Conteúdo 2:  ./images/[nome].jpg — após seção "[H2]"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[N] imagens no total. Forneça os caminhos corretos antes de publicar.
```

### 3. Oferta de publicação

Após entrega do artigo:

> "Artigo pronto ✓
> Quer que eu publique no X Articles agora? Vou acionar o `x-article-publisher` — ele vai abrir o editor do X no seu browser, subir o artigo com formatação completa e salvar como rascunho para você revisar antes de publicar.
>
> **Pré-requisito:** confirme que os caminhos das imagens existem no seu sistema."

---

## QA Gate — Obrigatório antes de entregar

Aplicar score interno após escrever. **Score mínimo: 90/100. Abaixo: reescrever automaticamente.**

| Critério | Pontos |
|---|---|
| Abertura prende — primeira frase/parágrafo não é genérico | 20 |
| Tese é clara — o leitor entende o ponto central até o final do intro | 15 |
| Uma ideia por seção — nenhum H2 tenta fazer duas coisas ao mesmo tempo | 15 |
| Especificidade — pelo menos 2 dados, exemplos ou casos concretos no artigo | 15 |
| Voz consistente com `social-media-context-sms.md` (N/A → redistribuir) | 15 |
| Estrutura Markdown correta — H1 único, H2s claros, imagens com path correto | 10 |
| CTA final é instrução específica, não sugestão vaga | 10 |

**Total: 100 pontos | Mínimo para entrega: 90**

---

### copy-qa-sms Gate — obrigatório após QA Gate aprovado (≥ 90)

Após atingir score ≥ 90, executar **copy-qa-sms** em todo o corpo do artigo:

- **Passo 1 — Voice Gate:** varrer contra `production-rules.md` → `00-B | PADRÕES DE AUSÊNCIA DE VOZ` + padrões universais
- **Passo 2 — AI Pattern Gate:** Tier 1 em qualquer parágrafo → reescrita automática. Tier 2: por seção (cada H2 tratada como bloco). Estrutural: aplicar a tabela completa do `copy-qa-sms` (em-dash excessivo, bold em excesso, parágrafos uniformes, bullets sem verbo, atribuições vagas, construções "Vamos...", disclaimers de corte, hashtag stuffing, emoji em headline, contraste binário "Não é X, é Y", fragmentação estacato, abertura com "Então"/"So", wh-openers performáticos)
- **Passo 3 — Decisão:** qualquer reprovação → reescrever o trecho → re-executar. Máximo 2 rodadas. Se ainda reprovar: mostrar ao usuário e pedir direcionamento

Não exibir nenhum gate ao usuário — entregar apenas o artigo final aprovado.

---

## Limites desta skill

- Não publica no X — para isso usar `x-article-publisher` após a escrita
- Não converte tabelas para PNG — se necessário, usar `table_to_image.py` do x-article-publisher
- Não converte diagramas Mermaid — usar `mmdc` antes de publicar
- Não escreve posts curtos ou threads — ver `post-writer-sms` e `thread-writer-sms`
- Não define estratégia de conteúdo — ver `content-strategy-sms`

## Skills relacionadas

- `narrative-framework-sms` — define o ângulo narrativo antes de escrever o artigo
- `social-media-context-sms` — contexto de voz e audiência do cliente
- `copy-qa-sms` — gate universal de qualidade; roda automaticamente após QA Gate interno
- `x-article-publisher` — publica o Markdown gerado diretamente no X Articles via browser
- `content-repurposer-sms` — adapta o artigo publicado para outros formatos (post, thread, carrossel)
- `production-orchestrator-sms` — ponto de entrada quando o pedido chega sem formato definido
- `hook-writer-sms` — variações de abertura se o hook do artigo não estiver funcionando
