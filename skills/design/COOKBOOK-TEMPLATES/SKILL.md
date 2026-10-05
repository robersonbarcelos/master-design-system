---
name: cookbook-templates
description: "Sistema de templates visuais pré-codificados do AI Visual Prompt Cookbook (VigoZhao). Use quando o usuário pedir uma capa de carrossel ou post com um estilo visual forte e específico, sem imagem de referência. Aciona estilos pré-codificados com variáveis substituíveis — produz prompts de alta densidade para Freepik, ChatGPT Image ou qualquer gerador. Triggers: 'estilo de revista', 'capa editorial', 'poster de impacto', 'estilo visual para capa', 'quero um visual diferente', 'poster tipográfico'."
---

# Cookbook Templates

Sistema de estilos visuais pré-codificados para geração de imagem AI. Cada estilo é um template com variáveis substituíveis que garante consistência visual entre múltiplas gerações.

## Repositório de origem
`https://github.com/VigoZhao/AI-Visual-Prompt-Cookbook` — 150+ estilos organizados por categoria.

---

## REGRA CRÍTICA — Nunca resumir o template ⚠️

**ERRADO:** extrair os pontos principais e reescrever o prompt
**CERTO:** usar o `prompt_template` EXATO da skill, substituindo apenas os `{PLACEHOLDERS}`

Resumir o template perde a densidade de instrução que produz resultados ricos.
O template completo tem 800–1200 palavras — use tudo.

---

## Workflow de uso

### Passo 1 — Escolher o estilo
Consultar `styles/` nesta pasta. Cada arquivo tem o template completo.
Para estilos não salvos aqui, buscar em `github.com/VigoZhao/AI-Visual-Prompt-Cookbook/styles/`.

### Passo 2 — Ler o brand do cliente
Carregar `visual-system.md` e `brand-spec.md` do cliente ativo antes de preencher as variáveis.

### Passo 3 — Preencher as variáveis
Substituir cada `{VARIÁVEL}` com conteúdo real do cliente:

| Variável universal | O que preencher |
|---|---|
| `{ASPECT_RATIO}` | 4:5 (feed Instagram) · 9:16 (stories) · 1:1 (quadrado) |
| `{SUBJECT}` | Sujeito principal — pessoa, produto, objeto |
| `{SUBJECT_ACTION}` | Pose, gesto ou ação específica |
| `{PRODUCT_OR_PROP}` | Objeto secundário ou prop visual |
| `{LOCATION}` | Ambiente ou contexto |
| `{BACKGROUND_ELEMENTS}` | Detalhes de fundo (2-3 elementos contidos) |
| `{MAIN_TEXT}` | Headline principal — copy da capa |
| `{SECONDARY_TEXT}` | Copy de suporte, deck, microcópia |
| `{ACCENT_SYMBOL}` | Símbolo de acento (seta, estrela, emblema) |
| `{WARDROBE_STYLE}` | Direção de figurino ou tratamento de superfície |
| `{STYLE_FIDELITY_ANCHORS}` | As âncoras do estilo — copiar do arquivo do estilo |
| `{SOURCE_CONTENT_TO_AVOID}` | O que NÃO replicar — copiar do arquivo do estilo |

### Passo 4 — Adaptação de cor para o brand (quando necessário)
Nos `{STYLE_FIDELITY_ANCHORS}`, substituir as cores originais do estilo pelas cores do cliente:

```
Original:  "signal red" → Brand:  "gold #F0B429"
Original:  "warm paper" → Brand:  "near-black #050D1F"
Original:  "cobalt"     → Brand:  "cobalt #1E4D9B" (manter se compatível)
```

Fazer isso nas âncoras E nos parágrafos de instrução do template.

### Passo 5 — Gerar
Colar o prompt completo no gerador (Freepik Mystic, ChatGPT Image, Midjourney).

---

## Estilos salvos localmente

| Arquivo | Estilo | Mood | Melhor uso |
|---|---|---|---|
| `styles/signal-red-petal-profile.md` | Magazine cover editorial | Autoridade, maximalista | Capa de carrossel de autoridade |
| `styles/signal-red-contour.md` | Contorno severo dois tons | Institucional, minimal | Post de impacto, anti-ruído |
| `styles/cobalt-pop-cutout.md` | Recorte pop fundo azul | Jovem, editorial, impacto | Carrossel de produto/creator |
| `styles/burnt-orange-halftone.md` | Colagem halftone hero | Editorial denso, herói | Post de autoridade/personagem |

---

## Integração com o sistema existente

Este sistema complementa (não substitui) o `json-prompt-generator`:

| Situação | Usar |
|---|---|
| Tem imagem de referência → quer replicar | `json-prompt-generator` |
| Não tem referência → quer estilo forte pré-definido | `cookbook-templates` |
| Quer consistência de estilo em múltiplos posts | `cookbook-templates` (mesmo estilo, variáveis trocadas) |

---

## Resultado validado

**Signal Red Petal Profile → Intus Hub** (2026-08-18):
- Template completo com cores adaptadas (vermelho→dourado, bege→escuro)
- Produziu capa editorial de alta qualidade com identidade de revista
- Manteve: tipografia fragmentada, figura de perfil, mantle de lobes, rail editorial, emblema, vinheta de gráfico

**Lição principal:** o template intacto produz resultado profundamente mais rico que qualquer versão resumida.
