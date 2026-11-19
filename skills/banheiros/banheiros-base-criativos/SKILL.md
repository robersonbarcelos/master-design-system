---
name: banheiros-base-criativos
description: "Base de criativos, ideias, estilos e perfil de marca da Banheiros Mônaco e da Banheiros LABELLE: voz, vocabulário, diferenciais confirmados, dados liberados, palavras-chave, eventos reais, calendário de pautas, CTAs aprovados, região e regras de cada marca. Acionada pela skill-banheiros no Gate 0, e também quando o pedido for pauta, ideia de conteúdo, storytelling ou carrossel da Mônaco ou da LaBelle ('ideias Mônaco', 'pauta LaBelle', 'história para a Mônaco', 'o que a Mônaco já fez')."
metadata:
  version: 1.0.0
  clientes: monaco-banheiros/monaco, monaco-banheiros/labelle
---

# Base de criativos : Mônaco e LaBelle

## Como usar
1. Ler a **Base comum** abaixo (vale para as duas marcas).
2. Ler o perfil da marca: `monaco.md` ou `labelle.md` (nesta pasta).
2b. Se o pedido for **artigo de LinkedIn** (formato Pulse, não é o blog): ler `artigos-monaco-linkedin.md` ou `artigos-labelle-linkedin.md` em vez do modelo de blog. Neles, cliente, local ou case com nome (ex.: Baden Baden) pode ser citado quando o usuário aprovar a pauta.
3. Quando existir, conferir na pasta do cliente (`clients/monaco-banheiros/[marca]/references/`) `diferenciais-produto.md` e `dados-ancora.md`: eles são a fonte oficial e vencem este perfil em caso de divergência. Avisar o usuário sobre a divergência.
4. Dado marcado ⚠️ não vai para texto publicado sem confirmação do dono.

## Base comum (white label)
- **Quem fala pelas marcas:** Marcelo, dono da Mônaco e da LABELLE. "O dono" nesta base = Marcelo. Diego é do Intus Hub e não fala por estas marcas.
- **Histórias:** idealizada pode narrar a cena (no blog, com moldura leve: "Uma cena comum em..."), sem depoimento, sem número do evento e sem nome de cliente. Caso real exige dado e depoimento reais e autorizados.
- **Nomes conhecidos** (celebridades, políticos, marcas, órgãos públicos): só com confirmação do dono.
- **Política:** nunca se posicionar. Evento político = fato logístico, sem opinião.
- **"Banheiro químico"** só em contraste, nunca como nome do produto.
- **Nunca misturar as marcas** no mesmo texto.
- **CTA:** convite natural, nunca checklist de dados ("Manda a cidade, a data e o número de convidados" é vetado).
- **Princípio de pauta (do dono):** o texto fala do evento e da dor de quem organiza; citar eventos reais da categoria dá autoridade.
- **Separação de ângulo entre as marcas** (evita as duas disputarem a mesma busca): Mônaco = evento premium de 1 a 3 dias, trailer com equipe; LaBelle = locação longa (semanas e meses), operação, obra, reforma e locais de difícil acesso.

## Calendário de pautas (as duas marcas, publicar na véspera)
Réveillon · carnaval · dia das mães · festa junina e São João · dia dos pais · dia das crianças · Finados · Natal e festas de fim de ano. Datas sem experiência real (ex.: carnaval na Mônaco) entram como guia para quem procura, sem afirmar evento feito.

## Padrão de JSON de imagem com a cabine/produto da marca (obrigatório)
Vale para capa de artigo e para qualquer imagem em que o produto (cabine LABELLE, trailer Mônaco) apareça dentro da cena gerada por IA. O produto nunca é inventado só por texto: entra uma **foto real de referência** anexada à geração, e o JSON traz o bloco `reference_lock`.

Campos do JSON (completo, sempre): `format`, `style`, `reference_lock`, `subject`, `lighting`, `camera`, `palette`, `composition`, `mood`, `quality`, `negative`.

`reference_lock` tem 4 partes:
- `reference_image`: a foto real anexada.
- `instruction`: usar a imagem anexada como modelo exato; não inventar outro desenho.
- `preserve_exactly`: forma e proporções, porta e fechadura, acabamento, cantos e teto, aberturas e indicador, logo e posição, material e cor.
- `do_not`: redesenhar, acrescentar janela ou porta, trocar cor, acrescentar ar-condicionado, texto ou logo novo.
- `adapt_to_scene`: escala real, perspectiva e linha do horizonte, direção e temperatura da luz, sombra de contato, reflexo ambiente e color grading iguais ao resto da foto.

Regras: o `subject` descreve só o cenário e chama o produto de "the cabin from the reference image". Sem medida em número até o dono confirmar. `negative` sempre termina com "a different cabin design from the reference". Com foto de referência, rodar antes a skill `json-prompt-generator`. Entregar 3 JSONs separados, completos, colados no chat.

### Título de cada bloco JSON (canônico)
Cada JSON vem colado no chat dentro do próprio bloco de código, com **dois títulos em negrito acima dele**:
1. `ARTIGO [nº] · [TEMA EM CAIXA ALTA]`
2. `OPÇÃO [A/B/C]: [TIPO DE CENA] · [enquadramento], [luz/hora], [elementos de contexto que identificam o tema], [pessoas se houver]. Anexar: [qual foto carregar]`

Exemplo: `ARTIGO 10 · MONTAGEM EM ATÉ 2 HORAS` / `OPÇÃO A: EXTERNA · picape rebocando o trailer na chegada, 3/4 traseiro, amanhecer, dois membros da equipe de colete orientando a manobra, cones e estrutura de tenda sendo montada. Anexar: foto externa do trailer`.

Regras do título: tipos de cena EXTERNA, INTERNA, AÉREA ou DETALHE; sempre listar 3 ou mais elementos visuais que tornam o tema reconhecível sem ler o artigo (ex.: docas e caminhão baú para galpão; caixa d'água para modo autônomo; tampa de inspeção e tubo PVC para rede de esgoto; betoneira, tapume e capacete para obra; rampa, corrimão e piso tátil para PNE); sempre dizer a foto a anexar (cabine unitária ou módulo PNE). Os mesmos títulos entram no `.md` do artigo, na seção JSONS DE CAPA.

## Idiomas
O dono pediu de 3 a 4 artigos em inglês e em espanhol para público internacional (eventos com estrangeiros, multinacionais). Ver `skill-banheiros`, seção Versões em inglês e espanhol.
