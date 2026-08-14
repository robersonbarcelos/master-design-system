# lp-mentoria-ia

Landing page da **Mentoria IA — INTUS HUB**.  
Página de captação de leads para empresas que querem implementar Inteligência Artificial nos processos internos, com formulário multi-step de diagnóstico gratuito e integração com Supabase + Telegram.

---

## Visão Geral

A landing page apresenta a proposta de valor da mentoria, coleta leads qualificados através de um formulário de 7 etapas e notifica a equipe em tempo real via Telegram.

**URL de produção:** `ia-ia.vercel.app` / `intushub.com.br/mentoria`

---

## Stack

- **HTML puro** + **CSS custom properties** + **JavaScript vanilla** — zero dependências de framework
- **Fontes self-hosted** (woff2) — sem requisições externas para Google Fonts
- **Supabase** — banco de dados PostgreSQL para armazenamento dos leads
- **Edge Function** — notificação instantânea via Telegram a cada novo lead
- **Deploy:** Vercel ou Cloudflare Pages (HTML estático, sem build)

---

## Estrutura de Arquivos

```
lp-mentoria-ia/
├── public/                          ← arquivos servidos publicamente
│   ├── index.html                   ← página principal da mentoria
│   ├── mentoria/
│   │   └── index.html               ← rota limpa /mentoria (redirect)
│   ├── fonts/                       ← fontes woff2 self-hosted
│   │   ├── space-grotesk-*.woff2    ← fonte principal (display)
│   │   ├── inter-*.woff2            ← fonte corpo
│   │   └── jetbrains-mono-*.woff2   ← fonte mono (tags/labels)
│   ├── assets/
│   │   ├── hexmark.svg              ← logo hexágono INTUS HUB
│   │   ├── hexgrid.svg              ← padrão de fundo decorativo
│   │   └── grain.svg                ← textura de grain
│   ├── diego.jpg                    ← foto principal (hero + OG image)
│   └── diego.webp                   ← versão webp otimizada
├── supabase/
│   ├── config.toml                  ← configuração do projeto Supabase
│   ├── functions/
│   │   └── notify-telegram/
│   │       └── index.ts             ← Edge Function: envia lead para Telegram
│   └── migrations/
│       ├── 20260704_notify_telegram.sql         ← trigger de notificação
│       └── 20260706_add_ia_impact_columns.sql   ← colunas de impacto de IA
├── .gitignore
├── CLOUDFLARE-PAGES.md              ← instruções de deploy no Cloudflare
├── MAP.md                           ← mapa de estrutura do projeto
└── README.md
```

---

## Seções da Landing Page

| Seção | Descrição |
|-------|-----------|
| **Hero** | Título principal, vídeo VSL do Diego, CTA primário |
| **Dor** | 3 problemas reais que empresas enfrentam (manifesto editorial) |
| **Solução** | Como a mentoria resolve em 3 etapas (timeline com dots) |
| **Como funciona** | Dashboard animado + 3 passos do processo |
| **Cases** | Resultados de clientes com métricas reais |
| **Diagnóstico** | CTA secundário para o formulário |
| **FAQ** | Perguntas frequentes em accordion |
| **Footer** | Links e identidade INTUS HUB |

---

## Formulário Multi-Step

7 etapas de qualificação de lead:

1. **Identificação** — Nome, empresa, cargo
2. **Contato** — Email, WhatsApp
3. **Perfil da empresa** — Segmento, faturamento, tamanho do time
4. **Desafios** — Áreas com maior gargalo (multi-seleção)
5. **Ferramentas de IA** — Nível de uso atual (0 = sem conhecimento / 5 = avançado)
6. **Impacto esperado** — Economia esperada em 12 meses, disposição a investir
7. **Urgência** — Prazo e decisor

Ao enviar, o lead é salvo no Supabase e uma notificação é disparada via Telegram.

---

## Integração Supabase

### Tabela `leads`

Armazena todos os campos do formulário:

```sql
nome, empresa, email, whatsapp, segmento, cargo,
faturamento, time_empresa, urgencia, decisor,
area, gargalo, ferramentas_ia, economia_esperada,
disposicao_investir
```

### Edge Function `notify-telegram`

Disparada via trigger após cada INSERT na tabela `leads`.  
Envia mensagem formatada em Markdown para o chat do Telegram da equipe.

---

## Deploy

### Vercel

1. Conectar o repositório no dashboard do Vercel
2. Configurar **Output Directory:** `public`
3. **Build Command:** deixar vazio (site estático)
4. Deploy automático a cada push no `main`

### Cloudflare Pages

Ver [CLOUDFLARE-PAGES.md](./CLOUDFLARE-PAGES.md) para configuração detalhada.

---

## Design System

Tokens CSS definidos no `:root` do `index.html`:

| Token | Valor | Uso |
|-------|-------|-----|
| `--gold` | `#C8960A` | Cor primária dourada |
| `--gold-hi` | `#F0B429` | Dourado destaque (CTAs, ênfase) |
| `--bg` | `#07070D` | Fundo principal |
| `--bg-alt` | `#111020` | Fundo alternado (seções) |
| `--tx` | `#F0F0F2` | Texto principal |
| `--tx-soft` | `#B8B8CC` | Texto secundário |
| `--tx-muted` | `#8A8AA8` | Texto terciário |

**Fontes:**
- Display/Títulos: `Space Grotesk` (weight 700/900)
- Corpo: `Inter` (weight 400/700)
- Mono/Labels: `JetBrains Mono`

---

## Variáveis de Ambiente

Configuradas diretamente no `index.html` (cliente público):

```js
const SUPABASE_URL = 'https://evtchedskwnwpioatjet.supabase.co'
const SUPABASE_KEY = 'sb_publishable_...'
```

> As chaves usadas são **publishable** (somente INSERT) — seguro expor no frontend.

---

## Manutenção

- Todas as edições visuais são feitas em `public/index.html`
- Após qualquer alteração: `git add public/index.html && git commit -m "..." && git push`
- O Vercel faz deploy automático em ~30 segundos após o push
