# Você Ignorava Isso — Contexto de Produção

> Este arquivo é lido automaticamente pelo Claude Code ao abrir esta pasta.

---

## Ativação automática

Você está trabalhando com o cliente **Você Ignorava Isso** (@voceignorava) — perfil de carrosséis de curiosidades sobre vida cotidiana e cultura pop.

Ao iniciar qualquer sessão nesta pasta, leia obrigatoriamente em sequência:

1. `.agents/social-media-context-sms.md` — voz, pilares, plataformas, público
2. `brand-spec.md` — identidade visual, paleta, tipografia, marca
3. `DESIGN.md` — referência visual para geração de código e componentes
4. `production-rules.md` — gatilho pré-copy, padrões proibidos, guia de voz com exemplos
5. `content-system.md` — editorias, grade semanal, copy por tipo, CTAs, dados âncora, hashtags
6. `visual-system.md` — grupos visuais, JSON padrão, regras de prompt

Confirme em uma linha antes de iniciar: *"Trabalhando com Você Ignorava Isso. O que vamos produzir hoje?"*

---

## Escopo do perfil

- **Formato principal:** carrossel de curiosidades (Instagram)
- **Nicho:** vida cotidiana, comportamento humano, cultura pop, curiosidades do dia a dia
- **Tom:** impactante/choque — hook de revelação forte, "você não sabia disso"
- **Perfis irmãos** (mesmo dono, nichos diferentes, nunca misturar voz/paleta/tema entre eles): [ciencia-chocante](../ciencia-chocante/CLAUDE.md) (ciência/espaço/corpo humano), [historia-proibida](../historia-proibida/CLAUDE.md) (história/casos bizarros/paranormal/Brasil)

---

## Arquivos de referência (carregar sob demanda)

- `references/copies-aprovadas.md` — copies reais aprovadas. Carregar ao calibrar tom ou revisar copy.
- `references/dados-ancora.md` — fatos e números do cliente. Carregar ao escrever copy com dado âncora.
- `references/temas.md` — banco de pautas por editoria. Carregar ao planejar calendário.

---

## Salvamento de artefatos

Salve todos os artefatos de produção em `runs/[AAAA-MM-DD]/`. Use a data de hoje como nome da pasta. Se a pasta não existir, crie-a.

| Tipo de artefato | Nome do arquivo |
|---|---|
| 3 ângulos propostos | `angulos-[tema].md` |
| Script de carrossel aprovado | `carrossel-[tema].md` |
| Variações de capa | `capas-[tema].md` |
| Variações de legenda | `legendas-[tema].md` |
| JSONs de capa solicitados | `json-capas-[tema].md` |

Use kebab-case para o tema. Ex: `memoria-cheiro`, `efeito-mandela`.

---

## Regras de produção

- Todo carrossel passa obrigatoriamente pela skill `carousel-writer-sms` (gate global do repositório) — nunca escrever slides manualmente "por fora"
- Nunca escreva copy sem executar o Gatilho Pré-Copy do `production-rules.md`
- Nunca entregue sem confirmar a voz contra `.agents/social-media-context-sms.md`
- Se algum arquivo estiver ausente ou com placeholders não preenchidos, informe antes de produzir
- Nunca misturar tema/paleta/voz com os perfis irmãos (ciencia-chocante, historia-proibida)
