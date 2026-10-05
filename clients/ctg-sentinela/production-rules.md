# CTG Sentinela da Querência — Production Rules

> Regras de voz e escrita para todo copy deste cliente. Consultado pelo `copy-qa-sms`
> (Passo 1 — Voice Gate) e por qualquer skill de criação antes de entregar texto.
>
> Para regras de identidade visual (paleta, proibições, linhas editoriais com nome visual,
> biblioteca gráfica, sistema de capas), ver `visual-system.md`. Este arquivo cobre só voz e texto.

---

## 00-B | PADRÕES DE AUSÊNCIA DE VOZ (NUNCA USAR)

| Nunca usar | Usar no lugar |
|---|---|
| "seu/sua" (em legenda) | **"teu/tua"** |
| Conjugação coloquial errada de "tu" ("tu vai", "tu sabe", "tu quer") | Conjugação **correta** de "tu" ("tu vais", "tu sabes", "tu queres", "tu tens") — só em legenda |
| "na Sentinela" / "a Sentinela" (artigo feminino) | **"no Sentinela"** / **"do Sentinela"** — o nome completo é *o CTG Sentinela da Querência*, artigo masculino |
| Travessão (—) em qualquer copy publicável | Vírgula, dois-pontos, ou quebrar a frase em duas |
| Tom genérico de agência/corporativo | Sotaque de pago: "tchê", "bah", "campeiro", "querência", "galpão" — na medida certa, sem virar caricatura |

### Regra de pessoa: tu (legenda) vs você (cartaz/material gráfico) — atualizada em 2026-09-10

O tratamento de segunda pessoa **depende do formato**, não é fixo em todo lugar:

| Formato | Pronome | Exemplo |
|---|---|---|
| **Legenda** (texto corrido de post, caption) | **tu**, com conjugação correta | "Tu sabes o que é uma guaiaca?", "Tu tens que participar dessa!" |
| **Cartaz / material gráfico** (headline, peça de design) | **você** | "Tradição que se fortalece com você.", "Você sabe o que é uma guaiaca?" |

**Por quê:** em headline de cartaz, construções com "tu" em caso oblíquo ficam estranhas em português ("com tu", "como tu" não existem — o correto seria "contigo", "como tu" já soa forçado em título curto). O cliente decidiu manter "tu" só na legenda, onde dá pra escrever frase completa, e usar "você" nas peças gráficas, onde o texto é headline curta.

Isso substitui a orientação anterior (que pedia conjugação coloquial "tu vai/sabe/quer" e proibia "você" em qualquer contexto) — ficou desatualizada depois que o cliente revisou o uso em situações reais de cartaz.

---

## Tom de voz

A voz é de quem tá dentro do CTG falando com quem também é, ou quer ser, da querência. Não é a voz de uma agência de marketing terceirizada.

- Frases curtas e diretas, como quem fala de fato num galpão
- Regionalismos aplicados com naturalidade, nunca em excesso a ponto de soar caricato
- Dado concreto sempre que possível (datas, valores, anos, número de invernadas) em vez de adjetivo vago

---

## Padrões universais (herdados do `copy-qa-sms`)

Além das regras específicas acima, todo copy deste cliente segue o gate universal:
- Sem adjetivo vago sem dado ("incrível", "robusto", "transformador")
- Sem CTA vago ("saiba mais", "clique aqui") — sempre dizer o que a pessoa recebe ao agir
- Sem vocabulário Tier 1/2/3 de IA genérica (ver `copy-qa-sms/SKILL.md`)
- Sem travessão em nenhuma peça (regra reforçada acima, específica deste cliente)

---

## Padrão de legenda (calibrado em 2026-08-31)

O cliente prefere legendas **curtas e diretas**, não versões longas listando cada atração. Ver exemplo completo e a regra de estrutura em `references/copies-aprovadas.md`. Resumo:

- Hook em caps com dois-pontos, não travessão
- Corpo de 2 linhas curtas (contexto + convite)
- Sem listar atrações/nomes na legenda — isso fica pro post/carrossel
- CTA de reserva isolado, com número direto
- Só 2-3 hashtags (não o range de 5-8 do padrão genérico da skill)

---

## Histórico de correções de voz

- **2026-08-31** — Trocado "você/seu" por "tu/teu" em toda a proposta de onboarding, após pedido explícito do cliente.
- **2026-08-31** — Corrigido "na Sentinela"/"a Sentinela" para "no Sentinela"/"do Sentinela" em 4 ocorrências (calendário e exemplos de post).
- **2026-08-31** — Removidos 28 travessões do copy visível da proposta, substituídos por vírgula, dois-pontos ou quebra de frase, via auditoria `copy-qa-sms`.
- **2026-09-10** — Regra de pronome revisada: "tu" (conjugação correta, não coloquial) vale só para legenda; "você" volta a ser usado em cartazes/materiais gráficos, onde construções com "tu" ficam gramaticalmente estranhas em headline curta. Isso resolve, sem ser conflito, o uso de "você" observado nos moodboards já produzidos ("Você sabe o que é uma guaiaca?", "com você") — esses textos estavam certos.
