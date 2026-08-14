# Blank-style — Grupos 2 e 3 (v2) — sem linha divisória, opção 1 (espaço negativo)

> Correção: removida qualquer possibilidade de linha/traço decorativo separando blocos de texto (lia como travessão visual). Substituído por respiro maior (espaço negativo) entre headline e corpo. Regra adicionada explicitamente em `negative_rules` nos dois, pra não voltar a acontecer na aplicação real.

---

## GRUPO 3 — Texto puro, sem imagem (CLARA v2, sem divisória)

```json
{
  "template": "carrossel-blank-style",
  "version": "grupo-3-texto-puro-clara-v2",
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "background_color": "#F7F5F1"
  },
  "zones": {
    "header": {
      "height": "50px",
      "position": "top",
      "margin_lateral": "56px",
      "margin_top": "40px",
      "blocks": [
        { "id": "handle", "content": "@diego.spanevello", "font_family": "sans-serif", "font_weight": 700, "font_size": "14px", "font_color": "#1A1A1A" },
        { "id": "categoria", "content": "| Inteligência Artificial", "font_family": "sans-serif", "font_weight": 600, "font_size": "14px", "font_color": "rgba(26,26,26,0.45)" }
      ],
      "avatar": "nenhum — apenas texto, sem foto de perfil",
      "note": "handle + categoria na mesma linha, separados por pipe — mesmo padrão já usado na capa"
    },
    "content": {
      "position": "centralizado verticalmente no corpo do frame",
      "margin_lateral": "56px",
      "blocks": [
        {
          "id": "pre-headline",
          "type": "text",
          "content": "Texto de contexto pequeno aqui",
          "font_family": "sans-serif regular",
          "font_size": "16px",
          "font_color": "#E8722A",
          "text_transform": "uppercase",
          "letter_spacing": "2px",
          "margin_bottom": "16px"
        },
        {
          "id": "headline",
          "type": "text",
          "content": "Frase central do slide, pode quebrar em 2-3 linhas",
          "font_family": "serif display",
          "font_size": "48px",
          "font_style": "regular, com trecho em itálico para ênfase",
          "font_color": "#1A1A1A",
          "line_height": "1.1",
          "margin_bottom": "48px",
          "note": "margin_bottom aumentado de 20px para 48px — respiro faz o papel que antes era feito pela linha divisoria, agora removida"
        },
        {
          "id": "body",
          "type": "text",
          "content": "Texto complementar mais leve, explicando ou aprofundando a ideia central.",
          "font_family": "sans-serif regular",
          "font_size": "22px",
          "font_color": "rgba(26,26,26,0.6)",
          "line_height": "1.5"
        }
      ]
    },
    "image": { "exists": false, "note": "GRUPO 3 não tem zona de imagem — slide 100% tipográfico" },
    "footer": {
      "height": "40px",
      "position": "bottom",
      "margin_lateral": "56px",
      "margin_bottom": "36px",
      "content": "INTUS HUB",
      "note": "somente texto — sem logomark/ícone",
      "font_family": "sans-serif regular",
      "font_size": "13px",
      "font_color": "rgba(26,26,26,0.5)",
      "letter_spacing": "3px",
      "text_transform": "uppercase",
      "position_horizontal": "esquerda"
    }
  },
  "markings_available": {
    "italic_emphasis": { "usage": "palavra ou trecho de destaque dentro da headline serif" },
    "color_swap": { "accent_color": "#E8722A", "usage": "pré-headline sempre em laranja; uso pontual na headline se necessário" },
    "underline": { "color": "#E8722A", "thickness": "3px", "usage": "reforço em frase de apoio dentro do body" }
  },
  "negative_rules": [
    "sem travessao",
    "sem linha ou traco decorativo separando blocos de texto (headline/corpo) — usar APENAS espaco negativo (respiro) pra separar secoes",
    "sem avatar no header",
    "sem logomark no footer — apenas texto INTUS HUB",
    "maximo 1 ideia central por slide",
    "headline sempre serif display, nunca sans-serif bold",
    "nunca forcar uma imagem so pra preencher espaco",
    "respiro generoso: priorizar espaco negativo sempre que precisar separar blocos",
    "fundo sempre off-white, nunca branco puro (#FFFFFF)"
  ]
}
```

---

## GRUPO 2 — Imagem lateral (esquerda) + Texto (direita) (CLARA v2, sem divisória)

```json
{
  "template": "carrossel-blank-style",
  "version": "grupo-2-split-imagem-texto-clara-v2",
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "background_color": "#F7F5F1"
  },
  "zones": {
    "header": {
      "height": "50px",
      "position": "top",
      "margin_lateral": "56px",
      "margin_top": "40px",
      "blocks": [
        { "id": "handle", "content": "@diego.spanevello", "font_family": "sans-serif", "font_weight": 700, "font_size": "14px", "font_color": "#1A1A1A" },
        { "id": "categoria", "content": "| Inteligência Artificial", "font_family": "sans-serif", "font_weight": 600, "font_size": "14px", "font_color": "rgba(26,26,26,0.45)" }
      ],
      "avatar": "nenhum — apenas texto, sem foto de perfil",
      "note": "handle + categoria na mesma linha, separados por pipe — mesmo padrão já usado na capa"
    },
    "content": {
      "layout": "split-2-colunas",
      "position": "abaixo do header, ocupa o corpo principal do frame",
      "margin_top": "32px",
      "note": "desvio do schema padrão header/image/content/footer — imagem aninhada na coluna esquerda do content",
      "columns": [
        {
          "id": "coluna-imagem",
          "width": "45%",
          "position": "esquerda",
          "margin_lateral_externa": "56px",
          "image": {
            "height": "100% da altura da coluna",
            "border_radius": "16px",
            "full_bleed": false,
            "asset_prompt": "PLACEHOLDER — preencher via json-prompt-generator no momento da geração real do slide. Não baked-in no template.",
            "note": "foto retrato ou still, ocupa toda a altura da coluna"
          }
        },
        {
          "id": "coluna-texto",
          "width": "55%",
          "position": "direita",
          "margin_lateral_interna": "32px",
          "margin_lateral_externa": "56px",
          "blocks": [
            {
              "id": "headline",
              "type": "text",
              "content": "Manchete ou dado de impacto",
              "font_family": "serif display",
              "font_size": "34px",
              "font_style": "regular, com trecho em itálico para ênfase",
              "font_color": "#1A1A1A",
              "line_height": "1.1",
              "margin_bottom": "28px",
              "note": "margin_bottom aumentado de 16px para 28px — reforca separacao por espaco negativo, sem linha"
            },
            {
              "id": "texto-apoio",
              "type": "text",
              "content": "Texto complementar, explicação ou citação relacionada à imagem ao lado.",
              "font_family": "sans-serif regular",
              "font_size": "20px",
              "font_color": "rgba(26,26,26,0.65)",
              "line_height": "1.4"
            }
          ]
        }
      ]
    },
    "footer": {
      "height": "40px",
      "position": "bottom",
      "margin_lateral": "56px",
      "margin_bottom": "36px",
      "content": "INTUS HUB",
      "note": "somente texto — sem logomark/ícone",
      "font_family": "sans-serif regular",
      "font_size": "13px",
      "font_color": "rgba(26,26,26,0.5)",
      "letter_spacing": "3px",
      "text_transform": "uppercase",
      "position_horizontal": "esquerda"
    }
  },
  "markings_available": {
    "italic_emphasis": { "usage": "palavra ou trecho de destaque dentro da headline serif" },
    "color_swap": { "accent_color": "#E8722A", "usage": "uso pontual, quando o itálico não for suficiente para o destaque" }
  },
  "negative_rules": [
    "sem travessao",
    "sem linha ou traco decorativo separando blocos de texto (headline/corpo) — usar APENAS espaco negativo (respiro) pra separar secoes",
    "sem avatar no header",
    "sem logomark no footer — apenas texto INTUS HUB",
    "asset_prompt de imagem nunca baked-in no template — sempre placeholder, preenchido na geracao real",
    "maximo 1 ideia central por slide",
    "imagem sempre com border_radius, nunca sem",
    "headline sempre serif display, nunca sans-serif bold",
    "coluna de texto nunca mais larga que 60% do frame",
    "fundo sempre off-white, nunca branco puro (#FFFFFF)"
  ]
}
```
