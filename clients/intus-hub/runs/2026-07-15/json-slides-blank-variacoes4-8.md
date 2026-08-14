# Blank-style — Novas variações estruturais (baseadas nas referências de futebol)

> Padrão fixo aprovado aplicado em todas: fundo off-white `#F7F5F1`, header `@diego.spanevello | Inteligência Artificial`, footer `INTUS HUB` (sem logomark), sem linha/traço divisório entre blocos, margem lateral única herdada via `layout_grid`, `asset_prompt` em PLACEHOLDER.

---

## VARIAÇÃO 1 — Headline → Imagem full-width → Corpo (peso misto: negrito + regular)

```json
{
  "template": "carrossel-blank-style",
  "version": "variacao-1-headline-imagem-corpo-peso-misto",
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "background_color": "#F7F5F1"
  },
  "layout_grid": {
    "margem_lateral_global": "56px",
    "note": "headline, imagem e corpo compartilham a mesma largura util — mesma margem lateral nos dois lados"
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
      "note": "handle + categoria na mesma linha, separados por pipe — padrão aprovado"
    },
    "content": {
      "position": "abaixo do header",
      "margin_lateral": "56px",
      "margin_top": "28px",
      "blocks": [
        {
          "id": "headline",
          "type": "text",
          "content": "Para a alegria de todos nós, o Brasil acabou de conquistar mais uma vitória e estamos um passo mais perto do tão sonhado hexa.",
          "font_family": "serif display (ex: Fraunces, Playfair Display)",
          "font_size": "32px",
          "font_style": "regular, com trechos em itálico para ênfase (ex: 'conquistar mais uma vitória', 'sonhado hexa')",
          "font_color": "#1A1A1A",
          "line_height": "1.15",
          "margin_bottom": "28px",
          "note": "headline mais longa, 3-4 linhas, funciona quase como um parágrafo de abertura — mais de uma palavra em itálico ao longo do texto"
        }
      ]
    },
    "image": {
      "position": "abaixo da headline",
      "height": "36% do frame",
      "margin_lateral": "56px",
      "margin_top": "0px",
      "margin_bottom": "32px",
      "border_radius": "12px",
      "full_bleed": false,
      "asset_prompt": "PLACEHOLDER — preencher via json-prompt-generator no momento da geração real do slide.",
      "note": "foto documental/editorial — nunca ilustração cartoon"
    },
    "body": {
      "position": "abaixo da imagem",
      "margin_lateral": "56px",
      "blocks": [
        {
          "id": "paragrafo-1-negrito",
          "type": "text",
          "content": "Há quem diga que os tempos de glória do Brasil no futebol já se foram, assim como há gente que acredita e torce até o último segundo.",
          "font_family": "sans-serif",
          "font_weight": 700,
          "font_size": "22px",
          "font_color": "#1A1A1A",
          "line_height": "1.4",
          "margin_bottom": "20px"
        },
        {
          "id": "paragrafo-2-regular",
          "type": "text",
          "content": "Mas uma coisa todos nós podemos concordar: a chegada do Ancelotti, um dos melhores técnicos do mundo, trouxe muitas expectativas.",
          "font_family": "sans-serif regular",
          "font_size": "22px",
          "font_color": "rgba(26,26,26,0.6)",
          "line_height": "1.4"
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
    "italic_emphasis": { "usage": "trechos de destaque dentro da headline serif — pode ocorrer mais de uma vez na mesma headline" },
    "bold_paragraph": { "usage": "primeiro parágrafo do corpo em negrito (peso mais forte que o segundo), cria hierarquia dentro do próprio bloco de texto" }
  },
  "negative_rules": [
    "sem travessao",
    "sem linha ou traco decorativo separando blocos de texto",
    "sem avatar no header",
    "sem logomark no footer — apenas texto INTUS HUB",
    "asset_prompt de imagem nunca baked-in no template — sempre placeholder",
    "texto (headline e corpo) deve ocupar a mesma largura da imagem — mesma margem lateral",
    "imagem sempre com border_radius, nunca sem",
    "fundo sempre off-white, nunca branco puro (#FFFFFF)"
  ]
}
```

---

## VARIAÇÃO 2 — Imagem full-width no topo → Texto serifado longo → Interjeição em negrito → Corpo

```json
{
  "template": "carrossel-blank-style",
  "version": "variacao-2-imagem-topo-texto-interjeicao",
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "background_color": "#F7F5F1"
  },
  "layout_grid": {
    "margem_lateral_global": "56px",
    "note": "imagem e todos os blocos de texto compartilham a mesma largura util"
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
      "note": "handle + categoria na mesma linha, separados por pipe — padrão aprovado"
    },
    "image": {
      "position": "logo abaixo do header, topo do frame",
      "height": "36% do frame",
      "margin_lateral": "56px",
      "margin_top": "28px",
      "margin_bottom": "28px",
      "border_radius": "12px",
      "full_bleed": false,
      "asset_prompt": "PLACEHOLDER — preencher via json-prompt-generator no momento da geração real do slide.",
      "note": "foto documental/editorial, primeiro elemento visual do slide, antes de qualquer texto"
    },
    "content": {
      "position": "abaixo da imagem",
      "margin_lateral": "56px",
      "blocks": [
        {
          "id": "texto-serif-longo",
          "type": "text",
          "content": "O futebol tem mostrado cada vez mais uma tentativa de ter o maior controle possível, seja na hora de ver o impedimento no VAR ou na estratégia em campo.",
          "font_family": "serif display",
          "font_size": "30px",
          "font_style": "regular, com um trecho em itálico para ênfase",
          "font_color": "#1A1A1A",
          "line_height": "1.2",
          "margin_bottom": "32px",
          "note": "funciona como uma 'headline estendida' — tamanho grande mas estrutura de paragrafo corrido, nao frase curta"
        },
        {
          "id": "interjeicao-negrito",
          "type": "text",
          "content": "Só que existe um problema.",
          "font_family": "sans-serif",
          "font_weight": 700,
          "font_size": "22px",
          "font_color": "#1A1A1A",
          "margin_bottom": "20px",
          "note": "frase curta isolada, funciona como uma virada/gancho dentro do corpo — sempre sozinha, sem mais texto na mesma linha"
        },
        {
          "id": "corpo-regular",
          "type": "text",
          "content": "Copa do Mundo nunca foi um ambiente controlável, porque jogos decisivos inevitavelmente escapam do plano original.",
          "font_family": "sans-serif regular",
          "font_size": "22px",
          "font_color": "rgba(26,26,26,0.6)",
          "line_height": "1.4"
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
    "italic_emphasis": { "usage": "trecho de destaque dentro do texto serifado" },
    "bold_interjection": { "usage": "frase curta e isolada em negrito, funcionando como virada/gancho no meio do corpo" }
  },
  "negative_rules": [
    "sem travessao",
    "sem linha ou traco decorativo separando blocos de texto",
    "sem avatar no header",
    "sem logomark no footer — apenas texto INTUS HUB",
    "asset_prompt de imagem nunca baked-in no template — sempre placeholder",
    "texto deve ocupar a mesma largura da imagem — mesma margem lateral",
    "imagem sempre com border_radius, nunca sem",
    "fundo sempre off-white, nunca branco puro (#FFFFFF)",
    "interjeicao em negrito deve ficar sempre isolada — nunca colada em outro paragrafo"
  ]
}
```

---

## VARIAÇÃO 3 — Split invertido: Texto (esquerda) + Imagem (direita)

```json
{
  "template": "carrossel-blank-style",
  "version": "variacao-3-split-texto-imagem-invertido",
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
      "note": "handle + categoria na mesma linha, separados por pipe — padrão aprovado"
    },
    "content": {
      "layout": "split-2-colunas-invertido",
      "position": "abaixo do header, ocupa o corpo principal do frame",
      "margin_top": "32px",
      "note": "inverso do Grupo 2 aprovado — aqui o TEXTO fica na coluna esquerda e a IMAGEM na coluna direita",
      "columns": [
        {
          "id": "coluna-texto",
          "width": "55%",
          "position": "esquerda",
          "margin_lateral_externa": "56px",
          "margin_lateral_interna": "24px",
          "blocks": [
            {
              "id": "headline",
              "type": "text",
              "content": "Essa familiaridade aparece nos vídeos.",
              "font_family": "serif display",
              "font_size": "32px",
              "font_style": "regular",
              "font_color": "#1A1A1A",
              "line_height": "1.1",
              "margin_bottom": "20px"
            },
            {
              "id": "paragrafo-1",
              "type": "text",
              "content": "Céline não precisa entrevistar Haaland sobre a temporada ou perguntar a Mbappé como ele se sente antes de uma partida.",
              "font_family": "sans-serif regular",
              "font_size": "18px",
              "font_color": "rgba(26,26,26,0.65)",
              "line_height": "1.4",
              "margin_bottom": "18px"
            },
            {
              "id": "paragrafo-2",
              "type": "text",
              "content": "Ela pode colocar uma bola no chão e pedir que eles acertem um alvo, disputem um teste de reflexo ou tentem reconhecer outro jogador.",
              "font_family": "sans-serif regular",
              "font_size": "18px",
              "font_color": "rgba(26,26,26,0.65)",
              "line_height": "1.4",
              "margin_bottom": "18px"
            },
            {
              "id": "paragrafo-3-sublinhado",
              "type": "text-marked",
              "content": "A proposta é simples, mas resolve um problema importante: jogadores treinados para repetir respostas institucionais voltam a reagir de forma espontânea.",
              "font_family": "sans-serif regular",
              "font_size": "18px",
              "font_color": "#1A1A1A",
              "line_height": "1.4",
              "marking": { "type": "underline", "color": "#E8722A", "thickness": "2px" },
              "note": "paragrafo de fechamento com underline laranja — reforco visual do ponto principal"
            }
          ]
        },
        {
          "id": "coluna-imagem",
          "width": "45%",
          "position": "direita",
          "margin_lateral_externa": "56px",
          "image": {
            "height": "auto, proporcional ao conteudo da coluna de texto ao lado",
            "border_radius": "16px",
            "full_bleed": false,
            "asset_prompt": "PLACEHOLDER — preencher via json-prompt-generator no momento da geração real do slide.",
            "note": "foto retrato/still, alinhada ao topo da coluna de texto"
          }
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
    "underline": { "color": "#E8722A", "thickness": "2px", "usage": "paragrafo de fechamento/conclusao dentro da coluna de texto" }
  },
  "negative_rules": [
    "sem travessao",
    "sem linha ou traco decorativo separando blocos de texto",
    "sem avatar no header",
    "sem logomark no footer — apenas texto INTUS HUB",
    "asset_prompt de imagem nunca baked-in no template — sempre placeholder",
    "imagem sempre com border_radius, nunca sem",
    "coluna de imagem nunca mais larga que 45% do frame",
    "fundo sempre off-white, nunca branco puro (#FFFFFF)"
  ]
}
```

---

## VARIAÇÃO 4 — Headline + Corpo no topo → Imagem full-width no rodapé

```json
{
  "template": "carrossel-blank-style",
  "version": "variacao-4-headline-texto-imagem-rodape",
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "background_color": "#F7F5F1"
  },
  "layout_grid": {
    "margem_lateral_global": "56px",
    "note": "headline, corpo e imagem compartilham a mesma largura util"
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
      "note": "handle + categoria na mesma linha, separados por pipe — padrão aprovado"
    },
    "content": {
      "position": "abaixo do header",
      "margin_lateral": "56px",
      "margin_top": "32px",
      "blocks": [
        {
          "id": "headline",
          "type": "text",
          "content": "Talvez seja por isso que uma garota belga, gravada quase sempre pelo próprio namorado, tenha conseguido superar canais com centenas de funcionários.",
          "font_family": "serif display",
          "font_size": "30px",
          "font_style": "regular",
          "font_color": "#1A1A1A",
          "line_height": "1.18",
          "margin_bottom": "24px",
          "note": "headline mais longa, funciona quase como abertura de paragrafo — sem itálico neste exemplo especifico, mas o campo continua disponivel"
        },
        {
          "id": "paragrafo-1",
          "type": "text",
          "content": "Ela escolheu um assunto que conhecia desde antes de trabalhar com conteúdo, encontrou uma forma simples de apresentá-lo ao mundo e passou anos acumulando acesso.",
          "font_family": "sans-serif regular",
          "font_size": "20px",
          "font_color": "rgba(26,26,26,0.65)",
          "line_height": "1.45",
          "margin_bottom": "18px"
        },
        {
          "id": "paragrafo-2-com-negrito-inline",
          "type": "text",
          "content": "Quando a Copa colocou os mesmos jogadores diante de bilhões de pessoas, {{Céline já estava ao lado deles.}}",
          "font_family": "sans-serif regular",
          "font_size": "20px",
          "font_color": "rgba(26,26,26,0.65)",
          "line_height": "1.45",
          "margin_bottom": "28px",
          "note": "trecho entre {{ }} deve renderizar em negrito (#1A1A1A, font_weight 700) dentro da mesma frase — negrito inline, nao paragrafo separado"
        }
      ]
    },
    "image": {
      "position": "rodape do frame, abaixo de todo o texto",
      "height": "34% do frame",
      "margin_lateral": "56px",
      "margin_bottom": "80px",
      "border_radius": "12px",
      "full_bleed": false,
      "asset_prompt": "PLACEHOLDER — preencher via json-prompt-generator no momento da geração real do slide.",
      "note": "foto documental/editorial, ultimo elemento visual antes do footer, com respiro generoso antes do footer"
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
    "bold_inline": { "usage": "trecho de fechamento em negrito dentro do ultimo paragrafo, antes da imagem" },
    "italic_emphasis": { "usage": "opcional na headline, quando fizer sentido" }
  },
  "negative_rules": [
    "sem travessao",
    "sem linha ou traco decorativo separando blocos de texto",
    "sem avatar no header",
    "sem logomark no footer — apenas texto INTUS HUB",
    "asset_prompt de imagem nunca baked-in no template — sempre placeholder",
    "texto e imagem compartilham a mesma largura util — mesma margem lateral",
    "imagem sempre com border_radius, nunca sem",
    "fundo sempre off-white, nunca branco puro (#FFFFFF)",
    "respiro generoso entre a imagem e o footer — imagem nunca colada no rodape"
  ]
}
```

---

## VARIAÇÃO 5 — Texto puro, headline + 3 parágrafos (regular / negrito / regular)

```json
{
  "template": "carrossel-blank-style",
  "version": "variacao-5-texto-puro-multi-paragrafo",
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
      "note": "handle + categoria na mesma linha, separados por pipe — padrão aprovado"
    },
    "content": {
      "position": "no terço superior/central do frame — NAO centralizado verticalmente igual ao Grupo 3, comeca logo apos respiro do header",
      "margin_lateral": "56px",
      "margin_top": "120px",
      "blocks": [
        {
          "id": "headline",
          "type": "text",
          "content": "Com o tempo, o acesso começou a produzir mais acesso.",
          "font_family": "serif display",
          "font_size": "36px",
          "font_style": "regular",
          "font_color": "#1A1A1A",
          "line_height": "1.12",
          "margin_bottom": "28px"
        },
        {
          "id": "paragrafo-1-regular",
          "type": "text",
          "content": "Um vídeo com um grande jogador aumentava a audiência. A audiência tornava o próximo convite mais interessante para outro clube. E cada nova colaboração reforçava a posição de Céline dentro daquele ambiente.",
          "font_family": "sans-serif regular",
          "font_size": "20px",
          "font_color": "rgba(26,26,26,0.6)",
          "line_height": "1.45",
          "margin_bottom": "20px"
        },
        {
          "id": "paragrafo-2-negrito",
          "type": "text",
          "content": "Em algum momento, ela deixou de ser apenas uma fã tentando se aproximar dos jogadores.",
          "font_family": "sans-serif",
          "font_weight": 700,
          "font_size": "20px",
          "font_color": "#1A1A1A",
          "line_height": "1.45",
          "margin_bottom": "20px"
        },
        {
          "id": "paragrafo-3-regular",
          "type": "text",
          "content": "Virou uma das poucas pessoas capazes de oferecer a eles contato direto com dezenas de milhões de torcedores.",
          "font_family": "sans-serif regular",
          "font_size": "20px",
          "font_color": "rgba(26,26,26,0.6)",
          "line_height": "1.45"
        }
      ]
    },
    "image": { "exists": false, "note": "slide 100% tipográfico" },
    "footer": {
      "height": "40px",
      "position": "bottom",
      "margin_lateral": "56px",
      "margin_bottom": "36px",
      "content": "INTUS HUB",
      "note": "somente texto — sem logomark/ícone. Respiro grande entre o ultimo paragrafo e o footer, propositalmente vazio",
      "font_family": "sans-serif regular",
      "font_size": "13px",
      "font_color": "rgba(26,26,26,0.5)",
      "letter_spacing": "3px",
      "text_transform": "uppercase",
      "position_horizontal": "esquerda"
    }
  },
  "markings_available": {
    "bold_paragraph": { "usage": "um dos parágrafos do meio em negrito, criando um 'pico' de enfase dentro do bloco de texto corrido" }
  },
  "negative_rules": [
    "sem travessao",
    "sem linha ou traco decorativo separando blocos de texto",
    "sem avatar no header",
    "sem logomark no footer — apenas texto INTUS HUB",
    "headline sempre serif display, nunca sans-serif bold",
    "nunca forcar uma imagem so pra preencher espaco",
    "respiro generoso e deliberado — o vazio antes do footer faz parte do design, nao e erro",
    "fundo sempre off-white, nunca branco puro (#FFFFFF)"
  ]
}
```
