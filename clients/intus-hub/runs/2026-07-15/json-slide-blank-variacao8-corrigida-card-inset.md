# Variação 8 — corrigida (card inset com moldura off-white)

> Correção sobre a v1: a imagem + painel escuro agora formam um CARD inset dentro do frame, com margem de fundo off-white (#F7F5F1) visível nas 4 bordas — igual à referência original (foto sobre fundo branco, com borda clara dando contraste ao card escuro). Antes eu tinha feito o card ir até a borda do frame inteiro, o que estava errado.

```json
{
  "template": "carrossel-blank-style",
  "version": "variacao-8-imagem-topo-painel-solido-escuro-v2-card-inset",
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "background_color": "#F7F5F1"
  },
  "card_frame": {
    "outer_background": "#F7F5F1",
    "margin": "24px",
    "border_radius": "24px",
    "note": "CORRECAO aplicada: o card inteiro (imagem no topo + painel solido escuro embaixo) fica INSET dentro do frame, com margem de fundo off-white visivel nas 4 bordas — exatamente como a referencia original mostra (foto + painel preto formam um card unico, com moldura clara ao redor). NUNCA full-bleed ate a borda do frame inteiro."
  },
  "zones": {
    "header": {
      "exists": false,
      "note": "confirmado — subgrupo full-bleed/painel nao usa header, consistente com variacoes 6 e 7."
    },
    "image": {
      "position": "topo do card, full-width DENTRO do card (nao do frame)",
      "height": "aprox. 45% do card",
      "width": "100% do card",
      "margin_lateral": "0px",
      "margin_top": "0px",
      "border_radius": "herda de card_frame.border_radius nas pontas superiores (24px 24px 0px 0px)",
      "asset_prompt": "PLACEHOLDER — preencher via json-prompt-generator no momento da geração real do slide. Não baked-in no template.",
      "note": "foto documental/still, tratamento preto e branco ou dessaturado — sem overlay, a transicao pro painel solido resolve o contraste sozinha. Altura reduzida de 58% para 45% do CARD (nao do frame) porque agora o card em si ja e menor que o frame — ajuste pra manter a proporcao visual do painel de texto"
    },
    "content": {
      "position": "painel solido escuro, ocupa o restante do card abaixo da imagem",
      "background_color": "#0D0D0D",
      "margin_lateral": "32px",
      "margin_top": "28px",
      "blocks": [
        {
          "id": "headline",
          "type": "text",
          "content": "Só que havia um limite difícil de ignorar.",
          "font_family": "serif display",
          "font_size": "30px",
          "font_style": "regular",
          "font_color": "#FFFFFF",
          "line_height": "1.1",
          "margin_bottom": "18px",
          "note": "headline curta e direta, funciona como uma virada dentro da narrativa do carrossel — sem itálico neste caso"
        },
        {
          "id": "paragrafo-1",
          "type": "text",
          "content": "O CEMI dependia da vida do casal, de um público muito jovem e de um mercado pequeno. Céline podia continuar crescendo, mas provavelmente continuaria sendo uma celebridade belga conhecida por crianças.",
          "font_family": "sans-serif regular",
          "font_size": "16px",
          "font_color": "rgba(255,255,255,0.75)",
          "line_height": "1.45",
          "margin_bottom": "14px"
        },
        {
          "id": "paragrafo-2",
          "type": "text",
          "content": "Em maio de 2023, ela abriu um canal solo e colocou o futebol no centro de tudo. Foi uma escolha arriscada porque significava se afastar do público que havia sustentado sua carreira até ali.",
          "font_family": "sans-serif regular",
          "font_size": "16px",
          "font_color": "rgba(255,255,255,0.75)",
          "line_height": "1.45",
          "margin_bottom": "14px"
        },
        {
          "id": "paragrafo-3-negrito",
          "type": "text",
          "content": "Quatro meses depois, ela já tinha 10 milhões de inscritos.",
          "font_family": "sans-serif",
          "font_weight": 700,
          "font_size": "16px",
          "font_color": "#FFFFFF",
          "line_height": "1.45",
          "note": "fechamento em negrito branco — dado de impacto, mesma logica dos 'picos de enfase' dos outros grupos"
        }
      ]
    },
    "footer": {
      "exists": false,
      "note": "confirmado — subgrupo full-bleed/painel nao usa footer."
    }
  },
  "markings_available": {
    "bold_paragraph": { "usage": "ultimo paragrafo (dado de impacto/fechamento) sempre em negrito branco, funcionando como o clímax do bloco de texto" }
  },
  "negative_rules": [
    "sem travessao",
    "sem linha ou traco decorativo separando blocos de texto",
    "painel solido escuro e excecao documentada — so aparece neste subgrupo (imagem-topo + painel), nunca nos grupos off-white padrao",
    "imagem sempre sem overlay/gradiente nesta variacao especifica — contraste resolvido pelo painel solido, nao por gradiente sobre a foto",
    "asset_prompt de imagem nunca baked-in no template — sempre placeholder",
    "ultimo paragrafo do corpo sempre em negrito, funcionando como fechamento/dado de impacto",
    "card SEMPRE inset dentro de margem de fundo off-white (card_frame.margin) — NUNCA full-bleed ate a borda do frame inteiro",
    "fundo geral do frame sempre off-white #F7F5F1, visivel como moldura ao redor do card inteiro (imagem + painel escuro)",
    "sem header e sem footer neste subgrupo — consistente com variacoes 6 e 7"
  ]
}
```
