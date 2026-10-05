# BNB Connect — Referências de Vídeo (para adaptar ao modelo de negócio)

> Pasta criada em 2026-09-10 a pedido do Diego. Aqui entram vídeos de referência (de outros creators, concorrentes, anúncios, clipes de inspiração) que precisam ser **adaptados** para a BNB Connect — nunca copiados.

## Skills envolvidas (localizadas em `SKILLS/SKILLS-DE-VIDEOS/`)

| Skill | Papel |
|---|---|
| `video-motion-pro` | Orquestrador — decide o fluxo certo a partir do que for pedido |
| `video-perception` | "Claude Vision" para vídeo — usa o MCP `claude-video-vision`, que roda `ffmpeg` internamente (scene changes, corte, movimento, silêncio) + extrai frames + transcreve áudio |
| `ref-video-concepts` | **A skill de adaptação.** Usa o `video-perception` pra ler a referência, destrincha o que faz o vídeo funcionar (elemento técnico, emocional, rítmico) e propõe 2-3 conceitos diferenciados — nunca cópia, sempre reinterpretação com identidade própria |
| `motion-scenes` / `motion-takes` | Produção do conceito escolhido em prompts de motion design (Google Flow / Gemini Omni) |
| `seedance-15-real-estate` | Skill de prompt cinematográfico específica pra imóveis/real estate — relevante direto pro nicho da BNB |

## Fluxo que vou seguir quando você mandar um vídeo de referência

1. `video-perception` assiste o vídeo (frames + transcrição + análise de ffmpeg: cortes, ritmo, movimento de câmera)
2. `ref-video-concepts` extrai paleta, ritmo de corte, movimento de câmera, atmosfera, estrutura narrativa — e propõe **2-3 conceitos diferenciados**, cada um mudando pelo menos 2 das 5 dimensões (paleta, câmera, ritmo, atmosfera, narrativa) em relação ao original
3. Cada conceito já sai adaptado ao modelo de negócio da BNB Connect: linguagem de co-hosting premium, pilares de funil (fundo: DINHEIRO/INTELIGÊNCIA/PERFORMANCE/EDUCAÇÃO/PROVA; topo: imóveis/viagem/bastidor da Glauce — ver `estrategia-funil-conteudo.md`), e cruzado com os 4 sistemas visuais já mapeados em `auditoria-identidade-visual.md`
4. Você escolhe o conceito → vira prompt pronto pra colar no gerador (Flow/Omni/Seedance)

## Como usar esta pasta

- Salve aqui os arquivos de vídeo de referência (.mp4, .mov) ou cole o link do YouTube diretamente na conversa — não precisa upload manual se for link.
- Para cada referência trabalhada, salvo aqui os concept cards gerados (`concept-[tema]-[data].md`), pra manter histórico do que já foi proposto e escolhido.
