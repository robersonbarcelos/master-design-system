# CTG Sentinela da Querência — Contexto de Produção

> Este arquivo é lido automaticamente pelo Claude Code ao abrir esta pasta.

---

## Ativação automática

Você está trabalhando com o cliente **CTG Sentinela da Querência** (Santa Maria - RS).

Ao iniciar qualquer sessão nesta pasta, leia obrigatoriamente em sequência:

1. `.agents/social-media-context-sms.md` — voz, pilares, plataformas, público
2. `brand-spec.md` — identidade visual, paleta, tipografia, marca
3. `DESIGN.md` — referência visual para geração de código e componentes
4. `production-rules.md` — gatilho pré-copy, padrões proibidos, guia de voz com exemplos
5. `content-system.md` — editorias, grade semanal, copy por tipo, CTAs, dados âncora, hashtags
6. `visual-system.md` — grupos visuais, JSON padrão, regras de prompt

Confirme em uma linha antes de iniciar: *"Trabalhando com CTG Sentinela da Querência. O que vamos produzir hoje?"*

---

## Sobre o cliente

**Status: cliente ativo.** Proposta de onboarding e contrato de prestação de serviços
(R$ 750,00/mês, mínimo 2 meses) aceitos em setembro de 2026. `visual-system.md` e
`production-rules.md` já existem e valem como fonte de verdade para produção.

CTG (Centro de Tradições Gaúchas) Sentinela da Querência, sediado em Santa Maria - RS.
Produz material de divulgação para eventos tradicionalistas — o principal caso de uso até
agora é o **convite/banner da Semana Farroupilha** (peça impressa/digital, frente e verso),
com programação diária de almoços, jantares, valores e apresentações culturais.

Muitos artefatos deste cliente serão **peças de convite/programação de evento**, não apenas
posts de social media — considerar isso ao escolher template e formato de entrega.

---

## Material de referência bruto

- `references/material-2026-semana-farroupilha.md` — transcrição integral do convite
  "Semana Farroupilha 2026" (frente + verso, 3 dobras) enviado pelo cliente como referência
  para o refazimento do material. Usar como fonte de verdade de conteúdo/copy ao redesenhar
  a peça — não inventar datas, valores ou apresentações que não estejam listadas ali.

---

## Arquivos de referência (carregar sob demanda)

- `references/copies-aprovadas.md` — copies reais aprovadas. Carregar ao calibrar tom ou revisar copy.
- `references/dados-ancora.md` — fatos e números do cliente. Carregar ao escrever copy com dado âncora.
- `references/temas.md` — banco de pautas por editoria. Carregar ao planejar calendário.
- `references/material-2026-semana-farroupilha.md` — conteúdo integral do convite atual (ver acima).

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
| Convite/programação de evento | `convite-[evento].md` + JSON de peça |

Use kebab-case para o tema. Ex: `semana-farroupilha-2026`, `torneio-bocha`, `baile-veterano`.

---

## Regras de produção

- Nunca escreva copy sem executar o Gatilho Pré-Copy do `production-rules.md`
- Nunca entregue sem confirmar a voz contra `.agents/social-media-context-sms.md`
- Nunca use o mesmo dado âncora duas vezes na mesma semana (`references/dados-ancora.md`)
- Se algum arquivo estiver ausente ou com placeholders não preenchidos, informe antes de produzir
- Ao redesenhar o convite da Semana Farroupilha, todos os dados de programação (datas, cardápios,
  valores, apresentações) devem vir de `references/material-2026-semana-farroupilha.md` —
  confirmar com o usuário qualquer dado que pareça incompleto ou inconsistente antes de publicar
