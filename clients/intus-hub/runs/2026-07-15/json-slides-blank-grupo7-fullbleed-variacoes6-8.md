# Blank-style — Grupo novo: Full-bleed / texto sobreposto ou painel sólido (Variações 6-8)

> Estas 3 referências pertencem a um grupo estruturalmente diferente dos Grupos 1-3 e das Variações 1-5: aqui a imagem ocupa o frame inteiro (full-bleed), e o texto fica em branco, sobreposto direto na foto (com overlay de gradiente localizado) OU hospedado num painel sólido escuro que sucede a imagem.
>
> **Desvio importante identificado nas 3 referências**: nenhuma delas mostra header (@handle) nem footer (INTUS HUB) visíveis. Isso quebra o padrão fixo aprovado nos grupos anteriores (que sempre tinham header+footer). Marquei os campos como `"exists": false` com nota, fiel à referência — mas fica pendente de confirmação: isso é proposital (slides de "impacto"/meio de carrossel, onde o header já apareceu na capa e não precisa repetir) ou devo reativar o header/footer padrão mesmo aqui?
>
> Esta leva também resolve, na prática, a pergunta em aberto sobre o "Grupo 7 full-bleed": sim, ele mantém overlay/painel escuro por exceção documentada — nunca o fundo off-white padrão, porque o fundo aqui É a foto.

---

## VARIAÇÃO 6 — Full-bleed, texto sobreposto alinhado à esquerda

```json
{
  "template": "carrossel-blank-style",
  "version": "variacao-6-fullbleed-texto-sobreposto-esquerda",
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "background_color": "coberto integralmente pela imagem full-bleed — nenhuma cor de fundo visivel"
  },
  "zones": {
    "header": {
      "exists": false,
      "note": "DESVIO do padrao — nesta referencia nao ha header visivel (sem handle, sem categoria). Confirmar se e proposital (slide de impacto no meio do carrossel) ou se deve reativar o header padrao @diego.spanevello | Inteligencia Artificial"
    },
    "image": {
      "position": "full-bleed, ocupa 100% do frame",
      "height": "100%",
      "width": "100%",
      "full_bleed": true,
      "border_radius": "24px",
      "border_radius_note": "aplicado ao card inteiro (as 4 pontas), nao a imagem isolada — imagem e frame sao a mesma coisa aqui",
      "asset_prompt": "PLACEHOLDER — preencher via json-prompt-generator no momento da geração real do slide. Não baked-in no template.",
      "overlay": {
        "type": "gradiente escuro parcial, apenas atras das zonas de texto",
        "zonas_aplicadas": ["atras da headline (terco superior)", "atras do corpo de texto (terco inferior)"],
        "color": "rgba(0,0,0,0.25) a rgba(0,0,0,0.55), mais forte perto do texto",
        "note": "imagem NUNCA escurecida por inteiro — overlay so nas areas onde o texto se sobrepoe, pra manter legibilidade sem perder a foto"
      },
      "note": "foto documental/editorial de jogo — cores naturais preservadas fora das zonas de overlay"
    },
    "content": {
      "position": "sobreposto a imagem, terco superior do frame",
      "margin_lateral": "56px",
      "margin_top": "180px",
      "blocks": [
        {
          "id": "headline",
          "type": "text",
          "content": "Mas a grande verdade é que o Brasil trabalha melhor em jogos mais acirrados.",
          "font_family": "serif display",
          "font_size": "34px",
          "font_style": "regular, com trecho final em itálico para ênfase (ex: 'jogos mais acirrados')",
          "font_color": "#FFFFFF",
          "line_height": "1.15",
          "text_align": "esquerda",
          "note": "texto branco sobreposto direto na foto — depende do overlay atras para legibilidade"
        }
      ]
    },
    "body": {
      "position": "sobreposto a imagem, terco inferior do frame",
      "margin_lateral": "56px",
      "margin_bottom": "80px",
      "blocks": [
        {
          "id": "paragrafo-1-negrito",
          "type": "text",
          "content": "Pode ser pura teimosia brasileira ou estratégia do Mister, mas, quando o jogo fica imprevisível e acelerado, a Seleção cresce.",
          "font_family": "sans-serif",
          "font_weight": 700,
          "font_size": "22px",
          "font_color": "#FFFFFF",
          "line_height": "1.4",
          "margin_bottom": "20px"
        },
        {
          "id": "paragrafo-2-regular",
          "type": "text",
          "content": "E podemos finalmente ver em campo o elenco perigoso que pode nos levar ao hexa.",
          "font_family": "sans-serif regular",
          "font_size": "22px",
          "font_color": "rgba(255,255,255,0.85)",
          "line_height": "1.4"
        }
      ]
    },
    "footer": {
      "exists": false,
      "note": "DESVIO do padrao — sem footer visivel na referencia. Confirmar se deve reativar INTUS HUB texto no rodape"
    }
  },
  "markings_available": {
    "italic_emphasis": { "usage": "trecho final da headline, dentro da mesma frase" },
    "bold_paragraph": { "usage": "primeiro paragrafo do corpo em negrito, segundo em regular — mesma logica de hierarquia dos outros grupos" }
  },
  "negative_rules": [
    "sem travessao",
    "sem linha ou traco decorativo separando blocos de texto",
    "overlay aplicado somente atras do texto, nunca na imagem inteira",
    "asset_prompt de imagem nunca baked-in no template — sempre placeholder",
    "texto sempre branco quando sobreposto a foto — nunca #1A1A1A nessas variacoes full-bleed",
    "imagem sempre full-bleed nesta variacao — sem margem lateral pra propria foto"
  ]
}
```

---

## VARIAÇÃO 7 — Full-bleed, headline centralizada + corpo único embaixo

```json
{
  "template": "carrossel-blank-style",
  "version": "variacao-7-fullbleed-headline-centralizada",
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "background_color": "coberto integralmente pela imagem full-bleed — nenhuma cor de fundo visivel"
  },
  "zones": {
    "header": {
      "exists": false,
      "note": "DESVIO do padrao — sem header visivel na referencia."
    },
    "image": {
      "position": "full-bleed, ocupa 100% do frame",
      "height": "100%",
      "width": "100%",
      "full_bleed": true,
      "border_radius": "24px",
      "border_radius_note": "aplicado ao card inteiro (as 4 pontas)",
      "asset_prompt": "PLACEHOLDER — preencher via json-prompt-generator no momento da geração real do slide. Não baked-in no template.",
      "overlay": {
        "type": "gradiente escuro parcial, apenas atras das zonas de texto",
        "zonas_aplicadas": ["atras da headline (terco superior)", "atras do paragrafo (terco inferior)"],
        "color": "rgba(0,0,0,0.2) a rgba(0,0,0,0.5)",
        "note": "mais sutil que a variacao 6, pois o fundo natural da foto (ceu/arquibancada desfocada) ja tem contraste suficiente em boa parte da area"
      },
      "note": "foto documental/editorial, plano fechado em jogador comemorando"
    },
    "content": {
      "position": "sobreposto a imagem, terco superior do frame",
      "margin_lateral": "72px",
      "margin_top": "140px",
      "blocks": [
        {
          "id": "headline",
          "type": "text",
          "content": "No fim, o jogo de hoje mostrou, para além do resultado, o choque entre dois modelos de performance: um baseado em previsibilidade e outro em adaptação.",
          "font_family": "serif display",
          "font_size": "28px",
          "font_style": "regular, com a clausula final apos os dois-pontos em itálico para ênfase",
          "font_color": "#FFFFFF",
          "line_height": "1.25",
          "text_align": "centro",
          "note": "unica variacao do grupo com headline centralizada — margem lateral maior (72px) pra compensar a centralizacao e evitar linhas muito longas"
        }
      ]
    },
    "body": {
      "position": "sobreposto a imagem, terco inferior do frame",
      "margin_lateral": "56px",
      "margin_bottom": "90px",
      "blocks": [
        {
          "id": "paragrafo-unico",
          "type": "text",
          "content": "E talvez o futebol moderno esteja descobrindo que o controle absoluto funciona... até o cenário mudar.",
          "font_family": "sans-serif regular",
          "font_size": "20px",
          "font_color": "rgba(255,255,255,0.85)",
          "line_height": "1.4",
          "text_align": "esquerda",
          "note": "unico paragrafo do corpo — sem par negrito/regular aqui, headline ja carrega o peso conceitual do slide"
        }
      ]
    },
    "footer": {
      "exists": false,
      "note": "DESVIO do padrao — sem footer visivel na referencia."
    }
  },
  "markings_available": {
    "italic_emphasis": { "usage": "clausula final da headline, apos os dois-pontos" }
  },
  "negative_rules": [
    "sem travessao",
    "sem linha ou traco decorativo separando blocos de texto",
    "overlay aplicado somente atras do texto, nunca na imagem inteira",
    "asset_prompt de imagem nunca baked-in no template — sempre placeholder",
    "texto sempre branco quando sobreposto a foto",
    "headline centralizada e excecao neste grupo — usar apenas quando a frase tiver simetria natural, nao forcar centralizacao em headlines assimetricas"
  ]
}
```

---

## VARIAÇÃO 8 — Imagem no topo (full-width) + painel sólido escuro embaixo

```json
{
  "template": "carrossel-blank-style",
  "version": "variacao-8-imagem-topo-painel-solido-escuro",
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "background_color": "#0D0D0D",
    "note": "excecao documentada ao fundo off-white padrao — usada apenas neste subgrupo full-bleed/painel, quando a imagem ocupa a parte superior e um painel solido escuro hospeda o texto embaixo"
  },
  "zones": {
    "header": {
      "exists": false,
      "note": "DESVIO do padrao — sem header visivel na referencia."
    },
    "image": {
      "position": "topo do frame, full-width",
      "height": "aprox. 58% do frame",
      "width": "100%",
      "margin_lateral": "0px",
      "margin_top": "0px",
      "full_bleed": true,
      "border_radius": "24px 24px 0px 0px",
      "border_radius_note": "arredondamento apenas nas pontas superiores do card — a imagem se funde direto no painel escuro abaixo, sem gap ou linha de transicao",
      "asset_prompt": "PLACEHOLDER — preencher via json-prompt-generator no momento da geração real do slide. Não baked-in no template.",
      "note": "foto documental/still, tratamento preto e branco ou dessaturado — sem overlay, a transicao pro painel solido resolve o contraste sozinha"
    },
    "content": {
      "position": "painel solido escuro, ocupa o restante do frame abaixo da imagem",
      "background_color": "#0D0D0D",
      "margin_lateral": "56px",
      "margin_top": "32px",
      "blocks": [
        {
          "id": "headline",
          "type": "text",
          "content": "Só que havia um limite difícil de ignorar.",
          "font_family": "serif display",
          "font_size": "32px",
          "font_style": "regular",
          "font_color": "#FFFFFF",
          "line_height": "1.1",
          "margin_bottom": "20px",
          "note": "headline curta e direta, funciona como uma virada dentro da narrativa do carrossel — sem itálico neste caso"
        },
        {
          "id": "paragrafo-1",
          "type": "text",
          "content": "O CEMI dependia da vida do casal, de um público muito jovem e de um mercado pequeno. Céline podia continuar crescendo, mas provavelmente continuaria sendo uma celebridade belga conhecida por crianças.",
          "font_family": "sans-serif regular",
          "font_size": "17px",
          "font_color": "rgba(255,255,255,0.75)",
          "line_height": "1.45",
          "margin_bottom": "16px"
        },
        {
          "id": "paragrafo-2",
          "type": "text",
          "content": "Em maio de 2023, ela abriu um canal solo e colocou o futebol no centro de tudo. Foi uma escolha arriscada porque significava se afastar do público que havia sustentado sua carreira até ali.",
          "font_family": "sans-serif regular",
          "font_size": "17px",
          "font_color": "rgba(255,255,255,0.75)",
          "line_height": "1.45",
          "margin_bottom": "16px"
        },
        {
          "id": "paragrafo-3-negrito",
          "type": "text",
          "content": "Quatro meses depois, ela já tinha 10 milhões de inscritos.",
          "font_family": "sans-serif",
          "font_weight": 700,
          "font_size": "17px",
          "font_color": "#FFFFFF",
          "line_height": "1.45",
          "note": "fechamento em negrito branco — dado de impacto, mesma logica dos 'picos de enfase' dos outros grupos"
        }
      ]
    },
    "footer": {
      "exists": false,
      "note": "DESVIO do padrao — sem footer visivel na referencia."
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
    "ultimo paragrafo do corpo sempre em negrito, funcionando como fechamento/dado de impacto"
  ]
}
```
