# Artigos LinkedIn: LABELLE (modelagem)

Base: o modelo dos 3 artigos Pulse da página Mônaco Banheiros no LinkedIn (ver `artigos-monaco-linkedin.md`), adaptado ao perfil da LABELLE. A LABELLE ainda não tem artigos próprios no LinkedIn analisados; este arquivo aplica a mesma estrutura com as regras da marca. Para artigo de LinkedIn da LABELLE, usar este modelo e NÃO o de blog (skill-banheiros).

## Objetivo
Posicionamento e lead de empresário, construtora, incorporadora, síndico e responsável por obra ou local de difícil acesso. Não é SEO nem página de destino do Google Ads.

## Estrutura (mesma do modelo Mônaco)
- **Autor:** a página da marca, Banheiros LABELLE.
- **Título:** frase de efeito ou pergunta, sem palavra-chave técnica. Subtítulo opcional.
- **Abertura:** 1 a 3 frases curtas com a dor do cliente.
- **Corpo:** 4 a 6 H2 em forma de frase de efeito. Subtítulos numerados quando houver passos. Listas curtas de benefícios.
- **Cena:** bloco "Imagine a seguinte situação:".
- **CTA:** 2 a 3 vezes, uma no meio. Telefone e WhatsApp oficial: **(11) 95223-2818**.
- **Fechamento:** frase de efeito com a tese.
- **Tamanho:** 450 a 600 palavras. Sem FAQ. Sem links internos de blog.
- **Tom:** persuasão e storytelling, direto ao empresário.

## Regras da LABELLE (diferentes da Mônaco)
- **Sem climatização:** os módulos não têm ar-condicionado. Nunca escrever "climatizado" ou "ar-condicionado".
- **Produto:** módulo branco; vaso com descarga, pia, gabinete, espelho, iluminação interna, fechadura, indicador livre/ocupado, exaustão, dispensers, sem odor, área descoberta.
- **Modos:** autônomo (caixa d'água e tanque lacrado, vaso de pedal) ou ligado à rede de esgoto. Locação de semanas a meses. Pronta entrega. Orçamento em até 2 horas úteis. Todo o Brasil, prioridade Sudeste, Sul e Centro-Oeste.
- **Não usar:** preço, medidas em número (até o dono confirmar) e dados não validados pelo Marcelo.
- **Cliente, local ou case com nome:** pode, desde que a pauta tenha sido aprovada pelo usuário.
- **Telefone:** sempre (11) 95223-2818. Nunca o (11) 97628-4782 (é da Mônaco).

## O que continua valendo (copy-qa-sms)
Sem travessão; no máximo 1 uso de staccato por texto; pergunta de venda com dado ou cena concreta; nada de número, cliente ou depoimento inventado. Acionar `article-writer-sms` e passar pelo `copy-qa-sms` antes de entregar.

## Capa LinkedIn (banner com texto embutido)
Modelo adaptado dos banners LinkedIn da Mônaco (pasta `C:\ARQUIVOS\JOBS E EMPREGOS\BANHEIROS MONACO\exemplo de banners linkedin`): 16:9, 1600x900, com recuos (faixa clara de cerca de 100 px em cima e embaixo e 130 px nas laterais) e moldura fina dourada arredondada. **Fundo SEMPRE claro (creme `#FAF7F1`), nunca verde nem escuro**: o layout dos banners da Mônaco é escuro, mas na LABELLE só a estrutura é copiada, nunca as cores. Esquerda: gancho curto em 2 ou 3 linhas (a palavra-chave numa barra dourada com texto verde-petróleo), linha de apoio e 3 ícones de linha com legenda curta. Direita: foto da cabine LABELLE dentro do contexto do artigo, fundida ao fundo. Logo da LABELLE no canto superior direito.
- Cores: fundo creme `#FAF7F1` (claro); texto do gancho e das legendas em verde-petróleo `#043333` (cor de texto da marca, nunca fundo); barra e detalhes em dourado `#B7881D`; logo na versão dourada sobre creme.
- Fonte do gancho: Cinzel Regular 400, caixa alta, fina e delicada (a mesma do headline do Reel de Halloween da Mônaco). Textos de apoio e legendas: sans fina estilo Montserrat Medium.
- Ícones: só benefícios confirmados no perfil (sem climatização, sem preço, sem medida).
- JSON: `reference_lock` da cabine + `layout_reference` (banner da Mônaco só como layout) + `brand_logo` + `canvas` + `typography` + `text_elements` com o texto exato. Título do bloco no formato canônico (cena e o que anexar: foto da cabine, logo e banner de layout).
- Os JSONs ficam em `runs/AAAA-MM-DD/capas-linkedin-labelle.md`.
- **Template oficial (versão clara, a única):** `clients/monaco-banheiros/labelle/references/template-json-capa-linkedin.md`. Usar sempre este template; a versão com fundo verde-petróleo foi descartada e não existe como opção.

## Processo validado (passo a passo)
1. **Origem:** partir de um artigo de blog LABELLE já aprovado. Nome de cliente ou case só com a pauta aprovada pelo usuário.
2. **Skills de verdade:** chamar a skill `article-writer-sms` com o Skill tool (e `narrative-framework-sms` se o ângulo estiver em aberto) e ler `labelle.md`. Mostrar o arco só se o ângulo mudar em relação ao artigo de origem.
3. **Escrever:** 450 a 600 palavras, no máximo 6 H2, estrutura acima. Arquivo `.md` com cabeçalho (MARCA, AUTOR, FORMATO, ORIGEM, H1), texto entre `---` e NOTAS no fim.
4. **Copy-qa de verdade:** chamar `copy-qa-sms` com o Skill tool e fazer a varredura Tier 1, 2 e 3 e os padrões estruturais. Conferir também as regras da marca: nenhuma climatização, telefone (11) 95223-2818, sem travessão, sem preço ou medida. Relatar o resultado e a linha de rastreabilidade. Nunca dizer "conferi" só com um script próprio.
5. **`.docx`:** gerar pelo gerador de `.docx` e checar H1, H2 e ausência de erro.
6. **Entregar:** colar os textos no chat em bloco copiável, dizer a pasta e listar com honestidade o que foi pulado ou decidido sem aprovação (arco, escolha de temas, trechos pendentes do Marcelo).
7. **Depois de aprovado:** copiar `.md` e `.docx` para `C:\ARQUIVOS\JOBS E EMPREGOS\BANHEIROS MONACO\PRODUZIDOS\ARTIGOS LA BELLE\[slug do artigo de blog]\` com o prefixo `linkedin-`, sem sobrescrever.
8. **Capas:** primeiro 3 ideias por artigo (gancho curto, cena e o que anexar), sem JSON; o usuário escolhe; depois os JSONs completos no chat a partir do template, cada um com título de cena e anexos.

## Entrega
Salvar em `clients/monaco-banheiros/labelle/runs/AAAA-MM-DD/linkedin-[slug].md` e `.docx`. Depois de aprovado, copiar para a pasta `ARTIGOS LA BELLE\[slug]\` (passo 7). Colar o texto no chat em bloco copiável.
