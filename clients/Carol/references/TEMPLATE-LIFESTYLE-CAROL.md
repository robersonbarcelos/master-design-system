# Prompt Templates — Slides Centrais (Carrossel "Peças-Chave / Guarda-Roupa Cápsula")
**Cliente:** Carol Staggemeier
**Formato fixo:** 1080x1350px · 4:5 Instagram Feed
**Criado em:** 2026-07-17
**Status:** ✅ Template FECHADO — as 9 variações (3 estruturas x 3 versões cada) foram testadas e aprovadas pela cliente. Cobre os slides CENTRAIS do carrossel de peças-chave (não a capa). Pacote novo, separado do "Não Tenho Roupa" (`TEMPLATE-CABIDE-TEXTO-CAROL.md`).

---

## Como usar (GATE — responder antes de gerar)

Este template só deve ser usado depois de confirmar com quem está pedindo a peça:

```
1. QUAL ESTRUTURA?
   → GRID (título + legenda + 3 fotos em coluna)
   → HOOK QUOTE (foto full-bleed + citação com gradiente escuro)
   → CAPA LIFESTYLE (foto full-bleed + headline + legenda + CTA bold + seta)

2. QUAL VARIAÇÃO DENTRO DA ESTRUTURA ESCOLHIDA?
   → ver guia de escolha abaixo — nunca assumir estilo

3. QUAL TEXTO VAI? (título/legenda ou frase curta/frase principal ou headline/CTA,
   dependendo da estrutura)
   → se não for informado, perguntar antes de gerar. Nunca assumir copy.

4. Copie o JSON da variação escolhida
5. Anexe as imagens de referência necessárias (ver contagem indicada em cada
   variação — GRID pede 3 fotos, HOOK e CAPA LIFESTYLE pedem 1 foto cada)
6. GARMENT FIDELITY LOCK: a peça deve ser reproduzida EXATAMENTE como na(s)
   foto(s) de referência anexada(s)
7. Substitua os textos entre [colchetes] pelo texto confirmado no passo 3
8. Cole no gerador junto com a(s) foto(s)
```

> Mesma lógica de gate usada no `TEMPLATE-CABIDE-TEXTO-CAROL.md` e `TEMPLATE-COLAGEM-POSES-CAROL.md`: nunca gerar a peça final sem antes confirmar estrutura + variação + copy.

---

## Guia de escolha — status de cada variação

| Estrutura | Variação | Nome | Imagens de referência | Status |
|---|---|---|---|---|
| GRID | GRID-A | Linho Clean | 3 fotos | **✅ APROVADO — fechado** |
| GRID | GRID-B | Salva Contraste | 3 fotos | **✅ APROVADO — fechado** |
| GRID | GRID-C | Areia Quente Bloco | 3 fotos | **✅ APROVADO — fechado** |
| HOOK QUOTE | HOOK-A | Café Terroso Gradiente | 1 foto | **✅ APROVADO — fechado** |
| HOOK QUOTE | HOOK-B | Verde Floresta Gradiente | 1 foto | **✅ APROVADO — fechado** |
| HOOK QUOTE | HOOK-C | Cápsula Sólida | 1 foto | **✅ APROVADO — fechado** |
| CAPA LIFESTYLE | CAPA-LS-A | Verde Floresta Vinheta | 1 foto | **✅ APROVADO — fechado** |
| CAPA LIFESTYLE | CAPA-LS-B | Café Terroso Vinheta | 1 foto | **✅ APROVADO — fechado** |
| CAPA LIFESTYLE | CAPA-LS-C | Vinheta Sutil + Bloco de Texto Salva | 1 foto | **✅ APROVADO — fechado** |

---

## Regras fixas em todas as estruturas

- **Formato:** 1080x1350px · 4:5 · Instagram Feed · safe area 952x1222px (mínimo 64px em todos os lados)
- **Fidelidade da peça:** GARMENT FIDELITY LOCK — reprodução exata da referência anexada, sem reinterpretação, sem redesign
- **Tecido:** MATTE obrigatório — zero shimmer, zero lurex, zero brilho, zero metálico (exceto seda genuína)
- **Header padrão (obrigatório, sempre presente nos slides centrais):**
  "CAROL STAGGEMEIER" (Nunito Sans Bold, 18px, all caps, letter-spacing 3px, esquerda) + "MODA AUTORAL" (Nunito Sans Regular, 18px, all caps, letter-spacing 3px, direita) + linha separadora fina (1px, opacidade 30%) abaixo
  - Cor em fundo escuro: `rgba(229,222,211,0.55–0.6)`
  - Cor em fundo claro: `rgba(39,61,41,0.45)`
- **Footer dos slides centrais:** sempre "@carolstaggemeier" (Nunito Sans Regular, 16px, opacidade baixa, centralizado na base) — NUNCA "arraste para ver →" (isso é exclusivo da capa)
- **Paleta:** nunca fundo branco puro nem preto puro — sempre Verde Floresta `#273d29`, Café Terroso `#4c3529`, Argila `#786c5c`, Salva `#9db4a1`, Areia Quente `#c2b6a5`, Linho `#e5ded3`
- **Tipografia:** Halant (títulos/headlines/citações) + Nunito Sans (legendas/corpo/header/footer) — nunca Inter, Montserrat, Playfair, DM Sans, Cormorant, Futura
- **Skin Realism Standard obrigatório** sempre que houver modelo humano na(s) foto(s) de referência (estruturas HOOK QUOTE, CAPA LIFESTYLE e as 3 fotos de referência do GRID)
- **Texto de subtítulo/legenda/frase secundária:** lição aprendida em testes — sempre pecar para MAIOR. Tamanhos mínimos consolidados: legenda de GRID 34px, frase curta de HOOK 30px, frase principal de HOOK 52px. Nunca deixar como elemento discreto/pequeno.
- **Vocabulário proibido:** "premium", "luxo", "trends", "must-have", "fashionista", "lacrou", "empoderamento", "alfaiataria"
- **Sem travessão (—)** em nenhum texto

---

## GRID-A — Linho Clean ✅ APROVADO
**📸 Carregar 3 imagens de referência** (as 3 fotos verticais do grid, mesma peça/look em modelos ou ângulos distintos)

```json
{
  "template": "slides_centrais_carol",
  "peca": "peça-chave (definida pelas 3 fotos de referência carregadas)",
  "estrutura": "GRID",
  "versao": "GRID-A_linho_clean_v2",
  "format": "1080x1350px, 4:5",
  "prompt": {
    "scene": {
      "description": "Slide central de carrossel de moda autoral brasileira, fundo sólido em tom Linho quente (#e5ded3), layout limpo e editorial. No topo, header_padrao fixo: à esquerda 'CAROL STAGGEMEIER' (Nunito Sans Bold, 18px, caixa alta, letter-spacing 3px, cor rgba(39,61,41,0.45)), à direita 'MODA AUTORAL' (mesmo estilo), com linha separadora fina de 1px a 30% de opacidade logo abaixo. Centralizado no terço superior, título editorial em Halant Bold, tamanho 56px, cor Café Terroso (#4c3529), duas linhas centralizadas, com nome da peça/look (definido pelas fotos de referência). Abaixo do título, uma legenda explicativa em Nunito Sans Regular — GRANDE e claramente legível, tamanho 34px, cor Café Terroso a 85% de opacidade, line-height 1.4, largura máxima 720px centralizada, 2 linhas de texto curto e editorial (nunca do tamanho de legenda pequena ou rodapé). Abaixo da legenda, grid de 3 fotos verticais em colunas iguais, separadas por gutter fino de 8px em tom Linho, cada foto mostrando a mesma peça de roupa (fidelidade exata ao(s) look(s) de referência) em enquadramento de corpo inteiro, luz natural suave e consistente entre as 3 colunas. Rodapé com '@carolstaggemeier' centralizado, Nunito Sans Regular 16px, cor Café Terroso a 55% de opacidade.",
      "subject": "Peça de roupa (definida pelas fotos de referência carregadas pelo usuário) fotografada em 3 variações de look/modelo/ângulo",
      "setting": "Fundo sólido Linho (#e5ded3), estúdio ou locação neutra dependendo da referência de cada foto",
      "action": "static — grid editorial de apresentação de produto"
    },
    "style": {
      "primary": "editorial lifestyle, moda autoral brasileira, minimalismo escandinavo",
      "rendering_quality": "hyperrealistic, alta definição",
      "surface_textures": "tecidos foscos, texturas naturais de algodão/linho/malha conforme referência",
      "lighting": "luz natural suave, difusa, consistente entre as 3 fotos do grid, sem sombras duras"
    },
    "technical": {
      "camera": { "focal_length": "50mm", "aperture": "f/4", "depth_of_field": "moderada — modelo nítido, fundo levemente suave", "angle": "eye level, corpo inteiro" },
      "resolution": "alta definição, qualidade editorial de revista",
      "rendering": "cores naturais, grão sutil, sem oversaturação",
      "physics_accuracy": "sombra e luz coerentes com ambiente de cada foto de referência"
    },
    "materials": {
      "skin": "pele com tom fiel à referência, poros visíveis na testa e maçãs do rosto, buço fino individual, imperfeições naturais, acabamento fosco — SEM base, SEM pó iluminador, SEM brilho cosmético, SEM suavização artificial, zero pós-processamento, pele natural e viva",
      "fabric": "trama visível do tecido, caimento realista, sem brilho artificial, fosco (exceto seda genuína se presente na referência)",
      "surfaces": "fundo Linho liso e uniforme, sem textura de parede"
    },
    "composition": {
      "perspective": "frontal, 3 colunas verticais iguais",
      "framing": "grid simétrico de 3 colunas com gutter fino",
      "subject_placement": "header no topo, título centralizado, legenda centralizada abaixo do título, grid de fotos ocupando o corpo do slide, footer centralizado na base",
      "safe_area": "952x1222px de área segura dentro do frame 1080x1350px — nenhum texto ou elemento encostando nas bordas",
      "ui_elements": [
        { "elemento": "header esquerda", "texto": "CAROL STAGGEMEIER", "fonte": "Nunito Sans Bold", "tamanho": "18px", "cor": "rgba(39,61,41,0.45)", "posicao": "topo esquerda" },
        { "elemento": "header direita", "texto": "MODA AUTORAL", "fonte": "Nunito Sans Regular", "tamanho": "18px", "cor": "rgba(39,61,41,0.45)", "posicao": "topo direita" },
        { "elemento": "linha separadora", "descricao": "1px, 30% opacidade, largura total da safe area", "posicao": "abaixo do header" },
        { "elemento": "título", "texto": "[definido pela referência/peça]", "fonte": "Halant Bold", "tamanho": "56px", "cor": "#4c3529", "alinhamento": "centralizado", "posicao": "terço superior" },
        { "elemento": "legenda", "texto": "[definida pelo usuário — texto curto explicativo sobre a peça]", "fonte": "Nunito Sans Regular", "tamanho": "34px", "cor": "rgba(76,53,41,0.85)", "alinhamento": "centralizado", "line_height": "1.4", "largura_maxima": "720px", "posicao": "abaixo do título, ANTES do grid de fotos" },
        { "elemento": "grid de fotos", "descricao": "3 colunas verticais iguais, gutter 8px, fotos de corpo inteiro", "posicao": "corpo do slide" },
        { "elemento": "footer", "texto": "@carolstaggemeier", "fonte": "Nunito Sans Regular", "tamanho": "16px", "cor": "rgba(76,53,41,0.55)", "alinhamento": "centralizado", "posicao": "base" }
      ]
    },
    "quality": {
      "include": ["editorial", "minimalista", "moda autoral brasileira", "tipografia legível e proporcional", "luz natural", "pele realista", "fidelidade de tecido", "grid limpo e simétrico", "hierarquia tipográfica clara"],
      "avoid": ["plastic skin", "airbrushed skin", "poreless skin", "CGI smoothness", "wax texture", "cosmetic sheen", "specular hotspot on forehead", "beauty retouch", "frequency separation", "legenda minúscula ou ilegível", "fundo branco puro", "fundo preto puro", "tipografia genérica (Inter, Montserrat, Playfair, DM Sans, Futura)"],
      "reference_standard": "Kinfolk + Everlane + Peter Lindbergh (pele) — editorial brasileiro contemporâneo"
    }
  },
  "negative_rules": [
    "Sem travessão (—) em nenhum texto — regra fixa do brand, nunca usar em título, legenda, headline, CTA ou qualquer campo de texto",
    "GARMENT FIDELITY LOCK: reproduzir a peça exatamente como nas fotos de referência, sem redesenhar ou reinterpretar, tecido fosco (sem brilho/lurex/metálico/cetim, exceto seda genuína)",
    "Nunca usar fundo branco puro nem preto puro — sempre paleta oficial Carol",
    "Legenda NUNCA pode renderizar em tamanho pequeno tipo rodapé — deve ser claramente maior e mais proeminente que o header e o footer",
    "Nunca misturar vocabulário proibido: premium, luxo, trends, must-have, fashionista, lacrou, empoderamento, alfaiataria"
  ]
}
```

---

## GRID-B — Salva Contraste ✅ APROVADO
**📸 Carregar 3 imagens de referência** (as 3 fotos verticais do grid, mesma peça/look em modelos ou ângulos distintos)

```json
{
  "template": "slides_centrais_carol",
  "peca": "peça-chave (definida pelas 3 fotos de referência carregadas)",
  "estrutura": "GRID",
  "versao": "GRID-B_salva_contraste_v2",
  "format": "1080x1350px, 4:5",
  "prompt": {
    "scene": {
      "description": "Slide central de carrossel de moda autoral brasileira, fundo sólido em tom Salva (#9db4a1), layout limpo e editorial com contraste suave entre fundo esverdeado e texto claro. No topo, header_padrao fixo: à esquerda 'CAROL STAGGEMEIER' (Nunito Sans Bold, 18px, caixa alta, letter-spacing 3px, cor rgba(229,222,211,0.6)), à direita 'MODA AUTORAL' (mesmo estilo), com linha separadora fina de 1px a 30% de opacidade logo abaixo. Centralizado no terço superior, título editorial em Halant Bold, tamanho 56px, cor Linho (#e5ded3), duas linhas centralizadas, com nome da peça/look (definido pelas fotos de referência). Abaixo do título, uma legenda explicativa em Nunito Sans Regular — GRANDE e claramente legível, tamanho 34px, cor Linho a 90% de opacidade, line-height 1.4, largura máxima 720px centralizada, 2 linhas de texto curto e editorial (nunca do tamanho de legenda pequena ou rodapé). Abaixo da legenda, grid de 3 fotos verticais em colunas iguais, separadas por gutter fino de 8px em tom Salva, cada foto mostrando a mesma peça de roupa (fidelidade exata ao(s) look(s) de referência) em enquadramento de corpo inteiro, luz natural suave e consistente entre as 3 colunas. Rodapé com '@carolstaggemeier' centralizado, Nunito Sans Regular 16px, cor Linho a 55% de opacidade.",
      "subject": "Peça de roupa (definida pelas fotos de referência carregadas pelo usuário) fotografada em 3 variações de look/modelo/ângulo",
      "setting": "Fundo sólido Salva (#9db4a1), estúdio ou locação neutra dependendo da referência de cada foto",
      "action": "static — grid editorial de apresentação de produto"
    },
    "style": {
      "primary": "editorial lifestyle, moda autoral brasileira, minimalismo escandinavo com toque orgânico",
      "rendering_quality": "hyperrealistic, alta definição",
      "surface_textures": "tecidos foscos, texturas naturais de algodão/linho/malha conforme referência",
      "lighting": "luz natural suave, difusa, consistente entre as 3 fotos do grid, sem sombras duras"
    },
    "technical": {
      "camera": { "focal_length": "50mm", "aperture": "f/4", "depth_of_field": "moderada — modelo nítido, fundo levemente suave", "angle": "eye level, corpo inteiro" },
      "resolution": "alta definição, qualidade editorial de revista",
      "rendering": "cores naturais, grão sutil, sem oversaturação",
      "physics_accuracy": "sombra e luz coerentes com ambiente de cada foto de referência"
    },
    "materials": {
      "skin": "pele com tom fiel à referência, poros visíveis na testa e maçãs do rosto, buço fino individual, imperfeições naturais, acabamento fosco — SEM base, SEM pó iluminador, SEM brilho cosmético, SEM suavização artificial, zero pós-processamento, pele natural e viva",
      "fabric": "trama visível do tecido, caimento realista, sem brilho artificial, fosco (exceto seda genuína se presente na referência)",
      "surfaces": "fundo Salva liso e uniforme, sem textura de parede"
    },
    "composition": {
      "perspective": "frontal, 3 colunas verticais iguais",
      "framing": "grid simétrico de 3 colunas com gutter fino",
      "subject_placement": "header no topo, título centralizado, legenda centralizada abaixo do título, grid de fotos ocupando o corpo do slide, footer centralizado na base",
      "safe_area": "952x1222px de área segura dentro do frame 1080x1350px — nenhum texto ou elemento encostando nas bordas",
      "ui_elements": [
        { "elemento": "header esquerda", "texto": "CAROL STAGGEMEIER", "fonte": "Nunito Sans Bold", "tamanho": "18px", "cor": "rgba(229,222,211,0.6)", "posicao": "topo esquerda" },
        { "elemento": "header direita", "texto": "MODA AUTORAL", "fonte": "Nunito Sans Regular", "tamanho": "18px", "cor": "rgba(229,222,211,0.6)", "posicao": "topo direita" },
        { "elemento": "linha separadora", "descricao": "1px, 30% opacidade, largura total da safe area", "posicao": "abaixo do header" },
        { "elemento": "título", "texto": "[definido pela referência/peça]", "fonte": "Halant Bold", "tamanho": "56px", "cor": "#e5ded3", "alinhamento": "centralizado", "posicao": "terço superior" },
        { "elemento": "legenda", "texto": "[definida pelo usuário — texto curto explicativo sobre a peça]", "fonte": "Nunito Sans Regular", "tamanho": "34px", "cor": "rgba(229,222,211,0.9)", "alinhamento": "centralizado", "line_height": "1.4", "largura_maxima": "720px", "posicao": "abaixo do título, ANTES do grid de fotos" },
        { "elemento": "grid de fotos", "descricao": "3 colunas verticais iguais, gutter 8px, fotos de corpo inteiro", "posicao": "corpo do slide" },
        { "elemento": "footer", "texto": "@carolstaggemeier", "fonte": "Nunito Sans Regular", "tamanho": "16px", "cor": "rgba(229,222,211,0.55)", "alinhamento": "centralizado", "posicao": "base" }
      ]
    },
    "quality": {
      "include": ["editorial", "minimalista", "moda autoral brasileira", "tipografia legível e proporcional", "luz natural", "pele realista", "fidelidade de tecido", "grid limpo e simétrico", "contraste suave verde/linho", "hierarquia tipográfica clara"],
      "avoid": ["plastic skin", "airbrushed skin", "poreless skin", "CGI smoothness", "wax texture", "cosmetic sheen", "specular hotspot on forehead", "beauty retouch", "frequency separation", "legenda minúscula ou ilegível", "fundo branco puro", "fundo preto puro", "tipografia genérica (Inter, Montserrat, Playfair, DM Sans, Futura)"],
      "reference_standard": "Kinfolk + Everlane + Peter Lindbergh (pele) — editorial brasileiro contemporâneo"
    }
  },
  "negative_rules": [
    "Sem travessão (—) em nenhum texto — regra fixa do brand, nunca usar em título, legenda, headline, CTA ou qualquer campo de texto",
    "GARMENT FIDELITY LOCK: reproduzir a peça exatamente como nas fotos de referência, sem redesenhar ou reinterpretar, tecido fosco (sem brilho/lurex/metálico/cetim, exceto seda genuína)",
    "Nunca usar fundo branco puro nem preto puro — sempre paleta oficial Carol",
    "Legenda NUNCA pode renderizar em tamanho pequeno tipo rodapé — deve ser claramente maior e mais proeminente que o header e o footer",
    "Nunca misturar vocabulário proibido: premium, luxo, trends, must-have, fashionista, lacrou, empoderamento, alfaiataria"
  ]
}
```

---

## GRID-C — Areia Quente Bloco ✅ APROVADO
**📸 Carregar 3 imagens de referência** (as 3 fotos verticais do grid, mesma peça/look em modelos ou ângulos distintos)

```json
{
  "template": "slides_centrais_carol",
  "peca": "peça-chave (definida pelas 3 fotos de referência carregadas)",
  "estrutura": "GRID",
  "versao": "GRID-C_areia_quente_bloco",
  "format": "1080x1350px, 4:5",
  "prompt": {
    "scene": {
      "description": "Slide central de carrossel de moda autoral brasileira, fundo sólido em tom Areia Quente (#c2b6a5), layout limpo e editorial com bloco de contraste em Café Terroso (#4c3529) atrás do título para reforçar hierarquia. No topo, header_padrao fixo: à esquerda 'CAROL STAGGEMEIER' (Nunito Sans Bold, 18px, caixa alta, letter-spacing 3px, cor rgba(39,61,41,0.5)), à direita 'MODA AUTORAL' (mesmo estilo), com linha separadora fina de 1px a 30% de opacidade logo abaixo. Centralizado no terço superior, um bloco retangular sólido em Café Terroso (#4c3529) com cantos levemente arredondados, contendo o título editorial em Halant Bold, tamanho 56px, cor Linho (#e5ded3), centralizado dentro do bloco. Abaixo do bloco, uma legenda explicativa em Nunito Sans Regular — GRANDE e claramente legível, tamanho 34px, cor Café Terroso (#4c3529) a 90% de opacidade, line-height 1.4, largura máxima 720px centralizada, 2 linhas de texto curto e editorial (nunca do tamanho de legenda pequena ou rodapé). Abaixo da legenda, grid de 3 fotos verticais em colunas iguais, separadas por gutter fino de 8px em tom Areia Quente, cada foto mostrando a mesma peça de roupa (fidelidade exata ao(s) look(s) de referência) em enquadramento de corpo inteiro, luz natural suave e consistente entre as 3 colunas. Rodapé com '@carolstaggemeier' centralizado, Nunito Sans Regular 16px, cor Café Terroso a 55% de opacidade.",
      "subject": "Peça de roupa (definida pelas fotos de referência carregadas pelo usuário) fotografada em 3 variações de look/modelo/ângulo",
      "setting": "Fundo sólido Areia Quente (#c2b6a5), estúdio ou locação neutra dependendo da referência de cada foto",
      "action": "static — grid editorial de apresentação de produto"
    },
    "style": {
      "primary": "editorial lifestyle, moda autoral brasileira, minimalismo escandinavo com toque orgânico",
      "rendering_quality": "hyperrealistic, alta definição",
      "surface_textures": "tecidos foscos, texturas naturais de algodão/linho/malha conforme referência",
      "lighting": "luz natural suave, difusa, consistente entre as 3 fotos do grid, sem sombras duras"
    },
    "technical": {
      "camera": { "focal_length": "50mm", "aperture": "f/4", "depth_of_field": "moderada — modelo nítido, fundo levemente suave", "angle": "eye level, corpo inteiro" },
      "resolution": "alta definição, qualidade editorial de revista",
      "rendering": "cores naturais, grão sutil, sem oversaturação",
      "physics_accuracy": "sombra e luz coerentes com ambiente de cada foto de referência"
    },
    "materials": {
      "skin": "pele com tom fiel à referência, poros visíveis na testa e maçãs do rosto, buço fino individual, imperfeições naturais, acabamento fosco — SEM base, SEM pó iluminador, SEM brilho cosmético, SEM suavização artificial, zero pós-processamento, pele natural e viva",
      "fabric": "trama visível do tecido, caimento realista, sem brilho artificial, fosco (exceto seda genuína se presente na referência)",
      "surfaces": "fundo Areia Quente liso e uniforme, bloco Café Terroso sólido e opaco atrás do título, sem textura de parede"
    },
    "composition": {
      "perspective": "frontal, 3 colunas verticais iguais",
      "framing": "grid simétrico de 3 colunas com gutter fino, bloco de contraste centralizado no topo",
      "subject_placement": "header no topo, bloco Café Terroso com título centralizado, legenda centralizada abaixo do bloco, grid de fotos ocupando o corpo do slide, footer centralizado na base",
      "safe_area": "952x1222px de área segura dentro do frame 1080x1350px — nenhum texto ou elemento encostando nas bordas",
      "ui_elements": [
        { "elemento": "header esquerda", "texto": "CAROL STAGGEMEIER", "fonte": "Nunito Sans Bold", "tamanho": "18px", "cor": "rgba(39,61,41,0.5)", "posicao": "topo esquerda" },
        { "elemento": "header direita", "texto": "MODA AUTORAL", "fonte": "Nunito Sans Regular", "tamanho": "18px", "cor": "rgba(39,61,41,0.5)", "posicao": "topo direita" },
        { "elemento": "linha separadora", "descricao": "1px, 30% opacidade, largura total da safe area", "posicao": "abaixo do header" },
        { "elemento": "bloco de contraste", "descricao": "retângulo sólido Café Terroso (#4c3529), cantos levemente arredondados, largura suficiente para acomodar o título com respiro interno", "posicao": "terço superior, atrás do título" },
        { "elemento": "título", "texto": "[definido pela referência/peça]", "fonte": "Halant Bold", "tamanho": "56px", "cor": "#e5ded3", "alinhamento": "centralizado", "posicao": "dentro do bloco de contraste" },
        { "elemento": "legenda", "texto": "[definida pelo usuário — texto curto explicativo sobre a peça]", "fonte": "Nunito Sans Regular", "tamanho": "34px", "cor": "rgba(76,53,41,0.9)", "alinhamento": "centralizado", "line_height": "1.4", "largura_maxima": "720px", "posicao": "abaixo do bloco de contraste, ANTES do grid de fotos", "observacao_critica": "legenda deve renderizar GRANDE — nunca no tamanho de um rodapé ou nota de rodapé" },
        { "elemento": "grid de fotos", "descricao": "3 colunas verticais iguais, gutter 8px, fotos de corpo inteiro", "posicao": "corpo do slide" },
        { "elemento": "footer", "texto": "@carolstaggemeier", "fonte": "Nunito Sans Regular", "tamanho": "16px", "cor": "rgba(76,53,41,0.55)", "alinhamento": "centralizado", "posicao": "base" }
      ]
    },
    "quality": {
      "include": ["editorial", "minimalista", "moda autoral brasileira", "tipografia legível e proporcional", "luz natural", "pele realista", "fidelidade de tecido", "grid limpo e simétrico", "contraste sólido areia/café", "hierarquia tipográfica clara", "bloco de destaque elegante"],
      "avoid": ["plastic skin", "airbrushed skin", "poreless skin", "CGI smoothness", "wax texture", "cosmetic sheen", "specular hotspot on forehead", "beauty retouch", "frequency separation", "legenda minúscula ou ilegível", "fundo branco puro", "fundo preto puro", "tipografia genérica (Inter, Montserrat, Playfair, DM Sans, Futura)", "travessão em qualquer campo de texto"],
      "reference_standard": "Kinfolk + Everlane + Peter Lindbergh (pele) — editorial brasileiro contemporâneo"
    }
  },
  "negative_rules": [
    "Sem travessão (—) em nenhum texto — regra fixa do brand, nunca usar em título, legenda, headline, CTA ou qualquer campo de texto",
    "GARMENT FIDELITY LOCK: reproduzir a peça exatamente como nas fotos de referência, sem redesenhar ou reinterpretar, tecido fosco (sem brilho/lurex/metálico/cetim, exceto seda genuína)",
    "Nunca usar fundo branco puro nem preto puro — sempre paleta oficial Carol",
    "Legenda NUNCA pode renderizar em tamanho pequeno tipo rodapé — deve ser claramente maior e mais proeminente que o header e o footer",
    "Nunca misturar vocabulário proibido: premium, luxo, trends, must-have, fashionista, lacrou, empoderamento, alfaiataria"
  ]
}
```

---

## HOOK-A — Café Terroso Gradiente ✅ APROVADO
**📸 Carregar 1 imagem de referência** (a foto full-bleed still portrait da modelo com a peça)

```json
{
  "template": "carrossel-carol",
  "peca": "slide_interno",
  "estrutura": "hook_quote_gradiente",
  "versao": "HOOK-A_cafe_terroso_gradiente",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "safe_area": "952x1222px (64px mínimo todos os lados)" },
  "prompt": {
    "scene": {
      "description": "Slide interno de carrossel de moda autoral brasileira, foto full-bleed lifestyle de mulher (definida pela foto de referência carregada pelo usuário) em ambiente interno, still portrait tipo selfie de espelho, luz ambiente natural de interior. No topo, header_padrao fixo: à esquerda 'CAROL STAGGEMEIER' (Nunito Sans Bold, 18px, caixa alta, letter-spacing 3px, cor rgba(229,222,211,0.6)), à direita 'MODA AUTORAL' (mesmo estilo), linha separadora fina 1px a 30% de opacidade logo abaixo. Overlay em gradiente escuro Café Terroso (#4c3529) subindo da base da imagem até aproximadamente 55-60% da altura do frame, escurecendo progressivamente para garantir legibilidade do texto sem esconder a peça/modelo. No terço inferior, sobre o gradiente: uma frase curta introdutória em Nunito Sans Regular, tamanho 30px, cor Linho (#e5ded3) a 90% de opacidade, alinhada à esquerda dentro da safe area. Logo abaixo, a frase principal em Halant Regular, tamanho 52px, cor Linho (#e5ded3), alinhada à esquerda, quebrando em até 2 linhas, com uma palavra-chave em Halant Bold com sublinhado (underline 2px, cor Salva #9db4a1 ou Linho conforme contraste). Rodapé com '@carolstaggemeier' centralizado, Nunito Sans Regular 16px, cor Linho a 55% de opacidade, próximo à base do frame.",
      "subject": "Mulher (definida pela foto de referência) em still portrait tipo selfie de espelho, roupa fiel à referência (fidelidade exata de peça e cor)",
      "setting": "Ambiente interno residencial, luz ambiente natural, decoração de fundo conforme referência",
      "action": "static — still portrait editorial"
    },
    "style": {
      "primary": "editorial lifestyle, moda autoral brasileira, still portrait natural",
      "rendering_quality": "hyperrealistic, alta definição",
      "surface_textures": "tecido fosco de malha/suede, textura de pele natural",
      "lighting": "luz ambiente natural de interior, suave, levemente quente"
    },
    "technical": {
      "camera": { "focal_length": "35mm", "aperture": "f/2.8", "depth_of_field": "moderada — sujeito nítido, fundo levemente suave", "angle": "eye level, corpo inteiro/three-quarter" },
      "resolution": "alta definição, qualidade editorial de revista",
      "rendering": "cores naturais, grão sutil, sem oversaturação",
      "physics_accuracy": "luz de interior coerente, sombras suaves"
    },
    "materials": {
      "skin": "pele com tom fiel à referência, poros visíveis na testa e maçãs do rosto, buço fino individual, imperfeições naturais, acabamento fosco — SEM base, SEM pó iluminador, SEM brilho cosmético, SEM suavização artificial, zero pós-processamento, pele natural e viva",
      "fabric": "trama visível do tecido, caimento realista, fosco, sem brilho artificial (exceto seda genuína se presente na referência)"
    },
    "composition": {
      "perspective": "frontal/three-quarter, sujeito centralizado ou levemente deslocado conforme referência",
      "framing": "full-bleed, foto ocupando 100% do frame, overlay de gradiente na base",
      "subject_placement": "sujeito na metade superior/central do frame, texto no terço inferior sobre o gradiente",
      "safe_area": "952x1222px de área segura dentro do frame 1080x1350px — texto nunca encostando nas bordas",
      "ui_elements": [
        { "elemento": "header esquerda", "texto": "CAROL STAGGEMEIER", "fonte": "Nunito Sans Bold", "tamanho": "18px", "cor": "rgba(229,222,211,0.6)", "posicao": "topo esquerda" },
        { "elemento": "header direita", "texto": "MODA AUTORAL", "fonte": "Nunito Sans Regular", "tamanho": "18px", "cor": "rgba(229,222,211,0.6)", "posicao": "topo direita" },
        { "elemento": "linha separadora", "descricao": "1px, 30% opacidade, largura total da safe area", "posicao": "abaixo do header" },
        { "elemento": "overlay gradiente", "descricao": "gradiente escuro Café Terroso (#4c3529) subindo da base até ~55-60% da altura do frame", "posicao": "terço inferior" },
        { "elemento": "frase curta", "texto": "[definida pelo usuário — frase introdutória curta]", "fonte": "Nunito Sans Regular", "tamanho": "30px", "cor": "rgba(229,222,211,0.9)", "alinhamento": "esquerda", "posicao": "acima da frase principal" },
        { "elemento": "frase principal", "texto": "[definida pelo usuário — frase de impacto com palavra-chave destacada]", "fonte": "Halant Regular, palavra-chave em Halant Bold sublinhado", "tamanho": "52px", "cor": "#e5ded3", "alinhamento": "esquerda", "line_height": "1.2", "posicao": "terço inferior, abaixo da frase curta" },
        { "elemento": "footer", "texto": "@carolstaggemeier", "fonte": "Nunito Sans Regular", "tamanho": "16px", "cor": "rgba(229,222,211,0.55)", "alinhamento": "centralizado", "posicao": "base" }
      ]
    },
    "quality": {
      "include": ["editorial", "moda autoral brasileira", "luz natural de interior", "pele realista", "fidelidade de tecido", "hierarquia tipográfica forte", "headline com presença visual", "still portrait autêntico"],
      "avoid": ["plastic skin", "airbrushed skin", "poreless skin", "CGI smoothness", "wax texture", "cosmetic sheen", "specular hotspot on forehead", "beauty retouch", "frequency separation", "texto pequeno ou discreto demais", "fundo branco puro", "fundo preto puro", "tipografia genérica (Inter, Montserrat, Playfair, DM Sans, Futura)"],
      "reference_standard": "Kinfolk + Everlane + Peter Lindbergh (pele) — editorial brasileiro contemporâneo"
    }
  },
  "negative_rules": [
    "Sem travessão (—) em nenhum texto — regra fixa do brand, nunca usar em título, legenda, headline, CTA ou qualquer campo de texto",
    "GARMENT FIDELITY LOCK: reproduzir a peça exatamente como na foto de referência, sem redesenhar ou reinterpretar, tecido fosco (sem brilho/lurex/metálico/cetim, exceto seda genuína)",
    "Nunca usar fundo branco puro nem preto puro para o overlay — sempre paleta oficial Carol",
    "Frase curta e frase principal precisam ter clara hierarquia de headline — nunca pequenas ou discretas",
    "Nunca misturar vocabulário proibido: premium, luxo, trends, must-have, fashionista, lacrou, empoderamento, alfaiataria"
  ]
}
```

---

## HOOK-B — Verde Floresta Gradiente ✅ APROVADO
**📸 Carregar 1 imagem de referência** (a foto full-bleed da modelo com a peça)

```json
{
  "template": "carrossel-carol",
  "peca": "slide_interno",
  "estrutura": "hook_quote_gradiente",
  "versao": "HOOK-B_verde_floresta_gradiente",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "safe_area": "952x1222px (64px mínimo todos os lados)" },
  "prompt": {
    "scene": {
      "description": "Slide interno de carrossel de moda autoral brasileira, foto full-bleed lifestyle de mulher (definida pela foto de referência carregada pelo usuário) em ambiente externo natural, luz de fim de tarde. No topo, header_padrao fixo: à esquerda 'CAROL STAGGEMEIER' (Nunito Sans Bold, 18px, caixa alta, letter-spacing 3px, cor rgba(229,222,211,0.6)), à direita 'MODA AUTORAL' (mesmo estilo), linha separadora fina 1px a 30% de opacidade logo abaixo. Overlay em gradiente escuro Verde Floresta (#273d29) subindo da base da imagem até aproximadamente 55% da altura do frame, escurecendo progressivamente para garantir legibilidade do texto. No terço inferior, sobre o gradiente: uma frase curta introdutória em Nunito Sans Regular, tamanho 30px, cor Linho (#e5ded3) a 90% de opacidade, alinhada à esquerda dentro da safe area. Logo abaixo, a frase principal em Halant Regular/Bold, tamanho 52px, cor Linho (#e5ded3), alinhada à esquerda, com uma palavra-chave em Halant Bold com sublinhado (underline 2px, cor Linho), quebrando em até 2 linhas conforme o texto. Rodapé com '@carolstaggemeier' centralizado, Nunito Sans Regular 16px, cor Linho a 55% de opacidade, próximo à base do frame.",
      "subject": "Mulher (definida pela foto de referência) em pose natural/still portrait, roupa fiel à referência (fidelidade exata de peça e cor)",
      "setting": "Ambiente externo natural, luz de fim de tarde/dourada, campo aberto ou área rústica conforme referência",
      "action": "static — still portrait editorial"
    },
    "style": {
      "primary": "editorial lifestyle, moda autoral brasileira, luz natural dourada",
      "rendering_quality": "hyperrealistic, alta definição",
      "surface_textures": "tecido fosco de malha/algodão, textura de pele natural",
      "lighting": "luz natural de fim de tarde, quente, direcional, suave nas sombras"
    },
    "technical": {
      "camera": { "focal_length": "50mm", "aperture": "f/2.8", "depth_of_field": "moderada-rasa — sujeito nítido, fundo levemente suave", "angle": "eye level, three-quarter" },
      "resolution": "alta definição, qualidade editorial de revista",
      "rendering": "cores naturais e quentes, grão sutil, sem oversaturação",
      "physics_accuracy": "luz de fim de tarde coerente com sombras longas e tom dourado"
    },
    "materials": {
      "skin": "pele com tom fiel à referência, poros visíveis na testa e maçãs do rosto, buço fino individual, sardas/imperfeições naturais, acabamento fosco — SEM base, SEM pó iluminador, SEM brilho cosmético, SEM suavização artificial, zero pós-processamento, pele natural e viva",
      "fabric": "trama visível do tecido, caimento realista, fosco, sem brilho artificial (exceto seda genuína se presente na referência)"
    },
    "composition": {
      "perspective": "frontal/three-quarter, sujeito ocupando o centro-direita do frame",
      "framing": "full-bleed, foto ocupando 100% do frame, overlay de gradiente na base",
      "subject_placement": "sujeito na metade superior/central do frame, texto no terço inferior sobre o gradiente",
      "safe_area": "952x1222px de área segura dentro do frame 1080x1350px — texto nunca encostando nas bordas",
      "ui_elements": [
        { "elemento": "header esquerda", "texto": "CAROL STAGGEMEIER", "fonte": "Nunito Sans Bold", "tamanho": "18px", "cor": "rgba(229,222,211,0.6)", "posicao": "topo esquerda" },
        { "elemento": "header direita", "texto": "MODA AUTORAL", "fonte": "Nunito Sans Regular", "tamanho": "18px", "cor": "rgba(229,222,211,0.6)", "posicao": "topo direita" },
        { "elemento": "linha separadora", "descricao": "1px, 30% opacidade, largura total da safe area", "posicao": "abaixo do header" },
        { "elemento": "overlay gradiente", "descricao": "gradiente escuro Verde Floresta (#273d29) subindo da base até ~55% da altura do frame", "posicao": "terço inferior" },
        { "elemento": "frase curta", "texto": "[definida pelo usuário — frase introdutória curta]", "fonte": "Nunito Sans Regular", "tamanho": "30px", "cor": "rgba(229,222,211,0.9)", "alinhamento": "esquerda", "posicao": "acima da frase principal" },
        { "elemento": "frase principal", "texto": "[definida pelo usuário — frase de impacto com palavra-chave destacada]", "fonte": "Halant Regular, palavra-chave em Halant Bold sublinhado", "tamanho": "52px", "cor": "#e5ded3", "alinhamento": "esquerda", "line_height": "1.2", "posicao": "terço inferior, abaixo da frase curta" },
        { "elemento": "footer", "texto": "@carolstaggemeier", "fonte": "Nunito Sans Regular", "tamanho": "16px", "cor": "rgba(229,222,211,0.55)", "alinhamento": "centralizado", "posicao": "base" }
      ]
    },
    "quality": {
      "include": ["editorial", "moda autoral brasileira", "luz dourada natural", "pele realista", "fidelidade de tecido", "hierarquia tipográfica forte", "headline com presença visual"],
      "avoid": ["plastic skin", "airbrushed skin", "poreless skin", "CGI smoothness", "wax texture", "cosmetic sheen", "specular hotspot on forehead", "beauty retouch", "frequency separation", "texto pequeno ou discreto demais", "fundo branco puro", "fundo preto puro", "tipografia genérica (Inter, Montserrat, Playfair, DM Sans, Futura)"],
      "reference_standard": "Kinfolk + Everlane + Peter Lindbergh (pele) — editorial brasileiro contemporâneo"
    }
  },
  "negative_rules": [
    "Sem travessão (—) em nenhum texto — regra fixa do brand, nunca usar em título, legenda, headline, CTA ou qualquer campo de texto",
    "GARMENT FIDELITY LOCK: reproduzir a peça exatamente como na foto de referência, sem redesenhar ou reinterpretar, tecido fosco (sem brilho/lurex/metálico/cetim, exceto seda genuína)",
    "Nunca usar fundo branco puro nem preto puro para o overlay — sempre paleta oficial Carol",
    "Frase curta e frase principal precisam ter clara hierarquia de headline — nunca pequenas ou discretas",
    "Nunca misturar vocabulário proibido: premium, luxo, trends, must-have, fashionista, lacrou, empoderamento, alfaiataria"
  ]
}
```

---

## HOOK-C — Cápsula Sólida ✅ APROVADO
**📸 Carregar 1 imagem de referência** (a foto full-bleed da modelo com a peça)

```json
{
  "template": "carrossel-carol",
  "peca": "slide_interno",
  "estrutura": "hook_quote_gradiente",
  "versao": "HOOK-C_capsula_solida",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "safe_area": "952x1222px (64px mínimo todos os lados)" },
  "prompt": {
    "scene": {
      "description": "Slide interno de carrossel de moda autoral brasileira, foto lifestyle de mulher (definida pela foto de referência carregada pelo usuário) em ambiente externo urbano/arquitetônico, luz natural diurna, ocupando aproximadamente os 70% superiores do frame. No topo, header_padrao fixo: à esquerda 'CAROL STAGGEMEIER' (Nunito Sans Bold, 18px, caixa alta, letter-spacing 3px, cor rgba(229,222,211,0.6)), à direita 'MODA AUTORAL' (mesmo estilo), linha separadora fina 1px a 30% de opacidade logo abaixo. Nos 30% inferiores do frame, um BLOCO SÓLIDO retangular (não gradiente) na cor Café Terroso (#4c3529), com corte reto/horizontal separando nitidamente a foto do bloco de texto — sem transição suave, um corte definido tipo 'cápsula' de cor sólida. Dentro do bloco sólido: uma frase curta introdutória centralizada em Nunito Sans Regular, tamanho 28px, cor Linho (#e5ded3) a 90% de opacidade. Abaixo, a frase principal centralizada em Halant Bold, tamanho 50px, cor Linho (#e5ded3), quebrando em até 2 linhas, com uma palavra-chave em Halant Bold na cor Salva (#9db4a1) para destaque cromático (sem sublinhado — o destaque aqui é só de cor). Rodapé com '@carolstaggemeier' centralizado, Nunito Sans Regular 16px, cor Linho a 55% de opacidade, próximo à base do bloco sólido.",
      "subject": "Mulher (definida pela foto de referência) em pose natural em ambiente externo, roupa fiel à referência (fidelidade exata de peça e cor)",
      "setting": "Ambiente externo urbano/arquitetônico (colunas, palmeiras, jardim conforme referência), luz natural diurna",
      "action": "static — retrato editorial lifestyle"
    },
    "style": {
      "primary": "editorial lifestyle, moda autoral brasileira, luz natural diurna",
      "rendering_quality": "hyperrealistic, alta definição",
      "surface_textures": "tecido fosco de moletom/algodão, textura de pele natural",
      "lighting": "luz natural diurna, direta e suave, sombras curtas"
    },
    "technical": {
      "camera": { "focal_length": "50mm", "aperture": "f/3.2", "depth_of_field": "moderada — sujeito nítido, fundo levemente suave", "angle": "eye level, three-quarter" },
      "resolution": "alta definição, qualidade editorial de revista",
      "rendering": "cores naturais, grão sutil, sem oversaturação",
      "physics_accuracy": "luz diurna coerente, sombras curtas e definidas"
    },
    "materials": {
      "skin": "pele com tom fiel à referência, poros visíveis na testa e maçãs do rosto, buço fino individual, imperfeições naturais, acabamento fosco — SEM base, SEM pó iluminador, SEM brilho cosmético, SEM suavização artificial, zero pós-processamento, pele natural e viva",
      "fabric": "trama visível do tecido, caimento realista, fosco, sem brilho artificial (exceto seda genuína se presente na referência)"
    },
    "composition": {
      "perspective": "frontal/three-quarter, sujeito ocupando o centro do frame na área de foto",
      "framing": "foto nos 70% superiores do frame, bloco sólido de cor nos 30% inferiores com corte reto (sem gradiente)",
      "subject_placement": "sujeito centralizado na área de foto; texto centralizado dentro do bloco sólido inferior",
      "safe_area": "952x1222px de área segura dentro do frame 1080x1350px — texto nunca encostando nas bordas",
      "ui_elements": [
        { "elemento": "header esquerda", "texto": "CAROL STAGGEMEIER", "fonte": "Nunito Sans Bold", "tamanho": "18px", "cor": "rgba(229,222,211,0.6)", "posicao": "topo esquerda" },
        { "elemento": "header direita", "texto": "MODA AUTORAL", "fonte": "Nunito Sans Regular", "tamanho": "18px", "cor": "rgba(229,222,211,0.6)", "posicao": "topo direita" },
        { "elemento": "linha separadora", "descricao": "1px, 30% opacidade, largura total da safe area", "posicao": "abaixo do header" },
        { "elemento": "bloco sólido", "descricao": "retângulo sólido Café Terroso (#4c3529) ocupando os 30% inferiores do frame, corte reto horizontal (sem gradiente/transição)", "posicao": "terço inferior" },
        { "elemento": "frase curta", "texto": "[definida pelo usuário — frase introdutória curta]", "fonte": "Nunito Sans Regular", "tamanho": "28px", "cor": "rgba(229,222,211,0.9)", "alinhamento": "centralizado", "posicao": "topo do bloco sólido" },
        { "elemento": "frase principal", "texto": "[definida pelo usuário — frase de impacto com palavra-chave destacada em cor]", "fonte": "Halant Bold, palavra-chave em cor Salva (#9db4a1)", "tamanho": "50px", "cor": "#e5ded3", "alinhamento": "centralizado", "line_height": "1.2", "posicao": "centro do bloco sólido, abaixo da frase curta" },
        { "elemento": "footer", "texto": "@carolstaggemeier", "fonte": "Nunito Sans Regular", "tamanho": "16px", "cor": "rgba(229,222,211,0.55)", "alinhamento": "centralizado", "posicao": "base do bloco sólido" }
      ]
    },
    "quality": {
      "include": ["editorial", "moda autoral brasileira", "luz natural diurna", "pele realista", "fidelidade de tecido", "bloco de cor sólido e definido", "hierarquia tipográfica forte", "destaque cromático na palavra-chave"],
      "avoid": ["plastic skin", "airbrushed skin", "poreless skin", "CGI smoothness", "wax texture", "cosmetic sheen", "specular hotspot on forehead", "beauty retouch", "frequency separation", "texto pequeno ou discreto demais", "gradiente no lugar do bloco sólido", "fundo branco puro", "fundo preto puro", "tipografia genérica (Inter, Montserrat, Playfair, DM Sans, Futura)"],
      "reference_standard": "Kinfolk + Everlane + Peter Lindbergh (pele) — editorial brasileiro contemporâneo"
    }
  },
  "negative_rules": [
    "Sem travessão (—) em nenhum texto — regra fixa do brand, nunca usar em título, legenda, headline, CTA ou qualquer campo de texto",
    "GARMENT FIDELITY LOCK: reproduzir a peça exatamente como na foto de referência, sem redesenhar ou reinterpretar, tecido fosco (sem brilho/lurex/metálico/cetim, exceto seda genuína)",
    "Bloco inferior sempre SÓLIDO com corte reto — nunca gradiente (diferença chave em relação a HOOK-A e HOOK-B)",
    "Nunca usar fundo branco puro nem preto puro no bloco — sempre paleta oficial Carol",
    "Frase curta e frase principal precisam ter clara hierarquia de headline — nunca pequenas ou discretas",
    "Nunca misturar vocabulário proibido: premium, luxo, trends, must-have, fashionista, lacrou, empoderamento, alfaiataria"
  ]
}
```

---

## CAPA LIFESTYLE — nota importante sobre footer

Diferente das estruturas GRID e HOOK QUOTE (slides internos, footer sempre "@carolstaggemeier"), a estrutura **CAPA LIFESTYLE** é usada como CAPA do carrossel — portanto segue a mesma convenção do pacote "Não Tenho Roupa" (`TEMPLATE-CABIDE-TEXTO-CAROL.md`): footer sempre **"arraste para ver →"**, nunca "@carolstaggemeier".

---

## CAPA-LS-A — Verde Floresta Vinheta ✅ APROVADO
**📸 Carregar 1 imagem de referência** (a foto full-bleed lifestyle da modelo com a peça)

```json
{
  "template": "carrossel-carol",
  "peca": "capa",
  "estrutura": "capa_lifestyle_headline_cta",
  "versao": "CAPA-LS-A_verde_floresta_vinheta",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "safe_area": "952x1222px (64px mínimo todos os lados)" },
  "prompt": {
    "scene": {
      "description": "Capa de carrossel de moda autoral brasileira, foto full-bleed lifestyle de mulher (definida pela foto de referência carregada pelo usuário) em still portrait tipo selfie de espelho, ambiente interno residencial. Vinheta escura em Verde Floresta (#273d29) aplicada sobre toda a imagem, mais intensa nas bordas e na metade inferior/esquerda, preservando a legibilidade do rosto/expressão da modelo no canto superior direito. No topo, header_padrao fixo: à esquerda 'CAROL STAGGEMEIER' (Nunito Sans Bold, 18px, caixa alta, letter-spacing 3px, cor rgba(229,222,211,0.6)), à direita 'MODA AUTORAL' (mesmo estilo), linha separadora fina 1px a 30% de opacidade logo abaixo. No terço médio/inferior esquerdo, headline grande em Halant Bold, tamanho 72px, cor Linho (#e5ded3), alinhada à esquerda, quebrando em até 3 linhas curtas (efeito de grande impacto tipográfico, cada palavra/frase curta em sua própria linha). Abaixo da headline, um parágrafo de legenda em Nunito Sans Regular, tamanho 28px, cor Linho a 85% de opacidade, alinhado à esquerda, até 3 linhas curtas. Abaixo da legenda, uma linha de CTA em Nunito Sans Bold caixa alta, tamanho 26px, cor Linho a 95% de opacidade, letter-spacing 1px. Na base do frame, footer com 'arraste para ver →' alinhado à esquerda (Nunito Sans Regular, 18px, opacidade baixa) e um ícone de seta '→' isolado no canto inferior direito (Nunito Sans Regular ou ícone linear, cor Linho, tamanho grande ~32px) indicando swipe.",
      "subject": "Mulher (definida pela foto de referência) em still portrait tipo selfie de espelho, roupa fiel à referência (fidelidade exata de peça e cor)",
      "setting": "Ambiente interno residencial, luz ambiente natural, decoração de fundo conforme referência",
      "action": "static — still portrait editorial de capa"
    },
    "style": {
      "primary": "editorial lifestyle, moda autoral brasileira, capa de carrossel com forte hierarquia tipográfica",
      "rendering_quality": "hyperrealistic, alta definição",
      "surface_textures": "tecido fosco de malha/suede, textura de pele natural",
      "lighting": "luz ambiente natural de interior, suave, levemente quente, com vinheta de pós-produção"
    },
    "technical": {
      "camera": { "focal_length": "35mm", "aperture": "f/2.8", "depth_of_field": "moderada — sujeito nítido, fundo levemente suave", "angle": "eye level, corpo inteiro/three-quarter" },
      "resolution": "alta definição, qualidade editorial de revista",
      "rendering": "vinheta escura progressiva, cores naturais, grão sutil, sem oversaturação",
      "physics_accuracy": "luz de interior coerente, sombras suaves, vinheta aplicada de forma fotográfica (não como bloco de cor plano)"
    },
    "materials": {
      "skin": "pele com tom fiel à referência, poros visíveis na testa e maçãs do rosto, buço fino individual, imperfeições naturais, acabamento fosco — SEM base, SEM pó iluminador, SEM brilho cosmético, SEM suavização artificial, zero pós-processamento, pele natural e viva",
      "fabric": "trama visível do tecido, caimento realista, fosco, sem brilho artificial (exceto seda genuína se presente na referência)"
    },
    "composition": {
      "perspective": "frontal/three-quarter, sujeito deslocado para o lado direito do frame",
      "framing": "full-bleed, foto ocupando 100% do frame, vinheta escura sobre toda a imagem",
      "subject_placement": "sujeito à direita/centro-superior, headline e texto ocupando o lado esquerdo do frame do meio até a base",
      "safe_area": "952x1222px de área segura dentro do frame 1080x1350px — texto nunca encostando nas bordas",
      "ui_elements": [
        { "elemento": "header esquerda", "texto": "CAROL STAGGEMEIER", "fonte": "Nunito Sans Bold", "tamanho": "18px", "cor": "rgba(229,222,211,0.6)", "posicao": "topo esquerda" },
        { "elemento": "header direita", "texto": "MODA AUTORAL", "fonte": "Nunito Sans Regular", "tamanho": "18px", "cor": "rgba(229,222,211,0.6)", "posicao": "topo direita" },
        { "elemento": "linha separadora", "descricao": "1px, 30% opacidade, largura total da safe area", "posicao": "abaixo do header" },
        { "elemento": "vinheta", "descricao": "vinheta escura Verde Floresta (#273d29) sobre toda a imagem, mais intensa nas bordas e metade inferior/esquerda", "posicao": "imagem inteira" },
        { "elemento": "headline", "texto": "[definida pelo usuário — frase de impacto, até 3 linhas curtas]", "fonte": "Halant Bold", "tamanho": "72px", "cor": "#e5ded3", "alinhamento": "esquerda", "line_height": "1.05", "posicao": "terço médio/inferior esquerdo", "observacao_critica": "headline principal da capa — deve dominar visualmente o frame" },
        { "elemento": "legenda", "texto": "[definida pelo usuário — parágrafo curto explicativo]", "fonte": "Nunito Sans Regular", "tamanho": "28px", "cor": "rgba(229,222,211,0.85)", "alinhamento": "esquerda", "line_height": "1.4", "posicao": "abaixo da headline" },
        { "elemento": "CTA bold", "texto": "[definida pelo usuário — CTA curto em caixa alta]", "fonte": "Nunito Sans Bold", "tamanho": "26px", "cor": "rgba(229,222,211,0.95)", "estilo": "caixa alta, letter-spacing 1px", "alinhamento": "esquerda", "posicao": "abaixo da legenda" },
        { "elemento": "footer", "texto": "arraste para ver →", "fonte": "Nunito Sans Regular", "tamanho": "18px", "cor": "rgba(229,222,211,0.5)", "alinhamento": "esquerda", "posicao": "base do frame" },
        { "elemento": "ícone seta", "descricao": "seta '→' isolada, tamanho ~32px, cor Linho", "posicao": "canto inferior direito" }
      ]
    },
    "quality": {
      "include": ["editorial", "moda autoral brasileira", "capa de alto impacto tipográfico", "pele realista", "fidelidade de tecido", "vinheta fotográfica natural", "hierarquia clara headline > legenda > CTA", "still portrait autêntico"],
      "avoid": ["plastic skin", "airbrushed skin", "poreless skin", "CGI smoothness", "wax texture", "cosmetic sheen", "specular hotspot on forehead", "beauty retouch", "frequency separation", "headline pequena ou discreta", "vinheta em bloco de cor plano (deve ser fotográfica/gradual)", "fundo branco puro", "fundo preto puro", "tipografia genérica (Inter, Montserrat, Playfair, DM Sans, Futura)"],
      "reference_standard": "Kinfolk + Everlane + Peter Lindbergh (pele) — editorial brasileiro contemporâneo"
    }
  },
  "negative_rules": [
    "Sem travessão (—) em nenhum texto — regra fixa do brand, nunca usar em título, legenda, headline, CTA ou qualquer campo de texto",
    "GARMENT FIDELITY LOCK: reproduzir a peça exatamente como na foto de referência, sem redesenhar ou reinterpretar, tecido fosco (sem brilho/lurex/metálico/cetim, exceto seda genuína)",
    "Nunca usar fundo branco puro nem preto puro na vinheta — sempre paleta oficial Carol",
    "Footer da capa é sempre 'arraste para ver →', nunca '@carolstaggemeier' (diferente dos slides internos GRID e HOOK)",
    "Headline precisa dominar visualmente o frame — nunca pequena ou discreta",
    "Nunca misturar vocabulário proibido: premium, luxo, trends, must-have, fashionista, lacrou, empoderamento, alfaiataria"
  ]
}
```

---

## CAPA-LS-C — Vinheta Sutil + Bloco de Texto Salva ✅ APROVADO
**📸 Carregar 1 imagem de referência** (a foto full-bleed lifestyle da modelo com a peça)

```json
{
  "template": "carrossel-carol",
  "peca": "capa",
  "estrutura": "capa_lifestyle_headline_cta",
  "versao": "CAPA-LS-C_vinheta_sutil_bloco_salva",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "safe_area": "952x1222px (64px mínimo todos os lados)" },
  "prompt": {
    "scene": {
      "description": "Capa de carrossel de moda autoral brasileira, foto full-bleed lifestyle de mulher (definida pela foto de referência carregada pelo usuário) em ambiente externo, luz de dia natural, vinheta MUITO SUTIL aplicada apenas nas bordas para preservar as cores vivas da foto original (céu azul, verde do gramado). No topo, header_padrao fixo: à esquerda 'CAROL STAGGEMEIER' (Nunito Sans Bold, 18px, caixa alta, letter-spacing 3px, cor rgba(39,61,41,0.5)), à direita 'MODA AUTORAL' (mesmo estilo), linha separadora fina 1px a 30% de opacidade logo abaixo. No terço superior esquerdo, um bloco de texto sólido em cor Salva (#9db4a1) com cantos levemente arredondados (radius ~16px), funcionando como cápsula de contraste sobre a foto — dentro dele, headline em Halant Bold, tamanho 46px, cor Café Terroso (#4c3529), 2 linhas, e abaixo uma legenda em Nunito Sans Regular, tamanho 26px, cor Café Terroso a 90% de opacidade, 2 linhas. Fora do bloco, abaixo dele e ainda sobre a foto, uma linha de CTA curta em Nunito Sans Bold, tamanho 28px, cor Verde Floresta (#273d29), com leve drop-shadow claro para legibilidade sobre a foto. Na base do frame, footer com 'arraste para ver →' alinhado à esquerda (Nunito Sans Regular, 18px, cor Linho, drop-shadow leve) e um ícone de seta '→' isolado no canto inferior direito (cor Café Terroso, tamanho grande ~32px, dentro de um pequeno círculo Areia Quente para contraste).",
      "subject": "Mulher (definida pela foto de referência) em pose sentada/reclinada, roupa fiel à referência (fidelidade exata de peça e cor)",
      "setting": "Ambiente externo natural, campo aberto, luz de dia clara e vívida",
      "action": "static — retrato editorial lifestyle de capa"
    },
    "style": {
      "primary": "editorial lifestyle, moda autoral brasileira, capa com bloco de texto sólido contrastante",
      "rendering_quality": "hyperrealistic, alta definição",
      "surface_textures": "tecido fosco de malha/algodão, textura de pele natural",
      "lighting": "luz natural de dia, viva e clara, vinheta apenas sutil nas bordas"
    },
    "technical": {
      "camera": { "focal_length": "50mm", "aperture": "f/3.2", "depth_of_field": "moderada — sujeito nítido, fundo levemente suave", "angle": "eye level, three-quarter" },
      "resolution": "alta definição, qualidade editorial de revista",
      "rendering": "cores vivas e naturais preservadas, vinheta mínima apenas nas bordas, sem escurecimento pesado da foto",
      "physics_accuracy": "luz de dia coerente, sombras curtas e definidas"
    },
    "materials": {
      "skin": "pele com tom fiel à referência, poros visíveis na testa e maçãs do rosto, buço fino individual, imperfeições naturais, acabamento fosco — SEM base, SEM pó iluminador, SEM brilho cosmético, SEM suavização artificial, zero pós-processamento, pele natural e viva",
      "fabric": "trama visível do tecido, caimento realista, fosco, sem brilho artificial (exceto seda genuína se presente na referência)"
    },
    "composition": {
      "perspective": "frontal/three-quarter, sujeito ocupando o centro-direita/base do frame",
      "framing": "full-bleed, foto ocupando 100% do frame, vinheta sutil apenas nas bordas",
      "subject_placement": "sujeito na metade inferior/direita do frame; bloco de texto sólido Salva no terço superior esquerdo; CTA logo abaixo do bloco, ainda sobre a foto",
      "safe_area": "952x1222px de área segura dentro do frame 1080x1350px — texto nunca encostando nas bordas",
      "ui_elements": [
        { "elemento": "header esquerda", "texto": "CAROL STAGGEMEIER", "fonte": "Nunito Sans Bold", "tamanho": "18px", "cor": "rgba(39,61,41,0.5)", "posicao": "topo esquerda" },
        { "elemento": "header direita", "texto": "MODA AUTORAL", "fonte": "Nunito Sans Regular", "tamanho": "18px", "cor": "rgba(39,61,41,0.5)", "posicao": "topo direita" },
        { "elemento": "linha separadora", "descricao": "1px, 30% opacidade, largura total da safe area", "posicao": "abaixo do header" },
        { "elemento": "bloco de texto Salva", "descricao": "bloco sólido cor Salva (#9db4a1), cantos arredondados ~16px, sobreposto à foto no terço superior esquerdo", "posicao": "terço superior esquerdo" },
        { "elemento": "headline (dentro do bloco)", "texto": "[definida pelo usuário — frase de impacto, 2 linhas]", "fonte": "Halant Bold", "tamanho": "46px", "cor": "#4c3529", "alinhamento": "esquerda", "posicao": "dentro do bloco Salva, parte superior" },
        { "elemento": "legenda (dentro do bloco)", "texto": "[definida pelo usuário — legenda curta explicativa]", "fonte": "Nunito Sans Regular", "tamanho": "26px", "cor": "rgba(76,53,41,0.9)", "alinhamento": "esquerda", "posicao": "dentro do bloco Salva, abaixo da headline" },
        { "elemento": "CTA", "texto": "[definida pelo usuário — CTA curto]", "fonte": "Nunito Sans Bold", "tamanho": "28px", "cor": "#273d29", "estilo": "drop-shadow claro leve para legibilidade sobre a foto", "alinhamento": "esquerda", "posicao": "abaixo do bloco Salva, ainda sobre a foto" },
        { "elemento": "footer", "texto": "arraste para ver →", "fonte": "Nunito Sans Regular", "tamanho": "18px", "cor": "#e5ded3", "estilo": "drop-shadow leve", "alinhamento": "esquerda", "posicao": "base do frame" },
        { "elemento": "ícone seta", "descricao": "seta '→' isolada dentro de círculo Areia Quente para contraste, cor Café Terroso, tamanho ~32px", "posicao": "canto inferior direito" }
      ]
    },
    "quality": {
      "include": ["editorial", "moda autoral brasileira", "cores vivas preservadas", "bloco de texto sólido contrastante", "pele realista", "fidelidade de tecido", "hierarquia clara headline > legenda > CTA", "vinheta sutil"],
      "avoid": ["plastic skin", "airbrushed skin", "poreless skin", "CGI smoothness", "wax texture", "cosmetic sheen", "specular hotspot on forehead", "beauty retouch", "frequency separation", "headline ou legenda pequena", "vinheta pesada escurecendo toda a foto", "fundo branco puro", "fundo preto puro", "tipografia genérica (Inter, Montserrat, Playfair, DM Sans, Futura)"],
      "reference_standard": "Kinfolk + Everlane + Peter Lindbergh (pele) — editorial brasileiro contemporâneo"
    }
  },
  "negative_rules": [
    "Sem travessão (—) em nenhum texto — regra fixa do brand, nunca usar em título, legenda, headline, CTA ou qualquer campo de texto",
    "GARMENT FIDELITY LOCK: reproduzir a peça exatamente como na foto de referência, sem redesenhar ou reinterpretar, tecido fosco (sem brilho/lurex/metálico/cetim, exceto seda genuína)",
    "Vinheta sempre SUTIL nesta variação — nunca escurecer a foto inteira (diferença chave em relação a CAPA-LS-A e CAPA-LS-B)",
    "Footer da capa é sempre 'arraste para ver →', nunca '@carolstaggemeier'",
    "Bloco de texto Salva precisa ter contraste suficiente para leitura — nunca transparente demais",
    "Nunca misturar vocabulário proibido: premium, luxo, trends, must-have, fashionista, lacrou, empoderamento, alfaiataria"
  ]
}
```

---

## CAPA-LS-B — Café Terroso Vinheta ✅ APROVADO
**📸 Carregar 1 imagem de referência** (a foto full-bleed lifestyle da modelo com a peça)

> ⚠️ Atenção ao usar: o exemplo testado usou o texto "4 looks prontos com uma peça só — moletom preto." — o travessão deste exemplo NÃO deve ser reproduzido. Substituir por vírgula, ponto ou reestruturar a frase (ex: "4 looks prontos com uma peça só: moletom preto.").

```json
{
  "template": "carrossel-carol",
  "peca": "capa",
  "estrutura": "capa_lifestyle_headline_cta",
  "versao": "CAPA-LS-B_cafe_terroso_vinheta_v2",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "safe_area": "952x1222px (64px mínimo todos os lados)" },
  "prompt": {
    "scene": {
      "description": "Capa de carrossel de moda autoral brasileira, foto full-bleed lifestyle de mulher (definida pela foto de referência carregada pelo usuário) em ambiente externo urbano/arquitetônico, luz quente de fim de tarde. Vinheta escura em Café Terroso (#4c3529) aplicada sobre toda a imagem, mais intensa nas bordas e na metade inferior/esquerda. No topo, header_padrao fixo: à esquerda 'CAROL STAGGEMEIER' (Nunito Sans Bold, 18px, caixa alta, letter-spacing 3px, cor rgba(229,222,211,0.6)), à direita 'MODA AUTORAL' (mesmo estilo), linha separadora fina 1px a 30% de opacidade logo abaixo. No terço superior/médio esquerdo, headline grande em Halant Bold, tamanho 62px, cor Linho (#e5ded3), alinhada à esquerda, podendo quebrar em várias linhas curtas conforme o texto (SEM usar travessão para unir frases — usar ponto final entre ideias). Abaixo da headline, um parágrafo de legenda em Nunito Sans Regular — GRANDE e claramente legível, tamanho 32px, cor Linho a 92% de opacidade, line-height 1.4, alinhado à esquerda, até 3 linhas curtas. Abaixo da legenda, uma linha de CTA bold em Nunito Sans Bold, tamanho 32px, cor Areia Quente (#c2b6a5), letter-spacing 0.5px. Na base do frame, footer com 'arraste para ver →' alinhado à esquerda (Nunito Sans Regular, 18px, opacidade baixa) e um ícone de seta '→' isolado no canto inferior direito (cor Linho, tamanho ~32px).",
      "subject": "Mulher (definida pela foto de referência) em pose three-quarter, roupa fiel à referência (fidelidade exata de peça e cor)",
      "setting": "Ambiente externo urbano/arquitetônico (colunas, palmeiras), luz quente de fim de tarde",
      "action": "static — retrato editorial de capa"
    },
    "style": {
      "primary": "editorial lifestyle, moda autoral brasileira, capa com forte hierarquia tipográfica",
      "rendering_quality": "hyperrealistic, alta definição",
      "surface_textures": "tecido fosco de moletom/algodão, textura de pele natural",
      "lighting": "luz quente de fim de tarde, direcional, com vinheta de pós-produção"
    },
    "technical": {
      "camera": { "focal_length": "35mm", "aperture": "f/2.8", "depth_of_field": "moderada — sujeito nítido, fundo levemente suave", "angle": "eye level, three-quarter" },
      "resolution": "alta definição, qualidade editorial de revista",
      "rendering": "vinheta escura progressiva, cores quentes naturais, grão sutil",
      "physics_accuracy": "luz de fim de tarde coerente, vinheta aplicada de forma fotográfica"
    },
    "materials": {
      "skin": "pele com tom fiel à referência, poros visíveis na testa e maçãs do rosto, buço fino individual, imperfeições naturais, acabamento fosco — SEM base, SEM pó iluminador, SEM brilho cosmético, SEM suavização artificial, zero pós-processamento, pele natural e viva",
      "fabric": "trama visível do tecido, caimento realista, fosco, sem brilho artificial (exceto seda genuína se presente na referência)"
    },
    "composition": {
      "perspective": "frontal/three-quarter, sujeito à direita/centro do frame",
      "framing": "full-bleed, foto ocupando 100% do frame, vinheta escura sobre toda a imagem",
      "subject_placement": "sujeito à direita, headline/legenda/CTA ocupando o lado esquerdo do frame do meio até a base",
      "safe_area": "952x1222px de área segura dentro do frame 1080x1350px — texto nunca encostando nas bordas",
      "ui_elements": [
        { "elemento": "header esquerda", "texto": "CAROL STAGGEMEIER", "fonte": "Nunito Sans Bold", "tamanho": "18px", "cor": "rgba(229,222,211,0.6)", "posicao": "topo esquerda" },
        { "elemento": "header direita", "texto": "MODA AUTORAL", "fonte": "Nunito Sans Regular", "tamanho": "18px", "cor": "rgba(229,222,211,0.6)", "posicao": "topo direita" },
        { "elemento": "linha separadora", "descricao": "1px, 30% opacidade, largura total da safe area", "posicao": "abaixo do header" },
        { "elemento": "vinheta", "descricao": "vinheta escura Café Terroso (#4c3529) sobre toda a imagem, mais intensa nas bordas e metade inferior/esquerda", "posicao": "imagem inteira" },
        { "elemento": "headline", "texto": "[definida pelo usuário — frase de impacto, SEM travessão]", "fonte": "Halant Bold", "tamanho": "62px", "cor": "#e5ded3", "alinhamento": "esquerda", "posicao": "terço superior/médio esquerdo" },
        { "elemento": "legenda", "texto": "[definida pelo usuário — parágrafo curto explicativo, SEM travessão]", "fonte": "Nunito Sans Regular", "tamanho": "32px", "cor": "rgba(229,222,211,0.92)", "alinhamento": "esquerda", "line_height": "1.4", "posicao": "abaixo da headline", "observacao_critica": "texto grande, com presença visual clara, nunca parecer legenda pequena de rodapé" },
        { "elemento": "CTA bold", "texto": "[definida pelo usuário — CTA curto, SEM travessão]", "fonte": "Nunito Sans Bold", "tamanho": "32px", "cor": "#c2b6a5", "alinhamento": "esquerda", "posicao": "abaixo da legenda", "observacao_critica": "mesmo peso visual da legenda" },
        { "elemento": "footer", "texto": "arraste para ver →", "fonte": "Nunito Sans Regular", "tamanho": "18px", "cor": "rgba(229,222,211,0.5)", "alinhamento": "esquerda", "posicao": "base do frame" },
        { "elemento": "ícone seta", "descricao": "seta '→' isolada, tamanho ~32px, cor Linho", "posicao": "canto inferior direito" }
      ]
    },
    "quality": {
      "include": ["editorial", "moda autoral brasileira", "capa de alto impacto tipográfico", "pele realista", "fidelidade de tecido", "vinheta fotográfica natural", "hierarquia clara headline > legenda > CTA", "legenda com presença visual forte"],
      "avoid": ["plastic skin", "airbrushed skin", "poreless skin", "CGI smoothness", "wax texture", "cosmetic sheen", "specular hotspot on forehead", "beauty retouch", "frequency separation", "legenda ou CTA pequenos", "vinheta em bloco de cor plano", "fundo branco puro", "fundo preto puro", "tipografia genérica (Inter, Montserrat, Playfair, DM Sans, Futura)", "travessão em qualquer campo de texto"],
      "reference_standard": "Kinfolk + Everlane + Peter Lindbergh (pele) — editorial brasileiro contemporâneo"
    }
  },
  "negative_rules": [
    "Sem travessão (—) em nenhum texto — regra fixa do brand, nunca usar em título, legenda, headline, CTA ou qualquer campo de texto",
    "GARMENT FIDELITY LOCK: reproduzir a peça exatamente como na foto de referência, sem redesenhar ou reinterpretar, tecido fosco (sem brilho/lurex/metálico/cetim, exceto seda genuína)",
    "Legenda e CTA NUNCA podem renderizar pequenos — precisam ter clara presença de subtítulo/CTA",
    "Footer da capa é sempre 'arraste para ver →', nunca '@carolstaggemeier'",
    "Nunca misturar vocabulário proibido: premium, luxo, trends, must-have, fashionista, lacrou, empoderamento, alfaiataria"
  ]
}
```

---

## Status final deste template

- [x] GRID-A "Linho Clean": aprovada e fechada
- [x] GRID-B "Salva Contraste": aprovada e fechada
- [x] GRID-C "Areia Quente Bloco": aprovada e fechada
- [x] HOOK-A "Café Terroso Gradiente": aprovada e fechada
- [x] HOOK-B "Verde Floresta Gradiente": aprovada e fechada
- [x] HOOK-C "Cápsula Sólida": aprovada e fechada
- [x] CAPA-LS-A "Verde Floresta Vinheta": aprovada e fechada
- [x] CAPA-LS-B "Café Terroso Vinheta": aprovada e fechada (v2, fonte de legenda/CTA aumentada)
- [x] CAPA-LS-C "Vinheta Sutil + Bloco de Texto Salva": aprovada e fechada
- [x] Regra global "sem travessão (—)" aplicada em todas as 9 variações
- [x] Guia de escolha consolidado com status "fechado" em todas as 9 variações
- [ ] Pendente (fora deste template): avaliar com a Carol se este pacote ("Peças-Chave") deve ser combinado com o pacote "Não Tenho Roupa" (`TEMPLATE-CABIDE-TEXTO-CAROL.md`) em um carrossel único ou usado separadamente
