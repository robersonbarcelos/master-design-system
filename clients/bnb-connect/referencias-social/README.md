# BNB Connect — Referências Sociais da Glauce (Banco de Ideias)

> Pasta criada em 2026-09-10 a pedido do Diego. Recebe carrosséis e vídeos de referência que a Glauce está passando, pra virarem ideias adaptadas ao Banco de Ideias.

## Skills envolvidas (localizadas)

| Skill | Papel | Onde vive |
|---|---|---|
| `reference-analyzer-sms` | Analisa carrossel/post/thread de outro criador — extrai o mecanismo narrativo (não copia conteúdo, copia estrutura) e adapta pro cliente/produto | `Master-social-design-system/skills/social-media/reference-analyzer-sms` |
| `video-script-sms` (MODO B — Engenharia Reversa) | Analisa vídeo de referência: categoriza o gancho (0-3s) em uma das ~20 famílias psicológicas, mapeia estrutura de tensão, ritmo de corte, virada emocional e CTA — depois gera roteiro novo com a mesma técnica, tema da BNB | `Master-social-design-system/skills/social-media/video-script-sms` |
| `video-perception` | "Claude Vision" pra vídeo — MCP `claude-video-vision`, roda **ffmpeg** internamente (corte de cena, silêncio, movimento) + extrai frames + transcreve áudio. É a camada de leitura que alimenta o MODO B acima quando o vídeo não tem transcrição completa | `SKILLS-DE-VIDEOS/video-perception` |
| `ref-video-concepts` | Alternativa/complemento pro vídeo: já usa `video-perception` por baixo e devolve 2-3 conceitos diferenciados direto (paleta, câmera, ritmo, atmosfera) | `SKILLS-DE-VIDEOS/ref-video-concepts` |

**Fluxo por tipo de referência:**
- **Carrossel/imagem estática** → `reference-analyzer-sms` (Modo A: analisa o mecanismo / Modo C: adapta pro cliente)
- **Vídeo** → `video-perception` (assiste) → `video-script-sms` Modo B (categoriza o gancho, estrutura, CTA) → roteiro novo na voz da BNB

## Estrutura de pastas

- `carrosseis/` — imagens brutas dos carrosséis que a Glauce mandar
- `videos/` — arquivos de vídeo brutos (ou anotar aqui o link, se for link do Instagram/TikTok)
- `analises/` — 1 arquivo `.md` por referência analisada: gancho, estrutura, ritmo, CTA, o que faz funcionar
- `ideias-geradas/` — as variações adaptadas pra BNB Connect, já organizadas pela taxonomia abaixo

## Taxonomia do Banco de Ideias — 3 eixos: Linha Editorial × Formato × Funil

Cada ideia gerada é marcada nos 3 eixos, pra ficar fácil filtrar depois. O eixo principal não é um "ângulo" novo e solto — é a **linha editorial que já definimos** (`linhas-editoriais-em-espera.md` + `linha-editorial-autoridade-glauce.md`), porque o ângulo/gancho de cada referência normalmente já cai em uma dessas 6. O funil vem de graça: cada linha já tem posição de funil definida em `estrategia-funil-conteudo.md`.

**Linha editorial** (a referência é encaixada em uma destas — ou, se não couber em nenhuma, é sinal de que pode nascer uma 7ª linha):

| # | Linha | Funil herdado |
|---|---|---|
| 1 | Por trás da operação (Autoridade da Glauce) — já desenvolvida | Fundo (LinkedIn) / Topo-alcance (Instagram) |
| 2 | Mito vs. realidade | Fundo |
| 3 | Números que comprovam | Fundo |
| 4 | Casas com alma | Meio (emocional, mas ainda fala com o dono) |
| 5 | Como funciona | Fundo |
| 6 | Topo de funil puro (imóveis/viagem) | Topo |

**Formato:**
- Carrossel
- Vídeo (Reel/TikTok)
- Estático

**Funil:** herdado automaticamente da linha editorial (tabela acima) — não precisa escolher nas mãos toda vez, só confirmar se a adaptação específica não puxou a peça pra outro ponto do funil.

Uma ideia fica registrada assim: `[Referência original] → Linha: [nome] · Formato: [Y] · Funil: [fundo/meio/topo] → [3 variações adaptadas pra BNB]`.

## Como vamos expor isso no painel (Central BNB Connect)

O módulo **07 · Banco de Ideias** vai ganhar, dentro de "Ideias p/ Conteúdo", sub-divisão por linha editorial (as 6 já existentes), cada card mostrando os 3 selos (Linha · Formato · Funil) e linkando pra referência original — que também sobe pro site, conforme pedido do Diego. A referência original fica visível ao lado da ideia adaptada, não só a ideia final.

## Pendente

Aguardando os carrosséis e vídeos da Glauce para começar a rodar as análises. Assim que chegar o primeiro material, o fluxo roda: ler a referência → encaixar numa das 6 linhas editoriais (ou propor uma 7ª, se não couber) → rodar a skill certa (`reference-analyzer-sms` pra carrossel/estático, `video-perception` + `video-script-sms` Modo B pra vídeo) → gerar 3 variações → registrar em `ideias-geradas/` com os 3 selos (Linha · Formato · Funil) → subir pro painel, com a referência original ao lado.
