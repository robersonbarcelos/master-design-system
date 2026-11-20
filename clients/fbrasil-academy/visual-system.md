# Visual System: F. Brasil Academy

> Padrões extraídos das artes da Camila (21/10 a 30/10/2026) e do site. Pasta de referência: `assets/artes-camila-referencia/`.

---

## 01 | FLUXO DE PRODUÇÃO VISUAL

1. Propor 3 ideias visuais em texto (conceito, composição, paleta, tipografia).
2. Aguardar aprovação do Roberson (e, para peças de oferta, do Fabiano).
3. Gerar o JSON ou a arte só para as aprovadas.
4. Logo e foto do Fabiano usados como vieram, sem recriar.

## 02 | ESPECIFICAÇÕES TÉCNICAS

| Formato | Dimensões | Proporção | Obs |
|---|---|---|---|
| Carrossel | 1080 x 1350 px | 4:5 | Formato das artes da Camila |
| Stories | 1080 x 1920 px | 9:16 | Safe zone: 250 px topo e base |
| Reels e vídeos verticais | 1080 x 1920 px | 9:16 | Até 1min30 (8 vídeos de divulgação) |
| YouTube | 1920 x 1080 px | 16:9 | Aulas de cerca de 8 min e roteiros de 10 a 12 min |
| LinkedIn (post) | 1200 x 1200 px | 1:1 | Canal principal do Fabiano |

JPG para fotos, PNG para artes com texto e logo.

## 03 | GRUPOS VISUAIS (a partir das artes existentes)

**GRUPO 1: Navy institucional** (carrossel de 21/10)
Fundo azul-marinho `#06213A` (80% da arte), texto branco, etiqueta bronze com título em caixa alta condensada, foto do Fabiano recortada com etiqueta branca com o nome, logo branco no fechamento.
Quando usar: apresentação da Academy e do Fabiano, autoridade, peças de oferta.

**GRUPO 2: Cinza editorial** (carrossel de 28/10)
Fundo cinza azulado `#B8BCC0` com gradiente claro perto do rodapé, capa em pergunta com marca-texto bronze, foto lateral em corte vertical, balões bronze em zigue-zague, texto navy, cabeçalho discreto `@FBRASILACADEMY`.
Quando usar: identificação com o problema do currículo, conteúdo educativo.

**GRUPO 3: Story cinza liso** (23/10 e 30/10)
Fundo cinza `#B4B4B4`, boas-vindas, quem está por trás, tagline em extra pesada ("ASSISTIU. APRENDEU. APLICOU."), logo colorido. Fundo liso parece provisório, confirmar se é intencional.
Quando usar: apresentação e confiança. Último story leva sticker de link para o teste.

**GRUPO 4: Antes e depois** (a criar)
Duas colunas, esquerda "Antes" e direita "Depois", aviso "exemplo fictício", navy e dourado. Usa o exemplo do site (controle de documentos, atendimento e relatórios).
Quando usar: Currículo na prática.

## 04 | PADRÕES DE COMPOSIÇÃO (das artes)

- Etiqueta bronze com título em caixa alta condensada, texto navy (ex.: "O QUE É A F BRASIL ACADEMY?").
- Marca-texto bronze atrás de uma palavra ou frase.
- Balões bronze arredondados para listas de perguntas.
- Frase final em bronze.
- Autoridade em números: 34 anos, mais de 13 mil horas, "os dois lados da mesa".
- Fechamento: logo + chamada com destino (substituir "Acompanhe" e "Salve este conteúdo" por "Faça o teste do currículo. Link na bio.").

## 05 | JSON PADRÃO PARA GERADOR DE IMAGEM

```json
{
  "format": "4:5 1080x1350",
  "scene": "[composição descrita em uma frase]",
  "background": "solid navy #06213A with soft gradient to #164C7E at bottom right",
  "palette": {"navy": "#06213A", "gold": "#CB9A5A", "bronze": "#A3805B", "grey": "#B8BCC0", "white": "#FFFFFF"},
  "typography": {"headline": "condensed uppercase sans (Bebas Neue style), max 8 words", "body": "light geometric sans (Outfit style)"},
  "label": "bronze tag with navy text, uppercase condensed",
  "subject": "real photo of Fabiano Brasil (reference_lock), cutout, white name tag",
  "logo": "F. Brasil Academy logo supplied as-is, bottom area",
  "mood": "sober, trustworthy, premium, no stock-photo clichés"
}
```
Foto do Fabiano e logo entram como `reference_lock`, sem recriar nem alterar.

## 06 | NEGATIVE PROMPTS

stock photo smile handshake, neon, cartoon, 3D gloss, gradient rainbow, cluttered layout, fake charts, robot or humanoid AI cliché, text outside palette, altered logo, altered face of Fabiano.

## 07 | REGRAS DE PROMPT

- Fundo navy ou cinza `#B8BCC0`, nunca preto puro.
- Dourado `#CB9A5A` só em detalhe (botão, filete, número). Bronze só em etiqueta e texto grande.
- Texto sobre bronze é navy. Branco sobre bronze falha em contraste.
- Máximo 2 famílias de fonte.
- Fotos do Fabiano acima de banco de imagem nas peças de autoridade e oferta.
- Proibido: promessa na arte ("emprego garantido"), números não confirmados.
