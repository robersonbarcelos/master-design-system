# DESIGN.md — Servitec Comercial e Locações

> Referência visual para geração de código (HTML/CSS), componentes e direção de arte.
> Baseado em análise do Instagram @servitec_comercial e site serviteccomercial.com.br.

---

## Identidade visual em uma frase

**"Industrial bold com coração regional"** — contrastes fortes de azul e amarelo, tipografia impactante de setor de construção, mas com a proximidade e calor de uma empresa de 35 anos que conhece seus clientes pelo nome.

---

## Paleta

```css
/* Cores primárias */
--azul-servitec: #003087;       /* Azul marinho corporativo — fundos, headers */
--amarelo-servitec: #FFD100;    /* Amarelo vibrante — CTAs, destaques, logo */

/* Apoio */
--azul-profundo: #001F5B;       /* Versão mais escura para gradientes e contraste */
--amarelo-suave: #F5C800;       /* Variação levemente mais quente */
--off-white: #F5F5F5;           /* Fundo de posts informativos */
--preto-servitec: #0D0D0D;      /* Texto sobre fundos claros */

/* Estado de urgência / Alerta */
--vermelho-alerta: #C8102E;     /* Só para comunicados críticos ou campanhas específicas */
```

---

## Tipografia

### Para componentes web e HTML
```css
/* Display: Impacto — peso total */
font-family: 'Impact', 'Arial Narrow', sans-serif;
font-weight: 900;
text-transform: uppercase;

/* Headlines de suporte */
font-family: 'Arial Black', 'Helvetica Neue', sans-serif;
font-weight: 800;
text-transform: uppercase;

/* Body e descritivos */
font-family: 'Arial', 'Helvetica', sans-serif;
font-weight: 400–600;
```

### Escala aplicada a componentes
```
Display:    72–96px / weight 900 / uppercase / letter-spacing -0.02em
H1:         48px   / weight 800 / uppercase
H2:         32px   / weight 700
Body:       16–18px / weight 400
Badge:      13–14px / weight 700 / uppercase / letter-spacing 0.05em
```

---

## Componentes padrão

### Card de produto (Grupo A — Oferta)
```
┌──────────────────────────────────┐
│  [BADGE: "OFERTA ESPECIAL"]      │ ← Amarelo sobre azul, canto superior
│                                  │
│     [IMAGEM DO PRODUTO]          │ ← Centro, sem fundo, grande
│                                  │
│  NOME DO PRODUTO EM CAPS         │ ← Amarelo, impact
│  Especificação chave             │ ← Branco, menor
│                                  │
│  [LOGO SERVITEC] ──── [CTA]      │ ← Rodapé: logo à esq, botão à dir
└──────────────────────────────────┘
Fundo: azul marinho (#003087) ou gradiente azul escuro→preto
```

### Card educativo (Grupo C — Explica)
```
┌──────────────────────────────────┐
│  Servitec Explica                │ ← Label de editoria, menor, amarelo
│                                  │
│  PERGUNTA OU DICA                │ ← Branco ou amarelo, impact
│  Em Destaque                     │
│                                  │
│  • Ponto 1                       │ ← Lista com ícones simples
│  • Ponto 2                       │
│  • Ponto 3                       │
│                                  │
│  [LOGO SERVITEC]                 │ ← Rodapé
└──────────────────────────────────┘
Fundo: azul médio (#1B3E8F) com padrão sutil ou sólido
```

### Card institucional (Grupo D — Legado)
```
┌──────────────────────────────────┐
│  [FOTO REAL — equipe/loja/obra]  │ ← Foto dominante, cobre 60% do card
│  ─────────────────────────────── │
│  35 ANOS                         │ ← Número grande, amarelo
│  Servindo quem constrói          │ ← Branco, menor
│                                  │
│  [LOGO]  serviteccomercial.com.br│ ← Rodapé discreto
└──────────────────────────────────┘
Fundo: pode ser a própria foto com overlay escuro gradiente
```

---

## Layout e grid

- **Max-width:** 1080px (quadrado) ou 1080×1350 (retrato)
- **Margem interna (safe area):** 48px em todos os lados
- **Rodapé reservado:** 80px para logo + website + contato
- **Hierarquia visual:** 1 elemento dominante + 1 elemento de suporte + rodapé
- **Espaço negativo:** usar mais espaço vazio nos posts educativos — faz o conteúdo respirar

---

## Tom visual por editoria

| Editoria | Energia visual | Referência de sensação |
|---|---|---|
| Soluções em Campo | Alta energia, produto protagonista | Catálogo técnico profissional |
| Servitec Explica | Organizado, espaço para leitura | Manual técnico ilustrado |
| Ofertas da Semana | Urgência + clareza | Encarte de loja + catálogo industrial |
| Legado & Bastidores | Humano, real, orgulho | Reportagem de empresa regional |
| Datas & Campanhas | Cuidado + pertencimento | Comunicado oficial humanizado |

---

## Regras de aplicação do logo

- Logo sempre no rodapé — nunca como header principal
- Versão sobre azul: logo com texto amarelo ou versão branca
- Versão sobre amarelo: logo com texto azul ou escuro
- Nunca aplicar sobre fundo com baixo contraste (evitar cinza médio)
- Tamanho mínimo: 120px de largura no post 1080px
