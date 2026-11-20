# Visual System: ABS Moto Peças e Serviços

> Resumo operacional. Detalhe completo de cada família em `ABS_Memoria_Editorial.md` (seções 8 a 16). Paleta e tipografia em `brand-spec.md`.

---

## Princípio

Um único sistema ABS com cinco famílias. Compartilhar tipografia, margens, ícones, labels, assinatura da marca, cores e tom fotográfico. Variar composição, densidade, tipo de foto e função editorial.

**Proporção:** 70 a 80% dos posts claros, 20 a 30% dark (alerta, risco, desgaste severo).

---

## Famílias visuais

| Família | Visual | Dark? |
|---|---|---|
| **Motor Aberto** | Fundo claro ou cinza técnico, fotos grandes de motor e peças em close, amarelo para marcações, vermelho para defeito, verde para solução | Sublinha dark só em alto impacto |
| **ABS Explica** | Off-white com respiro, boxes, ícones lineares, números, checklists, amarelo como destaque | Sublinha "Alerta Mecânico" (preto/grafite) para risco |
| **Peça Certa** | Fundo claro, produto protagonista, preço em box dedicado, pouco texto | Evitar dark recorrente |
| **Antes de Rodar de Novo** | Split screen ou sequência em 2 a 3 etapas; vermelho = problema, amarelo = processo, verde = resultado | Não |
| **Bastidores ABS** | Foto real como protagonista, pouco design, moldura leve, tratamento natural | Evitar filtros dark pesados |

---

## Formatos

| Formato | Dimensão | Uso |
|---|---|---|
| Post estático | 1080x1350 (4:5) | Peça Certa, Bastidores, alertas |
| Carrossel (3 a 6 slides) | 1080x1350 (4:5) | ABS Explica, Motor Aberto, Antes de Rodar de Novo |
| Reels (15 a 30s, máx. 2/semana) | 1080x1920 (9:16) | Motor Aberto, Bastidores |

---

## Regras de prompt para geração de imagem

- Quando houver imagem de referência, usar a skill `json-prompt-generator` antes de escrever qualquer prompt (regra do `CLAUDE.md` raiz)
- Zero travessão em qualquer texto dentro da arte
- Logo ABS (`assets/logo-abs.png`) sempre como assinatura, sem alterar cores, sem sombra
- Fotografia real da oficina tem prioridade; quando gerar imagem, evitar aparência artificial de oficina
- Headline curta e grande em fonte condensada; texto de apoio em sans limpa
- Cores com função: vermelho para problema, amarelo para destaque, verde para solução

---

## Checklist antes de aprovar um post

Ver seção 23 de `ABS_Memoria_Editorial.md`.
