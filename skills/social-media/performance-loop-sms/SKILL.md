---
name: performance-loop-sms
description: "Analisador de performance de conteúdo publicado — recebe dados de posts reais (alcance, engajamento, saves, comentários, conversões) e identifica quais frameworks narrativos, formatos, hooks e temas performam melhor para cada cliente em cada plataforma. Produz um ranking de frameworks por performance e um relatório de aprendizados que retroalimenta o narrative-framework-sms. Usar quando o usuário traz dados de performance ('meu último carrossel teve X impressões'), quando quer entender 'o que está funcionando', quando quer calibrar a estratégia de conteúdo com base em resultados reais, ou para revisão periódica (semanal/mensal) de produção. Não substitui o performance-analyzer-sms — é uma camada de síntese estratégica sobre os dados, não análise individual de post."
metadata:
  version: 1.0.0
---

# Performance Loop — Analisador de Performance e Retroalimentação

## Quando Usar

**Acionamento direto:**
- "O que está funcionando no meu conteúdo?"
- "Quero entender quais posts performam melhor"
- "Revisão mensal de performance"
- "Meu último carrossel teve X impressões — o que isso me diz?"
- "Quero calibrar minha estratégia com base nos dados"

**Acionamento pelo sistema (revisão periódica):**
- `production-orchestrator-sms` — no Tipo 4 (revisão de ciclo), quando usuário traz dados ou pede retrospectiva
- Usuário traz uma batch de dados de performance (semana, mês, trimestre)
- Após 10+ posts publicados com o sistema — dados suficientes para padrão emergir
- Antes de uma nova fase de produção — para calibrar o framework de narrativa

**Não acionar quando:**
- O usuário não tem dados de performance — sem dados, sem análise
- O pedido é análise de um único post — usar `performance-analyzer-sms`
- O pedido é criação de conteúdo — esta skill é retrospectiva, não criativa

---

## Papel

Você é o analista de performance do sistema. Seu trabalho é identificar os padrões que os dados revelam — não o que parece verdade, mas o que os números dizem — e traduzir esses padrões em instruções concretas para calibrar o `narrative-framework-sms`. O output desta skill é um ranking de frameworks atualizado e uma lista de regras aprendidas com os dados reais do cliente.

---

## Dimensões de Análise

Cada post publicado é analisado em 5 dimensões:

| Dimensão | O que medir | Fonte de dado |
|---|---|---|
| **Framework narrativo** | Qual dos 5 frameworks foi usado (Value-Stack, Problem-Proof, Hack List, Rant Callout, Demo Walkthrough) | Briefing do post ou reconstrução pelo copy |
| **Formato** | Carrossel / Thread / Reel / Post longo | Metadado do post |
| **Hook** | Tipo de hook (dado, pergunta, afirmação, número, confronto) | Primeira linha/frase do post |
| **Tema / Pilar** | Qual pilar de conteúdo o post aborda | Classificação manual ou pela matrix de conteúdo |
| **Métricas de performance** | Impressões, alcance, engajamento (%), saves, compartilhamentos, comentários, cliques, conversões | Dados da plataforma |

---

## Métricas por Objetivo

Dependendo do objetivo do cliente, priorizar métricas diferentes:

| Objetivo | Métrica principal | Métricas secundárias |
|---|---|---|
| **Alcance / Topo de funil** | Impressões · Alcance | Compartilhamentos · Visualizações |
| **Engajamento / Autoridade** | Taxa de engajamento (%) · Comentários | Saves · Respostas |
| **Conversão / Leads** | Cliques · DMs · Respostas | Taxa de conversão · CTA clicks |
| **Comunidade / Fidelização** | Saves · Comentários qualitativos | Menções · Respostas de qualidade |

---

## Processo de Execução

### Passo 1 — Coletar os dados

Solicitar ao usuário ou ler do `social-media-context-sms.md`:

```
Para cada post publicado no período:
- Data de publicação
- Plataforma
- Formato (carrossel / thread / reel / post)
- Hook (primeira linha ou frase)
- Framework narrativo usado (se souber)
- Métricas: [impressões] [alcance] [engajamento%] [saves] [comentários] [compartilhamentos] [cliques]
```

Se o usuário não sabe qual framework foi usado → reconstruir a partir do copy ou da estrutura do post.

Se os dados estão em planilha ou print → solicitar que cole os dados em texto ou descreva os posts.

### Passo 2 — Classificar cada post

Para cada post, atribuir:
- **Framework:** Value-Stack / Problem-Proof / Hack List / Rant Callout / Demo Walkthrough / Indefinido
- **Tipo de hook:** Dado · Número · Pergunta · Afirmação confrontadora · Promessa de resultado · Narrativa pessoal
- **Pilar:** conforme definido no `social-media-context-sms.md`
- **Score de performance:** normalizar para comparação entre posts de datas diferentes

**Score de performance (normalizado):**
```
Score = (Engajamento% × 3) + (Saves/Impressões × 5) + (Comentários/Impressões × 4) + (Compartilhamentos/Impressões × 4)
```
Ajustar pesos conforme objetivo do cliente.

### Passo 3 — Identificar padrões

Com os posts classificados, gerar as seguintes análises:

**3A — Ranking de frameworks por performance**
Qual framework tem score médio mais alto para esse cliente nessa plataforma?

**3B — Ranking de tipos de hook**
Qual tipo de hook gera mais engajamento no primeiro slide/linha?

**3C — Temas que mais performam**
Qual pilar/tema gera mais saves? Mais comentários? Mais compartilhamentos?

**3D — Padrões de formato**
Carrossel vs. thread vs. reel — qual formato performa melhor por objetivo?

**3E — Padrões temporais**
Dias e horários de melhor performance (se dados disponíveis).

**3F — Anomalias**
Posts que performaram muito acima ou abaixo da média — o que os diferencia?

### Passo 4 — Gerar regras aprendidas

Traduzir os padrões em regras concretas para o sistema:

```
REGRAS APRENDIDAS — [Cliente] · [Plataforma] · [Período]

Framework com maior score médio: [framework]
→ Instrução para narrative-framework-sms: sugerir [framework] como primeira opção

Hook com maior engajamento: [tipo]
→ Instrução para hook-writer-sms: priorizar hooks de [tipo] nesta plataforma

Tema com mais saves: [pilar]
→ Instrução de calendário: aumentar frequência de [pilar] em X posts/semana

Formato mais eficiente para alcance: [formato]
→ Instrução operacional: priorizar [formato] quando objetivo = alcance

Anomalia positiva: [post] — superou média em [X]%
→ Investigar: [hipótese do que causou a anomalia]

Anomalia negativa: [post] — ficou [X]% abaixo da média
→ Evitar: [hipótese do que causou a queda]
```

### Passo 5 — Atualizar o ranking no social-media-context-sms.md

Propor ao usuário a atualização de uma seção de performance no arquivo de contexto:

```markdown
## Performance Loop — Ranking Atualizado
> Período: [data início] – [data fim] · N posts analisados · Atualizado em [data]

### Ranking de Frameworks (por score médio — [plataforma])
1. [Framework] — score médio [X]
2. [Framework] — score médio [X]
3. [Framework] — score médio [X]
4. [Framework] — score médio [X]
5. [Framework] — score médio [X]

### Hook mais eficiente
[Tipo de hook] — engajamento médio [X]% acima da média geral

### Temas que mais convertem saves
1. [Pilar/tema]
2. [Pilar/tema]

### Regras ativas para produção
- [Regra 1 aprendida com dados]
- [Regra 2 aprendida com dados]
- [Regra 3 aprendida com dados]

### Próxima revisão sugerida
[Data] — após [N] novos posts publicados
```

---

## Output — Relatório de Performance Loop

```
PERFORMANCE LOOP REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Cliente:    [cliente ativo]
Plataforma: [plataforma]
Período:    [data início] – [data fim]
Posts:      [N analisados]
Objetivo:   [alcance / engajamento / conversão]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RANKING DE FRAMEWORKS

🥇 [Framework 1] — score [X] · [N posts]
   Melhor post: "[hook]" → [métricas]

🥈 [Framework 2] — score [X] · [N posts]
   Melhor post: "[hook]" → [métricas]

🥉 [Framework 3] — score [X] · [N posts]

4. [Framework 4] — score [X]
5. [Framework 5] — score [X]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RANKING DE HOOKS

1. [Tipo de hook] — [X]% acima da média
2. [Tipo de hook]
3. [Tipo de hook]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEMAS QUE MAIS PERFORMAM

Saves:           [pilar/tema]
Comentários:     [pilar/tema]
Compartilhamentos: [pilar/tema]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ANOMALIAS

📈 POSITIVA: "[hook do post]"
   Score: [X]% acima da média · Hipótese: [1 linha]

📉 NEGATIVA: "[hook do post]"
   Score: [X]% abaixo da média · Hipótese: [1 linha]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REGRAS APRENDIDAS

→ [Regra 1 — instrução acionável]
→ [Regra 2 — instrução acionável]
→ [Regra 3 — instrução acionável]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CALIBRAÇÃO DO NARRATIVE-FRAMEWORK-SMS

Para o próximo ciclo de produção:
Framework recomendado como padrão: [framework]
Hook recomendado como ponto de partida: [tipo]
Temas para aumentar frequência: [lista]
Temas para reduzir: [lista]

→ Quer que eu atualize o social-media-context-sms.md com o ranking e as regras?
```

---

## Retroalimentação para o narrative-framework-sms

Quando o `narrative-framework-sms` é acionado após um Performance Loop rodado, ele lê o ranking atualizado no `social-media-context-sms.md` e:

1. **Apresenta os frameworks em ordem de ranking** (não sempre A/B/C/D/E — mas em ordem de performance histórica do cliente)
2. **Adiciona nota de performance** ao lado de cada framework:
   ```
   A · VALUE-STACK  ← 🥇 melhor performance histórica para [cliente]
   B · PROBLEM-PROOF
   C · HACK LIST    ← 📈 melhor para saves nesta plataforma
   ```
3. **Sinaliza quando a escolha do usuário vai contra os dados:**
   ```
   ⚠️ Você escolheu Rant Callout — nos últimos 30 dias, esse framework teve o menor score 
   para [cliente] no LinkedIn. Quer continuar mesmo assim ou revisitar as opções?
   ```

Essa retroalimentação não bloqueia a escolha do usuário — apenas informa com dados antes de executar.

---

## Cadência de Revisão Sugerida

| Volume de produção | Frequência ideal | Mínimo de posts para padrão |
|---|---|---|
| 1–2 posts/semana | Revisão mensal | 8–10 posts |
| 3–5 posts/semana | Revisão quinzenal | 15–20 posts |
| 5+ posts/semana | Revisão semanal | 20+ posts |

Com menos de 5 posts no período, os dados são insuficientes para ranking confiável. Relatar os dados sem gerar ranking — aguardar mais volume.

---

## Boundaries

- Não gera dados que o usuário não forneceu — se os dados estão incompletos, relata o que foi analisado e indica as lacunas
- Não usa score para bloquear criação — apenas informa e calibra sugestões
- Não analisa posts individuais em profundidade — para isso, usar `performance-analyzer-sms`
- Não faz projeções de crescimento — analisa padrões históricos, não prevê futuro
- A atualização do `social-media-context-sms.md` sempre requer confirmação do usuário antes de ser executada

## See also

**production-orchestrator-sms** — aciona esta skill no Tipo 4 (revisão de ciclo); encaminha para Tipo 1 ou 3 após o relatório
**narrative-framework-sms** — recebe o ranking e calibra as sugestões de framework
**performance-analyzer-sms** — análise profunda de post individual (complementar, não substituto; Tipo 5 no orquestrador)
**social-media-context-sms** — arquivo que armazena o ranking atualizado entre sessões
**content-calendar-sms** — usa os dados de tema para calibrar frequência no calendário
**audience-watering-hole-sms** — quando os dados revelam baixa performance, pode indicar desalinhamento de linguagem com a audiência
