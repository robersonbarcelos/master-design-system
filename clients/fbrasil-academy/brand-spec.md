# Brand Spec: F. Brasil Academy

last_updated: 2026-11-20

> Valores extraídos das artes da Camila (amostra de pixels), dos PDFs do Fabiano e do CSS do site no ar. Os arquivos originais de marca (logo vetorial, fontes, manual) ainda NÃO foram enviados. Tudo marcado "provisório" precisa de confirmação da Camila.

---

## Logo

**Descrição:** monograma "FB" com o F em azul-marinho e o B em dourado, encaixados. Abaixo, "F. BRASIL" em sans larga e "ACADEMY" espaçado entre dois filetes dourados.

**Arquivos (em `assets/logo/`):**
- `logo-academy-branco-transparente.png`: 834 x 143, PNG com fundo transparente, versão branca horizontal. É a usada no site e no quiz. Serve para fundo navy.
- `logo-academy-cor-referencia.png`: 620 x 470, versão colorida (F navy, B e "ACADEMY" dourados) sobre cinza. Fundo NÃO é transparente. Referência de baixa resolução.
- `logo-academy-branco-fundo-navy-referencia.png`: 880 x 150, versão branca sobre navy, recorte das artes. Referência.
- `favicon-icon.png`: ícone usado no site.

**Faltam (pedir à Camila):** logo em SVG ou PNG transparente de alta resolução, versão colorida com fundo transparente, símbolo FB isolado, manual de marca.

**Uso (provisório):**
- Fundo navy: logo branco. Fundo claro ou cinza: logo colorido.
- Nunca esticar, rotacionar, trocar as cores nem pôr sombra.
- Usar o arquivo como veio (regra do Diego: logo de cliente não se recria).

---

## Cores

### Paleta principal (a do site no ar)

| Papel | Nome | Hex | Uso |
|---|---|---|---|
| Fundo escuro, texto | Azul-marinho | `#06213A` | Abertura, rodapé, textos, títulos |
| Marca, botão, filete | Dourado | `#CB9A5A` | Botão principal, logo, filetes, números |
| Dourado hover | Dourado claro | `#D9AB6C` | Hover do botão dourado |
| Destaque | Bronze | `#A3805B` | Etiquetas (eyebrow), marca-texto, balões. Texto sobre ele é navy |
| Fundo secundário | Cinza azulado | `#B8BCC0` | Seções alternadas (carrossel de 28/10) |
| Fundo de leitura | Papel | `#F4F5F7` | Seções claras do site |
| Linha | Cinza-linha | `#DFE1EC` | Bordas e divisórias |
| Fundo do quiz | Azul profundo | `#041629` | Tela do quiz |
| Linha no escuro | Azul-linha | `#1C4468` | Bordas no quiz |
| Texto sobre escuro | Branco | `#FFFFFF` | Texto sobre navy |

**Gradiente da abertura:** `linear-gradient(222deg, #06213a 57%, #164c7e 100%)`.

**Cores das faixas do quiz (resultado):**

| Faixa | Hex |
|---|---|
| 0 a 39, Revisão urgente | `#E8806A` |
| 40 a 59, Melhorias necessárias | `#CB9A5A` |
| 60 a 79, Bem estruturado | `#7FB4E0` |
| 80 a 100, Preparação consistente | `#6CC28C` |

### Outras amostras (não oficializadas)
- PDFs do Fabiano (diagnóstico, slides, bônus): navy `#08233D`, dourado `#C0914D`.
- Stories da Camila: cinza liso `#B4B4B4`.
- Três tons de dourado convivem (`#CB9A5A` logo, `#C0914D` PDFs, `#A3805B` etiquetas). Decisão pendente: oficializar um dourado e um bronze.

### Variáveis CSS (do site no ar)
```css
:root {
  --navy: #06213a;
  --gold: #cb9a5a;
  --gold-hi: #d9ab6c;
  --bronze: #a3805b;
  --grey: #b8bcc0;
  --paper: #f4f5f7;
  --line: #dfe1ec;
  --grad: linear-gradient(222deg, #06213a 57%, #164c7e 100%);
  --f-display: var(--font-bebas), Impact, sans-serif;
  --f-body: var(--font-outfit), "Segoe UI", sans-serif;
}
/* quiz */
.quiz { --deep: #041629; --line-d: #1c4468; }
```

### Verificação de acessibilidade (calculada)

| Combinação | Ratio | WCAG |
|---|---|---|
| Branco sobre navy | 16,3:1 | AAA |
| Navy sobre dourado `#CB9A5A` | 6,5:1 | AA |
| Navy sobre dourado claro `#D9AB6C` | 7,8:1 | AAA |
| Navy sobre cinza `#B8BCC0` | 8,5:1 | AAA |
| Navy sobre papel `#F4F5F7` | 15,0:1 | AAA |
| Navy sobre bronze `#A3805B` | 4,5:1 | AA (limite) |
| Branco sobre bronze | 3,6:1 | Falha para texto pequeno |
| Bronze sobre cinza `#B4B4B4` | 1,7:1 | Falha |

**Regra decorrente:** sobre bronze, texto sempre navy, nunca branco. Bronze nunca como cor de texto fino sobre cinza. Bronze só em etiquetas e textos grandes.

---

## Tipografia

| Papel | Família | Peso | Fonte |
|---|---|---|---|
| Display, títulos, etiquetas, números | Bebas Neue | 400 | Google Fonts via `next/font` |
| Corpo, botões, UI | Outfit | 300, 400, 500, 600 | Google Fonts via `next/font` |

**Status:** provisório. As artes da Camila parecem usar uma condensada tipo Bebas Neue (títulos), uma extra pesada tipo Anton (tagline "ASSISTIU. APRENDEU. APLICOU.") e uma monoespaçada espaçada (só no story de boas-vindas), com corpo em sans geométrica leve tipo Outfit ou Poppins Light. Os nomes reais não foram confirmados. Pedir à Camila e reduzir de três para duas famílias.

### Escala usada no site

| Uso | Tamanho |
|---|---|
| Título da abertura (display) | `clamp(54px, 7vw, 92px)` |
| Título de seção | `clamp(42px, 5.4vw, 68px)` |
| Números grandes (34, 66, 13) | `clamp(72px, 9vw, 120px)` |
| Preço (R$97) | `clamp(80px, 10vw, 120px)` |
| Etiqueta (eyebrow) | 20px Bebas, caixa alta, espaçamento 0,03em |
| Texto de apoio (lead) | 19px Outfit |
| Botão | 16px Outfit 600 |

### CSS
```css
:root {
  --font-display: 'Bebas Neue', Impact, sans-serif;
  --font-body: 'Outfit', 'Segoe UI', sans-serif;
}
```

---

## Assets do produto

- `assets/fotos/fabiano.jpg`: foto do Fabiano usada na abertura da LP.
- `assets/artes-camila-referencia/carrossel/` (21-10 e 28-10) e `stories/` (23-10 e 30-10): 25 PNGs, 14 slides 1080x1350 e 11 stories 1080x1920. Referência de estilo.
- Materiais do Fabiano (fora do Master): `C:\ARQUIVOS\JOBS E EMPREGOS\FABIANO - CV NA ERA DE IA\` (briefing, isca, slides de 42 páginas, caderno bônus, roteiros, planilhas do LinkedIn e o curso gravado de 15 vídeos).

---

## Estilo visual geral

**Atmosfera:** sóbrio, confiável, premium acessível. Navy profundo com dourado discreto, tipografia condensada em caixa alta e muito respiro. Autoridade de quem contrata, sem agressividade.
**Fotografia:** fotos reais do Fabiano recortadas, com etiqueta branca com o nome. Priorizar o Fabiano nas peças de autoridade e de oferta; evitar misturar com banco de imagens.
**Ordem das marcas:** Academy como marca, Head Hunters como credencial, "Direto ao Ponto" como selo do método.

## Notas de aplicação

- **Padrão visual a adotar:** a Camila publicou dois sistemas (navy em 21/10 e cinza claro em 28/10, stories em cinza liso). O site e o quiz seguem o navy com dourado. Definir um padrão único com ela.
- Cargo nas peças: "Head Hunter" (não "Mentor e Educador").
- Número de autoridade só os que o Fabiano sustenta: 34 anos, 66 mil seguidores, mais de 13 mil horas. Ainda precisam de confirmação dele.
