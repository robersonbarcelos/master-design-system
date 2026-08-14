# Brand Spec — Servitec Comercial e Locações

last_updated: 2026-07-23

> Extraído de análise de identidade visual do Instagram @servitec_comercial e site serviteccomercial.com.br.
> Valores de cor são aproximações visuais — confirmar com arquivo oficial da marca.

---

## Logo

**Arquivo principal:** assets/logo.png *(solicitar ao cliente — versão vetorial preferencial)*
**Tagline:** "Soluções em Locações e Vendas"

**Descrição do logo:**
- Texto "SERVITEC" em caixa alta, negrito, fonte sans-serif condensada
- Fundo amarelo vibrante (#FFD100 aprox.)
- Borda/container em azul marinho escuro (#003087 aprox.)
- Tagline em texto menor abaixo ou integrada ao badge

**Variações disponíveis:**
- [ ] Versão horizontal — *solicitar ao cliente*
- [ ] Versão vertical / símbolo isolado — *solicitar ao cliente*
- [ ] Versão branca (para fundos escuros) — *solicitar ao cliente*
- [ ] Versão preta (para fundos claros) — *solicitar ao cliente*
- [ ] Favicon — *solicitar ao cliente*

**Uso do logo:**
- Sempre presente no rodapé dos posts (padrão atual do cliente)
- Espaço mínimo ao redor: 16px
- Nunca deformar, rotacionar ou alterar as cores da combinação azul+amarelo
- Fundos permitidos: branco, azul marinho, amarelo

---

## Cores

### Paleta principal

| Papel | Nome | Hex (aprox.) | Uso |
|---|---|---|---|
| Primária | Azul Servitec | #003087 | Fundos, headers, botões principais |
| Secundária | Amarelo Servitec | #FFD100 | Destaques, CTAs, logo, badges |
| Acento | Amarelo Vivo | #F5C800 | Variação do amarelo em elementos menores |
| Fundo claro | Off-white | #F5F5F5 | Backgrounds de posts informativos |
| Fundo escuro | Azul Profundo | #001F5B | Seções premium, fundos de destaque |
| Texto principal | Quase Preto | #0D0D0D | Copy principal |
| Texto sobre azul | Branco | #FFFFFF | Texto em fundos escuros |

> ⚠️ Confirmar hexadecimais exatos com o arquivo de logo oficial do cliente.

### Variáveis CSS
```css
:root {
  --color-primary: #003087;
  --color-secondary: #FFD100;
  --color-accent: #F5C800;
  --color-bg-light: #F5F5F5;
  --color-bg-dark: #001F5B;
  --color-text-main: #0D0D0D;
  --color-text-on-dark: #FFFFFF;
}
```

### Verificação de acessibilidade (estimada)
| Combinação | WCAG |
|---|---|
| Branco sobre Azul Servitec (#003087) | AA ✓ |
| Preto sobre Amarelo (#FFD100) | AAA ✓ |
| Amarelo sobre Azul Profundo (#001F5B) | AA ✓ |

---

## Tipografia

> Tipografia dos posts atual: sans-serif condensada bold, estilo impacto. Confirmar família exata.

### Fontes (estimativa visual — confirmar)

| Papel | Família | Peso(s) | Observação |
|---|---|---|---|
| Display / Headline | Impact ou equivalente condensado | 700–900 | Títulos grandes nos posts |
| Sub-headline | Arial / Helvetica Bold | 700 | Textos de suporte |
| Body | Arial / Helvetica | 400–500 | Textos longos, legendas |

### Escala tipográfica (para posts)

| Token | Tamanho | Peso | Uso |
|---|---|---|---|
| headline | 48–72px | 900 | Título principal do post |
| sub | 24–32px | 700 | Especificações, subtítulo |
| body | 16–20px | 400 | Descrição, detalhe |
| badge | 14px | 700 | "Disponível para Locação", "Oferta Especial" |

---

## Mascote

**Descrição:** Trabalhador masculino estilizado com:
- Capacete de segurança amarelo
- Uniforme/macacão azul (cor da marca)
- Expressão positiva, polegar para cima em alguns posts
- Estilo: semi-cartoon, mas com traço profissional

**Uso recomendado:**
- Posts institucionais e de engajamento
- Campanhas de data comemorativa
- Comunicados com tom positivo
- **Evitar:** não usar o mascote em todo post — reduz impacto quando aparece

---

## Assets do produto

**Categorias de imagem a produzir:**
- Plataformas elevatórias (tesoura, articulada) — em uso em obra
- Ferramentas de solda (tochas MIG/TIG, eletrodos)
- Compressores em operação industrial
- Equipamentos de corte e biselo
- Fachada/interior da loja (bastidores)

**Fornecedores parceiros com marca presente nos posts:**
- Mega Ferramentas (recorrente)
- DWT
- Berg Steel
- Chiaperini

---

## Estilo visual geral

**Referência visual:** Bold e direto — alta legibilidade de longe, muito texto em caixa alta, paleta contrastante azul/amarelo típica do setor industrial e de construção civil.

**Estilo de fotografia:**
- [x] Mockups de produto (fotos de catálogo)
- [x] Fotografia real de equipamentos
- [ ] Fotografia de clientes/equipe (oportunidade)
- [ ] Bastidores de obra em uso (oportunidade — alto impacto)

**Atmosfera atual:** comercial, promocional, "loja física que foi pro digital"
**Atmosfera desejada:** especialista confiável + parceiro de obra — mantendo o visual bold mas adicionando profundidade editorial

**DESIGN.md de referência:** DESIGN.md (arquivo nesta pasta)
