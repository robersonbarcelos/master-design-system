# Workflow 2 — Social Media

## Quando usar
Produção de carrosseis, posts, artigos, estáticos, legendas, stories, threads, calendário editorial, análise de performance.

## Ponto de entrada

Todo pedido de produção deste workflow deve passar pela **`production-orchestrator-sms`** — ela é quem diagnostica o pedido, roteia para a skill de criação certa e aplica os 4 gates obrigatórios (GATE A: formato → skill correta · GATE B: oferta do `narrative-framework-sms` · GATE C: `copy-qa-sms` antes da entrega · GATE D: empacotamento em `runs/[data]/`). Este workflow documenta o detalhe de cada fluxo por tipo de peça; os gates em si são especificados na skill orquestradora (`skills/social-media/production-orchestrator-sms/SKILL.md`).

## Skills envolvidas

| Skill | Função | Quando |
|---|---|---|
| production-orchestrator-sms | Ponto de entrada, roteamento e gates | Toda produção |
| social-media-context-sms | Contexto do cliente | Setup inicial (uma vez) |
| content-strategy-sms | Pilares e posicionamento | Setup inicial (uma vez) |
| platform-strategy-sms | Estratégia por plataforma | Setup inicial (uma vez) |
| narrative-framework-sms | Seleciona o ângulo/framework narrativo | Sempre que o ângulo estiver em aberto (GATE B) |
| hook-writer-sms | Hook / abertura | Toda peça |
| carousel-writer-sms | Script de carrossel | Carrosseis |
| card-news-generator-v2 | Visuais dos cards | Carrosseis |
| json-prompt-generator | JSON estruturado de imagem | Capas/visuais com referência |
| caption-writer-sms | Legenda | Toda peça |
| post-writer-sms | Post standalone | Posts únicos |
| thread-writer-sms | Thread / fio | X / LinkedIn |
| article-writer-sms | Artigo long-form / X Article / newsletter | Conteúdo editorial +500 palavras |
| illustration-writer-sms | Ilustração editorial | Artigos e carrosseis (opcional) |
| x-article-publisher | Publicação do artigo no X | Após article-writer-sms (rascunho, nunca automático) |
| content-repurposer-sms | Adaptação multiplataforma | Após peça aprovada |
| huashu-design | Infográfico / estático rico | Posts educativos visuais |
| content-calendar-sms | Calendário | Planejamento mensal |
| copy-qa-sms | Gate universal de qualidade (GATE C) | Antes de qualquer entrega de copy |
| performance-analyzer-sms | Análise de métricas | Com dados em mãos |
| content-pattern-analyzer-sms | Padrões de performance | Revisão mensal |
| optimization-advisor-sms | Recomendações | Após análise |
| audience-growth-tracker-sms | Crescimento | Revisão mensal |

## Fluxo por tipo de peça

### Carrossel
```
production-orchestrator-sms → diagnostica pedido (formato: carrossel)
          ↓
[GATE B] Ângulo definido pelo usuário?
  └── NÃO → narrative-framework-sms: 3-5 ângulos distintos
              (Nome do ângulo + Gancho de capa + Linha narrativa)
          ↓
[GATE 4.5] Ângulo aprovado pelo usuário?
  └── NÃO → STOP: refine ou reapresente os ângulos
          ↓
hook-writer-sms → aprofunda variações do gancho escolhido
          ↓
carousel-writer-sms → script 9-12 slides
  ├── Slides CERNE: 100% do espaço, dados, máx 8 linhas
  └── Slides SECUNDÁRIOS: máx 4 linhas, espaço para imagem
          ↓
[AUTO-GERAÇÃO — sem precisar solicitar]
  ├── 5 variações de capa (dado / contraste / personagem / tipografia / metáfora)
  └── 3 variações de legenda (storytelling / provocação / educativa)
  └── "Quer o prompt JSON de alguma dessas capas?" → json-prompt-generator
          ↓
[GATE 4] Script aprovado?
          ↓
[GATE C] copy-qa-sms → Voice Gate + AI Pattern Gate + padrões estruturais
          ↓
card-news-generator-v2 → visuais com brand-spec.md
          ↓
caption-writer-sms → legenda final otimizada para a plataforma
          ↓
content-repurposer-sms → adapta para outras plataformas (opcional)
          ↓
[GATE D] Salvar em clients/[cliente]/runs/[data]/
```

### Post estático educativo
```
production-orchestrator-sms → diagnostica pedido
          ↓
hook-writer-sms → copy do visual
     ↓
huashu-design (infográfico) → visual
     ↓
[GATE C] copy-qa-sms
     ↓
caption-writer-sms → legenda
```

### Post único (texto)
```
production-orchestrator-sms → diagnostica pedido
          ↓
[GATE B] Ângulo definido? NÃO → narrative-framework-sms
          ↓
hook-writer-sms → hook
     ↓
post-writer-sms → corpo do post
     ↓
[GATE C] copy-qa-sms
     ↓
caption-writer-sms → legenda (se plataforma visual)
```

### Thread
```
production-orchestrator-sms → diagnostica pedido
          ↓
[GATE B] Ângulo definido? NÃO → narrative-framework-sms
          ↓
hook-writer-sms → primeiro tweet/post
     ↓
thread-writer-sms → fio completo
     ↓
[GATE C] copy-qa-sms
```

### Artigo / long-form / X Article / newsletter
```
production-orchestrator-sms → diagnostica pedido
  (critério: +500 palavras, múltiplas seções H2, estrutura editorial)
          ↓
[GATE B] Ângulo definido? NÃO → narrative-framework-sms
          ↓
article-writer-sms → texto completo em Markdown
          ↓
[GATE C] copy-qa-sms
          ↓
Oferecer:
  [a] illustration-writer-sms → ilustrações editoriais (JSONs de prompt)
  [b] x-article-publisher → publica no X como rascunho (nunca automático)
```

### Calendário mensal
```
content-calendar-sms → cronograma com temas, datas, formatos
```

### Revisão de performance
```
performance-analyzer-sms → insights das métricas
     ↓
content-pattern-analyzer-sms → o que funcionou
     ↓
audience-growth-tracker-sms → tendência de crescimento
     ↓
optimization-advisor-sms → próximas ações
```

## Checklist de qualidade por peça

### Carrossel
- [ ] 3 ângulos propostos antes de qualquer slide
- [ ] Ângulo aprovado pelo usuário (GATE 4.5)
- [ ] Script com 9-12 slides estruturados (GANCHO → CONTEXTO → ANÁLISE → IMPLICAÇÕES → AÇÃO → CTA)
- [ ] Slides CERNE identificados e formatados (100% do espaço, dados quantificados, máx 8 linhas)
- [ ] Slides SECUNDÁRIOS formatados (máx 4 linhas, sem placeholder de imagem no copy)
- [ ] 5 variações de capa geradas automaticamente ao final
- [ ] 3 variações de legenda geradas automaticamente ao final
- [ ] Visual com consistência de brand-spec.md (card-news-generator-v2)
- [ ] Caption final tem primeira linha como hook (antes do "ver mais")

### Post único
- [ ] Primeira linha para o scroll sem depender do visual
- [ ] Voz do cliente reconhecível
- [ ] CTA específico ao final
- [ ] Hashtags relevantes (não genéricas)
- [ ] copy-qa-sms executado antes da entrega (GATE C)

### Artigo / long-form
- [ ] Ângulo aprovado antes da escrita (GATE B — narrative-framework-sms, se aplicável)
- [ ] Estrutura editorial com seções H2 claras
- [ ] copy-qa-sms executado antes da entrega (GATE C)
- [ ] Publicação sempre como rascunho (x-article-publisher nunca publica automaticamente)

### Todos os formatos (gate universal)
- [ ] Pedido passou por production-orchestrator-sms (ou skill de criação acionada diretamente e correta para o formato — GATE A)
- [ ] copy-qa-sms executado antes de qualquer entrega final (GATE C)
- [ ] Artefato salvo em clients/[cliente]/runs/[data]/ (GATE D)

### Safe area (obrigatório em todos os formatos visuais)
- [ ] Feed 4:5 (1080x1350): zona segura 952x1222px — 64px de padding em todos os lados
- [ ] Feed quadrado (1080x1080): zona segura 952x952px — 64px de padding em todos os lados
- [ ] Stories/Reels (1080x1920): 250px de margem no topo e rodapé (UI do Instagram/TikTok), 64px nas laterais
- [ ] Nenhum texto, ícone, CTA ou elemento de marca encostando nas bordas da imagem
- [ ] JSON gerado via json-prompt-generator deve incluir campo `safe_area` em `composition`

## Setup de cliente (executar uma vez)
```
social-media-context-sms → .agents/social-media-context-sms.md
     ↓
content-strategy-sms → pilares de conteúdo
     ↓
platform-strategy-sms → estratégia por plataforma
```
Após setup: todas as skills leem o contexto automaticamente.
