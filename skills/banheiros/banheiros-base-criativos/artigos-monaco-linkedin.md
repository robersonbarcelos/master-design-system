# Artigos LinkedIn: Mônaco Banheiros (modelagem)

Base: 3 artigos Pulse da página Mônaco Banheiros no LinkedIn (17/06/2026 reforma comercial sem interromper o negócio; 28/07/2026 logística para eventos em todo o Brasil; 03/09/2026 evento ao ar livre). Quando o pedido for artigo de LinkedIn da Mônaco, usar este modelo e NÃO o modelo de blog (skill-banheiros). O artigo de LinkedIn é um formato à parte, com objetivo próprio.

## Objetivo
Posicionamento da marca e geração de lead de empresário e organizador de evento. Não é SEO, não é página de destino do Google Ads.

## Estrutura (modelo aprovado)
- **Autor:** a página da marca, Mônaco Banheiros (não Marcelo Martins como no blog).
- **Título:** frase de efeito ou pergunta, sem palavra-chave técnica. Subtítulo opcional que entrega o tema.
- **Abertura:** 1 a 3 frases curtas com a dor ou a pergunta que o cliente faz.
- **Corpo:** 4 a 6 H2 em forma de frase de efeito ("Estrutura não é detalhe. É experiência.", "Quanto custa não ter uma solução?"). Subtítulos numerados (1., 2., 3.) quando houver passos ou cuidados. Listas curtas de benefícios.
- **Cena:** um bloco "Imagine a seguinte situação:" com a cena do cliente.
- **CTA:** de 2 a 3 vezes ("Solicite seu orçamento"), uma delas no meio do texto. Pode vir junto de um link de vídeo de case.
- **Fechamento:** frase de efeito que resume a tese ("A distância não é o desafio. O planejamento é.").
- **Tamanho:** 450 a 600 palavras.
- **Sem FAQ. Sem links internos de blog.** Só o CTA.
- **Tom:** persuasão e storytelling, direto ao empresário.
- **Símbolos:** ✔ e 👉 aparecem no original; usar com moderação nas listas e no CTA.

## O que pode (diferente da LABELLE)
- Dizer que os trailers têm ar-condicionado e ambiente climatizado (é verdade para a Mônaco): vaso e pia de louça, torneiras de metal, secadores de mão, ambiente decorado, água limpa, equipe de limpeza durante o evento, acabamento premium padrão residencial.
- Citar cliente, local ou case real com nome (ex.: cervejaria Baden Baden) **quando a pauta for aprovada pelo usuário**. Sem aprovação da pauta, não citar nome.
- Prazos já publicados no LinkedIn: até 700 km, cerca de 1 dia; de 700 a 1.400 km, cerca de 2 a 3 dias; acima de 1.400 km, conforme localização e complexidade; montagem em até 2 horas. Manter os mesmos números em textos novos para não contradizer o que foi postado.
- Sistema autossuficiente, sem ligação com esgoto.

## O que continua valendo (copy-qa-sms)
- Sem travessão.
- No máximo 1 uso de frases curtas soltas (staccato) por texto inteiro. O original usa muitas linhas isoladas; no nosso modelo reduzir.
- Pergunta de venda ("Quanto custa não ter uma solução?") precisa de um dado concreto ou de uma cena que dê base, não só retórica.
- Nada de número, cliente ou depoimento inventado. Situação idealizada só se aplicável ao trailer e às amenities (ver feedback da Mônaco).
- Nunca posicionamento político.
- Pelo Gate de Skill de Criação, acionar `article-writer-sms` e passar pelo `copy-qa-sms` antes de entregar.

## Diferenças em relação ao blog da Mônaco
| Ponto | LinkedIn | Blog |
|---|---|---|
| Objetivo | Posicionamento e lead | SEO, GEO e destino do Ads |
| Título | Frase de efeito ou pergunta | Palavra-chave, title tag até 60 caracteres, meta description |
| Estrutura | H2 retóricos, listas de benefícios | H1 e H2 informativos |
| FAQ e links internos | Não tem | FAQ de 4 perguntas e links internos |
| CTA | 2 a 3 vezes | 1 vez, no fim (o site insere o bloco) |
| Autor | Página da marca | Marcelo Martins |
| Tamanho | 450 a 600 palavras | cerca de 760 palavras |

## Capa LinkedIn (banner com texto embutido)
Estrutura e fontes da arte de referência "Conforto para o agro" (cartão com moldura creme, aba com logo, eyebrow espaçado, headline em serifa com dourado degradê, pílula dourada no rodapé), em 16:9 1600x900. **Cores normais da Mônaco: azul marinho, dourado e creme. Nunca roxo, violeta ou índigo.** Template oficial: `clients/monaco-banheiros/monaco/references/template-json-capa-linkedin.md`. Os JSONs de cada lote ficam em `runs/AAAA-MM-DD/capas-linkedin-monaco.md`, com título de cena e o que anexar (foto do trailer ou da bancada, logo Mônaco e a arte de referência só para estilo).

## Dados fixos da Mônaco nos textos
- **Telefone e WhatsApp:** (11) 97628-4782 (nunca o (11) 95223-2818, que é da LABELLE).
- **CTAs aprovados, alternar entre peças:** meio do texto "Solicite seu orçamento pelo WhatsApp: (11) 97628-4782."; fim "Quer levar essa ideia para o seu evento? A gente prepara o espaço com você. Chama a gente no WhatsApp (11) 97628-4782." (trocar "evento" pelo tema); assinatura opcional "Toda ideia precisa de um lugar à altura. A Mônaco cuida desse lugar."
- **Dados liberados:** mais de 500 eventos desde 2019, montagem em até 2 horas, chega 1 dia antes, "atendemos São Paulo e todo o Brasil". Sobre cheiro: "o objetivo é que não exista cheiro". "Banheiro químico" só em contraste. Sempre "a Mônaco".

## Processo validado (passo a passo)
1. **Origem:** partir de um artigo de blog Mônaco já aprovado. Nome de cliente ou case só com a pauta aprovada.
2. **Skills de verdade:** chamar a skill `article-writer-sms` com o Skill tool (e `narrative-framework-sms` se o ângulo estiver em aberto) e ler `monaco.md`. Mostrar o arco só se o ângulo mudar em relação ao artigo de origem.
3. **Escrever:** 450 a 600 palavras, no máximo 6 H2, estrutura acima. Arquivo `.md` com cabeçalho (MARCA, AUTOR, FORMATO, ORIGEM, H1), texto entre `---` e NOTAS no fim. Histórias idealizadas avisadas no texto ("é uma cena ilustrativa").
4. **Copy-qa de verdade:** chamar `copy-qa-sms` com o Skill tool e fazer a varredura Tier 1, 2 e 3 e os padrões estruturais. Conferir as regras da marca: telefone da Mônaco, ar-condicionado liberado, dados do perfil, sem travessão. Relatar o resultado e a linha de rastreabilidade. Nunca dizer "conferi" só com um script próprio.
5. **`.docx`:** gerar pelo gerador de `.docx` e checar H1, H2 e ausência de erro.
6. **Entregar:** colar os textos no chat em bloco copiável, dizer a pasta e listar com honestidade o que foi pulado ou decidido sem aprovação.
7. **Depois de aprovado:** copiar `.md` e `.docx` para `C:\ARQUIVOS\JOBS E EMPREGOS\BANHEIROS MONACO\PRODUZIDOS\artigos monaco\[slug do artigo de blog]\` com o prefixo `linkedin-`, sem sobrescrever.
8. **Capas:** primeiro 3 ideias por artigo (gancho curto, cena e o que anexar), sem JSON; o usuário escolhe; depois os JSONs completos no chat a partir do template, cada um com título de cena e anexos.

## Entrega
Salvar em `clients/monaco-banheiros/monaco/runs/AAAA-MM-DD/linkedin-[slug].md` e `.docx`. Depois de aprovado, copiar para `artigos monaco\[slug]\` (passo 7). Colar o texto no chat em bloco copiável.
