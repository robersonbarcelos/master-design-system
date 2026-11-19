# JSONs: As cinco datas (BNB Connect) · 8 slides · 1080x1350

Fotos reais anexadas pelo usuário: ANEXO_01 a ANEXO_08. Cada JSON indica o anexo e a zona onde ele entra. Logo sempre composto depois com `references/logo.jpg`.

## Slide 0 · Capa · L5 card-01
```json
{
  "variacao": "Slide 0 · Capa · L5 card-01 foto full-bleed + headline caixa alta",
  "slide": "0",
  "template": "POR-DENTRO-DA-GESTAO-BNB.json > card-01-fullbleed-equipe-inspecao (adaptado: imóvel sem pessoa)",
  "format": { "aspect_ratio": "4:5", "size": "1080x1350px", "safe_area": "64px em todas as bordas (zona útil 952x1222px)" },
  "zones": {
    "image": {
      "source": "ANEXO_01_capa.jpg (foto real anexada pelo usuário)",
      "conteudo_esperado": "fachada ou varanda de casa de praia ao entardecer, céu limpo no terço superior",
      "posicao": "full-bleed, ocupa 100% do frame 1080x1350",
      "reference_lock": "usar a foto anexada como está: não redesenhar o imóvel, não trocar móveis, não alterar arquitetura; permitido só crop 4:5 e leve ajuste de luz para legibilidade do texto",
      "area_livre_para_texto": "terço superior (y 0 a ~450px)"
    },
    "header": {
      "logo": "área reservada no topo esquerdo, versão clara #FFFFFF se o céu estiver escuro ou versão escura #005070 se estiver claro; NÃO gerar, compor depois com o arquivo oficial"
    },
    "content": {
      "headline": { "texto": "AS CINCO DATAS QUE FAZEM A DIFERENÇA NO ANO DE UMA CASA DE TEMPORADA", "fonte": "Manrope Bold 700, caixa alta, ~58px, 4 linhas", "cor": "Petróleo BNB #005070 sólido", "posicao": "terço superior, alinhado à esquerda, margem 64px" },
      "subtitulo": { "texto": "E por que o preço de cada uma precisa estar no ar antes da demanda aparecer.", "fonte": "Manrope Regular 400, ~26px, 2 linhas", "cor": "Dourado fosco #A9782E sólido", "posicao": "logo abaixo da headline, 24px de respiro" }
    },
    "footer": { "elemento": "seta discreta → no canto inferior direito, off-white #F8F4EA, indicando arraste" }
  },
  "text_rules": [ "Hierarquia só por peso e cor (Autoridade estratégica)", "Sem serifada neste slide", "Texto nunca sobre área movimentada da foto: se necessário, gradiente suave off-white no topo com no máximo 25% de opacidade" ],
  "negative_rules": [ "NUNCA gerar o logo via IA", "NUNCA travessão (—)", "NUNCA alterar o imóvel da foto anexada", "NUNCA fonte de sistema genérica (Arial, Helvetica, Times)", "NUNCA misturar Manrope e Sora", "NUNCA dourado metálico brilhante ou alaranjado", "NUNCA texto acinzentado ou desbotado", "NUNCA pessoas inventadas na cena" ]
}
```

## Slide 1 · Tese · L5 card-02
```json
{
  "variacao": "Slide 1 · Tese · L5 card-02 foto full-bleed + card navy flutuante com serifada dourada",
  "slide": "1",
  "template": "POR-DENTRO-DA-GESTAO-BNB.json > card-02-fullbleed-card-flutuante-navy-serifada",
  "format": { "aspect_ratio": "4:5", "size": "1080x1350px", "safe_area": "64px em todas as bordas (zona útil 952x1222px)" },
  "zones": {
    "image": {
      "source": "ANEXO_02_tese.jpg (foto real anexada pelo usuário)",
      "conteudo_esperado": "mesa de trabalho com caderno, calendário de papel e laptop com tela ilegível",
      "posicao": "full-bleed, ocupa 100% do frame",
      "reference_lock": "usar a foto anexada como está; só crop 4:5; se houver tela visível, manter ilegível, sem dados",
      "area_livre_para_card": "metade inferior esquerda"
    },
    "header": { "logo": "área reservada no topo esquerdo, versão clara sobre área escura da foto; NÃO gerar" },
    "content": {
      "card": { "cor": "Azul-marinho profundo #052F42 sólido", "tamanho": "~70% da largura x ~42% da altura", "posicao": "canto inferior esquerdo, contido nos 4 lados com margem mínima de 64px", "estilo": "100% flat, cantos arredondados ~24px, sem sombra, sem contorno" },
      "headline": { "texto": "Preço certo na data errada", "fonte": "Manrope SemiBold 600, ~48px", "cor": "Off-white #F8F4EA" },
      "headline_destaque": { "texto": "não resolve.", "fonte": "Newsreader Italic 400, mesmo tamanho", "cor": "Dourado fosco #A9782E" },
      "corpo": { "texto": "O que pesa no ano é a data certa com o preço já publicado. Essas cinco janelas concentram a procura por casas de temporada e pedem decisão com antecedência.", "fonte": "Manrope Regular 400, ~24px", "cor": "Off-white #F8F4EA" }
    },
    "footer": { "elemento": "seta → off-white dentro do card, canto inferior direito" }
  },
  "text_rules": [ "Newsreader Italic só em 'não resolve.'", "Card com padding interno de 48px", "Corpo em no máximo 4 linhas" ],
  "negative_rules": [ "NUNCA gerar o logo via IA", "NUNCA travessão (—)", "NUNCA sombra ou contorno no card", "NUNCA card cortado pela borda", "NUNCA dashboard ou números inventados em tela", "NUNCA outra serifada além de Newsreader Italic", "NUNCA fonte de sistema genérica" ]
}
```

## Slide 2 · Réveillon · L1 card-04
```json
{
  "variacao": "Slide 2 · Réveillon · L1 card-04 foto topo 60% + faixa off-white base 40%",
  "slide": "2",
  "template": "AUTORIDADE-BNB.json > card-04-split-horizontal-foto-topo-card-base (estilo Hospitalidade contemporânea, secundário permitido da Linha 5)",
  "format": { "aspect_ratio": "4:5", "size": "1080x1350px", "safe_area": "64px em todas as bordas (zona útil 952x1222px)" },
  "zones": {
    "image": {
      "source": "ANEXO_03_reveillon.jpg (foto real anexada pelo usuário)",
      "conteudo_esperado": "casa de praia à noite ou ao anoitecer, luzes acesas, mar ao fundo",
      "posicao": "60% superior do frame (1080x810px), borda a borda, corte reto na base",
      "reference_lock": "usar a foto anexada como está; só crop para 1080x810"
    },
    "header": { "logo": "nenhum neste slide (logo só na capa e no fechamento)" },
    "content": {
      "bloco": { "cor": "Off-white quente #F8F4EA sólido", "posicao": "40% inferior (1080x540px), largura total, sem arredondamento" },
      "tag": { "texto": "28 de dezembro a 2 de janeiro", "estilo": "pílula Azul-marinho #052F42, texto off-white Manrope Medium ~20px", "posicao": "topo do bloco, alinhada à esquerda, margem 64px" },
      "titulo": { "texto": "Réveillon", "fonte": "Manrope Bold 700, ~64px", "cor": "Petróleo BNB #005070" },
      "frase": { "texto": "A diária mais alta do ano para casas no litoral.", "fonte": "Manrope SemiBold 600, ~28px", "cor": "Dourado fosco #A9782E" },
      "corpo": { "texto": "Quem procura casa para a virada reserva cedo. Quando o preço entra tarde, a casa negocia com o que sobrou da demanda.", "fonte": "Manrope Regular 400, ~22px", "cor": "Petróleo BNB #005070" }
    },
    "footer": { "elemento": "linha fina #005070 a 40% de largura na base do bloco + número 01/05 à direita em Manrope Medium ~18px" }
  },
  "text_rules": [ "Molde fixo idêntico nos slides 2 a 6: tag, título, frase dourada, corpo", "Sem serifada nos slides de data", "Corpo em no máximo 3 linhas" ],
  "negative_rules": [ "NUNCA travessão (—)", "NUNCA alterar o imóvel da foto anexada", "NUNCA arredondar o bloco off-white", "NUNCA fonte de sistema genérica", "NUNCA dourado metálico ou alaranjado", "NUNCA texto sobre a foto neste slide" ]
}
```

## Slide 3 · Carnaval · L1 card-04
```json
{
  "variacao": "Slide 3 · Carnaval · L1 card-04 foto topo 60% + faixa off-white base 40%",
  "slide": "3",
  "template": "AUTORIDADE-BNB.json > card-04-split-horizontal-foto-topo-card-base (estilo Hospitalidade contemporânea, secundário permitido da Linha 5)",
  "format": { "aspect_ratio": "4:5", "size": "1080x1350px", "safe_area": "64px em todas as bordas (zona útil 952x1222px)" },
  "zones": {
    "image": {
      "source": "ANEXO_04_carnaval.jpg (foto real anexada pelo usuário)",
      "conteudo_esperado": "casa de praia com rua ou vila enfeitada ao fundo, fim de tarde",
      "posicao": "60% superior do frame (1080x810px), borda a borda, corte reto na base",
      "reference_lock": "usar a foto anexada como está; só crop para 1080x810"
    },
    "header": { "logo": "nenhum neste slide" },
    "content": {
      "bloco": { "cor": "Off-white quente #F8F4EA sólido", "posicao": "40% inferior (1080x540px), largura total, sem arredondamento" },
      "tag": { "texto": "Fevereiro (a data muda a cada ano)", "estilo": "pílula Azul-marinho #052F42, texto off-white Manrope Medium ~20px", "posicao": "topo do bloco, alinhada à esquerda, margem 64px" },
      "titulo": { "texto": "Carnaval", "fonte": "Manrope Bold 700, ~64px", "cor": "Petróleo BNB #005070" },
      "frase": { "texto": "A segunda grande janela do litoral.", "fonte": "Manrope SemiBold 600, ~28px", "cor": "Dourado fosco #A9782E" },
      "corpo": { "texto": "Casas perto de destinos com festa de rua ganham ainda mais procura, e a reserva acontece num prazo mais curto que o da virada.", "fonte": "Manrope Regular 400, ~22px", "cor": "Petróleo BNB #005070" }
    },
    "footer": { "elemento": "linha fina #005070 a 40% de largura na base do bloco + número 02/05 à direita em Manrope Medium ~18px" }
  },
  "text_rules": [ "Molde fixo idêntico nos slides 2 a 6: tag, título, frase dourada, corpo", "Sem serifada nos slides de data", "Corpo em no máximo 3 linhas" ],
  "negative_rules": [ "NUNCA travessão (—)", "NUNCA alterar o imóvel da foto anexada", "NUNCA arredondar o bloco off-white", "NUNCA fonte de sistema genérica", "NUNCA dourado metálico ou alaranjado", "NUNCA texto sobre a foto neste slide" ]
}
```

## Slide 4 · Semana Santa · L1 card-04
```json
{
  "variacao": "Slide 4 · Semana Santa · L1 card-04 foto topo 60% + faixa off-white base 40%",
  "slide": "4",
  "template": "AUTORIDADE-BNB.json > card-04-split-horizontal-foto-topo-card-base (estilo Hospitalidade contemporânea, secundário permitido da Linha 5)",
  "format": { "aspect_ratio": "4:5", "size": "1080x1350px", "safe_area": "64px em todas as bordas (zona útil 952x1222px)" },
  "zones": {
    "image": {
      "source": "ANEXO_05_semana-santa.jpg (foto real anexada pelo usuário)",
      "conteudo_esperado": "sala integrada ou mesa grande preparada para família, luz natural",
      "posicao": "60% superior do frame (1080x810px), borda a borda, corte reto na base",
      "reference_lock": "usar a foto anexada como está; só crop para 1080x810"
    },
    "header": { "logo": "nenhum neste slide" },
    "content": {
      "bloco": { "cor": "Off-white quente #F8F4EA sólido", "posicao": "40% inferior (1080x540px), largura total, sem arredondamento" },
      "tag": { "texto": "Março ou abril (muda a cada ano)", "estilo": "pílula Azul-marinho #052F42, texto off-white Manrope Medium ~20px", "posicao": "topo do bloco, alinhada à esquerda, margem 64px" },
      "titulo": { "texto": "Semana Santa", "fonte": "Manrope Bold 700, ~64px", "cor": "Petróleo BNB #005070" },
      "frase": { "texto": "Procura alta, com perfil de família.", "fonte": "Manrope SemiBold 600, ~28px", "cor": "Dourado fosco #A9782E" },
      "corpo": { "texto": "Grupos maiores buscam quartos suficientes, cozinha montada e espaço para todo mundo junto. A casa que mostra isso no anúncio sai na frente.", "fonte": "Manrope Regular 400, ~22px", "cor": "Petróleo BNB #005070" }
    },
    "footer": { "elemento": "linha fina #005070 a 40% de largura na base do bloco + número 03/05 à direita em Manrope Medium ~18px" }
  },
  "text_rules": [ "Molde fixo idêntico nos slides 2 a 6: tag, título, frase dourada, corpo", "Sem serifada nos slides de data", "Corpo em no máximo 3 linhas" ],
  "negative_rules": [ "NUNCA travessão (—)", "NUNCA alterar o imóvel da foto anexada", "NUNCA arredondar o bloco off-white", "NUNCA fonte de sistema genérica", "NUNCA dourado metálico ou alaranjado", "NUNCA texto sobre a foto neste slide" ]
}
```

## Slide 5 · Feriados prolongados · L1 card-04
```json
{
  "variacao": "Slide 5 · Feriados prolongados · L1 card-04 foto topo 60% + faixa off-white base 40%",
  "slide": "5",
  "template": "AUTORIDADE-BNB.json > card-04-split-horizontal-foto-topo-card-base (estilo Hospitalidade contemporânea, secundário permitido da Linha 5)",
  "format": { "aspect_ratio": "4:5", "size": "1080x1350px", "safe_area": "64px em todas as bordas (zona útil 952x1222px)" },
  "zones": {
    "image": {
      "source": "ANEXO_06_feriados.jpg (foto real anexada pelo usuário)",
      "conteudo_esperado": "varanda com mesa posta e vista, luz de dia",
      "posicao": "60% superior do frame (1080x810px), borda a borda, corte reto na base",
      "reference_lock": "usar a foto anexada como está; só crop para 1080x810"
    },
    "header": { "logo": "nenhum neste slide" },
    "content": {
      "bloco": { "cor": "Off-white quente #F8F4EA sólido", "posicao": "40% inferior (1080x540px), largura total, sem arredondamento" },
      "tag": { "texto": "Tiradentes, Corpus Christi, 7 de Setembro", "estilo": "pílula Azul-marinho #052F42, texto off-white Manrope Medium ~20px", "posicao": "topo do bloco, alinhada à esquerda, margem 64px" },
      "titulo": { "texto": "Feriados prolongados", "fonte": "Manrope Bold 700, ~60px", "cor": "Petróleo BNB #005070" },
      "frase": { "texto": "As datas que mais passam despercebidas.", "fonte": "Manrope SemiBold 600, ~28px", "cor": "Dourado fosco #A9782E" },
      "corpo": { "texto": "Feriado emendado com quinta ou sexta enche o litoral, mas muita casa continua com o preço de um fim de semana comum.", "fonte": "Manrope Regular 400, ~22px", "cor": "Petróleo BNB #005070" }
    },
    "footer": { "elemento": "linha fina #005070 a 40% de largura na base do bloco + número 04/05 à direita em Manrope Medium ~18px" }
  },
  "text_rules": [ "Molde fixo idêntico nos slides 2 a 6: tag, título, frase dourada, corpo", "Sem serifada nos slides de data", "Título pode reduzir para ~60px para caber em 1 linha" ],
  "negative_rules": [ "NUNCA travessão (—)", "NUNCA alterar o imóvel da foto anexada", "NUNCA arredondar o bloco off-white", "NUNCA fonte de sistema genérica", "NUNCA dourado metálico ou alaranjado", "NUNCA texto sobre a foto neste slide" ]
}
```

## Slide 6 · Férias de julho · L1 card-04
```json
{
  "variacao": "Slide 6 · Férias de julho · L1 card-04 foto topo 60% + faixa off-white base 40%",
  "slide": "6",
  "template": "AUTORIDADE-BNB.json > card-04-split-horizontal-foto-topo-card-base (estilo Hospitalidade contemporânea, secundário permitido da Linha 5)",
  "format": { "aspect_ratio": "4:5", "size": "1080x1350px", "safe_area": "64px em todas as bordas (zona útil 952x1222px)" },
  "zones": {
    "image": {
      "source": "ANEXO_07_julho.jpg (foto real anexada pelo usuário)",
      "conteudo_esperado": "interior aconchegante da casa com mantas, luz quente, dia nublado lá fora",
      "posicao": "60% superior do frame (1080x810px), borda a borda, corte reto na base",
      "reference_lock": "usar a foto anexada como está; só crop para 1080x810"
    },
    "header": { "logo": "nenhum neste slide" },
    "content": {
      "bloco": { "cor": "Off-white quente #F8F4EA sólido", "posicao": "40% inferior (1080x540px), largura total, sem arredondamento" },
      "tag": { "texto": "Julho", "estilo": "pílula Azul-marinho #052F42, texto off-white Manrope Medium ~20px", "posicao": "topo do bloco, alinhada à esquerda, margem 64px" },
      "titulo": { "texto": "Férias de julho", "fonte": "Manrope Bold 700, ~64px", "cor": "Petróleo BNB #005070" },
      "frase": { "texto": "A janela que pede outro tipo de casa.", "fonte": "Manrope SemiBold 600, ~28px", "cor": "Dourado fosco #A9782E" },
      "corpo": { "texto": "No inverno, o perfil de quem procura o litoral muda. Casa preparada para o frio, com cobertas extras e área coberta, aproveita melhor esse mês.", "fonte": "Manrope Regular 400, ~22px", "cor": "Petróleo BNB #005070" }
    },
    "footer": { "elemento": "linha fina #005070 a 40% de largura na base do bloco + número 05/05 à direita em Manrope Medium ~18px" }
  },
  "text_rules": [ "Molde fixo idêntico nos slides 2 a 6: tag, título, frase dourada, corpo", "Sem serifada nos slides de data", "Corpo em no máximo 3 linhas" ],
  "negative_rules": [ "NUNCA travessão (—)", "NUNCA alterar o imóvel da foto anexada", "NUNCA arredondar o bloco off-white", "NUNCA fonte de sistema genérica", "NUNCA dourado metálico ou alaranjado", "NUNCA texto sobre a foto neste slide" ]
}
```

## Slide 7 · Fechamento · L5 card-04
```json
{
  "variacao": "Slide 7 · Fechamento · L5 card-04 foto full-bleed + card off-white flutuante central",
  "slide": "7",
  "template": "POR-DENTRO-DA-GESTAO-BNB.json > card-04-fullbleed-card-flutuante-precificacao",
  "format": { "aspect_ratio": "4:5", "size": "1080x1350px", "safe_area": "64px em todas as bordas (zona útil 952x1222px)" },
  "zones": {
    "image": {
      "source": "ANEXO_08_fechamento.jpg (foto real anexada pelo usuário)",
      "conteudo_esperado": "mãos escrevendo num caderno ao lado de laptop com tela ilegível",
      "posicao": "full-bleed, ocupa 100% do frame",
      "reference_lock": "usar a foto anexada como está; só crop 4:5; tela sempre ilegível, sem dados"
    },
    "header": { "logo": "dentro do card, no topo, versão escura Petróleo #005070; NÃO gerar, compor depois" },
    "content": {
      "card": { "cor": "Off-white quente #F8F4EA sólido", "tamanho": "~80% da largura x ~58% da altura", "posicao": "centralizado, contido nos 4 lados com margem visível", "estilo": "100% flat, cantos arredondados ~24px, sem sombra, sem contorno" },
      "headline": { "texto": "Preço não é palpite.", "fonte": "Manrope Bold 700, ~56px, 2 linhas", "cor": "Petróleo BNB #005070" },
      "subtitulo": { "texto": "É a leitura diária da demanda para cada data render o que pode.", "fonte": "Manrope Regular 400, ~26px", "cor": "Dourado fosco #A9782E" },
      "corpo": { "texto": "A gente entra como coanfitriã no seu próprio anúncio e ajusta o calendário antes da procura chegar.", "fonte": "Manrope Regular 400, ~22px", "cor": "Petróleo BNB #005070" },
      "cta": { "texto": "Quer saber se o seu calendário já está pronto para essas cinco datas? Clica no link da bio.", "fonte": "Manrope SemiBold 600, ~22px", "cor": "Petróleo BNB #005070", "posicao": "última linha do card, isolada, separada por linha fina dourada" }
    },
    "footer": { "elemento": "nenhum fora do card" }
  },
  "text_rules": [ "Sem serifada (card-04 da Linha 5 é só sans)", "CTA sempre isolado na última linha", "Padding interno do card 56px" ],
  "negative_rules": [ "NUNCA gerar o logo via IA", "NUNCA travessão (—)", "NUNCA sombra ou contorno no card", "NUNCA card cortado pela borda", "NUNCA dashboard ou números inventados em tela", "NUNCA citar o nome interno da ferramenta de IA", "NUNCA fonte de sistema genérica" ]
}
```
