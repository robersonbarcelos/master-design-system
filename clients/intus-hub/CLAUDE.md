# Intus Hub — Contexto de Produção

> Este arquivo é lido automaticamente pelo Claude Code ao abrir esta pasta.

---

## Ativação automática

Você está trabalhando com o cliente **Intus Hub (Diego Spanevello)**.

Ao iniciar qualquer sessão nesta pasta, leia obrigatoriamente em sequência:

1. `.agents/social-media-context-sms.md` — voz, pilares, plataformas, público cripto brasileiro
2. `brand-spec.md` — identidade visual Intus, paleta, tipografia
3. `DESIGN.md` — referência visual para geração de código e componentes

Confirme em uma linha antes de iniciar: *"Trabalhando com Diego — Intus Hub. O que vamos produzir hoje?"*

---

## GATE OBRIGATÓRIO — Calibração de Headlines ⚠️

Antes de entregar qualquer variação de gancho ou headline de capa para Intus Hub, **obrigatoriamente cotejar contra `references/headlines-vencedoras.md`**.

O hook aprovado deve se enquadrar em pelo menos 1 dos 11 padrões catalogados.
Hook que não passa: reescrever até enquadrar — nunca entregar headline genérica.

Este gate roda dentro do `narrative-framework-sms` (Passo 1.5) e dentro do `carousel-writer-sms` (FASE 1, após propor os 3 ângulos).

---

## Templates disponíveis em `references/`

### Carrossel (Instagram 4:5 · 1080×1350px)

| Arquivo | Estilo | Quando usar |
|---|---|---|
| `TEMPLATE-SLIDE-CLARA.json` | Fundo branco, headline ultra bold condensed 96px, acento laranja #E8722A | Conteúdo de impacto com palavra-chave destacada; acento laranja no copy |
| `TEMPLATE-SLIDE-ESCURA.json` | Gradiente marrom-escuro (#2A1500→#0F0500), mesma estrutura da Clara | Versão noturna; ideal para alternância clara/escura slide a slide |
| `TEMPLATE-SLIDE-TWITTER-POST.json` | Fundo branco, estilo post de Twitter, texto corrido 34px FIXO, avatar circle no header | Conteúdo educacional/jornalístico; sem headline condensada; texto como protagonista |
| `TEMPLATE-SLIDE-BOLD-HIGHLIGHT.json` | Estilo Twitter/X-post gráfico: headline condensada extra-bold, highlight sólido dourado, rabiscos/setas/círculos à mão, alternância dark (#050D1F) / light (#F0F4FF) | Storytelling de autoridade pessoal do Diego, bastidores, prova social; quando o objetivo é retenção de swipe via variação visual forte |
| `TEMPLATE-SLIDE-BLANK.json` | Off-white #F7F5F1, Archivo Black, múltiplas capas ilustradas + slides internos | Arquivo mestre com variações de capa 3D/render + slides internos; tipografia editorial própria |
| `TEMPLATE-SISTEMA-CAMI-INTUS.json` | Sistema editorial completo Intus Hub | Sistema com regras visuais completas para toda linha editorial |

### Estático (NÃO usar para carrossel)

| Arquivo | Uso |
|---|---|
| `TEMPLATE-INTUS-AI-NEWS.json` | Posts estáticos de notícias de IA — badge + headline bold + imagem de personagem |

### Referências de conteúdo (não são templates visuais)

| Arquivo | Uso |
|---|---|
| `REFERENCIA-CARROSSEL-TWITTER.md` | Referência de conteúdo para carrosseis no estilo Twitter |
| `copies-aprovadas.md` | Banco de copies aprovadas pelo cliente |
| `dados-ancora.md` | Dados e números âncora para copy |
| `temas.md` | Temas e pilares de conteúdo |

---

## Salvamento de artefatos

Salve todos os artefatos de produção em `runs/[AAAA-MM-DD]/`.

Use a data de hoje como nome da pasta. Se a pasta não existir, crie-a.

### Convenção de nomes de arquivo

| Tipo de artefato | Nome do arquivo |
|---|---|
| 3 ângulos propostos | `angulos-[tema].md` |
| Script de carrossel aprovado | `carrossel-[tema].md` |
| Variações de capa | `capas-[tema].md` |
| Variações de legenda | `legendas-[tema].md` |
| JSONs de capa solicitados | `json-capas-[tema].md` |
| Roteiro de vídeo | `roteiro-[tema].md` |
| Copy de post | `post-[tema].md` |
| Briefing de LP | `lp-briefing-[tema].md` |

Use kebab-case para o tema. Ex: `halvng-bitcoin`, `ethereum-staking`, `defi-iniciantes`.

---

## Gate de Carrossel — Vinculação ao Produto ⚠️

Antes de modelar qualquer ângulo de carrossel para o Intus Hub, perguntar OBRIGATORIAMENTE:

> "Quer vincular este carrossel ao Super Agente no CTA final, ou é conteúdo de autoridade pura (follow/save)?"

**Contexto:** Intus Hub é a marca/pessoa (Diego Spanevello). Super Agente é um produto específico com LP própria. Nem todo carrossel educativo deve ter CTA de produto — forçar a conexão dilui a autoridade e prejudica o alcance.

| Modo | O que muda |
|---|---|
| **[A] Autoridade pura** | Nenhum slide menciona o Super Agente. CTA final: seguir / salvar / comentar. |
| **[B] Vinculado ao produto** | Slides educativos sem produto. CTA final (virada): conexão sutil ao Super Agente. |

**Regra de ouro:** o produto entra APENAS no slide final — nunca no gancho, nunca no ângulo.
Se a conexão parecer forçada no briefing, escolher modo [A] por padrão.

Este gate roda antes do `narrative-framework-sms`, pois define a intenção do arco antes de modelar os ângulos.

---

## Gate de Gancho de Capa — Seleção pelos 11 Padrões ⚠️

**Este gate roda OBRIGATORIAMENTE após o Gate de Vinculação ao Produto e ANTES de propor os 3 ângulos narrativos.**

### Quando acionar
Sempre que o usuário pedir um carrossel para Intus Hub e passar o tema — independentemente de ser autoridade pura ou vinculado ao produto.

### Fluxo obrigatório

**Passo 1 — Ler o arquivo de padrões**
Ler `references/headlines-vencedoras.md` na íntegra antes de qualquer modelagem.

**Passo 2 — Selecionar os 7 padrões mais fortes para o tema**
Dos 11 padrões catalogados, identificar os 7 que melhor se encaixam com:
- A tensão central do conteúdo
- O dado mais forte disponível
- O público (empreendedores 25–45 que tentaram IA e falharam)

**Passo 3 — Apresentar os 7 padrões com 3 variações cada**

Para cada um dos 7 padrões selecionados, apresentar no formato:

```
PADRÃO [N] — [NOME]
Fórmula: `[fórmula do padrão]`

A: [variação de gancho — dados reais, voz Diego, sem travessão, sem adjetivo vago]
B: [variação de gancho — ângulo diferente, mesmo padrão]
C: [variação de gancho — mais curta ou mais ousada]
```

**Regras das variações:**
- Usar apenas dados reais do conteúdo (nunca inventar número)
- Tom de repórter — sem adjetivo vago antes de dado
- Sem travessão (—) em nenhuma variação
- Cada variação deve ser diferente o suficiente para ser uma escolha real
- A variação C pode ser a mais arriscada/ousada das três

**Passo 4 — Aguardar seleção**

Perguntar: *"Qual padrão e variação você prefere para a capa? Posso ajustar antes de modelar os ângulos."*

**Somente após a confirmação do usuário,** prosseguir para propor os 3 ângulos narrativos — com a capa usando o padrão e variação aprovados.

### O que NÃO fazer
- Nunca propor ângulos antes de passar pelo gate de gancho
- Nunca apresentar menos de 7 padrões (a menos que o tema genuinamente não encaixe em mais de 7 — caso raro, justificar)
- Nunca inventar variações genéricas — cada variação deve ser específica ao tema passado
- Nunca pular este gate alegando que "o padrão já é óbvio" — a aprovação do usuário é obrigatória

---

## Gate de Geração de Imagem — Template Twitter Post ⚠️

**Quando este gate dispara:**
- Quando o usuário confirmar que o template é **TEMPLATE-SLIDE-TWITTER-POST**, OU
- Quando o `production-orchestrator-sms` concluir o ciclo `carousel-writer-sms → copy-qa-sms` para Intus Hub com este template

**O que fazer:** perguntar OBRIGATORIAMENTE:

> "Você quer o **JSON completo dos slides** (copy estruturado pronto para revisar) ou quer que eu **gere as imagens finais direto** (pipeline GPT → composite)?"

| Resposta | O que fazer |
|---|---|
| **JSON completo** | Entregar o copy de cada slide estruturado por zones (hook/body/scene) em JSON — sem rodar o CLI |
| **Imagens direto** | Acionar a skill `intus-hub-twitter-slide` e rodar `gen_twitter_slide.py` com os parâmetros de cada slide |

**Nunca assumir uma opção.** Aguardar a escolha antes de produzir qualquer coisa.

### Se escolher "Imagens direto":

**Ler obrigatoriamente antes de qualquer geração:**
```
references/PRD-TWITTER-POST-SLIDE.md
```
Este arquivo contém todas as regras operacionais: avatar coords, detect_slot(), PowerShell vs Bash, modos de falha e o comando exato.

Acionar obrigatoriamente a skill:

```
/intus-hub-twitter-slide
```

Esta skill documenta o CLI canônico (`clients/intus-hub/tools/gen_twitter_slide.py`) que:
- Carrega a chave OpenAI automaticamente (não perguntar ao usuário)
- Tem todo o pipeline embutido: GPT Image → resize → avatar composite → detect_slot() → scene composite
- Aceita `--hook`, `--body`, `--scene`, `--slide-num` como argumentos diretos

**Nunca reescrever o pipeline do zero.** Nunca pedir a chave da API. Nunca usar coordenada fixa de slot.

---

## Regra de produção

Nunca entregue sem confirmar a voz do cliente contra o que está em `.agents/social-media-context-sms.md`.
Se algum arquivo de contexto estiver ausente ou vazio, informe antes de produzir.
