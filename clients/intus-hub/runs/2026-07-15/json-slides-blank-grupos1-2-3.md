# Blank-style — Slides Internos — Grupos 1, 2 e 3 (exemplos de aplicação de template)

> Templates com `asset_prompt` em PLACEHOLDER — nunca baked-in. Preencher via skill `json-prompt-generator` no momento da geração real de cada slide.
> Elementos fixos (assinatura do estilo Blank): header só texto (sem avatar), footer com logomark + wordmark "BLANK".

---

## GRUPO 1 — Headline → Imagem full-width → Texto abaixo

```json
{
  "template": "carrossel-blank-style",
  "version": "grupo-1-headline-imagem-texto",
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "background_color": "#0D0D0D"
  },
  "zones": {
    "header": {
      "height": "70px",
      "position": "top",
      "margin_lateral": "56px",
      "margin_top": "40px",
      "content": "CSM — SOCIAL MEDIA",
      "note": "ADAPTAR para o handle real do Diego (ex: DIEGO SPANEVELLO | IA). Mantido genérico nas referências originais.",
      "font_family": "sans-serif regular",
      "font_size": "13px",
      "font_color": "rgba(255,255,255,0.55)",
      "letter_spacing": "2px",
      "text_transform": "uppercase",
      "avatar": "nenhum — apenas texto, sem foto de perfil"
    },
    "content": {
      "position": "abaixo do header",
      "margin_lateral": "56px",
      "margin_top": "28px",
      "blocks": [
        {
          "id": "headline",
          "type": "text",
          "content": "Manchete curta do slide aqui",
          "font_family": "serif display (ex: Fraunces, Playfair Display)",
          "font_size": "40px",
          "font_style": "regular, com uma palavra ou trecho em itálico para ênfase",
          "font_color": "#FFFFFF",
          "line_height": "1.05",
          "margin_bottom": "24px",
          "note": "headline curta, máximo 2 linhas, ênfase por itálico — nunca por cor"
        }
      ]
    },
    "image": {
      "position": "abaixo da headline",
      "height": "42% do frame",
      "margin_lateral": "56px",
      "margin_top": "0px",
      "margin_bottom": "24px",
      "border_radius": "16px",
      "full_bleed": false,
      "asset_prompt": "PLACEHOLDER — preencher via json-prompt-generator no momento da geração real do slide. Não baked-in no template.",
      "note": "imagem editorial, foto documental ou still — nunca ilustração cartoon"
    },
    "body": {
      "position": "abaixo da imagem",
      "margin_lateral": "56px",
      "blocks": [
        {
          "id": "texto-apoio",
          "type": "text",
          "content": "Texto complementar explicando o contexto da imagem ou reforçando a headline.",
          "font_family": "sans-serif regular",
          "font_size": "24px",
          "font_color": "rgba(255,255,255,0.7)",
          "line_height": "1.4"
        }
      ]
    },
    "footer": {
      "height": "50px",
      "position": "bottom",
      "margin_lateral": "56px",
      "margin_bottom": "36px",
      "left": {
        "content": "logomark + wordmark BLANK",
        "note": "símbolo minimalista à esquerda do texto BLANK, estilo assinatura de marca",
        "font_size": "13px",
        "font_color": "rgba(255,255,255,0.6)",
        "letter_spacing": "3px",
        "text_transform": "uppercase"
      },
      "right": {
        "content": null,
        "note": "vazio nos slides internos"
      }
    }
  },
  "markings_available": {
    "italic_emphasis": {
      "usage": "palavra ou trecho de destaque dentro da headline serif"
    },
    "color_swap": {
      "accent_color": "#E8722A",
      "usage": "uso pontual, quando o itálico não for suficiente para o destaque"
    }
  },
  "negative_rules": [
    "sem travessao",
    "sem avatar no header",
    "header sempre so texto, uppercase, tracking largo",
    "footer sempre com logomark + wordmark BLANK",
    "asset_prompt de imagem nunca baked-in no template — sempre placeholder, preenchido na geracao real",
    "maximo 1 ideia central por slide",
    "imagem sempre com border_radius, nunca sem",
    "headline sempre serif display, nunca sans-serif bold"
  ]
}
```

---

## GRUPO 2 — Imagem lateral (esquerda) + Texto (direita), 2 colunas

```json
{
  "template": "carrossel-blank-style",
  "version": "grupo-2-split-imagem-texto",
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "background_color": "#0D0D0D"
  },
  "zones": {
    "header": {
      "height": "70px",
      "position": "top",
      "margin_lateral": "56px",
      "margin_top": "40px",
      "content": "CSM — SOCIAL MEDIA",
      "note": "ADAPTAR para o handle real do Diego (ex: DIEGO SPANEVELLO | IA). Mantido genérico nas referências originais.",
      "font_family": "sans-serif regular",
      "font_size": "13px",
      "font_color": "rgba(255,255,255,0.55)",
      "letter_spacing": "2px",
      "text_transform": "uppercase",
      "avatar": "nenhum — apenas texto, sem foto de perfil"
    },
    "content": {
      "layout": "split-2-colunas",
      "position": "abaixo do header, ocupa o corpo principal do frame",
      "margin_top": "32px",
      "note": "desvio do schema padrão header/image/content/footer — aqui a imagem fica ANINHADA dentro da coluna esquerda do content, não como zona irmã separada, porque a estrutura é split lado a lado",
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
              "font_color": "#FFFFFF",
              "line_height": "1.1",
              "margin_bottom": "16px"
            },
            {
              "id": "texto-apoio",
              "type": "text",
              "content": "Texto complementar, explicação ou citação relacionada à imagem ao lado.",
              "font_family": "sans-serif regular",
              "font_size": "20px",
              "font_color": "rgba(255,255,255,0.7)",
              "line_height": "1.4"
            }
          ]
        }
      ]
    },
    "footer": {
      "height": "50px",
      "position": "bottom",
      "margin_lateral": "56px",
      "margin_bottom": "36px",
      "left": {
        "content": "logomark + wordmark BLANK",
        "note": "símbolo minimalista à esquerda do texto BLANK, estilo assinatura de marca",
        "font_size": "13px",
        "font_color": "rgba(255,255,255,0.6)",
        "letter_spacing": "3px",
        "text_transform": "uppercase"
      },
      "right": {
        "content": null,
        "note": "vazio nos slides internos"
      }
    }
  },
  "markings_available": {
    "italic_emphasis": {
      "usage": "palavra ou trecho de destaque dentro da headline serif"
    },
    "color_swap": {
      "accent_color": "#E8722A",
      "usage": "uso pontual, quando o itálico não for suficiente para o destaque"
    }
  },
  "negative_rules": [
    "sem travessao",
    "sem avatar no header",
    "header sempre so texto, uppercase, tracking largo",
    "footer sempre com logomark + wordmark BLANK",
    "asset_prompt de imagem nunca baked-in no template — sempre placeholder, preenchido na geracao real",
    "maximo 1 ideia central por slide",
    "imagem sempre com border_radius, nunca sem",
    "headline sempre serif display, nunca sans-serif bold",
    "coluna de texto nunca mais larga que 60% do frame — imagem precisa manter peso visual"
  ]
}
```

---

## GRUPO 3 — Texto puro (sem imagem)

```json
{
  "template": "carrossel-blank-style",
  "version": "grupo-3-texto-puro",
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "background_color": "#0D0D0D"
  },
  "zones": {
    "header": {
      "height": "70px",
      "position": "top",
      "margin_lateral": "56px",
      "margin_top": "40px",
      "content": "CSM — SOCIAL MEDIA",
      "note": "ADAPTAR para o handle real do Diego (ex: DIEGO SPANEVELLO | IA). Mantido genérico nas referências originais.",
      "font_family": "sans-serif regular",
      "font_size": "13px",
      "font_color": "rgba(255,255,255,0.55)",
      "letter_spacing": "2px",
      "text_transform": "uppercase",
      "avatar": "nenhum — apenas texto, sem foto de perfil"
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
          "font_color": "#FFFFFF",
          "line_height": "1.1",
          "margin_bottom": "20px"
        },
        {
          "id": "body",
          "type": "text",
          "content": "Texto complementar mais leve, explicando ou aprofundando a ideia central.",
          "font_family": "sans-serif regular",
          "font_size": "22px",
          "font_color": "rgba(255,255,255,0.65)",
          "line_height": "1.5"
        }
      ]
    },
    "image": {
      "exists": false,
      "note": "GRUPO 3 não tem zona de imagem — slide 100% tipográfico"
    },
    "footer": {
      "height": "50px",
      "position": "bottom",
      "margin_lateral": "56px",
      "margin_bottom": "36px",
      "left": {
        "content": "logomark + wordmark BLANK",
        "note": "símbolo minimalista à esquerda do texto BLANK, estilo assinatura de marca",
        "font_size": "13px",
        "font_color": "rgba(255,255,255,0.6)",
        "letter_spacing": "3px",
        "text_transform": "uppercase"
      },
      "right": {
        "content": null,
        "note": "vazio nos slides internos"
      }
    }
  },
  "markings_available": {
    "italic_emphasis": {
      "usage": "palavra ou trecho de destaque dentro da headline serif"
    },
    "color_swap": {
      "accent_color": "#E8722A",
      "usage": "pré-headline sempre em laranja; uso pontual na headline se necessário"
    },
    "underline": {
      "color": "#E8722A",
      "thickness": "3px",
      "usage": "reforço em frase de apoio dentro do body, quando necessário"
    }
  },
  "negative_rules": [
    "sem travessao",
    "sem avatar no header",
    "header sempre so texto, uppercase, tracking largo",
    "footer sempre com logomark + wordmark BLANK",
    "maximo 1 ideia central por slide",
    "headline sempre serif display, nunca sans-serif bold",
    "nunca forcar uma imagem so pra preencher espaco — grupo 3 e deliberadamente so tipografia",
    "respiro generoso: nunca lotar o frame de texto, priorizar espaco negativo"
  ]
}
```
