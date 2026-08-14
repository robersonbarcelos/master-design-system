# JSONs de Capa — "Você conhece o Pato?" — 3 variações de fonte + imagem

Template base: `capa-ilustrada-mascote` (derivado das referências "Blank": full bleed, header sem avatar, headline no terço inferior, sem footer).
Análise de imagem feita via skill `json-prompt-generator` (scene/style/materials/composition/quality), integrada em `zones.image.asset_prompt`.

---

## Variação A — Anton (headline) + Big Shoulders Text (header) — Ganso de smoking

```json
{
  "template": "capa-ilustrada-mascote",
  "version": "pato-v3-A",
  "combinacao_fonte": {
    "headline_font": "Anton",
    "header_font": "Big Shoulders Text",
    "referencia_headline": "Bryson",
    "referencia_header": "Highfat"
  },
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "orientation": "portrait — SLIDE SEMPRE 4:5 PORTRAIT. NUNCA ALTERAR.",
    "platform": "Instagram Feed / Carrossel Capa",
    "dpi": 72,
    "color_mode": "RGB"
  },
  "zones": {
    "header": {
      "height": "auto",
      "position": "top",
      "margin_lateral": "28px",
      "margin_top": "28px",
      "avatar": {
        "exists": false,
        "note": "SEM AVATAR — regra explícita do cliente, não usar foto de perfil nem placeholder circular."
      },
      "text_block": {
        "content": "Diego Spanevello | Inteligência Artificial",
        "font_family": "Big Shoulders Text",
        "font_weight": 900,
        "font_size": "16px",
        "text_transform": "uppercase",
        "letter_spacing": "0.3px",
        "layout": "linha única, separador pipe",
        "color_nome": "#FFFFFF",
        "color_categoria": "rgba(255,255,255,0.45)",
        "note": "PROIBIDO travessão (—). Separador travado em pipe ( | )."
      }
    },
    "image": {
      "position": "full frame — full bleed",
      "margin_lateral": "0px",
      "border_radius": "0px",
      "note": "EXCEÇÃO às regras padrão dos outros templates do Diego (que proíbem full bleed) — aqui é intencional, seguindo a referência 'Blank' original.",
      "asset_prompt": {
        "scene": {
          "description": "Retrato semi-realista pintado de um ganso branco antropomorfizado, vestindo smoking preto completo com camisa branca e gravata borboleta preta, segurando com a asa/mão enluvada de branco uma xícara de chá de cerâmica clara da qual sobe um fio de vapor visível. O bico é laranja vivo, o olho é escuro e expressivo, em pose de três quartos voltada para a direita. Fundo verde-oliva/marrom-esverdeado fosco, com silhuetas escuras de talos de capim/trigo seco emergindo nas bordas inferiores, sugerindo um campo ao entardecer. Paleta quente e contida: verde-oliva, marrom, branco da plumagem, preto do smoking, laranja do bico.",
          "subject": "Ganso branco antropomorfizado em traje de gala (smoking + gravata borboleta), segurando xícara de chá com vapor",
          "setting": "Campo aberto estilizado ao entardecer, fundo verde-oliva fosco com silhuetas de vegetação seca",
          "action": "Estático, pose de retrato editorial, segurando a xícara em gesto elegante e contido"
        },
        "style": {
          "primary": "ilustração pintada digital semi-realista, retrato editorial com humor sutil (anthropomorphic portrait)",
          "rendering_quality": "detalhado, pincelada visível controlada, sem textura fotográfica de câmera",
          "surface_textures": "penas com transição suave de luz e sombra, tecido do smoking com leve textura de lã, porcelana lisa da xícara com reflexo suave",
          "lighting": "luz difusa quente, direção frontal-lateral suave, sem sombras duras, contraste moderado"
        },
        "materials": {
          "fabric": "smoking preto em lã fina com leve textura, camisa branca lisa, gravata borboleta em cetim fosco",
          "surfaces": "penugem branca com variação sutil de tom, bico laranja com acabamento semi-brilhante, xícara de cerâmica fosca clara"
        },
        "environment": {
          "atmosphere": "névoa leve de vapor subindo da xícara, ar parado, sem partículas no fundo",
          "time": "entardecer estilizado, luz quente e baixa"
        },
        "composition": {
          "perspective": "plano médio, três quartos, olhar do ganso levemente fora de eixo em relação à câmera",
          "framing": "sujeito centralizado horizontalmente, levemente deslocado para a esquerda para abrir espaço à direita",
          "subject_placement": "cabeça e torso ocupando o terço superior a médio do frame, deixando o terço inferior mais neutro para sobreposição da headline",
          "safe_area": "zona seguz de 992x1262px dentro do frame 1080x1350px — nenhum elemento crítico da ilustração deve tocar as bordas, já que a headline e o header serão sobrepostos digitalmente",
          "note": "NÃO incluir moldura/borda de quadro (photo frame) — usar apenas a cena, sem o efeito de moldura decorativa que aparecia na imagem de referência original"
        },
        "quality": {
          "include": ["ilustração pintada", "antropomorfismo elegante", "paleta quente contida", "textura de pincel controlada", "expressão sutil e nobre", "vapor visível e legível", "acabamento editorial"],
          "avoid": ["moldura ou borda de quadro decorativa", "textura fotográfica realista de estúdio", "fundo genérico branco", "expressão cômica exagerada", "textura plástica ou 3D render", "excesso de ruído/grão"],
          "reference_standard": "ilustração editorial pintada estilo capa de revista satírica clássica, tom Wes Anderson meets classic pet-portrait painting"
        }
      }
    },
    "content": {
      "position": "terço inferior do frame, sobreposto à imagem",
      "margin_lateral": "28px",
      "margin_bottom": "40px",
      "overlay": {
        "type": "gradiente escuro",
        "direction": "de baixo para cima",
        "stops": [
          {"position": "0%", "color": "rgba(0,0,0,0.78)"},
          {"position": "55%", "color": "rgba(0,0,0,0.35)"},
          {"position": "100%", "color": "rgba(0,0,0,0)"}
        ],
        "note": "overlay obrigatório apenas atrás da headline, para garantir legibilidade do texto branco sobre a ilustração"
      },
      "blocks": [
        {
          "id": "headline",
          "type": "text",
          "content": "VOCÊ CONHECE O PATO?",
          "font_family": "Anton",
          "font_size": "48px",
          "text_transform": "uppercase",
          "line_height": 0.95,
          "font_color": "#FFFFFF",
          "accent_word": "PATO",
          "accent_color": "#E8722A",
          "note": "quebra de linha sugerida: 'VOCÊ CONHECE / O PATO?'"
        }
      ]
    },
    "footer": {
      "exists": false,
      "note": "sem footer — confirmado que a referência 'Blank' original não tem footer"
    }
  },
  "negative_rules": [
    "NUNCA usar travessão no header",
    "NUNCA adicionar avatar",
    "NUNCA remover o overlay atrás da headline (perde legibilidade)",
    "NUNCA usar a headline fora do terço inferior",
    "NUNCA incluir moldura decorativa na imagem",
    "NUNCA adicionar footer"
  ]
}
```

---

## Variação B — Archivo Black (headline) + Big Shoulders Display (header) — Pato de terno amarelo

```json
{
  "template": "capa-ilustrada-mascote",
  "version": "pato-v3-B",
  "combinacao_fonte": {
    "headline_font": "Archivo Black",
    "header_font": "Big Shoulders Display",
    "referencia_headline": "Exulta",
    "referencia_header": "At Slam Grotesk"
  },
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "orientation": "portrait — SLIDE SEMPRE 4:5 PORTRAIT. NUNCA ALTERAR.",
    "platform": "Instagram Feed / Carrossel Capa",
    "dpi": 72,
    "color_mode": "RGB"
  },
  "zones": {
    "header": {
      "height": "auto",
      "position": "top",
      "margin_lateral": "28px",
      "margin_top": "28px",
      "avatar": {
        "exists": false,
        "note": "SEM AVATAR — regra explícita do cliente."
      },
      "text_block": {
        "content": "Diego Spanevello | Inteligência Artificial",
        "font_family": "Big Shoulders Display",
        "font_weight": 900,
        "font_size": "17px",
        "text_transform": "uppercase",
        "letter_spacing": "0.3px",
        "layout": "linha única, separador pipe",
        "color_nome": "#FFFFFF",
        "color_categoria": "rgba(255,255,255,0.45)",
        "note": "PROIBIDO travessão (—). Separador travado em pipe ( | )."
      }
    },
    "image": {
      "position": "full frame — full bleed",
      "margin_lateral": "0px",
      "border_radius": "0px",
      "note": "EXCEÇÃO às regras padrão — full bleed intencional, seguindo referência 'Blank'.",
      "asset_prompt": {
        "scene": {
          "description": "Retrato frontal hiper-realista em render 3D de um pato/ganso antropomorfizado usando chapéu fedora amarelo mostarda combinando com um terno amarelo texturizado (leve efeito bolinha/quilted em relevo), camisa xadrez branca e cinza por baixo, gravata borboleta bordô estampada. Fundo amarelo mostarda sólido salpicado de partículas brancas brilhantes soltas no ar, como neve ou glitter, criando um efeito festivo e lúdico. Iluminação uniforme tipo estúdio, cores saturadas e contrastantes — amarelo dominante com bordô como contraponto.",
          "subject": "Pato/ganso antropomorfizado em terno amarelo completo com chapéu e gravata borboleta bordô",
          "setting": "Fundo de estúdio amarelo mostarda sólido com partículas brancas suspensas",
          "action": "Estático, pose frontal quase direta, expressão neutra e elegante"
        },
        "style": {
          "primary": "render 3D fotorrealista, still de moda editorial lúdica, CGI de alta definição",
          "rendering_quality": "hiper-realista, texturas de tecido e pena em alta definição",
          "surface_textures": "tecido do terno com relevo de bolinhas/quilted, algodão xadrez da camisa, cetim estampado da gravata, penugem fina e definida no rosto",
          "lighting": "luz de estúdio uniforme e frontal, sombras suaves e controladas, sem contraluz dramático"
        },
        "materials": {
          "fabric": "lã texturizada amarela com relevo de bolinhas no terno, algodão xadrez branco/cinza na camisa, cetim estampado bordô na gravata",
          "surfaces": "bico alaranjado com acabamento semi-fosco, penugem branca/cinza com textura individual visível, partículas brancas com leve brilho especular"
        },
        "environment": {
          "atmosphere": "partículas brancas suspensas no ar (tipo neve/glitter), sem névoa ou profundidade atmosférica",
          "time": "não aplicável — fundo de estúdio"
        },
        "composition": {
          "perspective": "frontal, câmera na altura dos olhos, leve enquadramento de busto",
          "framing": "sujeito centralizado horizontalmente, cabeça e chapéu próximos ao topo do frame",
          "subject_placement": "ocupa o terço superior a médio do frame, deixando o terço inferior mais neutro (fundo amarelo com partículas) para a headline",
          "safe_area": "zona segura de 992x1262px dentro do frame 1080x1350px — elementos do figurino não devem tocar as bordas"
        },
        "quality": {
          "include": ["render 3D hiper-realista", "paleta amarelo/bordô vibrante", "textura de tecido em alta definição", "acabamento festivo e lúdico", "iluminação de estúdio limpa", "partículas suspensas com profundidade"],
          "avoid": ["fundo genérico liso sem partículas", "textura plástica/borracha nas penas", "iluminação plana sem volume", "expressão de personagem infantil exagerada", "ruído excessivo nas partículas"],
          "reference_standard": "campanha de moda editorial lúdica estilo Pinterest/CGI character design, acabamento tipo render Blender/Octane comercial"
        }
      }
    },
    "content": {
      "position": "terço inferior do frame, sobreposto à imagem",
      "margin_lateral": "28px",
      "margin_bottom": "40px",
      "overlay": {
        "type": "gradiente escuro",
        "direction": "de baixo para cima",
        "stops": [
          {"position": "0%", "color": "rgba(0,0,0,0.78)"},
          {"position": "55%", "color": "rgba(0,0,0,0.35)"},
          {"position": "100%", "color": "rgba(0,0,0,0)"}
        ],
        "note": "overlay obrigatório — o fundo amarelo claro exige ainda mais contraste para o texto branco não se perder"
      },
      "blocks": [
        {
          "id": "headline",
          "type": "text",
          "content": "VOCÊ CONHECE O PATO?",
          "font_family": "Archivo Black",
          "font_size": "42px",
          "text_transform": "uppercase",
          "line_height": 0.95,
          "font_color": "#FFFFFF",
          "accent_word": "PATO",
          "accent_color": "#E8722A",
          "note": "quebra de linha sugerida: 'VOCÊ CONHECE / O PATO?'"
        }
      ]
    },
    "footer": {
      "exists": false,
      "note": "sem footer"
    }
  },
  "negative_rules": [
    "NUNCA usar travessão no header",
    "NUNCA adicionar avatar",
    "NUNCA remover o overlay atrás da headline",
    "NUNCA usar a headline fora do terço inferior",
    "NUNCA adicionar footer"
  ]
}
```

---

## Variação C — Hanken Grotesk (headline) + Hanken Grotesk (header) — Pato minimalista flat

```json
{
  "template": "capa-ilustrada-mascote",
  "version": "pato-v3-C",
  "combinacao_fonte": {
    "headline_font": "Hanken Grotesk",
    "header_font": "Hanken Grotesk",
    "referencia_headline": "Rebork",
    "referencia_header": "Rebork"
  },
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "orientation": "portrait — SLIDE SEMPRE 4:5 PORTRAIT. NUNCA ALTERAR.",
    "platform": "Instagram Feed / Carrossel Capa",
    "dpi": 72,
    "color_mode": "RGB"
  },
  "zones": {
    "header": {
      "height": "auto",
      "position": "top",
      "margin_lateral": "28px",
      "margin_top": "28px",
      "avatar": {
        "exists": false,
        "note": "SEM AVATAR — regra explícita do cliente."
      },
      "text_block": {
        "content": "Diego Spanevello | Inteligência Artificial",
        "font_family": "Hanken Grotesk",
        "font_weight": 800,
        "font_size": "15px",
        "text_transform": "none",
        "letter_spacing": "0.2px",
        "layout": "linha única, separador pipe",
        "color_nome": "#1A1A1A",
        "color_categoria": "rgba(26,26,26,0.5)",
        "note": "PROIBIDO travessão (—). Separador travado em pipe ( | ). Cor do texto ESCURA nesta variação porque o fundo da imagem é claro (verde-menta) — ajustar contraste, ver nota em image."
      }
    },
    "image": {
      "position": "full frame — full bleed",
      "margin_lateral": "0px",
      "border_radius": "0px",
      "note": "EXCEÇÃO às regras padrão — full bleed intencional, seguindo referência 'Blank'.",
      "asset_prompt": {
        "scene": {
          "description": "Ilustração vetorial flat minimalista de um pato branco simples, contorno preto grosso e uniforme, patas e cauda em laranja sólido, bico amarelo pequeno, olho representado por um único ponto preto. O pato está em pose de caminhada lateral, visto de perfil, com uma sombra suave elíptica cinza abaixo dele. Fundo verde-menta sólido e chapado, sem gradiente, sem textura, sem elementos adicionais — composição extremamente minimalista com muito espaço negativo ao redor do personagem, que ocupa uma pequena porção do frame, levemente à direita do centro, na metade inferior.",
          "subject": "Pato branco em ilustração flat vetorial, contorno preto grosso, patas e cauda laranja",
          "setting": "Fundo sólido verde-menta, sem cenário, estilo sticker/ícone",
          "action": "Caminhando, pose lateral estática de perfil"
        },
        "style": {
          "primary": "ilustração vetorial flat, estilo sticker/mascote minimalista",
          "rendering_quality": "vetor limpo, sem textura, sem gradiente, sem sombra complexa",
          "surface_textures": "preenchimento de cor 100% chapado, sem ruído nem textura de nenhum tipo",
          "lighting": "não aplicável — ilustração flat sem simulação de luz, apenas sombra de contato simples"
        },
        "materials": {
          "surfaces": "todas as superfícies em preenchimento sólido de cor única, sem reflexo nem brilho, contorno vetorial uniforme de espessura constante"
        },
        "environment": {
          "atmosphere": "não aplicável — fundo sólido sem atmosfera"
        },
        "composition": {
          "perspective": "vista lateral (perfil), 2D puro, sem profundidade",
          "framing": "muito espaço negativo — personagem pequeno dentro do frame, não centralizado, deslocado para a direita e para baixo",
          "subject_placement": "metade inferior do frame, ocupando aproximadamente 15-20% da altura total, deixando o restante do frame como fundo verde-menta vazio",
          "safe_area": "zona segura de 992x1262px dentro do frame 1080x1350px",
          "note": "ESTE fundo é CLARO (verde-menta), diferente das outras 2 variações que têm fundo escuro/saturado — headline e header precisam de tratamento de cor específico para contraste (ver overlay e cores de texto abaixo)"
        },
        "quality": {
          "include": ["vetor flat limpo", "contorno preto uniforme", "paleta minimalista de 4 cores (branco, preto, laranja, amarelo)", "espaço negativo generoso", "estilo sticker/ícone", "silhueta simples e reconhecível"],
          "avoid": ["textura ou gradiente no preenchimento", "sombra complexa ou 3D", "excesso de detalhe realista", "linhas de contorno variáveis em espessura", "fundo com padrão ou textura"],
          "reference_standard": "estilo sticker minimalista tipo emoji/ícone flat design, próximo de ilustrações do estilo 'Blush' ou 'Humaaans' simplificado"
        }
      }
    },
    "content": {
      "position": "terço inferior do frame, sobreposto à imagem",
      "margin_lateral": "28px",
      "margin_bottom": "40px",
      "overlay": {
        "type": "bloco sólido claro (não gradiente escuro)",
        "color": "rgba(255,255,255,0.85)",
        "border_radius": "0px",
        "note": "ATENÇÃO — esta variação tem fundo CLARO (verde-menta), então o padrão de overlay escuro das outras 2 variações NÃO se aplica aqui. Usar bloco branco semi-opaco atrás da headline escura para manter legibilidade e consistência de marca."
      },
      "blocks": [
        {
          "id": "headline",
          "type": "text",
          "content": "VOCÊ CONHECE O PATO?",
          "font_family": "Hanken Grotesk",
          "font_weight": 800,
          "font_size": "40px",
          "text_transform": "none",
          "line_height": 1.0,
          "font_color": "#1A1A1A",
          "accent_word": "PATO",
          "accent_color": "#E8722A",
          "note": "cor de texto ESCURA (#1A1A1A) nesta variação — inverso das outras 2, por causa do fundo claro"
        }
      ]
    },
    "footer": {
      "exists": false,
      "note": "sem footer"
    }
  },
  "negative_rules": [
    "NUNCA usar travessão no header",
    "NUNCA adicionar avatar",
    "NUNCA usar overlay escuro nesta variação — fundo é claro, usar bloco claro",
    "NUNCA usar a headline fora do terço inferior",
    "NUNCA adicionar footer",
    "NUNCA adicionar textura ou gradiente na imagem — deve permanecer 100% flat"
  ]
}
```

---

## Correção pós-teste visual — Variação C tinha 2 problemas

Ao renderizar a Variação C, ficou visível que: (1) o bloco sólido claro atrás do headline era desnecessário e destoava do estilo flat/minimalista, já que o fundo mint já tem contraste suficiente com texto escuro sozinho; (2) o header (`Diego Spanevello | Inteligência Artificial`) ficou pequeno demais em `15px` num frame de 1080px.

Abaixo, 2 variações de correção — mesma imagem/fonte (Hanken Grotesk, ref: Rebork), tratamentos diferentes de overlay:

---

## Variação C1 — Hanken Grotesk + Hanken Grotesk — SEM overlay, header maior

```json
{
  "template": "capa-ilustrada-mascote",
  "version": "pato-v3-C1",
  "combinacao_fonte": {
    "headline_font": "Hanken Grotesk",
    "header_font": "Hanken Grotesk",
    "referencia_headline": "Rebork",
    "referencia_header": "Rebork"
  },
  "ajuste_aplicado": "Remoção total do overlay/bloco atrás do headline (o fundo mint sólido já tem contraste suficiente com texto #1A1A1A) + aumento do header de 15px para 22px para dar presença de assinatura no topo.",
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "orientation": "portrait — SLIDE SEMPRE 4:5 PORTRAIT. NUNCA ALTERAR.",
    "platform": "Instagram Feed / Carrossel Capa",
    "dpi": 72,
    "color_mode": "RGB"
  },
  "zones": {
    "header": {
      "height": "auto",
      "position": "top",
      "margin_lateral": "28px",
      "margin_top": "28px",
      "avatar": {
        "exists": false,
        "note": "SEM AVATAR — regra explícita do cliente."
      },
      "text_block": {
        "content": "Diego Spanevello | Inteligência Artificial",
        "font_family": "Hanken Grotesk",
        "font_weight": 800,
        "font_size": "22px",
        "text_transform": "none",
        "letter_spacing": "0.2px",
        "layout": "linha única, separador pipe",
        "color_nome": "#1A1A1A",
        "color_categoria": "rgba(26,26,26,0.5)",
        "note": "PROIBIDO travessão (—). Separador pipe. Tamanho aumentado de 15px→22px — 15px estava fraco demais como assinatura de topo num frame 1080px de largura."
      }
    },
    "image": {
      "position": "full frame — full bleed",
      "margin_lateral": "0px",
      "border_radius": "0px",
      "note": "EXCEÇÃO às regras padrão — full bleed intencional, seguindo referência 'Blank'.",
      "asset_prompt": {
        "scene": {
          "description": "Ilustração vetorial flat minimalista de um pato branco simples, contorno preto grosso e uniforme, patas e cauda em laranja sólido, bico amarelo pequeno, olho representado por um único ponto preto. O pato está em pose de caminhada lateral, visto de perfil, com uma sombra suave elíptica cinza abaixo dele. Fundo verde-menta sólido e chapado, sem gradiente, sem textura, sem elementos adicionais — composição extremamente minimalista com muito espaço negativo ao redor do personagem, que ocupa uma pequena porção do frame, levemente à direita do centro, na metade inferior.",
          "subject": "Pato branco em ilustração flat vetorial, contorno preto grosso, patas e cauda laranja",
          "setting": "Fundo sólido verde-menta, sem cenário, estilo sticker/ícone",
          "action": "Caminhando, pose lateral estática de perfil"
        },
        "style": {
          "primary": "ilustração vetorial flat, estilo sticker/mascote minimalista",
          "rendering_quality": "vetor limpo, sem textura, sem gradiente, sem sombra complexa",
          "surface_textures": "preenchimento de cor 100% chapado, sem ruído nem textura de nenhum tipo",
          "lighting": "não aplicável — ilustração flat sem simulação de luz, apenas sombra de contato simples"
        },
        "materials": {
          "surfaces": "todas as superfícies em preenchimento sólido de cor única, sem reflexo nem brilho, contorno vetorial uniforme de espessura constante"
        },
        "environment": {
          "atmosphere": "não aplicável — fundo sólido sem atmosfera"
        },
        "composition": {
          "perspective": "vista lateral (perfil), 2D puro, sem profundidade",
          "framing": "muito espaço negativo — personagem pequeno dentro do frame, não centralizado, deslocado para a direita e para baixo",
          "subject_placement": "metade inferior do frame, ocupando aproximadamente 15-20% da altura total, deixando o restante do frame como fundo verde-menta vazio",
          "safe_area": "zona segura de 992x1262px dentro do frame 1080x1350px",
          "note": "fundo CLARO (verde-menta) — texto direto sobre o fundo, sem necessidade de overlay pois é cor sólida chapada sem variação tonal"
        },
        "quality": {
          "include": ["vetor flat limpo", "contorno preto uniforme", "paleta minimalista de 4 cores (branco, preto, laranja, amarelo)", "espaço negativo generoso", "estilo sticker/ícone", "silhueta simples e reconhecível"],
          "avoid": ["textura ou gradiente no preenchimento", "sombra complexa ou 3D", "excesso de detalhe realista", "linhas de contorno variáveis em espessura", "fundo com padrão ou textura"],
          "reference_standard": "estilo sticker minimalista tipo emoji/ícone flat design, próximo de ilustrações do estilo 'Blush' ou 'Humaaans' simplificado"
        }
      }
    },
    "content": {
      "position": "terço inferior do frame, sobreposto à imagem",
      "margin_lateral": "28px",
      "margin_bottom": "40px",
      "overlay": {
        "exists": false,
        "note": "REMOVIDO — o fundo mint é cor sólida chapada, sem variação tonal, então texto #1A1A1A direto já tem contraste suficiente (WCAG AA). Bloco branco anterior era redundante e quebrava a estética flat/minimalista da peça."
      },
      "blocks": [
        {
          "id": "headline",
          "type": "text",
          "content": "VOCÊ CONHECE O PATO?",
          "font_family": "Hanken Grotesk",
          "font_weight": 800,
          "font_size": "40px",
          "text_transform": "none",
          "line_height": 1.0,
          "font_color": "#1A1A1A",
          "accent_word": "PATO",
          "accent_color": "#E8722A",
          "note": "cor de texto ESCURA (#1A1A1A) — sem caixa/bloco atrás, direto sobre o fundo mint"
        }
      ]
    },
    "footer": {
      "exists": false,
      "note": "sem footer"
    }
  },
  "negative_rules": [
    "NUNCA usar travessão no header",
    "NUNCA adicionar avatar",
    "NUNCA adicionar bloco/overlay atrás do headline nesta variação — fundo sólido já tem contraste suficiente",
    "NUNCA usar a headline fora do terço inferior",
    "NUNCA adicionar footer",
    "NUNCA adicionar textura ou gradiente na imagem — deve permanecer 100% flat",
    "NUNCA usar header abaixo de 20px neste formato — fica fraco como assinatura"
  ]
}
```

---

## Variação C2 — Hanken Grotesk + Hanken Grotesk — highlight leve só atrás do texto, header maior

```json
{
  "template": "capa-ilustrada-mascote",
  "version": "pato-v3-C2",
  "combinacao_fonte": {
    "headline_font": "Hanken Grotesk",
    "header_font": "Hanken Grotesk",
    "referencia_headline": "Rebork",
    "referencia_header": "Rebork"
  },
  "ajuste_aplicado": "Em vez de remover o overlay totalmente (como na C1), troca o bloco retangular full-width por um highlight sutil, com padding curto e cantos arredondados, encostado só no texto — mantém uma leve separação visual do fundo sem parecer um 'cartão colado'. Header também aumentado de 15px para 22px.",
  "format": {
    "aspect_ratio": "4:5",
    "resolution": "1080x1350px",
    "orientation": "portrait — SLIDE SEMPRE 4:5 PORTRAIT. NUNCA ALTERAR.",
    "platform": "Instagram Feed / Carrossel Capa",
    "dpi": 72,
    "color_mode": "RGB"
  },
  "zones": {
    "header": {
      "height": "auto",
      "position": "top",
      "margin_lateral": "28px",
      "margin_top": "28px",
      "avatar": {
        "exists": false,
        "note": "SEM AVATAR — regra explícita do cliente."
      },
      "text_block": {
        "content": "Diego Spanevello | Inteligência Artificial",
        "font_family": "Hanken Grotesk",
        "font_weight": 800,
        "font_size": "22px",
        "text_transform": "none",
        "letter_spacing": "0.2px",
        "layout": "linha única, separador pipe",
        "color_nome": "#1A1A1A",
        "color_categoria": "rgba(26,26,26,0.5)",
        "note": "PROIBIDO travessão (—). Separador pipe. Tamanho aumentado de 15px→22px."
      }
    },
    "image": {
      "position": "full frame — full bleed",
      "margin_lateral": "0px",
      "border_radius": "0px",
      "note": "EXCEÇÃO às regras padrão — full bleed intencional, seguindo referência 'Blank'.",
      "asset_prompt": {
        "scene": {
          "description": "Ilustração vetorial flat minimalista de um pato branco simples, contorno preto grosso e uniforme, patas e cauda em laranja sólido, bico amarelo pequeno, olho representado por um único ponto preto. O pato está em pose de caminhada lateral, visto de perfil, com uma sombra suave elíptica cinza abaixo dele. Fundo verde-menta sólido e chapado, sem gradiente, sem textura, sem elementos adicionais — composição extremamente minimalista com muito espaço negativo ao redor do personagem, que ocupa uma pequena porção do frame, levemente à direita do centro, na metade inferior.",
          "subject": "Pato branco em ilustração flat vetorial, contorno preto grosso, patas e cauda laranja",
          "setting": "Fundo sólido verde-menta, sem cenário, estilo sticker/ícone",
          "action": "Caminhando, pose lateral estática de perfil"
        },
        "style": {
          "primary": "ilustração vetorial flat, estilo sticker/mascote minimalista",
          "rendering_quality": "vetor limpo, sem textura, sem gradiente, sem sombra complexa",
          "surface_textures": "preenchimento de cor 100% chapado, sem ruído nem textura de nenhum tipo",
          "lighting": "não aplicável — ilustração flat sem simulação de luz, apenas sombra de contato simples"
        },
        "materials": {
          "surfaces": "todas as superfícies em preenchimento sólido de cor única, sem reflexo nem brilho, contorno vetorial uniforme de espessura constante"
        },
        "environment": {
          "atmosphere": "não aplicável — fundo sólido sem atmosfera"
        },
        "composition": {
          "perspective": "vista lateral (perfil), 2D puro, sem profundidade",
          "framing": "muito espaço negativo — personagem pequeno dentro do frame, não centralizado, deslocado para a direita e para baixo",
          "subject_placement": "metade inferior do frame, ocupando aproximadamente 15-20% da altura total, deixando o restante do frame como fundo verde-menta vazio",
          "safe_area": "zona segura de 992x1262px dentro do frame 1080x1350px",
          "note": "fundo CLARO (verde-menta) — highlight sutil atrás do texto, não um bloco full-width"
        },
        "quality": {
          "include": ["vetor flat limpo", "contorno preto uniforme", "paleta minimalista de 4 cores (branco, preto, laranja, amarelo)", "espaço negativo generoso", "estilo sticker/ícone", "silhueta simples e reconhecível"],
          "avoid": ["textura ou gradiente no preenchimento", "sombra complexa ou 3D", "excesso de detalhe realista", "linhas de contorno variáveis em espessura", "fundo com padrão ou textura"],
          "reference_standard": "estilo sticker minimalista tipo emoji/ícone flat design, próximo de ilustrações do estilo 'Blush' ou 'Humaaans' simplificado"
        }
      }
    },
    "content": {
      "position": "terço inferior do frame, sobreposto à imagem",
      "margin_lateral": "28px",
      "margin_bottom": "40px",
      "overlay": {
        "type": "highlight sutil, ajustado ao texto (não bloco full-width)",
        "color": "rgba(255,255,255,0.55)",
        "padding": "6px 10px",
        "border_radius": "6px",
        "scope": "aplicado individualmente atrás de cada linha do headline, largura ajustada ao texto — NÃO é uma faixa/retângulo esticado pela largura toda do frame",
        "note": "Mantém uma leve separação do fundo (reforça legibilidade em variações de luz da tela do usuário) sem criar o efeito 'cartão colado' do bloco full-width anterior."
      },
      "blocks": [
        {
          "id": "headline",
          "type": "text",
          "content": "VOCÊ CONHECE O PATO?",
          "font_family": "Hanken Grotesk",
          "font_weight": 800,
          "font_size": "40px",
          "text_transform": "none",
          "line_height": 1.0,
          "font_color": "#1A1A1A",
          "accent_word": "PATO",
          "accent_color": "#E8722A",
          "note": "cor de texto ESCURA (#1A1A1A), com highlight sutil individual atrás de cada linha (ver content.overlay)"
        }
      ]
    },
    "footer": {
      "exists": false,
      "note": "sem footer"
    }
  },
  "negative_rules": [
    "NUNCA usar travessão no header",
    "NUNCA adicionar avatar",
    "NUNCA esticar o highlight como bloco full-width — deve ser ajustado ao texto, com padding curto",
    "NUNCA usar a headline fora do terço inferior",
    "NUNCA adicionar footer",
    "NUNCA adicionar textura ou gradiente na imagem — deve permanecer 100% flat",
    "NUNCA usar header abaixo de 20px neste formato"
  ]
}
```
