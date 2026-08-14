# Carol Staggemeier — Contexto de Produção

> Este arquivo é lido automaticamente pelo Claude Code ao abrir esta pasta.

---

## Ativação automática

Você está trabalhando com a cliente **Carol Staggemeier**.

Ao iniciar qualquer sessão nesta pasta, leia obrigatoriamente em sequência:

1. `.agents/social-media-context-sms.md` — voz, pilares, plataformas, público
2. `brand-spec.md` — identidade visual, paleta, tipografia, marca
3. `DESIGN.md` — referência visual para geração de código e componentes
4. `production-rules.md` — gatilho pré-copy, padrões proibidos, guia de voz com exemplos
5. `content-system.md` — editorias, grade semanal, copy por tipo, CTAs, dados âncora, hashtags
6. `visual-system.md` — grupos visuais, JSON padrão, regras de prompt

Confirme em uma linha antes de iniciar: *"Trabalhando com Carol Staggemeier. O que vamos produzir hoje?"*

---

## Contexto rápido da marca

**Categoria:** Moda autoral brasileira — Criativo Casual / Urban Craft
**Localização:** Santa Maria, Rio Grande do Sul, Brasil
**Fundadora:** Carol Staggemeier — designer de moda com +12 anos de trajetória
**Essência:** Roupas com alma. Criativo casual, handmade, atemporal, versátil.
**Público:** Mulheres 30–45 anos, urbanas, profissionais liberais, renda R$ 8–20k familiar
**Ticket médio:** R$ 250–350/peça (range R$ 150–450)
**Produção:** Pequena escala, Santa Maria/RS, tecidos naturais, feito à mão

---

## Arquivos de referência (carregar sob demanda)

- `references/copies-aprovadas.md` — copies reais aprovadas. Carregar ao calibrar tom ou revisar copy.
- `references/dados-ancora.md` — fatos e números do cliente. Carregar ao escrever copy com dado âncora.
- `references/temas.md` — banco de pautas por editoria. Carregar ao planejar calendário.

---

## Salvamento de artefatos

Salve todos os artefatos de produção em `runs/[AAAA-MM-DD]/`.

Use a data de hoje como nome da pasta. Se a pasta não existir, crie-a.

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

---

## GATE DE CARROSSEL — obrigatório antes de qualquer produção de carrossel

**Quando o pedido for carrossel: executar este gate completo antes de qualquer slide, ângulo ou copy.**

Carregar `guia-linhas-editoriais-carrossel.md` e perguntar em sequência:

---

**ETAPA 1 — Linha editorial**

> "Este carrossel é produto ou conteúdo?
>
> **PRODUTO** (termina em CTA de contato / agendar atendimento)
> A — A Peça: material, técnica, detalhe, acabamento
> B — O Corpo: silhueta, caimento, movimento, liberdade de uso
> C — O Look: composições, formas de usar, versatilidade
>
> **CONTEÚDO** (termina em engajamento, salvar ou reflexão)
> D — Cultura de Moda: história, silhuetas, o que move a moda
> E — Moda Autoral: autoral vs. massa, posicionamento pela escolha
> F — Identidade: relação da mulher com o que veste, reconhecimento"

→ Aguardar escolha (A / B / C / D / E / F) antes de prosseguir.

---

**ETAPA 2 — Voz narrativa**

> "Qual voz para este carrossel?
>
> ① **Carol narradora** — primeira pessoa: 'Escolhi esse tecido porque...'
>    (seguir production-rules.md — voz da Carol, tom de amiga próxima)
>
> ② **Editorial impessoal** — narrador externo: 'Antes do shift dress, a silhueta...'
>    (tom de revista/documental — Linhas D e E recomendam este)
>
> ③ **Íntima conversacional** — sem ser Carol, fala sobre a cliente: 'quando você encontra a peça certa...'
>    (Linha F recomenda este — lowercase opcional)"

→ Aguardar escolha (① / ② / ③) antes de prosseguir.

---

**ETAPA 3 — Confirmar peça ou tema**

> "Qual a peça ou tema deste carrossel?"

→ Só após as 3 etapas confirmadas: acionar `carousel-writer-sms` com linha + voz + tema como briefing.

**Gate obrigatório: nenhum slide é escrito sem linha + voz definidos.**

---

## Regras de produção

- Nunca escreva copy sem executar o Gatilho Pré-Copy do `production-rules.md`
- Nunca entregue sem confirmar a voz contra `.agents/social-media-context-sms.md`
- Nunca use o mesmo dado âncora duas vezes na mesma semana (`references/dados-ancora.md`)
- Vocabulário PROIBIDO: "premium", "luxo", "trends", "must-have", "fashionista", "lacrou", "empoderamento"
- Se algum arquivo estiver ausente ou com placeholders não preenchidos, informe antes de produzir
