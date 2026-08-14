---
name: regras-materiais-html
description: "Regras canônicas para produção e auditoria de materiais HTML do curso Claude na Prática — processo, proibições e checklist obrigatório"
---

# Regras Canônicas · Materiais HTML · Claude na Prática

Documento de referência obrigatório antes de criar ou revisar qualquer `material.html` do curso.

---

## Processo obrigatório antes de escrever HTML

Para cada aula, nesta ordem:

1. **Ler o `.md` da aula** em `aulas/mX-nome/X.Y-titulo.md`
   - Objetivo, tópicos em ordem, entregável, notas de gravação
2. **Ler o roteiro** em `roteiros/mX-X.Y-roteiro.md`
   - Frases exatas do Diego, ordem das cenas, ação final
3. **Só então montar o HTML** com base nesses dois arquivos
   - Seções = tópicos do .md em sequência
   - Texto dos cards = frases do roteiro adaptadas (nunca inventadas)
   - Entregável = "Ação final" do .md no checklist e CTA

**Nunca inventar conteúdo quando .md e roteiro existem.**

---

## Estrutura obrigatória de cada material

| Elemento | Fonte |
|---|---|
| Título, duração, tipo (CONCEITUAL / AO VIVO / PRÁTICA) | Frontmatter do `.md` |
| Seções em ordem | Tópicos numerados do `.md` |
| Texto dos cards e parágrafos | Frases do roteiro |
| Conquistas ou bullets de resultado | "Ação final" + cena de conquistas do roteiro |
| CTA e próxima aula | Última cena do roteiro + rodapé do `.md` |

---

## Paleta e visual (brand guide canônico)

Seguir `referencias/brand-guide-curso.md`. Resumo:

- **Fundo:** `#FAFAF8` — nunca dark theme
- **Navy:** `#1E3A5F` — títulos, hero, barras
- **Amber:** `#F59E0B` — accent, badges, destaques
- **Texto corpo:** `#374151`
- **Texto mudo:** `#6B7280`
- **Borda:** `#E5E7EB`
- **Sem texturas de fundo** (hexágonos, losangos, grids SVG)
- **Fontes:** Inter Tight (display) + JetBrains Mono (labels/badges)

---

## Proibições absolutas de copy

| Proibido | Substituir por |
|---|---|
| Travessão `—` | `:` ou reformular a frase |
| Listas triplas forçadas ("a, b e c" como gancho) | Frase direta em prosa |
| Termos que Diego não usa: squads, mental model, framework, onboarding | time de agentes, entendimento, método, entrada |
| Superlativos vazios: incrível, poderoso, transformador, revolucionário | Descrever o resultado concreto |
| Frases começando com "Isso" como gancho ("Isso não é hipótese...") | Afirmação direta |
| "a maioria das pessoas nunca vai descobrir" | Desnecessário, cortar |
| Padrão IA listy: "Primeiro X. Depois Y. Por fim Z." | Prosa corrida ou tabela |

---

## Tom de voz do Diego (Intus Hub)

- Direto, sem enrolação
- Foco no resultado do aluno, não na ferramenta
- Sem promessa inflável, sem ferramenta mágica
- Sem "na marra" — ele pesquisou, testou, aprimorou
- Frases curtas, afirmativas, sem hesitação
- Postura de quem já fez e está mostrando o caminho, não vendendo

---

## Checklist de auditoria antes de entregar

Rodar este checklist em todo material antes de mostrar ao Diego:

- [ ] Todo parágrafo tem base no `.md` ou roteiro da aula?
- [ ] Existe algum travessão `—` no conteúdo visível? (buscar no código)
- [ ] Alguma frase soa como lista gerada por IA?
- [ ] O entregável da aula aparece no checklist e no CTA final?
- [ ] A próxima aula está correta no rodapé e no botão?
- [ ] A paleta segue o brand guide (fundo `#FAFAF8`, navy, amber)?
- [ ] Nenhuma textura ou padrão SVG no fundo?
- [ ] Nenhum termo proibido: squads, mental model, framework, incrível?
- [ ] O tipo da aula (CONCEITUAL / AO VIVO / PRÁTICA) está no badge do header?
- [ ] A duração está correta conforme o `.md`?

---

## Como acionar este gate

**Ao receber pedido de novo material HTML:**
1. Confirmar qual aula (ex: M1-1.1)
2. Ler `.md` + roteiro da aula antes de qualquer produção
3. Apresentar mapeamento do conteúdo (seções planejadas) para aprovação
4. Produzir o HTML
5. Rodar o checklist de auditoria acima antes de entregar

**Ao receber pedido de revisão de material existente:**
1. Ler o HTML atual
2. Ler o `.md` e roteiro correspondentes
3. Comparar seção por seção
4. Rodar o checklist de auditoria
5. Reportar divergências antes de editar
