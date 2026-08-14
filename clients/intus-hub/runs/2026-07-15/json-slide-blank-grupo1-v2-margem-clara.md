# Blank-style — Grupo 1 (v2) — margem de texto travada na margem da imagem + versão clara

> Correção sobre a v1 do Grupo 1: a v1 tinha `margin_lateral: 56px` repetido em cada bloco separadamente, sem trava explícita de que a LARGURA do texto deve ser idêntica à LARGURA da imagem. Isso deixava margem pra divergência na hora de gerar. Nesta v2, adicionei o campo `layout_grid` no topo do schema, que define a margem lateral global UMA VEZ e todas as zonas herdam dela — headline, corpo de texto e imagem compartilham exatamente a mesma largura útil, ponta a ponta.
> Também já aplicado: fundo off-white, header "Diego Spanevello | Inteligência Artificial", footer "INTUS HUB" sem logomark — mesmo padrão fechado no Grupo 2.

```json
{
  "template": "carrossel-blank-style",
  "version": "grupo-1-headline-imagem-texto-clara-v2",
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "background_color": "#F7F5F1"
  },
  "layout_grid": {
    "margem_lateral_global": "56px",
    "note": "REGRA ESTRUTURAL: todas as zonas do slide (header, headline, imagem, corpo de texto, footer) usam a MESMA margem lateral de 56px dos dois lados do frame. A largura útil do texto (headline e corpo) deve ser IDÊNTICA à largura da imagem — nunca mais estreita. Isso é herdado, não redefinido zona por zona."
  },
  "zones": {
    "header": {
      "height": "50px",
      "position": "top",
      "margin_lateral": "herda de layout_grid.margem_lateral_global (56px)",
      "margin_top": "40px",
      "blocks": [
        {
          "id": "handle",
          "content": "Diego Spanevello",
          "font_family": "sans-serif",
          "font_weight": 700,
          "font_size": "13px",
          "font_color": "#1A1A1A",
          "letter_spacing": "1.5px",
          "text_transform": "uppercase"
        },
        {
          "id": "categoria",
          "content": "| Inteligência Artificial",
          "font_family": "sans-serif",
          "font_weight": 600,
          "font_size": "13px",
          "font_color": "rgba(26,26,26,0.5)",
          "letter_spacing": "1.5px",
          "text_transform": "uppercase"
        }
      ],
      "avatar": "nenhum — apenas texto, sem foto de perfil",
      "note": "handle + categoria na mesma linha, separados por pipe, tracking largo em uppercase — mesmo padrão da referência"
    },
    "content": {
      "position": "abaixo do header",
      "margin_lateral": "herda de layout_grid.margem_lateral_global (56px)",
      "margin_top": "36px",
      "width": "igual a largura util da imagem — mesma margem lateral dos dois lados",
      "blocks": [
        {
          "id": "headline",
          "type": "text",
          "content": "Manchete curta do slide aqui, pode quebrar em 2 linhas",
          "font_family": "serif display (ex: Fraunces, Playfair Display)",
          "font_size": "44px",
          "font_style": "regular, com uma palavra ou trecho em itálico para ênfase",
          "font_color": "#1A1A1A",
          "line_height": "1.08",
          "margin_bottom": "32px",
          "note": "headline ocupa a largura total do grid — quebra de linha natural, nao forcada por caixa mais estreita"
        }
      ]
    },
    "image": {
      "position": "abaixo da headline",
      "height": "38% do frame",
      "margin_lateral": "herda de layout_grid.margem_lateral_global (56px)",
      "margin_top": "0px",
      "margin_bottom": "32px",
      "border_radius": "20px",
      "full_bleed": false,
      "asset_prompt": "PLACEHOLDER — preencher via json-prompt-generator no momento da geração real do slide. Não baked-in no template.",
      "note": "imagem editorial, foto documental ou still — nunca ilustração cartoon. Largura da imagem = largura do grid, referencia de alinhamento pra headline e corpo"
    },
    "body": {
      "position": "abaixo da imagem",
      "margin_lateral": "herda de layout_grid.margem_lateral_global (56px)",
      "width": "igual a largura da imagem — MESMA margem lateral dos dois lados, texto vai ate a mesma borda direita/esquerda da imagem",
      "blocks": [
        {
          "id": "texto-apoio",
          "type": "text",
          "content": "Texto complementar explicando o contexto da imagem ou reforçando a headline, ocupando a largura total disponivel ate a borda da imagem.",
          "font_family": "sans-serif regular",
          "font_size": "24px",
          "font_color": "rgba(26,26,26,0.7)",
          "line_height": "1.45"
        }
      ]
    },
    "footer": {
      "height": "40px",
      "position": "bottom",
      "margin_lateral": "herda de layout_grid.margem_lateral_global (56px)",
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
    "sem logomark no footer — apenas texto INTUS HUB",
    "asset_prompt de imagem nunca baked-in no template — sempre placeholder, preenchido na geracao real",
    "maximo 1 ideia central por slide",
    "imagem sempre com border_radius, nunca sem",
    "headline sempre serif display, nunca sans-serif bold",
    "fundo sempre off-white, nunca branco puro (#FFFFFF)",
    "texto (headline e corpo) deve ocupar EXATAMENTE a mesma largura da imagem — mesma margem lateral nos dois lados, nunca mais estreito que a imagem",
    "margem lateral definida uma unica vez em layout_grid e herdada por todas as zonas — nunca redefinir margem diferente zona a zona"
  ]
}
```
