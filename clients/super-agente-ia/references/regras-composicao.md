# Regras de Composição & Montagem — Referência de Design

> Princípios de composição extraídos de curadoria externa (@ankitgraphic) para aplicar em cards, carrosséis e criativos Meta Ads.
> Complementa — não substitui — as regras de safe zone (`meta-ads-specs.md`) e elementos visuais recorrentes (`visual-system.md`).
> Vale para qualquer paleta em uso (canônica ou de variação).

---

## Regra 60-30-10 (proporção de cor)

Fórmula de equilíbrio: 60% cor dominante (fundo) · 30% cor secundária (texto/blocos) · 10% cor de destaque (CTA/acento).

Isso já é essencialmente o que o sistema atual pratica — `bg` ≈ 60%, `text-primary` ≈ 30%, `accent` ≈ 10% — mas vale formalizar como checagem explícita em toda peça nova, principalmente ao aplicar uma paleta de variação (`paletas-variacao.md`): se o acento passar muito de 10% do frame, a peça perde hierarquia e o CTA some no meio do resto.

## Contraste

Usar diferença de cor, tamanho e peso para fazer elemento saltar. Já é prática no Grupo 1 (Contraste/Problema) via cor; reforçar também com **tamanho** e **peso de fonte** — não depender só da cor de acento para criar hierarquia, principalmente nas paletas mais monocromáticas (ex: `V4-petroleo-editorial`).

## Repetição

Repetir elemento gráfico fixo cria coesão entre peças de uma mesma campanha — já documentado como "Elementos Visuais Recorrentes" em `visual-system.md` (glow, borda laranja, task dot, seta CTA). Ao trocar de paleta de variação, manter a mesma lógica de elemento repetido, só trocando a cor — não trocar a forma.

## Proporção

Elementos precisam ter tamanho relativo coerente entre si. Aplicação direta: cards de testemunho (Grupo 6) e value stack de oferta (Grupo 5) — ícone, número e texto de resultado precisam manter proporção entre si, senão quebra a leitura em mobile.

## Movimento

Guiar o olho do espectador numa sequência lógica pelo layout. Aplicação direta: carrossel educativo (Grupo 4, numeração por slide) e layout de dois painéis (Grupo 1, esquerda ruim / direita bom) — o percurso visual precisa ser óbvio sem depender de seta explícita.

## Espaço em branco / negativo

Espaço vazio não é desperdício — dá foco e clareza. Reforça diretamente a regra de safe zones e padding já validada em `meta-ads-specs.md` (100px recomendado em elementos críticos no Feed; zona livre de topo/base no Stories/Reels). Resistir à tentação de preencher todo o frame — o espaço negativo é o que faz o acento (laranja ou o da paleta de variação) realmente saltar.

---

## Fonte da Curadoria

- Pasta de origem: `regras de design de qualidade` (12 imagens — série "7 Rules" + série "Colour Theory 60-30-10", curadoria @ankitgraphic), recebida e absorvida em 2026-07-09.
