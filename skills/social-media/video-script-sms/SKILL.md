---
name: video-script-sms
description: "When the user wants to write a video script, reel, talking head, voiceover, TikTok video, Instagram Reel, YouTube Shorts, long-form YouTube video, video sales letter (VSL), webinar script, or when they mention 'roteiro', 'script', 'cenas', 'narração', 'gravar vídeo', 'fazer reel', 'fazer TikTok'. Also use when content-repurposer identifies a Reel/TikTok/Short derivative and hands off for scripting. Covers spoken video (talking head), voiceover, and animated video structure. For animated/motion design output, combine with huashu-design."
metadata:
  version: 1.3.0
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
- CTA desejado ao final
- Tom da cena (urgente, descontraído, emocional, técnico)
- Restrições (não mencionar concorrentes, evitar jargão X)

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

## Hooks por plataforma — referência rápida

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
