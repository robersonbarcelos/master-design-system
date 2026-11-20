# Templates de capa LA BELLE (JSON para colar no GPT) | atualizado em 11/11/2026
Regra comum: fundo BRANCO-CREME #FAF7F1 (nunca escuro), petróleo #043333 só no texto, dourado #B7881D, Cormorant Garamond + Plus Jakarta Sans, logo SEMPRE anexada para a IA aplicar (nunca redesenhada), sem travessão, sem "1994".

## 9:16 (Reels, TikTok, Shorts), todos COM RECUO 4:5 (o feed recorta y 285 a 1635; nada importante fora disso nem a menos de 250 px do topo e da base)
| Arquivo | Estilo | Anexos |
|---|---|---|
| `TEMPLATE-FICHA-MARCA-DAGUA-LABELLE-REELS.json` | Ficha clara: foto desfocada a 18-22% como marca d'água, moldura dourada recuada, textos centralizados, logo no rodapé | foto + logo |
| `TEMPLATE-JANELA-EM-FADE-LABELLE-REELS.json` | Janela clara: foto nítida em cima dissolvendo no creme, texto e logo embaixo, dentro da moldura recuada | foto + logo |
| `TEMPLATE-BORDAS-CLARA-LABELLE-REELS.json` | Bordas clara: fundo desfocado clareado, card recuado com margem creme, aba de pasta com a logo, véu creme no topo, título petróleo e dourado, pílula de local | foto + logo oficial |
| `TEMPLATE-MOLDURA-FADE-CLARA-LABELLE-REELS.json` | Moldura fade clara: card recuado com foto, moldura dourada, degradê creme subindo da base, título à esquerda, logo no rodapé | foto + logo oficial |
Os quatro são CLAROS (creme, petróleo e dourado). Não existe versão escura da LA BELLE. Bordas e Moldura fade clara foram criados em 11/11/2026 como equivalentes dos estilos da Mônaco (não testados no GPT).

## YouTube 16:9, 1280x720 (não há corte 4:5: usar margem útil de 64 px e deixar o canto inferior direito livre para a duração)
| Arquivo | Estilo | Anexos |
|---|---|---|
| `CAPA-YOUTUBE-LABELLE-1-JANELA-FOTO-CLARA.json` | COM FOTO: janela nítida à direita que dissolve no creme, texto à esquerda em 3 linhas (3ª em dourado itálico), logo no canto inferior esquerdo | foto + logo oficial |
| `CAPA-YOUTUBE-LABELLE-2-MOLDURA-LOGO-CLARA.json` | SEM FOTO: moldura dourada, logo oficial grande no alto, filete e slogan em 2 linhas, tudo centralizado (igual à abertura do institucional) | só a logo oficial |
Origem: capa do Rei Charles (08/11) e institucional (10/11). Logo oficial: `_LOGOS-MONACO-LABELLE/labelle/logo_labelle_oficial_transparente.png`.

## Como usar
1. Escolher o estilo e o formato. 2. Trocar só os textos em `ui_elements` (e `anexos`). 3. Colar o JSON no GPT com a(s) imagem(ns) anexada(s). 4. Conferir acentos, logo intacta e fundo claro.
Os JSONs ainda não foram todos testados no GPT (ver o campo `status` de cada um).
