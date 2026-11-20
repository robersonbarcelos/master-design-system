# Perfil de vídeo · BNB CONNECT (Reels com a Glauce)
Aprovado em 08/10/2026 no Reels 01 (versão final REELS01_v15, 2:35). Inspiração: Reels da Tay (Vinci): DdBhfqGAAQv.mp4, DWG5Z9_DdzF.mp4, DVR5redDdo1.mp4 em C:\Users\Pichau\Downloads.
Usar SEMPRE em vídeo da BNB, salvo pedido contrário. Projeto de referência completo: C:\ARQUIVOS\JOBS E EMPREGOS\BNB CONNECT\PRODUZIDOS\07-10 - REELS 01 (BASES, BROLL, EDICAO). B-rolls do cliente: C:\ARQUIVOS\JOBS E EMPREGOS\BNB CONNECT\BROLSS e \broll (vídeos novos: casa pé na areia, pesquisa/sazonalidade, equipe trabalhando); fotos reais em \FOTOS REAIS IMOVEIS PORTFOLIO.
**2º vídeo de referência (20/10/2026): "Se eu fosse anunciar no Airbnb"** · versão aprovada `BOB-videos/bnb-se-eu-fosse/BNB_SE_EU_FOSSE_v11.mp4` (1:56). Projeto completo e scripts em `BOB-videos/bnb-se-eu-fosse/` (cadeia: `scripts/gerar.sh` → `finalizar.py` → `broll.py`). Tudo o que mudou nele está marcado abaixo como **(v. "Se eu fosse")**.

## 1. Ideia geral
Depoimento da Glauce no sofá, ritmo de Reels editorial: legenda tipográfica viva no peito, closes nas ênfases, cards de prova no topo, 1 ou 2 telas cheias, música contínua e cliques sutis. A pessoa fica sempre presente nos momentos de confiança e emoção; B-roll só onde ela descreve processo.

## 2. Formato e cor
- 1080x1920, 30 fps, H.264 CRF ~21, AAC 192k 48 kHz.
- Filtro "B" (quente, âmbar, pretos densos), aplicado ANTES de cards, legenda e botão:
  `eq=saturation=1.5:contrast=1.10:brightness=-0.03:gamma=0.93,colorbalance=rs=0.05:rm=0.08:bm=-0.09:bs=-0.05,vignette=angle=PI/6`
- B-roll (cards e tela cheia) fica com a cor original.
- **Filtro limpo (v. "Selos", aprovado 21/10/2026, padrão para gravação com pouca luz):** o filtro B amplia o grão da pele ("parece atrás de vidro sujo"). Quando o take for HEVC 720p escuro, tirar o ruído com nlmeans e usar cor mais leve:
  `scale=1080:1920:flags=lanczos,nlmeans=s=4:p=7:r=9,eq=saturation=1.18:contrast=1.04:brightness=0.0:gamma=0.98,colorbalance=rs=0.03:rm=0.04:bm=-0.04:bs=-0.02`
  hqdn3d não resolve. Sempre comparar um quadro do rosto antes de renderizar tudo.

## 3. Dinâmica de cortes
- O roteiro manda na ordem. Escolher o melhor take por cena (transcrição Whisper medium com prompt de nomes + mapa cena→take aprovado pelo usuário).
- Pausas internas > 0,35 s encurtadas para ~0,24 s (silencedetect -35 dB, KEEP 0,12 s de cada lado). A respiração natural fica.
- Início de cena = min(palavra do Whisper, fim do silêncio IMEDIATAMENTE anterior na janela a-0,6..a+0,5) - 0,15 s. Nunca começar no gesto de ajeitar o cabelo; terminar antes de ela se inclinar para a câmera.
- Troca de take/cena: dissolução de 0,3 s (xfade + acrossfade, com 0,3 s de pré-rolagem do take novo), SEM som. Dentro da fala: corte seco.
- Close simulado 1,4x (crop 770x1370 em x=145 y=338) nas ênfases emocionais: credencial falada, "não perde o controle", "não é só pra ficar bonito", "não tratamos de forma massificada", "Você escolhe, a gente se adapta" e a cena intimista antes do CTA. Plano aberto no gancho, nas viradas, no CTA e SEMPRE durante card no topo (no close a cabeça começa em y≈300 e o card cobriria o rosto). Enquadramento aplicado por take antes da dissolução.
- Scripts (scripts/): assemble_v5.py (cortes + dissoluções → timeline.json) · full5.py (PLAN de closes) · base_framed.py (render final: closes + filtro + cards + legenda + botão; env CARDS, SUBS, OUT, DUR) · remap.py (remapeia o PLAN para uma nova linha do tempo; CUIDADO: regrava full5.py a partir de full.py).

## 3a. Câmera virtual e velocidade (v. "Se eu fosse", aprovado 20/10/2026)
- **Câmera virtual no lugar dos closes estáticos** (`scripts/camera.py` + `camera.yaml` do projeto): zoom out no gancho (1,30→1,00 com easing "out" em ~2,9 s) e planos alternados por frase (aberto 1,00–1,03 / fechado ~1,16–1,20, deslocamento lateral ±20–25 px), deriva lenta dentro de cada plano. Roda sobre o render BASE (sem legenda) e a legenda é queimada depois, para não mexer com a câmera.
- **Zoom ancorado na BOCA** (AX=540, AY=1150): o rosto não desce no plano fechado e a legenda baixa nunca cobre a boca.
- **Gesto de mãos = plano aberto (1,00)**, como em "é assim que eu faria". 1,00 é o máximo: os takes da Glauce vêm com faixa preta (conteúdo 700x932 em 720x1280) e o filtro do projeto recorta para preencher o 9:16.
- **Velocidade por cena** (`scripts/velocidade_cenas.py`, troca no meio de cada dissolução, legenda e câmera aceleram junto, música NUNCA): 1,1x onde ela fala mais rápido e 1,2x nas cenas lentas. **Trechos importantes ficam em 1x** (no vídeo: ponte "Só que fazer isso toda semana..." e controle "Ter um coanfitrião não significa perder o controle"). Grava `trabalho/timeline_vel.json` para posicionar B-roll e sons na linha do tempo nova.
- **Respiro entre takes**: dá para encurtar por cena com `respiro_fade` e `inicio_cena` no projeto.yaml (reels.py aceita por cena).
- **Final do CTA**: o take termina com ela sorrindo ~1 s depois de "bio"; manter esse sorriso (o montar corta na fala, a cauda entra à parte).

## 3b. Transições de impacto (aprovado no gancho em 20/10/2026)
Usar no GANCHO e quando o roteiro TROCA DE SITUAÇÃO (ex.: do problema para a solução, do "antes" para o "como eu faria", de um passo para o outro). No resto, segue a dissolução de 0,3 s.
Script: `scripts/efeitos_transicao.py` (funções `flash_foto`, `whip_pan`, `bokeh`; teste: `python scripts/efeitos_transicao.py VIDEO.mp4 FIM_A INICIO_B pasta [efeito]`). Exemplos no gancho do vídeo "Se eu fosse anunciar": `exemplos_transicao/`.
- **flash_foto** (ref. DbL2tHmuz68 0:02): a pessoa vira silhueta branca (2 quadros), estoura exposta, tremor, 2 quadros brancos e corta. Som: `camera_foto_shutter_4` + `camera_foto_flash_1`. Combina com o tema fotos do anúncio.
- **whip_pan** (ref. DbL2tHmuz68 0:31): giro de câmera simulado, A sai para a esquerda com desfoque horizontal e B entra pela direita (4+4 quadros). Som: `swoosh_whoosh_3`. O mais dinâmico; ideal em troca de situação.
- **bokeh** (ref. DXL9nodDevc 0:31): clarão dourado com bolhas de bokeh e arco de luz, estoura e abre na cena seguinte. Som: `swoosh_15` + `sino_acerto_small_bell`. O mais acolhedor, no tom quente da marca.
Sons vêm do arsenal real (`sons/arsenal`); o pico do som é alinhado ao corte automaticamente. A música entra no corte do gancho.
**Aprovado (v. "Se eu fosse"): flash_foto no gancho** ("É assim que eu faria" → credencial, no lugar da dissolução) e **whip_pan na troca de situação** (anúncio → precificação). No vídeo final o efeito é aplicado sem mudar a duração (`finalizar.py`, `broll.py`).

## 4. Legenda tipográfica
Ver legenda_tipografica.py + exemplo_marcacao_reels01_completa.txt (vídeo inteiro: 47 blocos, 423 palavras).
- Montserrat Bold/ExtraBold + **Dancing Script Bold** (script, `fonts/DancingScript-Bold.ttf`, família "Dancing Script Bold BNB"; aprovada em 20/10/2026 no teste do vídeo "Se eu fosse", substitui a Gabriola). Pequena 72 · grande 150 · script 180 (a Dancing é maior por em que a Gabriola; a 260 antiga só vale para a Gabriola). No projeto.yaml: `legenda: {fonte_script: DancingScript-Bold.ttf, tamanho_script: 180}`. A Gabriola continua em fonts/ para refazer vídeos antigos.
- Modos @empilha (linhas acumulam até o fim da ideia) e @troca (uma expressão por vez); ~25 a 30% dos blocos em troca (listas e viradas).
- Linhas mistas ("s: no seu | b: anúncio,"); linha mista acima de 940 px quebra em duas (nunca encolher a pequena). Margem irregular por bloco. Entrelinha apertada.
- Cor de destaque: azul claro da família Petróleo `&H00D4B86B` (#6BB8D4), em ~1 a cada 2 ou 3 blocos (BNB CONNECT, primeiras, o controle, diagnóstico, inteligência, 2 mil, conversão, gestão completa, tempo real...). Texto branco, sombra suave, sem contorno.
- Posição **(v. "Se eu fosse", padrão novo)**: abaixo do queixo, `LEG_TOP=1350` e `LEG_PE=1680` (base máxima; bloco alto sobe só o necessário, para não entrar na interface do Instagram). Vídeos antigos: topo 1120. Bloco isolado pode descer com `@empilha +260` na marcação. Entrada: fade 60 ms + escala 88→100% em 120 ms.
- Por cima de **tela cheia** a legenda continua visível (broll.py renderiza a legenda de novo sobre o vídeo cheio).
- "BNB" e "BNB CONNECT" sempre em caixa alta; "Airbnb" intacto. Mostrar a marcação ao usuário antes do render final.
- Da revisão do v15: a script em AZUL (X) perde contraste sobre fundo claro (ex.: "você escolhe" na frente da parede). Preferir a script branca (x) quando o fundo atrás for claro.

## 5. B-roll (sistema de cards)
Estratégia: ~15 inserções em 2:35. Nada de B-roll no gancho falado, nos closes de ênfase, na cena intimista e no CTA. Cards = prova ou ilustração do que ela diz; tela cheia = momentos de "imagine / viva" (no máximo 2 por vídeo, 3 a 5 s).
Todos ficam no topo, centralizados, acima da cabeça; entram deslizando 40 px + fade 0,25 s e saem com fade 0,2 s.
- **Card de logo:** logo da BNB no próprio fundo petróleo, cantos 40, sombra, largura 620, y=90, na primeira menção a "BNB CONNECT" no gancho (assets_cards/c_logo.png).
- **Card de print/foto com moldura branca:** raio 40, padding 26, sombra; largura 540 a 720; y=70. Prints com texto entram INTEIROS (sem recorte).
- **Card de vídeo/foto 16:9:** moldura assets_cards/frame_video.png (680 px; conteúdo 628x352 com cantos 22 via mask_video.png); y=55. Vídeo exportado em .mov qtrle com alpha (função vcard); pode acelerar (ex.: 1,5x) e cortar a duração.
- **Sequência:** várias imagens trocando NO MESMO LUGAR (a anterior sai com fade 0,04 s, a próxima entra sem deslizar com fade 0,08 a 0,12 s), de ~0,9 a 3,5 s cada, sincronizadas com as palavras (ex.: "dados históricos" → imagem 2, "inteligência artificial" → imagem 3).
- **Tela cheia:** vídeo vertical 1080x1920, fade 0,2 s; voz e legenda continuam por cima; sem som de entrada.
- Formato da variável CARDS: [arquivo, t0, t1, y, (fade_in), (fade_out), (slide)]. Arquivos .mov/.mp4 entram com -itsoffset t0; imagens com -loop.
- Prints pequenos (<500 px) ficam suaves: pedir prints do celular em tela cheia.
**Novidades (v. "Se eu fosse", `scripts/broll.py`, compõe sobre o vídeo final com âncoras de palavra):**
- **Selos PASSO 1–4**: pílula petróleo #052F42 com ponto azul #6BB8D4, Montserrat Bold 64, y=110, ~1,6 s, na entrada de cada passo do roteiro, com `swoosh_whoosh_1` (+2 dB, precisa ser audível).
- **Card de vídeo a partir de mp4 comum** (sem .mov): moldura 680 px, recorte 16:9 (ex.: pesquisa/sazonalidade no "preço do vizinho", tablet 10-01 no "acompanhar pelo aplicativo", ~6 s, começando na frase e não só na palavra).
- **Tela cheia**: vídeo real do cliente (casa pé na areia na "sazonalidade"; equipe trabalhando na "equipe especializada"), som do B-roll MUDO, voz + música + legenda por cima.
- **Comparativo dos 2 produtos** (no "você escolhe qual envolvimento"): dois cards lado a lado no topo · esquerda bege "VOCÊ OPERA / Gestão do Anúncio / Apoio estratégico e comercial" · direita petróleo "A GENTE CUIDA / Gestão Completa / Do anúncio à operação"; itens linha a linha (Anúncio e fotos, Preço semanal, Estratégia, Operação do dia a dia), ✓ azul e **X vermelho** na operação do dia a dia da Gestão do Anúncio. Textos do site da BNB; itens a confirmar com a Glauce.
- **Material reaproveitável já pronto**: cards do Reels 01 (`PRODUZIDOS/07-10 - REELS 01/BROLL/cards`: c_anuncios1/2, c_logo, c_05-01 gráficos, c_11-01 produto, v03–v12 vídeos com moldura) + print do perfil novo da Glauce (aprovado 21/10/2026, card largo 980 px, entra em "anos"; substitui o c_perfil antigo) + selo Airbnb e 2 avaliações reais 5★ (`bnb-se-eu-fosse/broll_cliente/`).
- Evitar card de foto que não bate com a fala (ex.: sala no "calendário"): na dúvida, deixar só ela falando.

**Novidades (v. "Selos Superhost x Preferido", aprovado 21/10/2026, `scripts/selos/broll.py`, exemplos em `exemplos_selos/`):**
- **E-mail/print do cliente em tela cheia** logo depois do flash do gancho ("atualização"), com a legenda por cima.
- **Pílulas de selo** (SUPERHOST, PREFERIDO DOS HÓSPEDES, A CADA 3 MESES): mesma pílula petróleo dos PASSOS, ficam até a frase seguinte terminar (não sumir rápido).
- **Recortes de e-mail do Airbnb** como cards (medalha, KPIs, recompensa, avaliação), cada um na frase que cita o item.
- **Prints reais de anúncios BNB com o selo** em sequência (largura 720): foto do anúncio + selo recortados juntos, trocando a cada ~1,4 s.
- **Medalhas douradas 3D Top 10/5/1** lado a lado (`assets_cards/medalhas/m10, m5, m1`), uma por palavra. O "5" foi sintetizado: trocar por arte real se aparecer.
- **Comparativo de selos**: dois cards "SUPERHOST · é um selo do ANFITRIÃO · vale para a pessoa" x "PREFERIDO DOS HÓSPEDES · é um selo do ANÚNCIO · vale para cada imóvel". Copy curta e paralela; a 1ª versão (mais longa) confundiu.
- Card de avaliação real fica até o fim da palavra-chave + 0,3 s.

## 6. Som
- Música: "Rising" (Origo, Epidemic Sound; licença do usuário cobre cliente) a -17,4 dB (~12 dB abaixo da voz), fade in 0,4 s e out 2,5 s. **(v. "Se eu fosse"): "Let's Go!" (Speedy The Spider, Epidemic)** no mesmo nível, entrando no flash do gancho. Opções em `BNB CONNECT/PRODUZIDOS/ES_*.mp3`.
- **Efeitos do arsenal real** (`BOB-videos/sons/arsenal`, aba Sons da biblioteca; os sintéticos foram reprovados): obturador `camera_foto_shutter_4` em fotos, `ui_digital_mouse_click` em card de pessoa/vídeo/botão, `sino_acerto_ding` no selo Airbnb, `sino_acerto_correct` nas avaliações, `swoosh_*` em logo, PASSOS e transições, `dinheiro_cash_register` baixinho em número/estratégia, `ui_digital_chat_message` em cards que pipocam. Nada de humor/meme ou tensão pesada (exceção: erro bem baixo no X vermelho).
- Cliques (sfx/; biblioteca completa em BOB-videos/sons): **clique_mouse** = card de logo, pessoa, vídeo e botão LINK NA BIO; **obturador_foto** = cada imagem estática (prints, fotos e cada troca de sequência). Pico -18 dBFS, ~0,18 s após o início do card (0,05 s nas trocas de sequência; 0,30 s no botão).
- Final: alimiter 0.75 → ~-15,4 LUFS, pico ~-2,2 dBFS.

## 7. CTA
Botão "LINK NA BIO" variação 3 (gradiente IG, em ../../assets/button) no topo, y=110, entra na palavra "link", com clique de mouse no pouso.
**Final (v. "Se eu fosse", padrão novo):** logo BNB entra em "Clique no link" e o botão logo abaixo; depois do sorriso dela a tela faz **fade para branco (0,4 s)** e logo + botão ficam mais **2,8 s** sobre o branco, com a música terminando em fade (EXTRA em `finalizar.py`). A legenda tipográfica do CTA termina em "render." grande.

**Final (v. "Selos"):** nunca cortar no meio da fala. A frase final do take vai inteira (ex.: "É isso que buscamos… para que o imóvel tenha uma performance melhor na plataforma."), depois **~1,2 s do rosto dela em silêncio, tirado do próprio take** (`scripts/selos/cauda.sh`), e o card branco entra 0,9 s depois da última palavra: logo y=430, frase padrão "Seu imóvel precisa / *performar.*" y=900, botão LINK NA BIO y=1250.
Sons extras aprovados: rise antes da virada, glitch no flash, ding mais alto no "preferido", caixa registradora em "visibilidade", swoosh_15 em palavras de peso, chat pop em "É simples"/"e outros não". Música "Keep Waiting" (Victor Lundberg, Epidemic) a -15,5.

## 8. Fluxo de produção
1. Transcrever os takes → mapa cena/take → aprovação.
2. assemble_v5 → timeline.
3. Plano de closes (full5).
4. Marcação da legenda (aprovação).
5. Plano de B-roll por minutagem (aprovação; material real do cliente primeiro).
6. Render (base_framed) + mix de música e cliques.
7. QA: decode, LUFS/pico, folha de quadros, legenda sem cobrir rosto, cards sem cobrir a cabeça.
8. **Depois de cada `reels.py montar`:** rodar `scripts/selos/corrigir_falas.py` ("Superhost do Airbnb", "o Airbnb vai") e apagar palavras de borda que vazam na legenda; conferir que a marcação tem o mesmo número de palavras da linha do tempo.
9. Velocidade por cena via `VEL` (abertura/explicação 1,15x, trecho principal 1x, BNB 1,05x); cortar tropeço/olho fechado medindo o RMS da fala.
10. Enviar SEMPRE a partir de BOB-videos/ (arquivo em C:\ARQUIVOS aparece "Indisponível" no app).

## Motion (skill video-motion-hf, aprovado 10/10/2026 no Reels 01)
- **Lower-third de apresentação da pessoa (PADRÃO, usar sempre que ela se apresenta):** `BOB-videos/biblioteca-motion/lower-third-apresentacao/` · "Glauce Terra" + "COANFITRIÃ · BNB CONNECT", barra e cargo azul #6BB8D4, caixa rgba(10,32,44,.78), Montserrat Bold, y=1440, 4,2 s, entra ~0,5 s antes do nome.
- **Card de destaque compacto:** só palavras-chave (ex.: "uma das primeiras" em Dancing Script 80 (antes Gabriola 92) azul #2E8FB3 + "COANFITRIÃS AIRBNB · BRASIL" Montserrat 30), cartão branco pequeno centralizado no topo (y=120). NÃO usar card grande com frase inteira (ocupa a cena).
- **Citação:** UMA linha, aspas coladas no texto ("Você não perde o controle de nada"), Montserrat 44 branca com sombra, palavra-chave em faixa azul #2E8FB3 (azul solto some na parede clara), palavra a palavra no ritmo da fala, y=190.
- Fonte das peças: `BOB-videos/biblioteca-motion/cards/bnb-destaque-e-citacao/index.html`.
- Legenda atrás da pessoa (gancho): 3 variações testadas (ink, loud, keynote) em `projetos-motion/bnb-legendas/`; escolha pendente.

## Voz de narração (aprovada em 16/10/2026)
**PADRÃO / TOP 1: `Glauce acolhedora`** (a própria Glauce preferiu esta). Amostra de referência do resultado: `BOB-videos/testes-voz/glauce-clonagem/testes/Glauce_acolhedora-pausa_blocos.mp3`. Usar sempre que o vídeo precisar de narração na voz dela; `Glauce completa` é a 2ª opção e as BNB Voz 1/2/3 ficam para quando não for falar como a Glauce.
Usar quando o vídeo pedir narração que não foi gravada pela Glauce (gate GV do orquestrador bob-videos).
| Voz | Motor | Como chamar | Amostra aprovada |
|---|---|---|---|
| **BNB Voz 1** · feminina adulta, tom grave | VoiceStudio (grátis, local) | `python ferramentas/voicestudio/narrar.py texto.txt saida.wav --voz "BNB Voz 1"` | `BOB-videos/testes-voz/bnb-5-coisas/I3_voicestudio_br_adulta_grave_NATURAL.wav` |
| **BNB Voz 2** · feminina jovem, tom médio | VoiceStudio | `--voz "BNB Voz 2"` | `.../J3_voicestudio_br_jovem_media_NATURAL.wav` |
| **BNB Voz 3** · feminina adulta, tom grave, pt-BR | VoiceStudio | `--voz "BNB Voz 3"` | `.../K3_voicestudio_ptBR_adulta_grave_NATURAL.wav` |
| Alternativas pagas | ElevenLabs | vozes Ana, Livia, Marianne adicionadas à conta como "(BNB teste)" | `.../F_elevenlabs_ana.mp3`, `G_..._livia.mp3`, `H_..._marianne.mp3` |
Receitas e perfis: `BOB-videos/ferramentas/voicestudio/vozes.json` (os 3 também estão salvos como perfis dentro do VoiceStudio).
**Modelagem do texto para a voz:** seguir `BOB-videos/ferramentas/voicestudio/ESTILO-MODELAGEM.md` (texto inteiro numa chamada; lista com ponto final em cada item; linha em branco entre blocos; velocidade 0.92; nunca cortar e colar silêncio).
**Voz clonada da Glauce (APROVADA em 16/10/2026; autorização confirmada pelo usuário):** `Glauce acolhedora` e `Glauce completa` (perfis no VoiceStudio "BNB Glauce · acolhedora-pausa" e "· completa-pausa"). Chamar: `python ferramentas/voicestudio/narrar.py texto.txt saida.mp3 --voz "Glauce acolhedora"` (gera por bloco com respiro, velocidade 0.88; entrega em MP3). Amostras aprovadas: `BOB-videos/testes-voz/glauce-clonagem/testes/Glauce_*-pausa_blocos.mp3`. Narrar em nome da Glauce só o que ela aprovaria dizer; registrar no BRIEFING.
