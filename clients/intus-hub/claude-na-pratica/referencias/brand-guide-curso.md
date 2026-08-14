---
name: brand-guide-claude-na-pratica
description: "Sistema visual completo do curso Claude na Prática — paleta, tipografia, componentes e regras de uso"
---

# Brand Guide — Claude na Prática
**Estilo:** Mineral · Clean · Atemporal
**Versão:** 1.0 · Julho 2026

---

## Paleta de cores

### Cores principais
| Nome | Hex | Uso |
|---|---|---|
| Fundo principal | `#FAFAF8` | Background de slides, páginas, cards |
| Índigo escuro | `#1E3A5F` | Títulos, textos principais, barras de módulo |
| Âmbar | `#F59E0B` | Accent, badges, marcadores, destaques |
| Texto corpo | `#374151` | Corpo de texto, bullets |
| Texto mudo | `#6B7280` | Subtítulos, meta info, timestamps |
| Neutro claro | `#E5E7EB` | Bordas, divisores, fundos secundários |
| Branco puro | `#FFFFFF` | Cards sobre fundo, popups |

### Cores de suporte
| Nome | Hex | Uso |
|---|---|---|
| Índigo médio | `#2D5A8E` | Hover states, variação do primário |
| Âmbar escuro | `#D97706` | Hover do accent, textos sobre fundo claro |
| Fundo módulo | `#1E3A5F` | Capas de módulo (fundo escuro) |
| Texto sobre escuro | `#FFFFFF` | Texto sobre fundo índigo |
| Texto suave escuro | `rgba(255,255,255,0.6)` | Subtítulos sobre fundo índigo |

### Nunca usar
- Preto puro `#000000` — usar `#111827` no máximo
- Branco puro como fundo de slide — usar `#FAFAF8`
- Cores saturadas sem relação com a paleta

---

## Tipografia

**Fonte principal:** Inter (Google Fonts)
**URL:** `https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap`

| Elemento | Tamanho | Peso | Cor |
|---|---|---|---|
| Título de capa | 32–40px | 700 | `#111827` |
| Título de slide | 18–22px | 600 | `#111827` |
| Badge / label | 9–10px | 600 | `#F59E0B` (ou `#1E3A5F`) |
| Corpo / bullets | 12–14px | 400 | `#374151` |
| Meta info | 9–10px | 600 | `#9CA3AF` |
| Logo/wordmark | 8px | 600 | varia por contexto |
| Letter-spacing badges | 1.5–2px | — | uppercase obrigatório |

---

## Componentes de slide

### 1. Capa do curso
```
Fundo: #FAFAF8
- Logo Intus Hub (topo, letter-spacing 2px, #F59E0B, uppercase)
- Título grande: "Claude na Prática" (#111827, 700)
- Subtítulo: tom descritivo (#6B7280)
- Barra dupla no rodapé: índigo (#1E3A5F) + âmbar (#F59E0B) 12px
```

### 2. Capa de módulo
```
Fundo: #1E3A5F (escuro)
- Badge módulo (topo, #F59E0B, letra maiúscula)
- Título do módulo (#FFFFFF, 700)
- Subtítulo: aulas do módulo (rgba branco 0.6)
- Indicador de progresso no rodapé (3 dots)
```

### 3. Slide de aula (conteúdo)
```
Fundo: #FAFAF8
- Barra vertical esquerda: #F59E0B (3px, altura total)
- Badge aula (topo, #F59E0B, uppercase, letter-spacing)
- Título da aula (#111827, 600)
- Bullets com marcador círculo #1E3A5F
- Meta rodapé: duração + tipo (DEMO/PRÁTICA) — #9CA3AF
```

### 4. Slide de conceito / comparativo
```
Fundo: #FAFAF8
- Header com badge
- Tabela ou grid de 2 colunas
- Coluna de destaque com borda esquerda #F59E0B
- Rodapé com barra índigo
```

### 5. Slide de ação / entregável
```
Fundo: #1E3A5F (escuro)
- Ícone de check ou seta em âmbar
- Texto da ação em branco
- CTA box com borda âmbar
```

---

## Regras de uso

### Logotipo / wordmark do curso
- Texto: `CLAUDE NA PRÁTICA`
- Fonte: Inter 600, letter-spacing 2px, uppercase
- Cor padrão: `#1E3A5F`
- Sobre fundo escuro: `#F59E0B` ou `#FFFFFF`
- Sempre acompanhar de: `· INTUS HUB` em opacidade 45%

### Accent (âmbar)
- Usado APENAS para: badges de aula, marcadores de bullet, linha de destaque, CTA buttons
- Nunca usar como fundo de área grande
- Máximo 2 elementos âmbar por slide

### Barras de rodapé
- Padrão padrão: barra índigo (`#1E3A5F`) + dot âmbar (`#F59E0B`) no canto direito
- Altura: 3px
- Border-radius: 2px

### Espaçamento interno dos slides
- Padding padrão: 24px horizontal, 20px vertical
- Gap entre elementos: 8–12px
- Gap entre seções: 16–20px

---

## Assets de aplicação

### Thumbnails de aula (formato Lastlink)
- Tamanho: 1280×720px (16:9)
- Fundo: `#FAFAF8`
- Índigo como elemento geométrico decorativo (barra lateral ou bloco)
- Âmbar para o número da aula
- Título da aula em Inter 700

### Cards de módulo (Lastlink)
- Seguir padrão `super-agente-modulos.md` adaptado para a paleta Mineral
- Fundo do card: `#1E3A5F`
- Texto: branco
- Accent: `#F59E0B`

### Cover/banner (Lastlink 16:9)
- Seguir padrão `super-agente-covers.md`
- Fundo: `#FAFAF8` ou split 50/50 com `#1E3A5F`
- Título do curso em índigo, destaque em âmbar

---

## Referência de combinações aprovadas

| Contexto | Fundo | Texto título | Accent |
|---|---|---|---|
| Slide normal | `#FAFAF8` | `#111827` | `#F59E0B` |
| Capa módulo | `#1E3A5F` | `#FFFFFF` | `#F59E0B` |
| Card destaque | `#FFFFFF` | `#1E3A5F` | `#F59E0B` |
| Slide de ação | `#1E3A5F` | `#FFFFFF` | `#F59E0B` |
| Badge label | `#FEF3C7` | `#92400E` | — |
| Tag tipo DEMO | `#FEF3C7` | `#92400E` | — |
| Tag tipo PRÁTICA | `#DCFCE7` | `#15803D` | — |
