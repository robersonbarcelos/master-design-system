# Brand Spec — Servitec Comercial e Locações

last_updated: 2026-08-20

> Extraído de análise de identidade visual do Instagram @servitec_comercial e site serviteccomercial.com.br.
> Paleta confirmada por análise direta dos arquivos de produção em `FAMILIAS VISUAIS/` (agosto 2026).
> Ver `familias-visuais.md` para paletas específicas por família visual.

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

### Paleta principal — valores confirmados de produção

| Papel | Nome | Hex | Família |
|---|---|---|---|
| Primária FV01 | Azul Navy | #0A2D6B | FV01 Comercial Limpo |
| Primária FV03 | Azul Escuro | #0A2A66 | FV03 Fullscreen Impacto |
| Primária FV04 | Navy | #0D2B5C | FV04 Catálogo Premium |
| Primária FV05 | Azul Navy | #0D2B63 | FV05 Editorial Técnico |
| Secundária | Amarelo Servitec | #FFD100 | FV01, FV04 |
| Secundária FV03 | Amarelo Vivo | #FFD200 | FV03 |
| Secundária FV05 | Amarelo Vivo | #FFCB00 | FV05 |
| Fundo light | Off-White | #F5F5F2 | FV01 |
| Texto | Grafite | #222426 | FV01 |
| Texto escuro FV05 | Grafite Escuro | #1B1B1D | FV05 |

> Nota: o azul da marca Servitec varia levemente entre famílias (0A2D6B / 0A2A66 / 0D2B5C / 0D2B63).
> Para referência de logo e identidade institucional: usar #0A2D6B como canônico.

### Hex canônicos para uso geral (logo, documentos, proposta)

```css
:root {
  --color-primary: #0A2D6B;    /* azul navy Servitec — confirmado FV01 */
  --color-secondary: #FFD100;  /* amarelo Servitec — confirmado FV01/FV04 */
  --color-bg-light: #F5F5F2;   /* off-white — confirmado FV01 */
  --color-grafite: #222426;    /* grafite texto — confirmado FV01 */
  --color-text-on-dark: #FFFFFF;
}
```

### Verificação de acessibilidade
| Combinação | WCAG |
|---|---|
| Branco sobre Azul Navy (#0A2D6B) | AA ✓ |
| Preto sobre Amarelo (#FFD100) | AAA ✓ |
| Amarelo (#FFD100) sobre Navy (#0A2D6B) | AA ✓ |

---

## Tipografia

> Tipografia dos posts atual: sans-serif condensada bold, estilo impacto. Confirmar família exata.

### Fontes confirmadas (análise dos arquivos de produção — agosto 2026)

| Papel | Família | Peso(s) | Famílias que usam |
|---|---|---|---|
| Headline / Título | **Anton Condensed** | Regular (sempre bold por design) | FV01, FV03, FV04, FV05 |
| Subtítulo / Destaques | **Bebas Neue Condensed** | Regular / Bold | FV05 exclusivo |
| Corpo / Specs | **Montserrat** | 400 Regular, 600 SemiBold, 700 Bold | FV01, FV03, FV04 |
| Corpo técnico | **Inter** | 400 Regular | FV05 exclusivo |
| Badges / Labels | **Montserrat** | 700 Bold | FV01, FV03, FV04 |

> Regra de ouro: Anton em títulos grandes é inviolável em todas as famílias.
> Inter e Bebas Neue são exclusivos de FV05 (Editorial Técnico Escuro).

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
