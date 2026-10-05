# Ciência Chocante — Contexto de Produção

> Este arquivo é lido automaticamente pelo Claude Code ao abrir esta pasta.

---

## Ativação automática

Você está trabalhando com o cliente **Ciência Chocante** (@cienciachocante) — perfil de carrosséis de curiosidades científicas: espaço, corpo humano e ciência em geral.

Ao iniciar qualquer sessão nesta pasta, leia obrigatoriamente em sequência:

1. `.agents/social-media-context-sms.md` — voz, pilares, plataformas, público
2. `brand-spec.md` — identidade visual, paleta, tipografia, marca
3. `DESIGN.md` — referência visual para geração de código e componentes
4. `production-rules.md` — gatilho pré-copy, padrões proibidos, guia de voz com exemplos
5. `content-system.md` — editorias, grade semanal, copy por tipo, CTAs, dados âncora, hashtags
6. `visual-system.md` — grupos visuais, JSON padrão, regras de prompt

Confirme em uma linha antes de iniciar: *"Trabalhando com Ciência Chocante. O que vamos produzir hoje?"*

---

## Escopo do perfil

- **Formato principal:** carrossel de curiosidades (Instagram)
- **Nicho:** ciência, espaço/astronomia, corpo humano, natureza
- **Tom:** impactante/choque — dado científico chocante como hook, "isso desafia o que você aprendeu"
- **Perfis irmãos** (mesmo dono, nichos diferentes, nunca misturar voz/paleta/tema entre eles): [voce-ignorava-isso](../voce-ignorava-isso/CLAUDE.md) (vida/cultura pop), [historia-proibida](../historia-proibida/CLAUDE.md) (história/casos bizarros/paranormal/Brasil)

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

Use kebab-case para o tema. Ex: `buraco-negro`, `dna-humano`.

---

## Regras de produção

- Todo carrossel passa obrigatoriamente pela skill `carousel-writer-sms` (gate global do repositório) — nunca escrever slides manualmente "por fora"
- Nunca escreva copy sem executar o Gatilho Pré-Copy do `production-rules.md`
- Nunca entregue sem confirmar a voz contra `.agents/social-media-context-sms.md`
- Se algum arquivo estiver ausente ou com placeholders não preenchidos, informe antes de produzir
- Nunca misturar tema/paleta/voz com os perfis irmãos (voce-ignorava-isso, historia-proibida)
- Dado científico sempre precisa de fonte real por trás (mesmo que não citada no slide) — nunca inventar número
