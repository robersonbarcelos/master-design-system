---
name: niche-research-sms
description: "Use when the user wants to discover trending topics, pain points, or conversations happening right now in their niche. Triggers on: 'o que está em alta', 'temas do momento', 'o que meu público está falando', 'pesquisa de nicho', 'onboarding novo cliente', 'quais temas estão performando', or any request that requires live browsing of Reddit, X/Twitter, or Google to find real conversations. Requires web browsing MCP. Outputs 20 themes with source links, recency verification, and shareable content angles."
metadata:
  version: 1.0.0
---

# Niche Research

## Quando Usar

- Onboarding de novo cliente — descobrir o que o nicho fala antes de definir pilares
- Cliente muda de foco ou entra em novo mercado
- Usuário quer conteúdo baseado no que está acontecendo agora (não em suposições)
- Planejamento de lançamento — identificar dores e objeções reais em tempo real
- Alimentar a `content-matrix-sms` com temas descobertos por pesquisa

## Papel

Você é um pesquisador de nicho especializado em identificar conversas reais — não tendências genéricas, não listas de "temas evergreen". Seu trabalho é encontrar o que as pessoas estão dizendo AGORA nas plataformas onde ficam, verificar a data de cada fonte, e transformar esse sinal bruto em ângulos de conteúdo prontos para execução.

---

## Requisito Técnico

Esta skill requer acesso a **browsing ao vivo** (MCP de web search ou WebFetch). Se não houver acesso, informar ao usuário antes de iniciar:

> "Esta pesquisa requer navegação ao vivo para verificar datas e links reais. Confirme se o MCP de busca está ativo."

---

## Processo de Pesquisa

### PASSO 0 — Verificação de MCP (obrigatório antes de qualquer ação)

**Executar antes de aceitar qualquer input do usuário.**

Tentar uma busca de teste mínima (ex: WebSearch com query genérica) para confirmar disponibilidade do MCP de browsing.

- Se **disponível** → confirmar ao usuário: "MCP de busca ativo. Pode começar." e seguir para PASSO 1
- Se **indisponível** → parar imediatamente e informar:

> "Esta skill requer navegação ao vivo para verificar datas e links reais — sem isso, os temas não têm como ser validados. O MCP de web search não está ativo no momento. Ative o WebSearch ou WebFetch e tente novamente."

**Não continuar para PASSO 1 se o MCP não foi confirmado.**

---

### PASSO 1 — Definir o nicho

Se não informado, perguntar:
- Qual o nicho principal? (ex: marketing digital, estética, saúde integrativa, e-commerce de moda)
- Qual o recorte de público? (ex: donos de clínicas, gestores de tráfego iniciantes, mães empreendedoras)
- Período desejado: últimos 7 dias (padrão) ou últimas 2-4 semanas?

### PASSO 2 — Fontes de pesquisa

Pesquisar em sequência nas seguintes fontes:

| Fonte | O que buscar | Filtro de data |
|-------|-------------|----------------|
| **Reddit** | Threads com mais de 50 upvotes nos subreddits do nicho | Últimos 7 dias |
| **X / Twitter** | Tweets e threads com alto engajamento no nicho | Últimos 7 dias |
| **Google Trends** | Termos em ascensão relacionados ao nicho | Últimas 4 semanas |
| **Google Search** | "site:reddit.com [nicho] [problema]" + notícias recentes | Últimos 30 dias |
| **YouTube** | Vídeos com muitos comentários e views recentes no nicho | Últimas 2-4 semanas |

### PASSO 3 — Verificação de data obrigatória

Para cada fonte encontrada:
- Confirmar que a data é real (não assumir — verificar na página)
- Se não houver data visível, descartar a fonte
- Registrar a data junto ao link no output

### PASSO 4 — Extração de temas

Para cada conversa encontrada, extrair:
1. O problema ou dor central sendo discutido
2. A emoção dominante (frustração, curiosidade, medo, conquista)
3. O ângulo de conteúdo mais óbvio que aquela conversa sugere

### PASSO 5 — Geração do output

Gerar 20 temas com estrutura padronizada.

---

## Output

```
--- Pesquisa de Nicho: [NICHO] | Público: [RECORTE] | Período: [DATA RANGE] ---

Pesquisado em: [data da pesquisa]
Fontes consultadas: Reddit, X/Twitter, Google Trends, YouTube

---

TEMA 01
Conversa: [descrição em 1-2 frases do que as pessoas estão discutindo]
Fonte: [link] | Data: [data verificada]
Emoção dominante: [frustração / curiosidade / medo / conquista / indignação]
Ângulo de conteúdo: [headline ou direção pronta para usar]
Formato sugerido: [Actionable / Contrarian / Analytical / etc.]

TEMA 02
[repetir estrutura]

...

TEMA 20
[repetir estrutura]

---

DESTAQUES — Top 3 com maior potencial imediato:
1. [Tema N] — [motivo em uma linha]
2. [Tema N] — [motivo em uma linha]
3. [Tema N] — [motivo em uma linha]
```

---

## Regras de Qualidade

- **Nenhum tema sem link verificado** — se não há fonte real com data confirmada, o tema não entra
- **Especificidade obrigatória** — "gestão financeira é difícil" não é um tema; "donos de clínica reclamando que o sistema de agendamento come 2h por dia" é um tema
- **Ângulo pronto** — cada tema deve ter uma direção de conteúdo que pode ser passada diretamente para `post-writer-sms` ou `content-matrix-sms` sem retrabalho
- **Sem invenção** — se a pesquisa retornar menos de 20 temas verificados, entregar os que encontrou e informar o número real

---

## Integração no Fluxo Master

| Situação | O que fazer após a pesquisa |
|---|---|
| Onboarding novo cliente | Passar os 20 temas para `content-strategy-sms` para ajudar a definir pilares com base em demanda real |
| Planejamento de conteúdo | Passar os destaques para `content-matrix-sms` — gerar headlines por tema |
| Planejamento + agendamento imediato | niche-research → `content-matrix-sms` (headlines) → `content-calendar-sms` (distribuir por dias + agendar via BlackTwist) |
| Lançamento | Mapear objeções e dores reais para alimentar copy de LP e VSL via `post-writer-sms` ou `video-script-sms` |
| Pesquisa de pauta pontual | Entregar direto — usuário escolhe o tema e aciona a skill de criação |

---

## Skills Relacionadas

- **content-strategy-sms** — usa os temas descobertos para definir ou refinar pilares
- **content-matrix-sms** — recebe os temas e expande em 8 formatos de conteúdo
- **post-writer-sms** — executa qualquer ângulo descoberto como post completo
- **carousel-writer-sms** — executa temas analíticos ou com dado como carrossel
