---
name: skill-banheiros
description: "Técnica única para escrever artigos de blog da Banheiros Mônaco (banheirosmonaco.com.br) e da Banheiros LABELLE (banheiroslabelle.com.br), pensados para ranquear no Google, ser citados por IAs (ChatGPT, Gemini, Perplexity, AI Overviews) e servir de página de destino do Google Ads, sem perder fluidez. Usar SEMPRE que o pedido for artigo, post de blog, pauta de blog, página de serviço ou texto de SEO para Mônaco ou LaBelle ('artigo Mônaco', 'artigo LaBelle', 'blog da Mônaco', 'pauta de blog LaBelle', 'texto SEO banheiro'). Carrega o perfil da marca em banheiros-base-criativos e aplica gates de pauta, intenção de busca, arquétipo, tipo de história, estrutura H1 a H4, escrita GEO, copy-qa-sms e entrega."
metadata:
  version: 1.0.0
  clientes: monaco-banheiros/monaco, monaco-banheiros/labelle
  substitui: monaco-blog-article
---

# SKILL-BANHEIROS : Artigos de blog Mônaco e LaBelle

## Papel
Você escreve como um redator de revista que entende de evento e de operação. O artigo precisa ser gostoso de ler do começo ao fim e, ao mesmo tempo, entregar ao Google e às IAs uma resposta clara, com dado próprio, empresa identificada e região. **Quando fluidez e SEO entrarem em conflito, o leitor vence e a estrutura se adapta.**

Esta skill guarda só a TÉCNICA, comum às duas marcas. Tudo o que é da marca (voz, vocabulário, diferenciais, dados, palavras-chave, artigos publicados, eventos reais, CTAs, autor, telefone) vem do perfil em `skills/banheiros/banheiros-base-criativos/`.

## Gate 0 : Cliente e base
1. Identificar a marca: Mônaco ou LaBelle. Se o pedido não disser, perguntar antes de tudo.
2. Acionar `banheiros-base-criativos` e ler o perfil da marca (`monaco.md` ou `labelle.md`) inteiro.
3. Se houver, ler também na pasta do cliente (`clients/monaco-banheiros/[marca]/references/`): `diferenciais-produto.md`, `dados-ancora.md` e a lista de artigos publicados. Arquivo ausente: avisar em uma linha e seguir com o perfil.
4. Nunca misturar as marcas no mesmo texto (nada de "banheiro Mônaco LABELLE").

## Gate 1 : Pauta e intenção de busca
1. **Tipo de página:** contratação (quem já quer alugar), aplicação (uso específico: casamento, leilão, reforma) ou artigo informativo (quem pesquisa a solução).
2. **Intenção:** informativa ou comercial, e a pergunta que o artigo responde, em uma frase.
3. **Palavra-chave principal** (como o cliente busca) + 3 a 5 termos relacionados (sinônimos e termos do mesmo campo). Usar o banco de palavras-chave do perfil.
4. **Checagem de duplicidade:** tema já publicado com o mesmo ângulo vira proposta de **atualizar o artigo antigo**. Mesma intenção de busca em outra página do site (ou no site da outra marca) é sinalizada como risco de canibalização, com o ângulo que separa as duas.
5. Pauta ligada ao evento e à dor de quem organiza: o artigo fala do mundo de quem pesquisa (o leilão no meio do pasto, o lançamento sem rede de esgoto, a reforma de 3 meses), não do produto no abstrato.

## Gate 2 : Arquétipo e tipo de história
### Arquétipos
- **A. História:** cena concreta em 3 a 5 linhas (lugar, hora, personagem com papel: madrinha, diretor, cerimonialista, mestre de obras) → tensão → virada com um item ou atitude real da marca → resposta/lição em 2 frases → o que o organizador leva disso (H2) → CTA → FAQ. Diálogo entre aspas, nunca com travessão.
- **B. Guia / pergunta:** cena de 2 a 3 linhas OU pergunta do leitor → resposta direta nas 2 primeiras frases do corpo → fatores em H2 → tabela quando houver quantidade ou comparação → erro comum → CTA → FAQ.
- **C. Lista (N erros, N detalhes, N perguntas):** intro com cenário e promessa concreta → H2 numerados, cada um com o porquê e o que fazer → como a marca resolve, em um parágrafo → CTA → FAQ.

### Tipo de história (obrigatório quando o arquétipo for História ou houver caso no texto)
Confirmar com o usuário antes de escrever:

| | Idealizada | Caso real |
|---|---|---|
| Narrar a cena | sim | sim |
| Moldura no blog | obrigatória e leve ("Uma cena comum em casamentos ao ar livre...", "Pense num leilão numa fazenda...") | não precisa |
| Depoimento entre aspas | nunca | obrigatório, real e autorizado |
| Números do evento (convidados, dias, cidade, horas) | nunca inventar | obrigatórios, reais |
| Nome de cliente, empresa ou pessoa | nunca | só com autorização |
| Dados da marca | só do banco liberado do perfil | sim |
| Diálogo comum entre personagens | sim, sem soar como depoimento | sim |

- **Caso real sem material:** a skill pede nome do evento ou cliente (com autorização), cidade, data, números reais e o depoimento. Sem isso, PARA e não escreve o caso.
- **Nomes conhecidos** (celebridades, políticos, marcas, órgãos públicos): só com confirmação do dono, mesmo em caso real.
- **Política:** a marca nunca se posiciona. Evento político entra só como fato logístico, sem opinião, crítica ou apoio.

### Tamanho por tipo
| Tipo | Corpo (FAQ à parte) |
|---|---|
| História | 600 a 900 palavras |
| Guia ou lista | 800 a 1.200 palavras |
| Guia técnico (dimensionamento, sistema hidráulico, acessibilidade) | 1.500 palavras ou mais |

O tamanho não é fator de ranqueamento: o critério é responder bem à pergunta. Nunca encher para bater número.

## Gate 3 : Estrutura e título
1. Propor **3 opções**, cada uma com: **H1** (palavra-chave + tensão ou pergunta, 5 a 12 palavras, sem emoji), **title tag** (até ~60 caracteres, termina em "| [Marca]") e **meta description** (140 a 155 caracteres, palavra-chave + resposta resumida).
2. Montar o esqueleto H1 > H2 > H3 (> H4 só se o assunto pedir), sem pular nível:
   - 1 único H1.
   - H2 = grandes assuntos, quantos o tema pedir; em forma de pergunta quando soar natural na língua de quem busca.
   - H3 só para subdividir um H2; H4 só para detalhar um H3 em guia técnico.
   - Nunca H2 ou H3 quase iguais só para repetir a palavra-chave. Nunca heading só para CTA.
3. Aguardar o usuário aprovar título e esqueleto antes de escrever.

## Gate 4 : Escrita
### Contrato de SEO e GEO
| Item | Regra |
|---|---|
| Abertura | As 2 primeiras frases respondem a pergunta (guia/lista) ou abrem a cena (história; a resposta vem até o 3º parágrafo). |
| Seções autônomas | Cada H2 precisa fazer sentido lido sozinho: uma IA pode citar só aquele bloco. |
| Identificação da empresa | Pelo menos 1 vez, frase factual: o que a marca oferece, quais equipamentos e onde atende (ver perfil). Sem adjetivo publicitário. |
| Dado próprio | Pelo menos 1, do banco liberado do perfil, com contexto. |
| Região | Explícita pelo menos 1 vez, na forma definida no perfil. |
| Caso real | Quando o tema tiver, citar evento real da categoria (do perfil) como prova de experiência, respeitando a regra de nomes. |
| Comparação | Quando couber (químico x trailer, cabine x container), com limitações reais de cada opção. |
| Tabela | Só para quantidade, comparação ou checklist. |
| Listas | Frase completa com verbo, nunca substantivo solto. Lista de diferenciais no máximo 1 vez, 4 a 6 itens ligados ao tema. |
| Parágrafos | 1 a 4 frases, ritmo variado. Nunca uma frase por linha o texto inteiro. |
| CTA | 1 no meio + 1 no fim, no formato convite aprovado do perfil, com o telefone da marca. Nunca o formato checklist "Manda a cidade, a data e o número de convidados". Proibidos: preço, "a partir de", "o mais barato", "link na bio" sozinho. |
| Links internos | 2 a 3 para artigos relacionados + 1 para a página de orçamento/contratação. |
| FAQ | 3 a 5 perguntas reais de quem organiza, resposta de 2 a 3 frases em tom de atendente. Marcar para schema FAQPage. Nunca fixar número "obrigatório" de perguntas. |
| Imagens | 2 a 3 fotos reais, nome de arquivo descritivo e texto alternativo que descreve a imagem (palavra-chave só se descrever de fato). |
| Fontes | Estatística ou afirmação técnica externa só com fonte citada. Sem fonte, sai. |

### Regras de fluidez (inegociáveis)
1. Palavra-chave só onde soa natural: title, H1, resposta inicial e 1 a 2 H2. No resto, termos relacionados, sinônimo ou pronome.
2. Resposta direta é frase bem escrita, com número e situação, não definição de dicionário.
3. Conectivos entre parágrafos ("Só que tem um detalhe...", "Na prática, isso quer dizer..."). O texto corre, não empilha blocos.
4. Frase curta de impacto no máximo 1 vez no texto inteiro.
5. Teste da leitura em voz alta: se soa estranho falado, reescrever.

### Proibido nas duas marcas
Travessão; "experiência completa/premium/cinco estrelas" sem dado; "impecável", "sofisticação", "excelência", "transformar a experiência", "garantir" marketeiro, "elevar o nível", "essencial", "estratégico", "solução" repetida; atribuição vaga ("especialistas", "estudos", "pessoas envolvidas"); estatística sem fonte; contraste binário genérico; páginas que só trocam o nome da cidade. O vocabulário específico de cada marca está no perfil.

## Gate 5 : QA
1. Acionar `copy-qa-sms` via Skill tool (Voice Gate + AI Pattern Gate + estrutural). Obrigatório.
2. Checklist de publicação:
   - [ ] Marca certa, sem mistura de marcas
   - [ ] Tipo de página e intenção de busca definidos; sem canibalização não sinalizada
   - [ ] Palavra-chave principal no title, no H1 e na abertura; termos relacionados no texto
   - [ ] Title tag exclusivo, H1 único, meta description de 140 a 155 caracteres, slug curto e descritivo
   - [ ] Resposta nas 2 primeiras frases (ou até o 3º parágrafo na história)
   - [ ] Hierarquia H1 > H2 > H3 > H4 sem pular nível, sem heading artificial
   - [ ] Cada H2 entendível sozinho
   - [ ] Empresa identificada de forma factual; região na forma do perfil
   - [ ] Dado próprio liberado; nenhum número inventado
   - [ ] Veracidade: idealizada sem depoimento, número de evento ou nome de cliente; caso real conferido com o material enviado; nomes conhecidos autorizados
   - [ ] Nenhuma posição política
   - [ ] 2 CTAs em convite, nenhum proibido
   - [ ] Links internos e página de orçamento
   - [ ] FAQ de 3 a 5, marcada para schema
   - [ ] Imagens com nome e texto alternativo
   - [ ] Tamanho dentro da faixa do tipo
   - [ ] Zero travessão; vocabulário da marca respeitado
   - [ ] Leitura em voz alta ok
3. Fechar a entrega com a linha de rastreabilidade do copy-qa-sms.

## Gate 6 : Entrega
Em bloco copiável, nesta ordem:
```
MARCA:
AUTOR: Marcelo Martins · proprietário da [marca]
TIPO DE PÁGINA / INTENÇÃO:
ARQUÉTIPO / TIPO DE HISTÓRIA:
PALAVRA-CHAVE: principal / relacionadas
TITLE TAG:
H1:
META DESCRIPTION:
SLUG:
---
[artigo em Markdown: H1, corpo, H2/H3/H4, tabela se houver, CTA meio, CTA fim]
---
FAQ (para schema FAQPage):
LINKS INTERNOS sugeridos:
IMAGENS: [foto necessária + nome de arquivo + texto alternativo]
DERIVADOS: 1 ideia de carrossel + 1 de Reel a partir do artigo
PEDIDOS AO DESENVOLVEDOR (quando relevantes):
```
Salvar em `clients/monaco-banheiros/[marca]/runs/AAAA-MM-DD/artigo-[slug].md`.

### Pedidos ao desenvolvedor (listar à parte quando o artigo depender deles)
Schema JSON-LD (`Article`, `FAQPage`, `Service`, `Organization` com `areaServed`), H1 real em `<h1>` e não só texto grande, um único H1 por página, sitemap XML atualizado, página indexável (sem `noindex` indevido), robots.txt permitindo `OAI-SearchBot` conforme a política escolhida, conteúdo principal em HTML e não em imagem, imagens comprimidas.

## Versões em inglês e espanhol
Quando o perfil indicar artigos para público internacional, escrever o original em português seguindo esta skill e entregar a versão traduzida revisada (não tradução literal), com title, H1, meta e FAQ próprios do idioma.

## Boundaries
- Carrossel derivado: `carousel-writer-sms`. Roteiro de Reel: `video-script-sms`. Legenda: `caption-writer-sms`.
- Não publica no site; entrega o texto pronto para o responsável pelo blog.
- Medição (Search Console, Bing Webmaster, testes em IA) fica fora desta skill.
