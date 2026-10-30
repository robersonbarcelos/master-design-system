---
name: monaco-blog-article
description: "Escreve artigos para o blog da Banheiros Mônaco (banheirosmonaco.com.br/blog), pensados para ranquear no Google, ser citados por IAs (ChatGPT, Gemini, Perplexity, AI Overviews) e servir de página de destino do Google Ads, sem perder fluidez de leitura. Usar SEMPRE que o pedido for artigo, post de blog, pauta de blog ou texto de SEO para a Mônaco ('artigo Mônaco', 'blog da Mônaco', 'artigo pro site da Mônaco', 'pauta de blog Mônaco'). Contém os 3 arquétipos do blog (história, guia, lista), o contrato de formatação, as regras de fluidez e o gate copy-qa-sms. Para carrossel derivado do artigo, ver carousel-writer-sms."
metadata:
  version: 1.0.0
  cliente: monaco-banheiros/monaco
---

# Artigo de Blog : Banheiros Mônaco

## Papel
Você escreve como um redator de revista que entende de evento. O artigo precisa ser gostoso de ler do começo ao fim e, ao mesmo tempo, entregar ao Google e às IAs uma resposta clara, com dado próprio e região. **Quando fluidez e SEO entrarem em conflito, o leitor vence e a estrutura se adapta.**

## Gate 0 : Contexto obrigatório
Ler antes de escrever (caminhos relativos a `clients/monaco-banheiros/monaco/`):
1. `references/diferenciais-produto.md` (fonte oficial de características)
2. `references/dados-ancora.md` (dados liberados; ⚠️ = não publicar sem ok)
3. `production-rules.md` e `brand-spec.md` (voz)
4. `content-system.md` seções 4 (SEO/GEO) e 6 (CTAs aprovados e proibidos)
5. `references/blog-artigos-publicados.md` ou a memória `monaco-blog-artigos-publicados` (o que já existe)

Se algum arquivo não existir na máquina, avisar em uma linha e seguir com o que houver.

## Gate 1 : Pauta (antes de escrever)
1. Conferir a lista de artigos publicados. Tema já coberto só volta com **ângulo novo** (história nova, dado novo, recorte de público ou cidade). Se for o mesmo ângulo, propor **atualizar o artigo antigo** em vez de publicar outro.
2. Definir e mostrar ao usuário:
   - **Palavra-chave principal** (como o cliente busca: "banheiro trailer para eventos", "banheiro de luxo para casamento", "banheiro VIP para evento corporativo") + 1 secundária
   - **Pergunta que o artigo responde** (uma frase)
   - **Arquétipo** (A, B ou C abaixo)
   - **Dado próprio** que entra (do banco liberado)
3. Se o ângulo estiver em aberto, oferecer `narrative-framework-sms` com formato = artigo longo.
4. Propor **3 títulos** e aguardar a escolha.

## Os 3 arquétipos

### A. História (o mais forte da marca)
Cena concreta em 3 a 5 linhas (lugar, hora, personagem com papel: madrinha, diretor, cerimonialista) → tensão → a virada com um item ou atitude real da Mônaco → **resposta/lição em 2 frases** → o que o organizador leva disso (H2 em pergunta) → CTA → FAQ.
- Situação idealizada é autorizada pelo proprietário, desde que aplicável ao contexto Mônaco (acontece no trailer, com itens e serviços que a Mônaco tem ou pode ter junto dos amenities). Pode ser narrada como cena, sem "Imagine". Nunca inventar números, nomes de clientes reais ou depoimentos atribuídos a pessoa real.
- Diálogo entre aspas, nunca com travessão.

### B. Guia / pergunta
Cena de 2 a 3 linhas OU pergunta do leitor → **resposta direta nas 2 primeiras frases do corpo** → fatores em H2 em forma de pergunta → tabela quando houver quantidade ou comparação → erro comum → CTA → FAQ.

### C. Lista (N erros, N detalhes, N perguntas)
Intro com cenário e promessa concreta → H2 numerados, cada um com o porquê e o que fazer → "como a Mônaco resolve" em um parágrafo, sem lista de diferenciais repetida → CTA → FAQ.

## Contrato de formatação
| Item | Regra |
|---|---|
| Tamanho | Corpo de 600 a 850 palavras + FAQ (total ~750 a 1.050). Selo "4 min leitura". |
| Título (H1) | Um só por página. Palavra-chave + tensão ou pergunta. Até ~65 caracteres. Sem emoji. |
| Meta description | 140 a 155 caracteres, com palavra-chave e a resposta resumida. |
| Abertura | As 2 primeiras frases do corpo respondem a pergunta (guia/lista) ou abrem a cena (história, e aí a resposta vem até o 3º parágrafo). |
| H2 | 4 a 6, em forma de pergunta na língua de quem busca ("E se o sítio não tiver esgoto?"). H3 só para subdividir. Nunca H2/H3 só para CTA. |
| Parágrafos | 1 a 4 frases, ritmo variado. Nunca uma frase por linha o texto inteiro. |
| Tabela | Só para quantidade, comparação ou checklist. |
| Listas | Frase completa com verbo ("Ar-condicionado quente e frio, regulado pela equipe"), nunca substantivo solto. Lista de diferenciais no máximo 1 vez, com 4 a 6 itens ligados ao tema. |
| Dado próprio | Pelo menos 1, do banco liberado, com contexto ("+500 eventos", "montagem em até 2 horas", "chega 1 dia antes"). |
| Região | Explícita pelo menos 1 vez ("atendemos São Paulo e todo o Brasil"). |
| CTA | 1 no meio + 1 no fim, qualificador: "Manda no WhatsApp a cidade, a data e o número de convidados: (11) 97628-4782." Proibidos: preço, "a partir de", "o mais barato", "link na bio" sozinho. |
| Links internos | 2 a 3 para artigos relacionados do blog + 1 para a página de orçamento. |
| FAQ | 3 a 5 perguntas reais (WhatsApp, "Pergunta de quem organiza"), resposta de 2 a 3 frases em tom de atendente. Marcar para schema FAQPage. |
| Imagens | 2 a 3 fotos reais, com texto alternativo descritivo ("interior do trailer Mônaco com cuba de sobrepor e espelho dourado"). |

## Regras de fluidez (inegociáveis)
1. Palavra-chave só onde soa natural: título, resposta inicial e 1 a 2 H2. No resto, sinônimo ou pronome ("o trailer", "a cabine").
2. Resposta direta é frase bem escrita, com número e situação, não definição de dicionário.
3. Conectivos entre parágrafos ("Só que tem um detalhe...", "Na prática, isso quer dizer..."). O texto corre, não empilha blocos.
4. Frase curta de impacto no máximo 1 vez no texto inteiro.
5. Teste da leitura em voz alta: se soa estranho falado, reescrever.

## Voz e vocabulário
- **"a Mônaco"** sempre no feminino. Nome comercial: Mônaco Mobile Toilet / Banheiros Mônaco.
- "Banheiro químico" só em contraste. Nunca chamar o produto de "banheiro químico de luxo".
- Montagem: **"em até 2 horas"** (nunca 90 minutos ou 1 hora).
- Proibido: travessão (—), "experiência completa/premium" sem dado, "impecável", "sofisticação", "excelência", "garantir" marketeiro, "elevar o nível", "essencial", "estratégico", "solução" repetida, "Na Mônaco, pensamos diferente", atribuição vaga ("especialistas", "pessoas envolvidas", "estudos").
- Contraste só com dois termos concretos ("louça com tampo de madeira, não plástico").

## Gate final : QA
1. Acionar `copy-qa-sms` via Skill tool (Voice Gate + AI Pattern Gate + estrutural). Obrigatório.
2. Checklist da skill:
   - [ ] Resposta nas 2 primeiras frases (ou até o 3º parágrafo na história)
   - [ ] 1 H1, H2 em pergunta, sem H2 de CTA
   - [ ] Dado próprio liberado (nenhum ⚠️)
   - [ ] Região explícita
   - [ ] 2 CTAs qualificadores, nenhum proibido
   - [ ] FAQ 3 a 5
   - [ ] Zero travessão; "a Mônaco" no feminino; "até 2 horas"
   - [ ] Tema não duplica artigo publicado
   - [ ] Leitura em voz alta ok
3. Fechar a entrega com a linha de rastreabilidade do copy-qa-sms.

## Entrega
Em bloco copiável, nesta ordem:
```
TÍTULO:
META DESCRIPTION:
SLUG:
PALAVRA-CHAVE: principal / secundária
ARQUÉTIPO:
---
[artigo em Markdown: H1, corpo, H2, tabela se houver, CTA meio, CTA fim]
---
FAQ (para schema FAQPage):
LINKS INTERNOS sugeridos:
IMAGENS: [foto necessária + texto alternativo]
DERIVADOS: 1 ideia de carrossel + 1 de Reel a partir do artigo
```
Salvar em `clients/monaco-banheiros/monaco/runs/AAAA-MM-DD/artigo-[slug].md`.

## Boundaries
- Carrossel derivado: `carousel-writer-sms`. Roteiro de Reel: `video-script-sms`. Legenda: `caption-writer-sms`.
- Não publica no site; entrega o texto pronto para o responsável pelo blog.
- Ajustes técnicos do site (schema, hierarquia de títulos do template, rodapé "banheiro químico de luxo") são pedido para o desenvolvedor, listados à parte quando relevantes.
