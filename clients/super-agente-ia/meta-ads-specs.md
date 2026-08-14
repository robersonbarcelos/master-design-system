# Meta Ads Specs — Super Agente de IA

> Referência técnica de dimensões, safe zones e recuos para criativos Meta Ads.
> Aplica para todas as campanhas do produto (Feed + Stories/Reels).
> **Validado em 2026-07-09** contra o Meta Unified Safe Zone (unificação Facebook/Instagram Stories+Reels, março 2026). Ver fontes no rodapé.

---

## Formatos Obrigatórios

| Formato | Dimensão | Placements cobertos |
|---------|----------|---------------------|
| **Feed 1:1** | 1080×1080px | Feed, Marketplace, Right Column, Messenger |
| **Feed 4:5** | 1080×1350px | Feed single-image vertical (mais espaço mobile) |
| **Stories / Reels 9:16** | 1080×1920px | Stories + Reels (mesmo asset cobre os dois) |

---

## Safe Zones — Stories e Reels (1080×1920)

| Zona | Pixels | % frame | Regra |
|------|--------|---------|-------|
| **Topo — LIVRE** | 0 → 250px | ~14% | Ícone de perfil + tag "Patrocinado" — NADA de texto/logo aqui |
| **Safe Zone — CONTEÚDO** | **250px → 1248px** | **~51%** | Todo conteúdo visual vai aqui (headline, logo, claim, foto) |
| **Base — LIVRE** | 1248px → 1920px | ~35% | Botão de CTA nativo do Meta + caption — NADA de texto/logo aqui |
| **Laterais** | 87px cada lado | ~6% | Manter margem mínima para evitar corte em telas largas |

### Diagrama de referência (9:16)

```
[0px]
─────────────────────────────────────
  TOPO LIVRE (~250px)
  ícone de perfil + "Patrocinado"
─────────────────────────────────────
[250px]
  
  SAFE ZONE — COLOCA TUDO AQUI
  headline · logo · foto Diego
  claim · número âncora · ícone
  
  998px de altura disponível
  
[1248px]
─────────────────────────────────────
  BASE LIVRE (~672px)
  botão CTA do Meta + caption
─────────────────────────────────────
[1920px]
```

---

## Regra de CTA — NÃO renderizar botão no criativo

O Meta Ads sempre exibe o próprio botão de CTA nativo (ex: "Saiba mais", "Comprar agora") direcionando pro site — no Feed ele aparece **abaixo** da imagem (fora do criativo); em Stories/Reels ele aparece **sobreposto** na zona "Base — LIVRE" (1248px → 1920px, ver tabela abaixo).

Por isso: **nunca** desenhar um botão, pill ou texto de CTA ("Saiba Mais →", "Clique aqui" etc.) dentro da arte do criativo. Isso duplica a informação e, em Stories/Reels, pode ficar coberto pelo botão real do Meta. O criativo leva só headline + subhead — CTA é resolvido pela plataforma. Regra vale para anúncio pago; não se aplica a posts orgânicos do feed @intushub.

---

## Safe Zones — Feed (1080×1080 e 1080×1350)

> Feed não tem overlay de UI sobre a imagem (CTA fica abaixo, fora do criativo). O risco aqui é **corte por crop** — o mesmo asset é reaproveitado em Feed, Marketplace, Right Column e Messenger, cada um cortando a imagem de forma diferente.

| Regra | Aplicação |
|-------|-----------|
| Padding mínimo (bordas) | 40px em todos os lados — abaixo disso, risco real de corte |
| Padding recomendado p/ elementos críticos | **100px** para logo, headline principal e CTA visual — cobre o crop mais agressivo (Right Column/Marketplace) |
| Centralizar produto/oferta | Zona central ~80% do frame (± 100px de cada borda) |
| Logo/wordmark SUPER AGENTE IA | Canto inferior — dentro dos 100px de padding recomendado (NUNCA logo INTUS HUB dentro da arte do criativo) |

---

## Checklist de Produção por Formato

### Feed 1:1 (1080×1080)
- [ ] Padding mínimo 40px em todos os lados
- [ ] Logo/wordmark SUPER AGENTE IA no canto inferior direito (dentro do padding) — nunca logo INTUS HUB na arte
- [ ] Texto principal centralizado no frame
- [ ] Paleta `#E84000` + `#0a0a0a`

### Feed 4:5 (1080×1350)
- [ ] Padding mínimo 40px em todos os lados
- [ ] Produto/oferta na metade superior (área mais visível no scroll)
- [ ] Sem botão/texto de CTA no criativo — o Meta Ads já exibe o botão nativo abaixo da imagem
- [ ] Logo/wordmark SUPER AGENTE IA no canto inferior direito — nunca logo INTUS HUB na arte

### Stories/Reels 9:16 (1080×1920)
- [ ] NADA acima de y=250px (ícone de perfil cobre)
- [ ] TODO conteúdo entre y=250px e y=1248px
- [ ] NADA abaixo de y=1248px (CTA nativo e caption do Meta cobrem)
- [ ] Margens laterais mínimas de 87px
- [ ] Logo/wordmark SUPER AGENTE IA posicionado entre y=1100px e y=1200px (perto do fim da safe zone) — nunca logo INTUS HUB na arte
- [ ] Sem botão/texto de CTA renderizado no criativo em nenhuma zona — o botão nativo do Meta cobre a base (y=1248px → 1920px)

---

## Recomendação de Versões por Criativo

Para cada criativo da campanha, produzir:
1. **1:1** (1080×1080) — version padrão, maior distribuição
2. **9:16** (1080×1920) — version Stories/Reels, adaptada com safe zones

> Nota: não adaptar o 1:1 para 9:16 simplesmente adicionando barras pretas.
> A versão 9:16 deve ser redesenhada para a proporção vertical desde o início.

---

## Fontes (validação 2026-07-09)

- [Meta Ads Safe Zones: A Guide to the 2026 Unified Creative Updates](https://billo.app/blog/meta-ads-safe-zones/)
- [Meta Reels Safe Zone 14% Top / 35% Bottom / 6% Sides — 2026 Official Guide](https://behaviour.digital/post/meta-reels-safe-zone-14-top-35-bottom-6-sides-the-2026-official-guide)
- [Meta Ad Sizes 2026: Every Placement Spec + Safe Zones](https://www.get-ryze.ai/blog/facebook-ad-sizes-complete-specs-guide-for-2026)
- [Meta Ads Safe Zone Checker 2026](https://www.poster.ly/tools/meta-ads-safe-zone-visualizer)
