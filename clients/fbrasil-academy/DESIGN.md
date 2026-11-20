# DESIGN.md: F. Brasil Academy

> Referência visual para agentes de IA. Espelha o que está no ar em fbrasilacademy.com.br (landing, quiz). Fonte do código: `C:\Users\Pichau\Downloads\clones\lp-push` (`src/app/lp.css`, `src/app/quiz/quiz.css`).

## Visão geral

**Estilo:** editorial sóbrio, navy e dourado, tipografia condensada em caixa alta com corpo leve.
**Atmosfera:** autoridade calma, de quem contrata. Premium acessível.
**Layout de origem:** adaptado de src-search.com (hero em gradiente com foto em máscara curva, ondas, cartões de 16px, contadores, slider, faixa).

## Cores

```
Navy:     #06213A  fundos, textos, cabeçalhos
Gold:     #CB9A5A  botão principal, logo, filetes, números
Gold-hi:  #D9AB6C  hover do botão
Bronze:   #A3805B  etiquetas, marca-texto, balões (texto navy)
Grey:     #B8BCC0  fundo secundário
Paper:    #F4F5F7  seções de leitura
Line:     #DFE1EC  bordas
Deep:     #041629  fundo do quiz
Line-d:   #1C4468  bordas no quiz
```
Gradiente da abertura: `linear-gradient(222deg, #06213a 57%, #164c7e 100%)`.

## Tipografia

**Display:** Bebas Neue 400, caixa alta, para títulos, etiquetas e números grandes.
**Corpo:** Outfit 300/400/500/600.
Títulos de seção `clamp(42px, 5.4vw, 68px)`; abertura `clamp(54px, 7vw, 92px)`; números `clamp(72px, 9vw, 120px)`; lead 19px.

## Layout e espaçamento

**Raio de borda:** cartões 16px; blocos grandes 24px; imagens do hero com máscara curva (`55% 0 0 45% / 65% 0 0 35%` no desktop, arco inferior no mobile); botões em pílula (`1600px`); marca-texto 4px.
**Sombras:** sutis, só para elevar cartões.
**Movimento:** faixa de palavras em rolagem (Clareza, Verdade, Contexto, Contribuição, Estratégia, IA com fatos reais, Direto ao ponto), contadores que sobem (34 anos, 66 mil, 13 mil+ horas), transição de 0,3s nos botões, seta que desliza 4px no hover. Respeitar `prefers-reduced-motion`.

## Componentes

### Botão primário (`.btn-gold`)
- Fundo `#CB9A5A`, borda `#CB9A5A`, texto navy.
- Padding `14px 22px 14px 28px`, pílula, Outfit 600 16px, ícone de seta à direita.
- Hover: fundo `#D9AB6C`, seta avança 4px.
- Regra: todos os CTAs do site usam este botão dourado (decisão de padronização).

### Botão fantasma (`.btn-ghost`) e navy (`.btn-navy`)
- Ghost: transparente com borda, para "Faça o teste gratuito" sobre fundo escuro.
- Navy: fundo navy com texto claro, sobre fundo claro.

### Etiqueta (eyebrow)
- Fundo bronze `#A3805B`, texto navy, Bebas 20px, caixa alta, `padding: 6px 12px 4px`.
- Usada acima dos títulos de seção ("Experiência dos dois lados da mesa", "O método", "Você se reconhece?").

### Cards
- Fundo branco ou papel, raio 16px, borda `#DFE1EC`.
- Cartão "Antes / Depois" em duas colunas, com aviso "Exemplo ilustrativo".
- Cartão de oferta: "Curso completo R$97" em Bebas grande, lista de 3 itens, botão dourado.

### Perguntas frequentes
- Lista com a pergunta em destaque e a resposta curta abaixo. Se virar balão bronze, texto navy.

### Quiz
- Fundo `#041629`, bordas `#1C4468`, logo branco no topo.
- Respostas em três botões: Não (0), Parcialmente (5), Sim (10).
- Resultado com nota 0 a 100 e cor da faixa; mostra as 3 perguntas de menor nota.

## Regras de contraste
- Texto sobre bronze: navy (4,5:1), nunca branco (3,6:1).
- Bronze não é cor de texto fino sobre cinza.
- Branco sobre navy 16,3:1; navy sobre dourado 6,5:1.
