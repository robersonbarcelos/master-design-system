# Prompt Templates — Cabide + Texto Editorial (Carrossel "Não Tenho Roupa")
**Cliente:** Carol Staggemeier
**Formato fixo:** 1080x1350px · 4:5 Instagram Feed
**Criado em:** 2026-07-16
**Status:** Template FECHADO — estrutura própria, separada dos demais templates de capa/produto da Carol. Segue paleta, tipografia e header/footer padrão da marca.

---

## Como usar (GATE — responder antes de gerar)

Este template só deve ser usado depois de confirmar duas respostas com quem está pedindo a peça:

```
1. QUAL TEXTO VAI?
   → copy do hook principal (ex: "quando bater o 'não tenho roupa' / este
     carrossel vai salvar seu look de trabalho em menos de 1 minuto")
   → se não for informado, perguntar antes de gerar. Nunca assumir copy.

2. QUAL DAS VARIAÇÕES DE CAPA?
   → escolher UM dos 3 estilos aprovados abaixo (CAPA-A, CAPA-B ou CAPA-C)
   → se não for informado, perguntar antes de gerar. Nunca assumir estilo.

3. Copie o JSON do estilo escolhido
4. Localize ═══ GARMENT DESCRIPTION ═══ (dentro de scene.description)
5. Anexe a foto real da peça no cabide — a peça deve ser reproduzida
   EXATAMENTE como na foto (GARMENT FIDELITY LOCK)
6. Substitua o texto de "quando bater o..." e a citação principal pelo
   texto confirmado no passo 1
7. Cole no gerador junto com a foto da peça
```

> Mesma lógica de gate usada no `TEMPLATE-COLAGEM-POSES-CAROL.md`: nunca gerar a peça final sem antes confirmar copy + variação escolhida.

---

## Guia de escolha — estilos de capa aprovados

| Estilo | Nome | Fundo | Zoom na peça | Quando usar |
|---|---|---|---|---|
| **CAPA-A** | Fade Monocromático | Linho claro, parede natural com sombra tonal (sem cor de marca aplicada) | Padrão — 65-75% da peça visível, cortada pelas bordas | Quando quiser uma capa mais clara/luminosa, fiel à foto original da peça, sem "pintura" de cor por cima |
| **CAPA-B** | Grading Verde Floresta — Zoom Extremo | Escuro, grading pesado em toda a imagem (Verde Floresta) | Extremo — só cabide + ombros/colarinho (40-50% visível) | Quando quiser impacto visual forte, mais abstrato, com foco no detalhe do cabide |
| **CAPA-C** | Grading Verde Floresta — Subtítulo XL | Escuro, grading pesado em toda a imagem (Verde Floresta) | Padrão — 65-75% da peça visível, cortada pelas bordas | Estilo mais equilibrado — mesmo grading do CAPA-B mas com crop tradicional e subtítulo em destaque máximo de legibilidade |

---

## Regras fixas em todos os estilos

- **Formato:** 1080x1350px · 4:5 · Instagram Feed
- **Fidelidade da peça:** GARMENT FIDELITY LOCK — reprodução exata da referência anexada, sem reinterpretação, sem redesign
- **Tecido:** MATTE obrigatório — zero shimmer, zero lurex, zero brilho, zero metálico (exceto seda genuína)
- **Header padrão (obrigatório, nunca trocar por @handle):**
  "CAROL STAGGEMEIER" (Nunito Sans Bold, 18px, all caps, letter-spacing 3px, esquerda) + "MODA AUTORAL" (Nunito Sans Regular, 18px, all caps, letter-spacing 3px, direita) + linha separadora fina (1px, opacidade 30%) abaixo
  - Cor em fundo escuro: `rgba(229,222,211,0.55)`
  - Cor em fundo claro: `rgba(39,61,41,0.45)`
- **Footer da capa:** "arraste para ver →" (Nunito Sans Regular, 18px, opacidade baixa, centralizado) — NUNCA usar "@carolstaggemeier" na capa (isso é footer de slide/CTA)
- **Texto sem caixa/scrim:** tipografia aplicada direto sobre a imagem (com apoio de grading ou sombra tonal), nunca dentro de caixa/cápsula sólida de fundo
- **Subtítulo sempre grande:** mínimo 34-38px, Nunito Sans Bold, alta opacidade — é o elemento de leitura principal do slide, nunca discreto
- **Peça cortada pelas bordas:** nunca mostrar a peça inteira contida no frame — sempre cortada por cima/baixo/lados conforme o crop do estilo escolhido
- **Sem travessão (—)** em nenhum texto
- **Skin Realism Standard** aplicável apenas se houver modelo humano nas próximas peças deste carrossel (slides/CTA) — não se aplica à capa, que é still-life de produto

---

## CAPA-A — Fade Monocromático · Fundo Claro

```json
{
  "template": "carrossel-carol",
  "peca": "capa",
  "estrutura": "still_life_hook_pergunta",
  "versao": "CAPA-A_fade_monocromatico_parede",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "safe_area": "952x1222px (64px mínimo todos os lados)" },
  "prompt": {
    "scene": {
      "description": "Still-life em close fechado da peça (═══ GARMENT DESCRIPTION — anexar foto real e descrever aqui: fabric type, color, silhouette, neckline, sleeves, seams, hem, closures ═══) pendurada em cabide, cortada pelas bordas do frame (65-75% superior visível). Fundo é a parede rebocada clara original (tom Linho/areia natural da própria foto), SEM introdução de nenhuma cor de marca (nada de Café Terroso ou Verde Floresta aplicado por cima). No terço inferior, onde o texto pousa, aplica-se um escurecimento MONOCROMÁTICO — a mesma cor da parede, apenas com a luminosidade reduzida progressivamente (como uma sombra natural se projetando, não uma cor estranha sobreposta). É essencial que a transição pareça fotográfica: sombra real de vinheta na mesma temperatura de cor da parede, nunca uma mistura de duas cores diferentes que gere uma faixa amarronzada/acinzentada esquisita. Pensar como se a luz do ambiente simplesmente diminuísse naquela área, mantendo o mesmo matiz. ═══ GARMENT FIDELITY LOCK ═══ Reproduzir a peça exatamente como na foto anexada, sem reinterpretação.",
      "subject": "peça de roupa real (fornecida em anexo), cabide visível no topo, peça cortada pelas bordas do frame",
      "setting": "still-life de estúdio claro, parede rebocada natural, escurecimento tonal (não cromático) apenas na zona de texto",
      "action": "estático — still-life em close"
    },
    "style": { "primary": "editorial commercial still-life claro e fotográfico, campanha de moda close-up com sombra natural localizada", "rendering_quality": "hyperrealistic, high-resolution", "surface_textures": "parede rebocada com textura visível mesmo na área mais escura", "lighting": "luz lateral suave e aberta no topo; luz decrescendo naturalmente (sem virar cor) na base do frame" },
    "technical": { "camera": { "focal_length": "100mm crop fechado", "aperture": "f/3.2", "depth_of_field": "moderate-shallow", "angle": "eye level, close extremo" }, "resolution": "ultra high definition", "rendering": "escurecimento por REDUÇÃO DE LUMINOSIDADE (curva tonal), não por sobreposição de cor — mesmo matiz da parede do início ao fim do degradê, apenas mais escuro na base" },
    "materials": { "fabric": "GARMENT FIDELITY LOCK: reproduzir a peça EXATAMENTE como na foto anexada — corte, cor, estampa, transparência e trama fiéis. MATTE obrigatório — zero shimmer, zero lurex, zero brilho." },
    "composition": {
      "perspective": "frontal, câmera próxima, crop fechado",
      "framing": "peça cortada pelas bordas do frame — 65-75% superior visível",
      "subject_placement": "cabide próximo ao topo sobre fundo claro; texto no terço inferior sobre a área com sombra monocromática (mesmo tom da parede, mais escuro)",
      "safe_area": "952x1222px safe zone dentro do frame 1080x1350px",
      "ui_elements": [
        { "text": "CAROL STAGGEMEIER", "font": "Nunito Sans Bold", "size": "18px", "style": "all caps, letter-spacing 3px", "color": "rgba(39,61,41,0.45)", "position": "header, esquerda (cor escura pois fundo é claro)" },
        { "text": "MODA AUTORAL", "font": "Nunito Sans Regular", "size": "18px", "style": "all caps, letter-spacing 3px", "color": "rgba(39,61,41,0.45)", "position": "header, direita" },
        { "type": "separator line", "thickness": "1px", "opacity": 0.3, "color": "#4c3529", "position": "abaixo do header" },
        { "text": "[LINHA DE ABERTURA — confirmar copy antes de gerar]", "font": "Halant Regular", "size": "42px", "color": "rgba(229,222,211,0.9)", "position": "acima da citação principal, já dentro da zona de sombra monocromática" },
        { "text": "[CITAÇÃO PRINCIPAL — confirmar copy antes de gerar]", "font": "Halant Bold", "size": "80px", "color": "#e5ded3", "position": "citação principal, aplicada sobre a sombra monocromática da parede, SEM caixa de fundo" },
        { "text": "[SUBTÍTULO — confirmar copy antes de gerar]", "font": "Nunito Sans Bold", "size": "36px", "color": "#e5ded3 (opacidade 0.95)", "position": "abaixo da citação, sobre a base da sombra onde a luminosidade é mais baixa (maior contraste), drop-shadow leve" },
        { "text": "arraste para ver →", "font": "Nunito Sans Regular", "size": "18px", "color": "rgba(229,222,211,0.5)", "position": "rodapé, inferior centralizado" }
      ]
    },
    "quality": {
      "include": ["fade monocromático — mesmo matiz da parede, apenas mais escuro", "transição fotográfica natural, sem mistura de cores", "fundo geral claro e autêntico", "contraste suficiente para leitura do texto claro", "text applied directly on shadow, no solid box", "tight campaign crop", "brand header padrao em versão escura para fundo claro", "subtítulo grande e altamente legível"],
      "avoid": ["mistura de duas cores diferentes gerando faixa amarronzada/acinzentada estranha", "gradiente que muda de matiz (hue shift)", "cor de marca aplicada como camada sobre a parede", "transição com borda dura", "subtítulo pequeno", "peça inteira visível", "shimmer ou brilho no tecido"],
      "reference_standard": "still-life de campanha claro com sombra de vinheta fotográfica real, mesma temperatura de cor do ambiente, sem filtro de cor sobreposto"
    }
  },
  "negative_rules": ["sem travessao (—)", "escurecimento sempre no mesmo matiz da parede, nunca introduzindo cor de marca diferente", "peça cortada pelas bordas, nunca inteira", "header em versão escura (compatível com fundo claro)", "subtítulo sempre grande e legível", "footer da capa é sempre 'arraste para ver →', nunca @handle"]
}
```

---

## CAPA-B — Grading Verde Floresta · Zoom Extremo

```json
{
  "template": "carrossel-carol",
  "peca": "capa",
  "estrutura": "still_life_hook_pergunta",
  "versao": "CAPA-B_verde_floresta_zoom_extremo",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "safe_area": "952x1222px (64px mínimo todos os lados)" },
  "prompt": {
    "scene": {
      "description": "Still-life em close EXTREMO da peça (═══ GARMENT DESCRIPTION — anexar foto real e descrever aqui: fabric type, color, silhouette, neckline, sleeves, seams, hem, closures ═══) pendurada em cabide. Enquadramento muito mais fechado que um crop de campanha comum: o cabide e o gancho preenchem quase toda a largura do frame, e apenas a região de ombros/colarinho/início do busto da peça aparece — cerca de 40-50% visível, o restante da peça sai do frame na parte inferior. Grading de cor aplicado em TODA a imagem — sombras aprofundadas, meio-tom puxado para Verde Floresta #273d29, leve vinheta. Tipografia aplicada diretamente sobre a área escurecida, SEM caixa de fundo. ═══ GARMENT FIDELITY LOCK ═══ Reproduzir a peça exatamente como na foto anexada, sem reinterpretação, mesmo em close extremo.",
      "subject": "peça de roupa real (fornecida em anexo), cabide/gancho em destaque máximo, apenas ombros e colarinho da peça visíveis",
      "setting": "still-life de estúdio, crop extremo tipo still-life editorial, grading de cor aplicado à imagem inteira",
      "action": "estático — still-life em close extremo"
    },
    "style": { "primary": "editorial commercial still-life com color grading pesado, campanha de moda extreme close-up", "rendering_quality": "hyperrealistic, high-resolution", "surface_textures": "parede rebocada, tecido com trama visível em alta definição pelo zoom", "lighting": "luz lateral quente original + grading de pós-produção aprofundando sombras" },
    "technical": { "camera": { "focal_length": "135mm (crop extremo)", "aperture": "f/2.8", "depth_of_field": "shallow, foco no gancho e ombros da peça", "angle": "eye level, extreme close-up" }, "resolution": "ultra high definition", "rendering": "color grading cinematográfico — sombras profundas, meio-tom na paleta da marca, leve vinheta, contraste aumentado na zona de texto" },
    "materials": { "fabric": "GARMENT FIDELITY LOCK: reproduzir a peça EXATAMENTE como na foto anexada — corte, cor, estampa, transparência e trama fiéis, mesmo em close extremo. MATTE obrigatório — zero shimmer, zero lurex, zero brilho." },
    "composition": {
      "perspective": "frontal, câmera muito próxima, crop extremo",
      "framing": "cabide/gancho preenchendo quase toda a largura superior do frame; apenas 40-50% da peça (ombros/colarinho) visível, restante sai do frame",
      "subject_placement": "gancho e ombros no terço superior, texto aplicado direto sobre a zona escurecida no terço inferior (área maior de fundo/parede disponível para o texto por conta do zoom na peça)",
      "safe_area": "952x1222px safe zone dentro do frame 1080x1350px",
      "ui_elements": [
        { "text": "CAROL STAGGEMEIER", "font": "Nunito Sans Bold", "size": "18px", "style": "all caps, letter-spacing 3px", "color": "rgba(229,222,211,0.55)", "position": "header, esquerda" },
        { "text": "MODA AUTORAL", "font": "Nunito Sans Regular", "size": "18px", "style": "all caps, letter-spacing 3px", "color": "rgba(229,222,211,0.55)", "position": "header, direita" },
        { "type": "separator line", "thickness": "1px", "opacity": 0.3, "color": "#e5ded3", "position": "abaixo do header" },
        { "text": "[LINHA DE ABERTURA — confirmar copy antes de gerar]", "font": "Halant Regular", "size": "42px", "color": "rgba(229,222,211,0.85)", "position": "acima da citação principal, terço inferior" },
        { "text": "[CITAÇÃO PRINCIPAL — confirmar copy antes de gerar]", "font": "Halant Bold", "size": "80px", "color": "#e5ded3", "position": "citação principal, aplicada direto sobre a área escurecida, SEM caixa de fundo" },
        { "text": "[SUBTÍTULO — confirmar copy antes de gerar]", "font": "Nunito Sans Bold", "size": "36px", "color": "#e5ded3 (opacidade 0.95)", "position": "abaixo da citação, drop-shadow reforçado, texto grande e legível" },
        { "text": "arraste para ver →", "font": "Nunito Sans Regular", "size": "18px", "color": "rgba(229,222,211,0.45)", "position": "rodapé, inferior centralizado" }
      ]
    },
    "quality": {
      "include": ["zoom extremo no cabide e ombros da peça", "heavy color grading for text contrast", "text applied directly on image, no solid box", "garment mostly out of frame, only shoulder/collar area visible", "brand header padrao", "subtítulo grande e altamente legível"],
      "avoid": ["peça inteira visível", "enquadramento aberto demais", "solid background capsule behind text", "flat ungraded image", "plastic fabric sheen", "subtítulo pequeno"],
      "reference_standard": "still-life de campanha com crop extremo no detalhe do cabide/ombro, grading pesado, tipografia pura sobreposta"
    }
  },
  "negative_rules": ["sem travessao (—)", "texto aplicado direto na imagem via grading, NUNCA em caixa solida de fundo", "peça cortada pelas bordas em zoom extremo, mostrando apenas ombros/colarinho", "header sempre padrao Carol", "footer da capa é sempre 'arraste para ver →', nunca @handle"]
}
```

---

## CAPA-C — Grading Verde Floresta · Subtítulo XL

```json
{
  "template": "carrossel-carol",
  "peca": "capa",
  "estrutura": "still_life_hook_pergunta",
  "versao": "CAPA-C_verde_floresta_subtitulo_xl",
  "format": { "aspect_ratio": "4:5", "resolution": "1080x1350px", "safe_area": "952x1222px (64px mínimo todos os lados)" },
  "prompt": {
    "scene": {
      "description": "Still-life em close fechado da peça (═══ GARMENT DESCRIPTION — anexar foto real e descrever aqui: fabric type, color, silhouette, neckline, sleeves, seams, hem, closures ═══) pendurada em cabide, cortada pelas bordas do frame (65-75% superior visível). Grading de cor aplicado em TODA a imagem — sombras aprofundadas e levemente dessaturadas, meio-tom puxado para Verde Floresta #273d29, leve vinheta nas bordas inferiores. Tipografia aplicada diretamente sobre a área escurecida, SEM caixa de fundo, com drop-shadow sutil para legibilidade. ATENÇÃO CRÍTICA: o subtítulo (segunda linha de texto, abaixo da citação principal) deve ser GRANDE e MUITO LEGÍVEL — tamanho mínimo 34px, ocupando visualmente uma faixa proporcional significativa da largura do frame, nunca um texto fino/discreto. Priorizar legibilidade do subtítulo acima de qualquer outro elemento tipográfico da peça. ═══ GARMENT FIDELITY LOCK ═══ Reproduzir a peça exatamente como na foto anexada, sem reinterpretação.",
      "subject": "peça de roupa real (fornecida em anexo), cabide visível no topo, peça cortada pelas bordas do frame",
      "setting": "still-life de estúdio, crop fechado tipo campanha, grading de cor aplicado à imagem inteira",
      "action": "estático — still-life em close"
    },
    "style": { "primary": "editorial commercial still-life com color grading pesado, campanha de moda close-up", "rendering_quality": "hyperrealistic, high-resolution", "surface_textures": "parede rebocada, tecido com trama visível", "lighting": "luz lateral quente original + grading de pós-produção aprofundando sombras" },
    "technical": { "camera": { "focal_length": "100mm crop fechado", "aperture": "f/3.2", "depth_of_field": "moderate-shallow", "angle": "eye level, close extremo" }, "resolution": "ultra high definition", "rendering": "color grading cinematográfico — sombras profundas, meio-tom na paleta da marca, leve vinheta, contraste aumentado na zona de texto" },
    "materials": { "fabric": "GARMENT FIDELITY LOCK: reproduzir a peça EXATAMENTE como na foto anexada — corte, cor, estampa, transparência e trama fiéis. MATTE obrigatório — zero shimmer, zero lurex, zero brilho." },
    "composition": {
      "perspective": "frontal, câmera próxima, crop fechado",
      "framing": "peça cortada pelas bordas do frame — 65-75% superior visível",
      "subject_placement": "cabide próximo ao topo, texto aplicado direto sobre a zona escurecida no terço inferior",
      "safe_area": "952x1222px safe zone dentro do frame 1080x1350px",
      "ui_elements": [
        { "text": "CAROL STAGGEMEIER", "font": "Nunito Sans Bold", "size": "18px", "style": "all caps, letter-spacing 3px", "color": "rgba(229,222,211,0.55)", "position": "header, esquerda" },
        { "text": "MODA AUTORAL", "font": "Nunito Sans Regular", "size": "18px", "style": "all caps, letter-spacing 3px", "color": "rgba(229,222,211,0.55)", "position": "header, direita" },
        { "type": "separator line", "thickness": "1px", "opacity": 0.3, "color": "#e5ded3", "position": "abaixo do header" },
        { "text": "[LINHA DE ABERTURA — confirmar copy antes de gerar]", "font": "Halant Regular", "size": "42px", "color": "rgba(229,222,211,0.85)", "position": "acima da citação principal, terço inferior" },
        { "text": "[CITAÇÃO PRINCIPAL — confirmar copy antes de gerar]", "font": "Halant Bold", "size": "80px", "color": "#e5ded3", "position": "citação principal, aplicada direto sobre a área escurecida, SEM caixa de fundo" },
        { "text": "[SUBTÍTULO — confirmar copy antes de gerar]", "font": "Nunito Sans Bold (peso aumentado para reforçar legibilidade)", "size": "38px", "color": "#e5ded3 (opacidade 0.95, quase sólida)", "position": "abaixo da citação, aplicação direta sobre a foto com drop-shadow reforçado (offset 2px, blur 6px, opacidade 0.6), texto ocupando até 90% da safe area horizontal, quebrado em 2-3 linhas curtas para aumentar a escala de cada linha" },
        { "text": "arraste para ver →", "font": "Nunito Sans Regular", "size": "18px", "color": "rgba(229,222,211,0.45)", "position": "rodapé, inferior centralizado" }
      ]
    },
    "quality": {
      "include": ["subtítulo grande e altamente legível", "heavy color grading for text contrast", "text applied directly on image with reinforced drop-shadow", "no solid text box", "tight campaign crop", "garment bleeding off frame edges", "brand header padrao"],
      "avoid": ["subtítulo pequeno ou fino", "texto discreto demais", "solid background capsule behind text", "flat ungraded image", "entire garment visible top to bottom", "plastic fabric sheen"],
      "reference_standard": "still-life de campanha com grading pesado e tipografia grande e pura sobreposta, referência editorial fashion close-crop"
    }
  },
  "negative_rules": ["sem travessao (—)", "texto aplicado direto na imagem via grading, NUNCA em caixa solida de fundo", "peça cortada pelas bordas, nunca inteira", "header sempre padrao Carol", "subtítulo NUNCA pequeno — é o elemento de leitura principal do slide", "footer da capa é sempre 'arraste para ver →', nunca @handle"]
}
```

---

## Próximos passos deste template (ainda não fechados)

- [ ] Slide Hook (V2 Café Terroso / V3 cápsula sólida) — a definir/testar
- [ ] Slide Grid (V1 Linho / V2 Areia Quente) — a definir/testar
- [ ] CTA (V1 Verde Floresta / V2 Café Terroso) — copy correta "salva esse post pra nunca mais sofrer com o 'não tenho roupa'... compartilha com uma amiga que vive esse dilema!" ainda precisa ser aplicada e testada
- [ ] Depois que slides + CTA forem testados e aprovados, consolidar guia de escolha final igual ao `TEMPLATE-CABIDE-CAROL.md` (tabela com todos os estilos do carrossel completo)
