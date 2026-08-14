# Paletas de Variação — Meta Ads (Teste de Performance)

> ⚠️ Escopo: estas paletas valem **APENAS para criativos de Meta Ads em teste**.
> O feed orgânico (@intushub) permanece 100% na paleta canônica — ver `brand-spec.md` e `production-rules.md`.
> Nunca aplicar uma paleta de variação em conteúdo orgânico sem aprovação explícita do Diego.

---

## Como usar

1. Cada paleta nova recebe um **ID curto** (ex: `V2-azul-tech`) — usado no campo `variacao_cor` dos JSONs de anúncio (`ads/*.json`), que hoje só tem o valor `canonica`.
2. Registrar aqui: hex codes, mood, para qual ângulo/pilar de criativo combina melhor, e status de teste.
3. Toda paleta de variação deve manter os requisitos técnicos do `meta-ads-specs.md` (safe zones) e a tipografia (`Inter Tight`) — só a cor muda.
4. Resultado de performance (quando disponível) entra na tabela de status — não apagar variações testadas, só marcar resultado.
5. **Heurística de variação por lote** (consolidada em produção, jul/2026): ao gerar 3 variações de copy a partir de uma referência (Var1/Var2/Var3), Var1 (quase idêntica ao original) usa por padrão a Paleta Canônica; Var2 e Var3 (mais divergentes) diversificam entre as paletas de variação aprovadas abaixo — evitar repetir a mesma paleta duas vezes no mesmo lote quando possível.

---

## Paleta Canônica (controle — referência, não é variação)

| Token | Hex | Uso |
|-------|-----|-----|
| `accent` | `#E84000` | Laranja principal |
| `accent-dark` | `#8C2000` | Laranja escuro / gradiente |
| `bg` | `#0a0a0a` | Fundo preto |
| `text-primary` | `#FFFFFF` | Texto principal |

---

## Paletas de Variação (banco de testes)

| ID | Hex principais | Mood / Ângulo | Melhor pilar | Status |
|----|-----------------|----------------|--------------|--------|
| `V2-verde-tech` | accent `#14E08E` (Turkish Green) · bg `#000000` | Tech, "IA viva", frio porém vibrante — mesma estrutura preto+acento da canônica, só troca a cor | Grupo 2 (Demonstração de Agente) | Aprovada — aguardando primeiro teste |
| `V3-lima-choque` | accent `#B6FF00` (Lima Radioativa) · bg `#0E0E0E` | Agressivo, altíssimo contraste, choque visual no feed | Grupo 1 (Contraste/Problema) | Aprovada — aguardando primeiro teste |
| `V4-petroleo-editorial` | bg `#004741` (Petróleo Amazônico) · texto `#F0EDE4` (Linho Claro) | Premium, editorial, mais sofisticado, menos "cara de anúncio" | Grupo 3 (Diego/Autoridade) · Grupo 4 (Educativo) | Aprovada — aguardando primeiro teste |
| `V5-lemon-urgencia` | accent `#FEEF4C` (Bright Lemon) · bg `#2A323F` (Charcoal Gray) | Alta chamada de atenção, ótimo para número/preço saltando | Grupo 5 (Oferta/Conversão) | Aprovada — aguardando primeiro teste |
| `V6-bege-claro` | bg `#F5EFE6` (Bege Claro) · texto `#141414` (quase preto) · accent `#E84000` mantido como contraste principal | ⚠️ **Exceção explícita** à regra "nunca fundo branco/claro" — autorizada por Diego pontualmente para teste A/B (fundo claro vs. fundo escuro no mesmo criativo). Mood: clean, editorial, "respiro" visual — o laranja salta mais forte por contraste em vez de se perder no preto | Teste A/B direto contra a paleta canônica no mesmo criativo (Grupo 2/3) | Aprovada só para este teste — não generalizar pra outros criativos sem nova aprovação |

### Descartada

| ID | Hex principais | Motivo do descarte |
|----|-----------------|---------------------|
| `V1-laranja-azul` | accent `#FF4103` (Laranja Vulcão) · bg `#001621` (Azul Abismo) | Conflita com a regra "nunca azul" do `brand-spec.md` — Diego optou por não abrir essa exceção, nem para teste de Ads |

---

## Nota — Exceção de fundo claro (`V6-bege-claro`)

A regra "nunca fundo branco/claro" continua valendo como padrão pra todo o material (canônico e demais variações V2-V5). `V6-bege-claro` é uma exceção pontual, autorizada explicitamente por Diego, criada só pra rodar teste A/B (2 variações fundo escuro vs. 2 variações fundo claro no mesmo criativo). Não usar fundo claro em nenhum outro criativo sem essa mesma autorização explícita repetida.

---

## Pool Master — 8 Paletas para Rotação de Criativos (2026-08-13)

> Regra ativa a partir desta data: **em toda rodada de geração de JSONs de artes, sempre gerar 3 variações por ideia, cada uma com uma paleta diferente tirada deste pool de 8.**
> Objetivo: abrangência visual máxima, evitando repetição e cobrindo espectros visuais distintos a cada lote de 10 ideias.

### Como selecionar as 3 paletas por ideia

As 8 paletas estão divididas em **3 grupos por temperatura/mood**. A regra de seleção é:

> **Sempre 1 do Grupo A + 1 do Grupo B + 1 do Grupo C**

Dentro de cada grupo, ciclar em sequência (round-robin) ao longo das ideias do lote — isso garante que todas as 8 sejam usadas ao longo de 10 ideias sem repetição concentrada.

---

### Grupo A — Neon / Verde Energia (3 paletas)

| ID | Nome | Hex principais | Mood |
|----|------|----------------|------|
| `A1` | Menta Elétrica | `#21F1A8` + `#171717` | Tech, fresco, digital |
| `A2` | Verde Laser | `#2BEE34` + `#141414` | Energia máxima, urgência |
| `A3` | Neon Limão | `#A4F900` + `#F2F2F2` + `#141414` | Esportivo, jovem, disruptivo |

### Grupo B — Navy / Institucional (3 paletas)

| ID | Nome | Hex principais | Mood |
|----|------|----------------|------|
| `B1` | Navy Âmbar Clássico | `#14213D` + `#FCA311` + `#E5E5E5` | Clássico institucional |
| `B2` | Navy Sport Verde | `#102540` + `#8DBF21` + `#D9D9D9` | Esportivo/institucional |
| `B3` | Marítimo Vibrante | `#024059` + `#F28705` + `#049DBF` | Dinâmico, energia marítima |

### Grupo C — Alto Contraste / Quente-Frio (2 paletas)

| ID | Nome | Hex principais | Mood |
|----|------|----------------|------|
| `C1` | Laranja Vulcão | `#FF4103` + `#001621` | Impacto máximo, urgência — ⚠️ contém fundo azul (V1 descartada anteriormente); reaberta para este pool por decisão explícita em 2026-08-13 |
| `C2` | Líquen Neon | `#DBEE00` + `#1D3F6D` | Inovação + solidez |

---

### Tabela de rotação para lote de 10 ideias

| Ideia | Var 1 | Var 2 | Var 3 |
|-------|-------|-------|-------|
| 1 | A1 — Menta Elétrica | B1 — Navy Âmbar | C1 — Laranja Vulcão |
| 2 | A2 — Verde Laser | B2 — Navy Sport | C2 — Líquen Neon |
| 3 | A3 — Neon Limão | B3 — Marítimo Vibrante | C1 — Laranja Vulcão |
| 4 | A1 — Menta Elétrica | B1 — Navy Âmbar | C2 — Líquen Neon |
| 5 | A2 — Verde Laser | B2 — Navy Sport | C1 — Laranja Vulcão |
| 6 | A3 — Neon Limão | B3 — Marítimo Vibrante | C2 — Líquen Neon |
| 7 | A1 — Menta Elétrica | B1 — Navy Âmbar | C1 — Laranja Vulcão |
| 8 | A2 — Verde Laser | B2 — Navy Sport | C2 — Líquen Neon |
| 9 | A3 — Neon Limão | B3 — Marítimo Vibrante | C1 — Laranja Vulcão |
| 10 | A1 — Menta Elétrica | B1 — Navy Âmbar | C2 — Líquen Neon |

> Claude deve aplicar esta tabela sequencialmente dentro do lote. Se o lote tiver menos de 10 ideias, usar as primeiras N linhas.

---

## Notas de Absorção

- **Fonte das referências:** pasta `ideias de color system paleta de cores` (10 imagens, curadoria @ankitgraphic), recebida e absorvida em 2026-07-09.
- Descartei da curadoria inicial as combinações redundantes com as 4 aprovadas acima (Menta Elétrica, Electric Lime, Sea Green, Dark Gray+Lime Green — todas na mesma família verde/lima, sem mood distinto o suficiente para justificar slot de teste próprio).
- Todas as 4 paletas aprovadas mantêm a proporção **60-30-10** (fundo dominante 60% / cor secundária-texto 30% / acento-CTA 10%) já praticada na paleta canônica — ver `regras-composicao.md` para o racional completo dessa proporção.
- Tipografia: independente da paleta de variação usada, a fonte segue as definições de `references/fontes-variacao.md` (headline geral, headline de impacto, números/badges) — nunca a fonte institucional Inter Tight sozinha nos testes de Ads.
- Preview visual gerado em HTML para todas as 4 paletas (+ a descartada) está em `references/preview-variacoes.html`.
