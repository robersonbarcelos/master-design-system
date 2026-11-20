# ABS Moto Peças e Serviços: Contexto de Produção

> Este arquivo é lido automaticamente pelo Claude Code ao abrir esta pasta.

---

## Ativação automática

Você está trabalhando com o cliente **ABS Moto Peças e Serviços** (@abspecas, Sertãozinho, SP).

Ao iniciar qualquer sessão nesta pasta, leia obrigatoriamente em sequência:

1. `ABS_Memoria_Editorial.md`: fonte principal da memória editorial (5 famílias, lógica claro x dark, paleta funcional, direção visual)
2. `.agents/social-media-context-sms.md`: voz, pilares, plataformas, público
3. `brand-spec.md`: logo, paleta, tipografia
4. `production-rules.md`: padrões proibidos e guia de voz
5. `content-system.md`: editorias, grade semanal, CTAs, assinatura de legenda
6. `visual-system.md`: famílias visuais, formatos, regras de prompt

Confirme em uma linha antes de iniciar: *"Trabalhando com a ABS Moto Peças e Serviços. O que vamos produzir hoje?"*

---

## Dados fixos (nunca alterar sem confirmação do cliente)

- **Endereço:** Avenida Nossa Senhora Aparecida, 540, Sertãozinho, SP (mudou em 09/2026; o antigo, Rua Braz Paschoal 464, NÃO vale mais)
- **WhatsApp:** (16) 99182-9495
- **Instagram:** @abspecas
- **Bio oficial:** ver `content-system.md`
- **Assinatura de legenda:** toda legenda fecha com o bloco de assinatura do `content-system.md`, antes das hashtags

## Relação com outros clientes

A **Moto Fácil** (@motoo_facil, também em Sertãozinho) vende moto no crédito. Não é concorrente da ABS: são negócios complementares (uma vende a moto, a outra mantém ela rodando). Nunca misturar paleta, copy ou identidade entre os dois.

---

## Arquivos de referência (carregar sob demanda)

- `references/copies-aprovadas.md`: copies reais aprovadas. Carregar ao calibrar tom ou revisar copy.
- `references/dados-ancora.md`: preços, condições e fatos reais da ABS. Carregar ao escrever copy com dado.
- `references/temas.md`: banco de pautas por editoria. Carregar ao planejar calendário.
- `assets/logo-abs.png`: logo com fundo transparente (337x89, baixa resolução, pedir versão vetorial ao cliente).
- `assets/logo-abs-fundo-branco.png`: logo com fundo branco (320x320).

---

## Salvamento de artefatos

Salve todos os artefatos de produção em `runs/[AAAA-MM-DD]/` (crie a pasta se não existir).

| Tipo de artefato | Nome do arquivo |
|---|---|
| 3 ângulos propostos | `angulos-[tema].md` |
| Script de carrossel aprovado | `carrossel-[tema].md` |
| Variações de capa | `capas-[tema].md` |
| Variações de legenda | `legendas-[tema].md` |
| JSONs de capa solicitados | `json-capas-[tema].md` |
| Roteiro de vídeo | `roteiro-[tema].md` |
| Copy de post | `post-[tema].md` |

Use kebab-case para o tema. Ex: `antes-depois-cg160`, `dia-das-criancas`.

---

## Regras de produção

- Todo copy passa pela skill de criação correspondente e pelo `copy-qa-sms` (gate do `CLAUDE.md` raiz)
- Travessão (—) proibido em qualquer copy
- Toda legenda usa a assinatura padrão e não repete o telefone no corpo do texto
- Antes de criar qualquer post, identificar a qual das 5 famílias ele pertence (ver `ABS_Memoria_Editorial.md`)
- Se algum arquivo estiver ausente ou com placeholders não preenchidos, informe antes de produzir
