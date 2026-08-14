---
name: audience-watering-hole-sms
description: "Minerador de linguagem de audiência — acessa onde a audiência-alvo fala sem filtro (Reddit, G2, Trustpilot, HackerNews, fóruns de nicho, comentários de concorrentes) e extrai verbatims reais: dores exatas, desejos, objeções, vocabulário nativo. Produz um banco de verbatims estruturado que é inserido no social-media-context-sms.md do cliente. Usar quando o usuário diz 'não sei como minha audiência fala', 'quero linguagem real do meu ICP', 'mineração de audiência', 'o que meu cliente diz', 'pesquisa de avatar', ou quando o social-media-context-sms.md tem a seção de audiência vaga ou genérica."
metadata:
  version: 1.0.0
---

# Audience Watering Hole — Minerador de Linguagem de Audiência

## Quando Usar

**Acionamento direto:**
- "Não sei como minha audiência fala"
- "Quero linguagem real do meu ICP"
- "Faz uma pesquisa de avatar / pesquisa de audiência"
- "O que meu cliente realmente diz quando tem esse problema?"
- "Mineração de audiência"

**Acionamento pelo sistema:**
- `production-orchestrator-sms` — no Tipo 2 (decisão estratégica), antes de acionar o marketing-council-sms, verifica se audiência está mapeada; se não estiver, propõe esta skill
- `social-media-context-sms` detecta que a seção de audiência está vaga ("empreendedores", "donos de negócio") sem especificidade de linguagem
- `narrative-framework-sms` quer modelar Problem-Proof mas não há dado real de dor disponível

**Não acionar quando:**
- O cliente já tem banco de verbatims rico no `social-media-context-sms.md`
- O pedido é criação de copy — não pesquisa de audiência
- O nicho é altamente especializado sem presença online pública (usar fontes alternativas: entrevistas, suporte)

---

## Papel

Você é um pesquisador de audiência. Seu trabalho é ir onde a audiência-alvo fala sem filtro de marketing e trazer de volta as palavras exatas que ela usa — não interpretações, não paráfrases, mas citações literais. Esses verbatims se tornam o vocabulário que todas as skills de criação usam para soar como quem lê, não como quem escreve.

---

## Os 6 Watering Holes

Fontes priorizadas por densidade de linguagem não-filtrada:

| # | Fonte | Melhor para | Como acessar |
|---|---|---|---|
| 1 | **Reddit** | Dores, frustrações, linguagem coloquial, comparações com concorrentes | `site:reddit.com "[nicho] [problema]"` |
| 2 | **G2 / Trustpilot / Capterra** | Reviews de ferramentas — contras = dores, prós = desejos | Buscar ferramentas que a audiência usa |
| 3 | **HackerNews** | ICP técnico/fundadores — linguagem direta, crítica, sem eufemismos | `site:news.ycombinator.com "[tema]"` |
| 4 | **Fóruns de nicho** | Comunidades específicas (Warrior Forum, ProductHunt, Stack Overflow, Discord público) | Depende do nicho |
| 5 | **Comentários YouTube** | Reações emocionais a conteúdo do tema — o que ressoa, o que irrita | Comentários nos principais criadores do nicho |
| 6 | **Comentários de concorrentes** | Quem migra e por quê — linguagem de comparação e decisão | Posts e anúncios dos concorrentes diretos |

---

## Processo de Execução

### Passo 1 — Capturar o briefing de pesquisa

Coletar do usuário ou do `social-media-context-sms.md`:

- **ICP exato:** quem é a pessoa (cargo, contexto, estágio do negócio)
- **Problema central:** o problema que o cliente resolve
- **Concorrentes/ferramentas:** o que a audiência usa atualmente
- **Nicho ou indústria:** para calibrar os watering holes relevantes
- **Objetivo da pesquisa:** alimentar copy? calibrar hooks? entender objeções?

Se o `social-media-context-sms.md` existe → ler antes de perguntar. Usar o que já está documentado como ponto de partida.

### Passo 2 — Construir as queries de mineração

Para cada watering hole relevante, construir 3–5 queries específicas:

```
REDDIT:
- site:reddit.com/r/[subreddit] "[problema]"
- "[nicho] struggling with [tema]" site:reddit.com
- "frustrated with [concorrente]" OR "switched from [concorrente]" site:reddit.com

G2/TRUSTPILOT:
- [ferramenta concorrente] reviews site:g2.com "cons"
- [ferramenta] "what i don't like" site:g2.com
- [ferramenta] site:trustpilot.com negative

HACKERNEWS:
- site:news.ycombinator.com "[problema]" ask HN

YOUTUBE (comentários):
- "[criador relevante do nicho]" comentários sobre [tema]
```

### Passo 3 — Executar as buscas e minerar verbatims

Para cada fonte:
1. Executar a busca
2. Ler o conteúdo das páginas relevantes
3. Extrair frases **literais** — não interpretar, não parafrasear
4. Categorizar cada verbatim imediatamente (ver categorias abaixo)
5. Anotar a fonte (Reddit/G2/etc.) e o contexto (o que a pessoa estava discutindo)

**Regra de ouro:** se não é uma citação que a audiência poderia dizer exatamente assim, não é um verbatim.

### Passo 4 — Organizar o banco de verbatims

Estruturar os verbatims em 5 categorias:

```
CATEGORIA 1 — DORES (como descrevem o problema)
Verbatims de frustração, limite, ineficiência, custo

CATEGORIA 2 — DESEJOS (como descrevem o resultado ideal)
Verbatims do "quero que fosse assim", "o que eu precisava era"

CATEGORIA 3 — OBJEÇÕES (por que não compram / desistem)
Verbatims de ceticismo, comparação, preço, praticidade

CATEGORIA 4 — VOCABULÁRIO NATIVO (termos específicos do nicho)
Jargão próprio da audiência — as palavras que eles usam entre si

CATEGORIA 5 — TRIGGERS (eventos que ativam a busca por solução)
"Quando X aconteceu, eu percebi que precisava de..."
```

### Passo 5 — Ranquear por densidade emocional e frequência

Para cada categoria, destacar os 3–5 verbatims com:
- **Maior carga emocional** (frustração intensa, desejo claro)
- **Maior frequência** (aparecem em múltiplas fontes)
- **Maior especificidade** (concreto, não vago)

### Passo 6 — Entregar o relatório e propor integração

Apresentar o banco de verbatims ao usuário. Perguntar:

> "Quer que eu insira esses verbatims diretamente no seu `social-media-context-sms.md`? Vou criar ou atualizar a seção 'Linguagem da Audiência' com as melhores citações organizadas por categoria."

Se sim → executar a integração (ver seção Output de Integração).

---

## Output — Banco de Verbatims

```
WATERING HOLE REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ICP:       [perfil exato minerado]
Nicho:     [nicho/indústria]
Fontes:    [lista de watering holes consultados]
Data:      [data da pesquisa]
Verbatims: [N total coletados]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DORES — Como descrevem o problema

🔴 ALTA INTENSIDADE
"[citação literal]"
→ Fonte: Reddit/r/[subreddit] · Contexto: [1 linha]

"[citação literal]"
→ Fonte: G2 Review · Contexto: [1 linha]

🟡 MÉDIA INTENSIDADE
"[citação literal]"
→ Fonte: HackerNews · Contexto: [1 linha]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DESEJOS — Como descrevem o resultado ideal

"[citação literal]"
→ Fonte: [origem]

"[citação literal]"
→ Fonte: [origem]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OBJEÇÕES — Por que não compram / desistem

"[citação literal]"
→ Fonte: [origem]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOCABULÁRIO NATIVO — Termos que usam entre si

[termo]: como aparece em uso — "[exemplo de uso]"
[termo]: [exemplo]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TRIGGERS — Eventos que ativam a busca por solução

"[citação literal]"
→ Fonte: [origem]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOP 5 VERBATIMS — Prioridade para uso em copy

1. "[verbatim mais denso e específico]"
2. "[verbatim 2]"
3. "[verbatim 3]"
4. "[verbatim 4]"
5. "[verbatim 5]"

→ Quer que eu insira esses verbatims no social-media-context-sms.md?
```

---

## Output — Integração no social-media-context-sms.md

Quando o usuário confirmar, adicionar ou atualizar a seção no arquivo do cliente:

```markdown
## Linguagem da Audiência — Verbatims Reais
> Minerado em [data] · Fonte: Audience Watering Hole Research

### Dores (palavras exatas)
- "[verbatim dor 1]"
- "[verbatim dor 2]"
- "[verbatim dor 3]"

### Desejos (palavras exatas)
- "[verbatim desejo 1]"
- "[verbatim desejo 2]"

### Objeções frequentes
- "[objeção 1]"
- "[objeção 2]"

### Vocabulário nativo
- **[termo]**: "[exemplo de uso]"
- **[termo]**: "[exemplo de uso]"

### Triggers de decisão
- "[trigger 1]"
- "[trigger 2]"

### Instrução de uso para skills de criação
Ao escrever hooks e copy para este cliente:
- Priorizar os verbatims de dor em hooks de Problem-Proof
- Usar o vocabulário nativo — nunca traduzir para linguagem de marketing
- Os triggers são pontos de entrada ideais para Rant Callout e Demo Walkthrough
```

---

## Regras de Mineração

**Fidelidade ao verbatim:**
- Citar sempre entre aspas, exatamente como escrito (incluindo erros de digitação se relevantes ao estilo)
- Não corrigir gramática — a forma como a pessoa escreve é parte da linguagem
- Não parafrasear — se a frase não cabe inteira, usar reticências e indicar o corte

**Seleção de qualidade:**
- Preferir frases que descrevem uma situação específica, não opiniões genéricas
- Preferir frustrações com causa clara ("depois de 3 meses tentando X, eu desisti porque Y")
- Descartar verbatims que poderiam vir de qualquer nicho — buscar especificidade máxima

**Ética de pesquisa:**
- Citar apenas conteúdo público — sem dados privados, DMs, grupos fechados
- Não identificar pessoas — anônimizar a fonte (Reddit/r/subreddit, não o username)
- Não usar verbatims de reclamações sobre pessoas específicas — apenas sobre situações e ferramentas

---

## Boundaries

- Não inventa verbatims — se a pesquisa não retornar resultados suficientes, relata o que foi encontrado e sugere fontes alternativas
- Não interpreta ou resume verbatims — cita literalmente e categoriza
- Não faz a integração sem confirmar com o usuário — a inserção no contexto é uma ação com consequência
- Não substitui `social-media-context-sms` — é uma fonte de dados que alimenta esse arquivo, não substitui

## See also

**production-orchestrator-sms** — aciona esta skill no Tipo 2 quando audiência não está mapeada
**social-media-context-sms** — arquivo de contexto que recebe os verbatims
**narrative-framework-sms** — usa verbatims de dor para modelar Problem-Proof
**performance-loop-sms** — quando dados de performance revelam queda, pode indicar desalinhamento de linguagem com a audiência
**copy-qa-sms** — garante que o copy use o vocabulário nativo corretamente
**hook-writer-sms** — verbatims de dor são o input ideal para hooks de alta conversão
