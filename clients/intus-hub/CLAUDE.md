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

## Templates disponíveis em `references/`

### Carrossel (Instagram 4:5 · 1080×1350px)

| Arquivo | Estilo | Quando usar |
|---|---|---|
| `TEMPLATE-SLIDE-CLARA.json` | Fundo branco, headline ultra bold condensed 96px, acento laranja #E8722A | Conteúdo de impacto com palavra-chave destacada; acento laranja no copy |
| `TEMPLATE-SLIDE-ESCURA.json` | Gradiente marrom-escuro (#2A1500→#0F0500), mesma estrutura da Clara | Versão noturna; ideal para alternância clara/escura slide a slide |
| `TEMPLATE-SLIDE-TWITTER-POST.json` | Fundo branco, estilo post de Twitter, texto corrido 34px FIXO, avatar circle no header | Conteúdo educacional/jornalístico; sem headline condensada; texto como protagonista |
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

## Regra de produção

Nunca entregue sem confirmar a voz do cliente contra o que está em `.agents/social-media-context-sms.md`.
Se algum arquivo de contexto estiver ausente ou vazio, informe antes de produzir.
