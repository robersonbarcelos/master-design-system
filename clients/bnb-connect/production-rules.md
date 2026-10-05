# Production Rules: BNB Connect

> Leia este arquivo ANTES de escrever qualquer copy.
> Nunca produza sem passar pelo Gatilho Pré-Copy.
> Preenchido em 21 set 2026 a partir do painel `bnbconnect.vercel.app` (Sistema Editorial e Direção Visual v1.1, itens 04.10 e 04.11) + `positioning-consolidado.md` (seção 14) + regras validadas em produção real nesta sessão (ver `feedback_bnb_connect_producao.md` na memória do projeto). Antes deste preenchimento, este arquivo era o template genérico da skill, nunca customizado pra esse cliente.

---

## 00 | GATILHO PRÉ-COPY: OBRIGATÓRIO ANTES DE QUALQUER ENTREGA

### Passo 1: Voz
- A marca fala em **primeira pessoa do plural**, com **"a gente" como voz dominante**, mas variando com **"nós"** e, ocasionalmente, **"a BNB Connect"** nos trechos mais institucionais (diagnóstico, operação contínua, distribuição), pra não repetir "a gente" demais num mesmo roteiro/texto longo (regra do Diego, 21 set 2026, depois de notar 8 repetições de "a gente" em ~370 palavras no roteiro 06.1). Guia prático: em textos curtos (post, legenda, card), "a gente" sozinho está ótimo. Em roteiros longos (vídeo com várias falas), variar a cada 2-3 ocorrências, mas manter "a gente" nos momentos mais pessoais/emocionais (fala direta da Glauce, a "conversa com você"/momento de escolha do proprietário, frases de assinatura como "não padronizamos imóvel").
- Quando é a Glauce falando pessoalmente (Linha 1), pode entrar 1ª pessoa do singular ("eu"), mas o trabalho da equipe continua em "a gente"/"nós"/"a BNB Connect".
- Verbos característicos: cuidamos, acompanhamos, entramos como coanfitriã, diagnosticamos, cruzamos dado com experiência.
- **Nunca:** "a empresa garante...", "a Glauce decide sozinha o que fazer com o seu imóvel" (ela apresenta opções, o proprietário decide). "A BNB Connect" como sujeito é permitido com moderação (ver acima), só não pode virar o padrão dominante nem soar formal/distante.

### Passo 2: Padrões de IA proibidos

| Padrão | Por que eliminar |
|--------|-----------------|
| Travessão (—) em qualquer texto | Zero tolerância confirmada pelo Diego, 10 set 2026, depois de auditoria retroativa achar 119 violações no site inteiro. Usar vírgula, dois-pontos, ponto ou meio-ponto (·). Rodar `grep "—"` no texto final antes de entregar. |
| "Isso tem nome." / revelação teatral | Não é a voz da marca: ela explica com clareza, não com suspense artificial. |
| "Não é X. É Y." em excesso | Usado com moderação na linha Mito ou Realidade (objeção real), mas não é a muleta padrão de toda peça. |
| Trios abstratos ("execução, segurança e confiança") | Preferir 1 conceito aprofundado com dado, não 3 palavras soltas. |
| Adjetivos de luxo sem dado ("robusto", "premium", "incrível") | Voz evita adjetivo hiperbólico e excesso de adjetivo de luxo (confirmado em 04.10 do painel). Trocar por mecanismo real ou número. |
| CTA vago ("saiba mais", "descubra") | CTA sempre aponta pro link da bio com uma pergunta específica antes (ver banco de CTAs em `content-system.md`). |
| Citar o nome interno da ferramenta de IA ("Estrela") | NUNCA em copy pública nem em material interno de produção. Ver regra 2 completa em `feedback_bnb_connect_producao.md`. |

### Passo 3: Checagem final
- [ ] Tem número ou fato específico sustentando a afirmação (ver Banco de Dados Âncora em `references/dados-ancora.md`)?
- [ ] Zero travessão (rodar grep antes de entregar)?
- [ ] O CTA está isolado, com pergunta específica antes de "clica no link da bio"?
- [ ] Se a peça é institucional/autoridade (Linha 1, 2, 3, 5, 7 do Banco de Ideias), valida a credencial da Glauce e/ou explica o mecanismo de coanfitriã quando a oportunidade permitir (regra 1 de `feedback_bnb_connect_producao.md`)?
- [ ] Nenhuma tela/dashboard/gráfico inventado: quando aparecer tela em vídeo ou imagem, é o próprio aplicativo do Airbnb, nunca um painel fictício da BNB (achado real, corrigido 11 set 2026, ver 07.1 do painel)?
- [ ] Passou pelo checklist visual completo de 04.11 do painel (10 pontos, complementa este gate, que é só sobre o texto)?

**Só depois de passar por esses três passos, produzir o copy final.**

---

## 00-A | GUIA DE VOZ: REGRAS COMPLETAS

### Princípio central
Autoridade demonstrada com dado e mecanismo real, nunca declarada com adjetivo. Fórmula recomendada (Sistema Editorial v1.1, item 04.10): **observação concreta + leitura estratégica + benefício humano.** Exemplo oficial de aplicação: *"Preço não é palpite. É a leitura diária da demanda pra encontrar o melhor equilíbrio entre ocupação, receita e posicionamento."*

### Voz
- Pessoa: primeira do plural, "a gente" (Glauce pode usar "eu" nas linhas de autoridade pessoal, mas fala da equipe em "a gente").
- Tom (04.10 do painel): claro e seguro · elegante sem ser rebuscado · próximo sem informalidade excessiva · estratégico quando explica · sensorial quando inspira.
- Ponto de partida do conteúdo: varia por linha editorial (autoridade pessoal, quebra de mito, prova, diferenciação emocional, método, desejo/topo de funil): ver as 6 linhas em `content-system.md` seção 01.
- Personalidade da marca (04.2.1 do painel): profissional mas não fria, estratégica mas simples de entender, sofisticada mas acessível, humana e presente, sensorial ao falar de casas e experiências, objetiva ao falar de gestão e resultados.

### Formatação
- Zero travessão (—) em qualquer peça: posts, legendas, carrosséis, roteiros, JSON de imagem.
- Newsreader Italic é a única serifada permitida, e só numa palavra/frase curta emocional, nunca em título técnico.
- Não misturar Manrope e Sora no mesmo título; máximo 2 famílias tipográficas por peça visual.
- CTA sempre isolado na última linha, quase sempre "clica no link da bio" precedido de uma pergunta específica ao contexto da peça.

### Problemas estruturais recorrentes a evitar
- **Dashboard/painel inventado:** peças de Linha 5 (Por Dentro da Gestão) tendem a querer mostrar "tela de sistema" pra provar transparência. Errado: não existe painel próprio da BNB. Certo: é o próprio app do Airbnb do proprietário.
- **Decisão unilateral da Glauce:** roteiros institucionais tendem a escrever "eu decido o que fazer com o imóvel". Errado: ela apresenta as opções (Gestão do Anúncio ou Gestão Completa), quem escolhe é o proprietário.
- **Prova de contraste dourado ausente:** cards com headline + texto secundário (subtítulo ou frase de fechamento serifada) tendem a sair sem cor de contraste. Regra: o texto secundário/de fechamento recebe dourado fosco #A9782E por padrão, salvo exceção documentada (nome próprio/assinatura). Ver lição 13 de `feedback_bnb_connect_card_json.md` na memória.

### Exemplos: antes e depois

**Promessa absoluta ("garante"), não o uso de "a BNB Connect" em si**
✗ "A BNB Connect garante que o proprietário nunca perde o controle do imóvel." (problema é "garante", promessa absoluta, não o sujeito)
✓ "A gente entra como coanfitriã dentro do seu próprio anúncio. Você não perde o controle, só deixa de carregar a operação sozinho." (ou, variando o sujeito: "A BNB Connect entra como coanfitriã dentro do seu próprio anúncio.")

**Painel/dashboard inventado**
✗ "Acompanhe tudo pelo painel exclusivo da BNB Connect."
✓ "Você acompanha as reservas no seu próprio aplicativo do Airbnb e pode bloquear a agenda quando quiser usar o imóvel."

**Decisão unilateral**
✗ "Eu decido se cuido só do anúncio ou da operação inteira."
✓ "Você escolhe: continuar por perto, com a gente cuidando do anúncio e do preço, ou se afastar de verdade, com a gente assumindo a operação inteira."

> Adicione novos pares antes/depois à medida que forem descobertos em produção real (ver histórico de correções em `feedback_bnb_connect_producao.md` e `feedback_bnb_connect_card_json.md` na memória do projeto).

### O que nunca é problema: não proibir
- Frases curtas e diretas: é ritmo da voz, não sinal de IA (ver copy aprovada "Preço atrai. Experiência fideliza." em `references/copies-aprovadas.md`).
- Vocabulário técnico do nicho (RevPAR, ocupação, coanfitriã, calendário): são termos reais da área, não jargão a esconder.
- Número/dado abrindo a frase: abertura concreta é bem-vinda (ex: "Hoje são mais de 120 imóveis na carteira").

---

## 00-B | PADRÕES DE AUSÊNCIA DE VOZ

### Pontuação: ausências confirmadas
| Elemento | Regra | Evidência |
|---|---|---|
| Travessão (—) | NUNCA usar | 119 violações encontradas e corrigidas em auditoria retroativa, 10 set 2026; gate copy-qa obrigatório desde então |
| Ponto de exclamação em excesso | Evitar: tom é "claro e seguro", não empolgado | Nenhuma copy aprovada usa exclamação |

### Abertura: o que esta voz nunca faz
| Padrão | Regra | Evidência |
|---|---|---|
| "Você sabia que..." | Evitar: abre com observação concreta, não pergunta genérica de curiosidade | Nenhuma copy aprovada abre assim |
| "Nós somos a BNB Connect" | NUNCA: voz não abre se apresentando institucionalmente | Copy aprovada abre em afirmação/dado ("Preço atrai. Experiência fideliza.") |

### Fechamento: o que esta voz nunca faz
| Padrão | Regra | Evidência |
|---|---|---|
| CTA vago ("saiba mais", "descubra mais") | NUNCA: sempre uma pergunta específica + "clica no link da bio" | Banco de CTAs reais em `content-system.md` seção 04 |
| "Em conclusão..." / "Para finalizar..." | NUNCA | Ausente em toda copy real levantada |

### Vocabulário: palavras e expressões proibidas por ausência
| Palavra / Expressão | Por que ausente | Substituição |
|---|---|---|
| "Estrela" (nome da ferramenta de IA) | Uso estritamente interno, nunca em copy pública nem material interno de produção (confirmado 15 set 2026) | "tecnologia própria", "inteligência de negócio própria", "nossa camada de inteligência" |
| Promessa garantida de renda/resultado | Voz evita promessa absoluta (04.10 do painel) | "estimamos o potencial", "trabalhamos pra maximizar a performance" |
| Adjetivo de luxo isolado ("premium", "incrível", "robusto") | Evitar excesso de adjetivo de luxo sem dado (04.10) | Trocar por mecanismo real, número ou detalhe concreto |

### Estrutura: padrões que esta voz evita
| Padrão estrutural | Regra | Evidência |
|---|---|---|
| Dashboard/interface/gráfico inventado em imagem ou vídeo | NUNCA: quando aparecer tela, é o próprio Airbnb, real | Corrigido 11 set 2026, ver 07.1 do painel e `carrossel-cohosting-premium-referencia.md` |
| Decisão apresentada como unilateral da Glauce/equipe | NUNCA: proprietário sempre escolhe entre as opções apresentadas | Corrigido em revisão do roteiro 06.1, 10-11 set 2026 |
| Mais de 2 famílias tipográficas por peça visual | NUNCA (Inter em microinformação não conta) | Regra fixa do Sistema Editorial v1.1, item 04.2.1 |

### Tom: o que esta voz nunca soa
| Tom proibido | Evidência |
|---|---|
| Agressivo de venda | 04.10 do painel: "evitar tom agressivo de venda" |
| Genérico de administradora qualquer | 04.10: "evitar texto que poderia pertencer a qualquer administradora" |
| Motivacional/coach-speak | Ausente em toda copy real levantada; voz é estratégica, não inspiracional vazia |

> Novo padrão descoberto em produção: registrar aqui com data e contexto, seguindo o mesmo formato.
