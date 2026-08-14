# JSONs de Capa — Repositório de Dados Financeiros para IA

Data: 2026-07-20
Template: TEMPLATE-SLIDE-TWITTER-POST
Regras aplicadas: zero travessão, zero cor no copy (só negrito), corpo 34px fixo, imagem sempre 16:9 landscape 1920x1080, nome de site externo nunca citado.

---

## GANCHO 1 — "Achei um repositório com 118 mil dados financeiros de graça pra treinar sua IA"
(ideias 1, 2, 3 — ver arquivo anterior no chat, replicar aqui se necessário)

---

## GANCHO 2 — "Isso substitui uma assinatura de R$100 mil/ano e é 100% grátis"

### Ideia 4 — Sátira de riqueza (estilo Tio Patinhas)

```json
{
  "template": "carrossel-twitter-post-style",
  "version": "clara",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "background_color": "#FFFFFF", "orientation": "portrait" },
  "zones": {
    "header": {
      "avatar": { "shape": "circle", "size": "64px", "note": "vazio — adicionar foto no Canva" },
      "text_block": {
        "line_1": { "content": "Diego Spanevello | Inteligência Artificial", "font_size": "26px", "font_style": "semibold sans-serif", "font_color": "#1A1A1A" },
        "line_2": { "content": "@diego.spanevello", "font_size": "22px", "font_style": "regular sans-serif", "font_color": "#888888" }
      },
      "verified_badge": { "type": "circle checkmark", "color": "#1D9BF0", "size": "20px" }
    },
    "content": {
      "copy": {
        "font_size": "34px",
        "font_style": "regular sans-serif",
        "font_color": "#1A1A1A",
        "line_height": "1.4",
        "bold_support": true,
        "text": "Isso substitui uma assinatura de **mais de R$100 mil por ano** e é 100% grátis"
      }
    },
    "image": {
      "slot_within_slide": { "width_px": 992, "height_px": 558, "aspect_ratio": "16:9" },
      "border_radius": "18px",
      "image_generation": {
        "format": { "dimensions": "1920x1080px", "aspect_ratio": "16:9", "orientation": "landscape" },
        "asset_prompt": {
          "scene": {
            "description": "Um executivo em terno escuro sentado em um escritório opulento e escuro, cercado por pilhas de moedas douradas e notas de dinheiro empilhadas ao fundo, com múltiplos monitores exibindo gráficos de trade (velas vermelhas e verdes) sobre a mesa. O ambiente mistura tons vermelho-vinho e dourado suntuoso com fundo geral escurecido para #111111, e um contorno laranja #E84000 emoldurando as telas de gráfico, criando ironia visual entre luxo excessivo e a gratuidade da ferramenta.",
            "subject": "Executivo de terno escuro, postura confiante à mesa, cercado por elementos de riqueza exagerada (moedas, notas, cofre ao fundo)",
            "setting": "Escritório de luxo escuro, cofre antigo ao fundo, pilha de moedas e notas, poltrona de couro vermelho, enquadramento horizontal amplo",
            "action": "Executivo operando os monitores de trade, cercado pelo cenário de riqueza"
          },
          "style": {
            "primary": "ilustração digital satírica hiper-detalhada, estilo editorial de exagero",
            "rendering_quality": "hyperrealistic",
            "surface_textures": "moedas com brilho metálico dourado, couro da poltrona com textura rica, madeira escura entalhada no cofre",
            "lighting": "luz quente dourada ambiente, contraluz laranja controlado saindo das telas de gráfico"
          },
          "technical": {
            "camera": { "focal_length": "28mm", "aperture": "f/4", "depth_of_field": "moderada, ambiente todo relativamente nítido para valorizar os detalhes de luxo", "angle": "levemente alto, três quartos" },
            "resolution": "ultra high definition",
            "rendering": "acabamento pictórico rico em detalhes, sem grão, saturação quente controlada"
          },
          "materials": {
            "surfaces": "ouro com reflexo especular realista, madeira escura entalhada, couro vermelho com brilho sutil"
          },
          "composition": {
            "perspective": "profundidade em camadas, executivo em primeiro plano, pilha de riqueza e cofre ao fundo",
            "framing": "regra dos terços horizontal",
            "subject_placement": "executivo centralizado levemente à esquerda, monitores de trade ocupando o terço direito",
            "safe_area": "nenhum elemento tocando as bordas do frame 1920x1080",
            "ui_elements": "nenhum texto embutido — headline fica na zona content do template"
          },
          "quality": {
            "include": ["exagero satírico controlado", "riqueza visual detalhada", "contraste entre luxo e gratuidade", "iluminação quente rica", "monitores de trade nítidos"],
            "avoid": ["excesso cartunesco raso", "textura de ouro plástica", "logo ou nome de site visível", "formato quadrado ou retrato", "poluição visual desorganizada"],
            "reference_standard": "Ilustração satírica editorial estilo caricatura de magnata financeiro, tom premium exagerado"
          }
        }
      }
    },
    "footer": { "exists": false }
  },
  "negative_rules": [
    "NUNCA travessão no copy",
    "NUNCA cor no corpo do texto — só negrito",
    "NUNCA fonte do corpo diferente de 34px",
    "NUNCA imagem quadrada ou retrato — slot 16:9 obrigatório",
    "avatar sempre vazio para Canva"
  ]
}
```

### Ideia 5 — Humanoide cabeça-tela

```json
{
  "template": "carrossel-twitter-post-style",
  "version": "clara",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "background_color": "#FFFFFF", "orientation": "portrait" },
  "zones": {
    "header": {
      "avatar": { "shape": "circle", "size": "64px", "note": "vazio — adicionar foto no Canva" },
      "text_block": {
        "line_1": { "content": "Diego Spanevello | Inteligência Artificial", "font_size": "26px", "font_style": "semibold sans-serif", "font_color": "#1A1A1A" },
        "line_2": { "content": "@diego.spanevello", "font_size": "22px", "font_style": "regular sans-serif", "font_color": "#888888" }
      },
      "verified_badge": { "type": "circle checkmark", "color": "#1D9BF0", "size": "20px" }
    },
    "content": {
      "copy": {
        "font_size": "34px",
        "font_style": "regular sans-serif",
        "font_color": "#1A1A1A",
        "line_height": "1.4",
        "bold_support": true,
        "text": "Isso substitui uma assinatura de **mais de R$100 mil por ano** e é 100% grátis"
      }
    },
    "image": {
      "slot_within_slide": { "width_px": 992, "height_px": 558, "aspect_ratio": "16:9" },
      "border_radius": "18px",
      "image_generation": {
        "format": { "dimensions": "1920x1080px", "aspect_ratio": "16:9", "orientation": "landscape" },
        "asset_prompt": {
          "scene": {
            "description": "Um humanoide de terno formal cuja cabeça é substituída por um monitor retrô volumoso exibindo uma tela de corretora ao vivo com gráfico de velas e livro de ofertas, em composição horizontal centralizada sobre fundo preto absoluto #0a0a0a. O corpo do monitor tem um leve acabamento âmbar/laranja #E84000 nas bordas, contrastando com o preto profundo do fundo, transmitindo a ideia de alguém completamente absorvido pelo dado de mercado.",
            "subject": "Figura humanoide de terno formal, cabeça substituída por monitor retrô volumoso exibindo tela de corretora",
            "setting": "Fundo preto absoluto, vazio, sem elementos de cenário, composição horizontal minimalista",
            "action": "Figura estática, de pé, monitor-cabeça ligado exibindo dados em tempo real"
          },
          "style": {
            "primary": "ilustração digital conceitual, tom entre editorial e surreal minimalista",
            "rendering_quality": "hyperrealistic",
            "surface_textures": "acabamento do monitor com plástico retrô fosco, tela com brilho de CRT sutil, terno com tecido liso formal",
            "lighting": "luz âmbar/laranja saindo da tela como única fonte de luz, resto do ambiente em preto absoluto"
          },
          "technical": {
            "camera": { "focal_length": "50mm", "aperture": "f/2.8", "depth_of_field": "moderada, figura nítida, fundo completamente escuro sem detalhe", "angle": "eye level, frontal" },
            "resolution": "ultra high definition",
            "rendering": "acabamento limpo, contraste alto entre preto absoluto e brilho da tela"
          },
          "materials": {
            "fabric": "tecido de terno liso, ligeiro brilho controlado",
            "surfaces": "plástico retrô do monitor com leve desgaste, tela de vidro com reflexo sutil"
          },
          "composition": {
            "perspective": "frontal, figura centralizada em composição horizontal ampla",
            "framing": "centralizado, muito espaço negativo ao redor",
            "subject_placement": "figura central, leve deslocamento para permitir espaço de respiro nas laterais",
            "safe_area": "nenhum elemento tocando as bordas do frame 1920x1080",
            "ui_elements": "nenhum texto embutido — headline fica na zona content do template"
          },
          "quality": {
            "include": ["conceito visual forte e simples", "contraste dramático preto/âmbar", "textura de monitor retrô realista", "composição minimalista impactante"],
            "avoid": ["fundo poluído", "brilho estourado na tela", "logo ou nome de site visível", "formato quadrado ou retrato"],
            "reference_standard": "Arte conceitual editorial minimalista, tom dark premium tipo campanha Super Agente"
          }
        }
      }
    },
    "footer": { "exists": false }
  },
  "negative_rules": [
    "NUNCA travessão no copy",
    "NUNCA cor no corpo do texto — só negrito",
    "NUNCA fonte do corpo diferente de 34px",
    "NUNCA imagem quadrada ou retrato — slot 16:9 obrigatório",
    "avatar sempre vazio para Canva"
  ]
}
```

---

## GANCHO 3 — "Você pode montar um sistema de trade com IA sem pagar 1 centavo em dado e eu vou te mostrar onde pegar"

### Ideia 7 — Estátua clássica versão "construção"

```json
{
  "template": "carrossel-twitter-post-style",
  "version": "clara",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "background_color": "#FFFFFF", "orientation": "portrait" },
  "zones": {
    "header": {
      "avatar": { "shape": "circle", "size": "64px", "note": "vazio — adicionar foto no Canva" },
      "text_block": {
        "line_1": { "content": "Diego Spanevello | Inteligência Artificial", "font_size": "26px", "font_style": "semibold sans-serif", "font_color": "#1A1A1A" },
        "line_2": { "content": "@diego.spanevello", "font_size": "22px", "font_style": "regular sans-serif", "font_color": "#888888" }
      },
      "verified_badge": { "type": "circle checkmark", "color": "#1D9BF0", "size": "20px" }
    },
    "content": {
      "copy": {
        "font_size": "34px",
        "font_style": "regular sans-serif",
        "font_color": "#1A1A1A",
        "line_height": "1.4",
        "bold_support": true,
        "text": "Você pode montar um **sistema de trade com IA** sem pagar 1 centavo em dado\n\ne eu vou te mostrar onde pegar"
      }
    },
    "image": {
      "slot_within_slide": { "width_px": 992, "height_px": 558, "aspect_ratio": "16:9" },
      "border_radius": "18px",
      "image_generation": {
        "format": { "dimensions": "1920x1080px", "aspect_ratio": "16:9", "orientation": "landscape" },
        "asset_prompt": {
          "scene": {
            "description": "A mesma estátua de mármore azul-acinzentado do universo visual anterior, agora com as duas mãos erguidas manipulando blocos flutuantes translúcidos de código e candles de gráfico, como se estivesse montando/construindo uma estrutura modular no ar. Fundo preto absoluto #0a0a0a, blocos com contorno em ciano e laranja #E84000, sugerindo montagem ativa de um sistema, não apenas observação passiva.",
            "subject": "Estátua de mármore esculpida, barba longa, tórax musculoso, mãos erguidas manipulando blocos flutuantes de dados",
            "setting": "Vazio infinito preto com blocos modulares de código e candles flutuando ao redor das mãos da estátua",
            "action": "Estátua montando/conectando blocos de dados flutuantes, gesto de construção ativa"
          },
          "style": {
            "primary": "fine art digital sculpture render com elementos de UI técnica modular",
            "rendering_quality": "hyperrealistic",
            "surface_textures": "mármore polido com veios sutis, blocos flutuantes com acabamento translúcido tipo vidro fosco",
            "lighting": "luz fria azul-elétrica de cima, brilho laranja saindo dos blocos em construção"
          },
          "technical": {
            "camera": { "focal_length": "35mm", "aperture": "f/2.8", "depth_of_field": "moderada, mãos e blocos em foco nítido, fundo levemente suavizado", "angle": "três quartos, levemente baixo para dar monumentalidade" },
            "resolution": "ultra high definition",
            "rendering": "sem grão, render 3D limpo, bloom controlado nos blocos translúcidos"
          },
          "materials": {
            "surfaces": "mármore com micro-arranhões, blocos translúcidos com refração sutil de luz"
          },
          "composition": {
            "perspective": "profundidade rasa, estátua centralizada, blocos flutuando ao redor das mãos",
            "framing": "regra dos terços horizontal",
            "subject_placement": "estátua central, mãos erguidas ocupando o eixo de atenção principal",
            "safe_area": "nenhum elemento tocando as bordas do frame 1920x1080",
            "ui_elements": "nenhum texto embutido — headline fica na zona content do template"
          },
          "quality": {
            "include": ["sensação de construção ativa", "textura de mármore realista", "blocos translúcidos nítidos", "paleta de marca coerente"],
            "avoid": ["blocos ilegíveis ou confusos", "textura plástica no mármore", "logo ou nome de site visível", "formato quadrado ou retrato"],
            "reference_standard": "Render editorial 3D estilo Behance/ArtStation, tom dark premium tipo elevenlabs"
          }
        }
      }
    },
    "footer": { "exists": false }
  },
  "negative_rules": [
    "NUNCA travessão no copy",
    "NUNCA cor no corpo do texto — só negrito",
    "NUNCA fonte do corpo diferente de 34px",
    "NUNCA imagem quadrada ou retrato — slot 16:9 obrigatório",
    "avatar sempre vazio para Canva"
  ]
}
```

### Ideia 8 — Macaco investidor confiante

```json
{
  "template": "carrossel-twitter-post-style",
  "version": "clara",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "background_color": "#FFFFFF", "orientation": "portrait" },
  "zones": {
    "header": {
      "avatar": { "shape": "circle", "size": "64px", "note": "vazio — adicionar foto no Canva" },
      "text_block": {
        "line_1": { "content": "Diego Spanevello | Inteligência Artificial", "font_size": "26px", "font_style": "semibold sans-serif", "font_color": "#1A1A1A" },
        "line_2": { "content": "@diego.spanevello", "font_size": "22px", "font_style": "regular sans-serif", "font_color": "#888888" }
      },
      "verified_badge": { "type": "circle checkmark", "color": "#1D9BF0", "size": "20px" }
    },
    "content": {
      "copy": {
        "font_size": "34px",
        "font_style": "regular sans-serif",
        "font_color": "#1A1A1A",
        "line_height": "1.4",
        "bold_support": true,
        "text": "Você pode montar um **sistema de trade com IA** sem pagar 1 centavo em dado\n\ne eu vou te mostrar onde pegar"
      }
    },
    "image": {
      "slot_within_slide": { "width_px": 992, "height_px": 558, "aspect_ratio": "16:9" },
      "border_radius": "18px",
      "image_generation": {
        "format": { "dimensions": "1920x1080px", "aspect_ratio": "16:9", "orientation": "landscape" },
        "asset_prompt": {
          "scene": {
            "description": "O mesmo chimpanzé de terno do universo visual anterior, agora em postura confiante e ereta, terno mais alinhado, sentado à mesma mesa escura, olhando diretamente para a câmera com leve meio-sorriso. Atrás dele, a tela grande agora mostra um gráfico de linha subindo consistentemente em verde-ciano sobre fundo #111111, com contorno laranja #E84000 na borda da tela, sugerindo domínio da situação em vez de confusão.",
            "subject": "Chimpanzé antropomorfizado, terno alinhado, postura confiante, leve meio-sorriso, mãos sobre a mesa",
            "setting": "Escritório escuro minimalista, mesa de madeira escura, tela de gráfico ascendente ao fundo",
            "action": "Postura confiante, olhando para a câmera, como se tivesse encontrado a estrutura certa"
          },
          "style": {
            "primary": "fotografia editorial satírica com tom vintage, still de escritório reinterpretado",
            "rendering_quality": "hyperrealistic",
            "surface_textures": "pelo com textura fina realista, tecido do terno com trama visível e caimento mais limpo",
            "lighting": "luz frontal mais suave e equilibrada que a versão anterior, brilho laranja controlado saindo da tela"
          },
          "technical": {
            "camera": { "focal_length": "85mm", "aperture": "f/2.8", "depth_of_field": "moderada-rasa, chimpanzé nítido, tela suavizada", "angle": "eye level, frontal direto" },
            "resolution": "ultra high definition",
            "rendering": "leve grão sutil tipo still fotográfico, cores levemente mais vivas que a versão irônica anterior"
          },
          "materials": {
            "fabric": "tecido de terno com trama visível, caimento mais alinhado",
            "surfaces": "mesa de madeira escura com riscos leves de uso"
          },
          "composition": {
            "perspective": "profundidade moderada, chimpanzé em primeiro plano, gráfico ascendente ao fundo",
            "framing": "regra dos terços horizontal",
            "subject_placement": "chimpanzé centralizado levemente à direita, espaço negativo à esquerda",
            "safe_area": "nenhum elemento tocando as bordas do frame 1920x1080",
            "ui_elements": "nenhum texto embutido — headline fica na zona content do template"
          },
          "quality": {
            "include": ["postura confiante", "textura de pelo realista", "gráfico ascendente nítido", "contraste sutil com acento laranja"],
            "avoid": ["expressão confusa ou cômica em excesso", "pelo com aspecto plástico", "logo ou nome de site visível", "formato quadrado ou retrato"],
            "reference_standard": "Still fotográfico satírico editorial, tom de virada de sorte com estrutura certa"
          }
        }
      }
    },
    "footer": { "exists": false }
  },
  "negative_rules": [
    "NUNCA travessão no copy",
    "NUNCA cor no corpo do texto — só negrito",
    "NUNCA fonte do corpo diferente de 34px",
    "NUNCA imagem quadrada ou retrato — slot 16:9 obrigatório",
    "avatar sempre vazio para Canva"
  ]
}
```

### Ideia 9 — Capa editorial "manual/blueprint"

```json
{
  "template": "carrossel-twitter-post-style",
  "version": "clara",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "background_color": "#FFFFFF", "orientation": "portrait" },
  "zones": {
    "header": {
      "avatar": { "shape": "circle", "size": "64px", "note": "vazio — adicionar foto no Canva" },
      "text_block": {
        "line_1": { "content": "Diego Spanevello | Inteligência Artificial", "font_size": "26px", "font_style": "semibold sans-serif", "font_color": "#1A1A1A" },
        "line_2": { "content": "@diego.spanevello", "font_size": "22px", "font_style": "regular sans-serif", "font_color": "#888888" }
      },
      "verified_badge": { "type": "circle checkmark", "color": "#1D9BF0", "size": "20px" }
    },
    "content": {
      "copy": {
        "font_size": "34px",
        "font_style": "regular sans-serif",
        "font_color": "#1A1A1A",
        "line_height": "1.4",
        "bold_support": true,
        "text": "Você pode montar um **sistema de trade com IA** sem pagar 1 centavo em dado\n\ne eu vou te mostrar onde pegar"
      }
    },
    "image": {
      "slot_within_slide": { "width_px": 992, "height_px": 558, "aspect_ratio": "16:9" },
      "border_radius": "18px",
      "image_generation": {
        "format": { "dimensions": "1920x1080px", "aspect_ratio": "16:9", "orientation": "landscape" },
        "asset_prompt": {
          "scene": {
            "description": "Composição horizontal estilo capa editorial técnica, com a mesma figura em traje escuro e capacete refletivo ajoelhada em cenário industrial, mas agora com linhas de blueprint e esquemas técnicos (circuitos, marcações de medida, setas de fluxo) sobrepostos em ciano fino sobre o ambiente ao redor da esfera dourada que ela segura. Fundo em tons verde-petróleo e cinza escuro, contorno laranja #E84000 na esfera, reforçando a sensação de 'aqui está o caminho/manual'.",
            "subject": "Figura em traje técnico escuro com capacete refletivo, ajoelhada, segurando esfera dourada, cercada por linhas de blueprint técnico flutuantes",
            "setting": "Ambiente industrial abandonado com overlay de esquema técnico/blueprint em ciano fino, enquadramento horizontal amplo",
            "action": "Figura ajoelhada apresentando a esfera dourada como se fosse o núcleo de um sistema, cercada pelo diagrama técnico"
          },
          "style": {
            "primary": "editorial book cover art com overlay técnico tipo blueprint, sci-fi retrô reinterpretado",
            "rendering_quality": "hyperrealistic",
            "surface_textures": "capacete com reflexo especular controlado, traje com textura de couro/metal desgastado, linhas de blueprint finas e nítidas",
            "lighting": "facho de luz suave difuso vindo de cima, contraluz esverdeada, brilho quente saindo da esfera dourada"
          },
          "technical": {
            "camera": { "focal_length": "35mm", "aperture": "f/4", "depth_of_field": "moderada, figura e esfera nítidas, fundo suavizado", "angle": "eye level, levemente frontal" },
            "resolution": "ultra high definition",
            "rendering": "acabamento limpo com leve grão editorial, linhas de blueprint com nitidez vetorial"
          },
          "materials": {
            "surfaces": "traje com couro desgastado e metal oxidado, esfera dourada líquido-metálica, estruturas de fundo com ferrugem"
          },
          "environment": {
            "atmosphere": "névoa leve suspensa, ar denso pós-chuva",
            "particles": "poeira fina suspensa, leve umidade"
          },
          "composition": {
            "perspective": "profundidade em camadas horizontais, figura centralizada levemente à esquerda, blueprint sobreposto em toda a cena",
            "framing": "centralizado, estilo capa técnica adaptada a landscape",
            "subject_placement": "figura no terço central/esquerdo, linhas de blueprint conectando a esfera ao restante do frame",
            "safe_area": "nenhum elemento tocando as bordas do frame 1920x1080",
            "ui_elements": "nenhum texto embutido — headline fica na zona content do template"
          },
          "quality": {
            "include": ["overlay de blueprint nítido e fino", "composição editorial dramática", "reflexo metálico realista", "sensação de manual/passo a passo"],
            "avoid": ["blueprint poluído ou ilegível", "esfera com reflexo genérico", "logo ou nome de site visível", "formato quadrado ou retrato"],
            "reference_standard": "Capa editorial sci-fi retrô com overlay técnico estilo diagrama de engenharia, tom industrial premium"
          }
        }
      }
    },
    "footer": { "exists": false }
  },
  "negative_rules": [
    "NUNCA travessão no copy",
    "NUNCA cor no corpo do texto — só negrito",
    "NUNCA fonte do corpo diferente de 34px",
    "NUNCA imagem quadrada ou retrato — slot 16:9 obrigatório",
    "avatar sempre vazio para Canva"
  ]
}
```
