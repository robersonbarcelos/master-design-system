# Visual System — Super Agente de IA

> Sistema visual da campanha: grupos, regras de prompt, specs.
> Paleta: laranja `#E84000` + preto `#0a0a0a` — SEPARADO da identidade institucional do INTUS HUB.

---

## 01 | Especificações Técnicas

| Formato | Dimensões | Uso |
|---------|-----------|-----|
| Feed quadrado | 1080×1080px | Instagram padrão |
| Feed retrato | 1080×1350px | Instagram 4:5 (preferencial) |
| Stories/Reels | 1080×1920px | Stories 9:16 |
| YouTube Thumb | 1280×720px | YouTube / Shorts |
| TikTok | 1080×1920px | Vertical |

---

## 02 | Grupos Visuais

### GRUPO 1 — Contraste / Problema
- **Quando usar:** Conteúdo TOPO — dor, contraste antes/depois, "isso não é agente"
- **Layout:** Full bleed escuro com texto centralizado ou dois painéis (esquerda ruim / direita bom)
- **Paleta:** Fundo `#0a0a0a` · texto branco · destaque laranja `#E84000` no contraste positivo
- **Mood:** Tenso, direto, reconhecível
- **Elementos:** Linha de separação laranja no meio, texto grande Inter Tight Black

### GRUPO 2 — Demonstração de Agente (Aspira/Clóvis)
- **Quando usar:** Conteúdo MEIO — mostrar o agente em ação, bastidores da operação
- **Layout:** Interface de chat/UI do agente + foto do Diego ou printscreen de conversa
- **Paleta:** Fundo `#0a0a0a` · card de chat com borda laranja `#E84000` + glow sutil
- **Mood:** Técnico, concreto, real — sem staging óbvio
- **Elementos:** Avatar do agente (Aspira/Clóvis), timestamp, mensagens reais

### GRUPO 3 — Diego / Autoridade
- **Quando usar:** Conteúdo MEIO — prova social pessoal, citação, speech de Diego
- **Layout:** Diego em fundo escuro + texto de citação em destaque
- **Paleta:** Foto com rim light azul `#1E4D9B` (camiseta preta) · texto branco · acento laranja nos números
- **Mood:** Autoridade sem arrogância, direto, sério mas humano
- **Elementos:** Foto de Diego com rim light, speech bubble ou texto solto com aspas
- **Referência de rosto:** sempre que o Diego aparecer, o JSON usa a foto de referência anexada pra rosto/características — o prompt só descreve pose, expressão, ângulo e roupa (ver `production-rules.md` → "Regra de referência de rosto — Diego")

### GRUPO 4 — Educativo / Carrossel
- **Quando usar:** Conteúdo de MEIO — explicar conceito (identidade, memória, contexto, módulos)
- **Layout:** Header com título laranja + corpo com texto em cards escuros; numeração por slide
- **Paleta:** `#0a0a0a` fundo · números/títulos em `#E84000` · texto body branco
- **Mood:** Didático, limpo, legível
- **Elementos:** Número do slide grande em laranja, linha divisória sutil, ícone emoji por conceito

### GRUPO 5 — Oferta / Conversão
- **Quando usar:** Conteúdo FUNDO — preço, value stack, garantia, CTA
- **Layout:** Card de oferta escuro com âncora riscada + preço real em destaque + lista de entregáveis
- **Paleta:** Fundo `#0a0a0a` · âncora riscada em text-muted · preço real em `#E84000` grande · verde para checkmarks
- **Mood:** Urgente, claro, sem hype
- **Elementos:** Âncora R$997 riscada, R$87,95 ou 6x R$16,50 em destaque, selos de garantia e acesso vitalício

### GRUPO 6 — Resultados / Alunos
- **Quando usar:** Prova social — depoimentos de Denys Buso, Arcanjo, outros
- **Layout:** Card de testemunho com foto do aluno + citação + resultado em destaque
- **Paleta:** `#0a0a0a` fundo · borda card laranja `#E84000` · texto principal branco · badge de resultado em laranja
- **Mood:** Autêntico, concreto, resultado específico
- **Elementos:** Foto de avatar real, badge "resultado real", quote em aspas, linha final de resultado

---

## 03 | Workflow de Produção de Prompts

1. Definir grupo visual (1-6 acima)
2. Propor ideias em texto (composição, ângulo, iluminação) — **cada ideia deve incluir a alocação de copy** (onde headline/subhead/CTA ficam na cena, com o texto real), não só a descrição visual
3. Aguardar aprovação de Diego
4. Gerar JSON com prompt completo para a variação aprovada — criativo **completo**, com copy final (headline/subhead — **sem CTA** em anúncio pago, ver "04 | Regras de Prompt"), fonte (`references/fontes-variacao.md`) e composição (`references/regras-composicao.md`) já embutidos no prompt
5. Revisar o resultado gerado — checar tipografia, acentuação e kerming do texto renderizado antes de aprovar entrega

---

## 04 | Regras de Prompt

### SEMPRE incluir
- Hex codes explícitos: `#E84000` e `#0a0a0a` (ou paleta de variação aprovada em `references/paletas-variacao.md`)
- "dark background, pure black" — sem variação
- "NO watermark, NO handle" na imagem
- Copy final exata — **headline + subhead apenas** (NUNCA CTA — ver "Regra de CTA em criativos de Meta Ads" abaixo), com texto, fonte (`references/fontes-variacao.md`) e posição especificados — criativo sai **completo** do prompt
- "cinematic lighting" ou "studio lighting" — nunca iluminação plana
- "area limpa para logo" quando relevante
- Margem/zona inferior limpa reservada para o botão de CTA nativo do Meta (safe zones em `meta-ads-specs.md`)

### Regra de CTA em criativos de Meta Ads
NUNCA renderizar botão ou texto de CTA ("Saiba Mais", "Clique aqui", pill button, seta de CTA) dentro da arte de um criativo de **anúncio pago** (Feed Ads, Stories/Reels Ads) — o Meta Ads já exibe o botão nativo (abaixo da imagem no Feed; sobreposto na zona inferior em Stories/Reels), então um CTA desenhado na arte duplica a informação e ainda pode ser coberto pelo botão real. O criativo leva só headline + subhead; a zona inferior fica limpa conforme as safe zones documentadas em `meta-ads-specs.md`. Essa regra é específica de anúncio pago — não vale pra posts orgânicos do feed @intushub, que não têm esse overlay.

### NUNCA incluir
- Fundo branco ou claro
- Elementos azuis ou roxos (conflito com paleta institucional, exceto rim light do Diego)
- "8K", "masterpiece", "ultra-realistic" — banidos como prompts clichê

> Robô humanoide **liberado** (decisão explícita do cliente — deixou de ser regra de trava). Pode usar robô/mão/braço mecânico, inclusive de frente pro Diego, como representação do agente.

### Negative prompt padrão
```
white background, light background, blue tones, purple tones, text overlay, watermark,
handle, username, logo in corner, neon cyberpunk, RGB gaming aesthetic,
overexposed, washed out colors, stock photo look, corporate clipart style
```

### JSON template padrão — Super Agente de IA

> ⚠️ Este é o schema simplificado — só usar quando não houver imagem de referência. Quando houver referência, seguir a regra do `CLAUDE.md` (usar a skill `json-prompt-generator`, schema completo).

```json
{
  "prompt": "[sujeito ou cena], dark background #0a0a0a, accent color #E84000 glow, [lighting: cinematic/rim/studio], [composição], exact headline/subhead copy rendered (SEM CTA — botão nativo do Meta cobre isso) in [fonte de fontes-variacao.md], Inter Tight aesthetic, premium dark UI feel, no watermark, clean area for logo, clean bottom margin for Meta's native CTA button",
  "negative_prompt": "white background, light background, blue tones, purple tones, watermark, neon cyberpunk, RGB gaming, overexposed",
  "aspect_ratio": "4:5",
  "style": "premium dark product photography, cinematic lighting, #E84000 accent glow",
  "composition": {
    "safe_area": "minimum 64px padding all sides — no icons or elements touching edges. Safe zone: 952x1222px inside 1080x1350px (feed 4:5). Stories/reels: 250px top and bottom for UI chrome, 64px sides."
  }
}
```

---

## 05 | Elementos Visuais Recorrentes

| Elemento | Descrição | Regra de uso |
|----------|-----------|--------------|
| Glow laranja | Radial glow `rgba(232,64,0,0.16)` | Em cards de destaque, bordas ativas, CTAs |
| Borda laranja | `border: 1px solid #E84000` ou `rgba(232,64,0,0.4)` | Cards, separadores, destaques |
| Eyebrow label | Texto pequeno uppercase + letter-spacing acima do título | SEMPRE antes de headline principal |
| Âncora riscada | R$997 com linha atravessada | Só em posts de conversão |
| Badge de garantia | "7 DIAS" em círculo laranja com anel gradiente | Só em posts de oferta/garantia |
| Task dot | Ponto `·` ou `•` laranja | Listas de entregáveis, features, tarefas dos agentes |
| Seta CTA | `→` no final do texto de CTA | Só em posts **orgânicos** (feed @intushub) ou em legendas/caption — NUNCA renderizado dentro da arte de criativo de anúncio pago Meta Ads (botão nativo do Meta já cobre isso, ver "Regra de CTA em criativos de Meta Ads") |
