# Template: Documento de Pautas Editoriais — ESENCA

## Arquivo
`references/template-documento-pautas.html`

## O que é
Template HTML aprovado para geração de documentos de pautas editoriais da ESENCA. Exportável como PDF via Chrome (Ctrl+P → Gráficos de segundo plano ativado).

## Estrutura do documento
1. **Capa** — fundo claro `#F4F4F8`, título em verde/roxo da marca, stats bar escura com métricas do banco de pautas
2. **Guia de leitura** — legenda visual explicando badges de canal e ângulo editorial
3. **Seções por categoria** — cada categoria com stripe colorida, header e cards de pauta
4. **Rodapé** — identificação do documento e data de referência

## Paleta aplicada (brand-spec aprovado)
| Token | Hex | Uso |
|-------|-----|-----|
| `--bg` | `#0A0A14` | Fundo cards dark |
| `--bg-card` | `#11111E` | Cards de pauta |
| `--verde` | `#B5E040` | Headline, Cat 01, título capa |
| `--verde-sym` | `#7CBC16` | Ângulo Esenca label |
| `--roxo` | `#642B83` | Subtítulo capa |
| `--roxo-overlay` | `#5B2090` | Cat 02 stripe |
| `--ambar` | `#B1852A` | Cat 03 stripe |
| `--laranja` | `#E54E3E` | Cat 04 stripe |
| `--magenta` | `#91307E` | Cat 05 stripe |

## Badges de canal
| Badge | Cor de fundo | Cor de texto |
|-------|-------------|-------------|
| LinkedIn | `#2D1248` | `#C084FC` |
| Instagram | `#3D1040` | `#E080C8` |
| LI + IG | `#1A3010` | `#B5E040` |
| Visão Founder | `#3A1A00` | `#D4A04A` |

## Categorias e cores de stripe
| Cat | Nome | Cor |
|-----|------|-----|
| 01 | Gestão de Crise e Reputação | `#B5E040` (verde) |
| 02 | Executive Positioning | `#5B2090` (roxo-overlay) |
| 03 | Regulação com Impacto em Comunicação | `#B1852A` (âmbar) |
| 04 | LatAm e Mercado Financeiro | `#E54E3E` (laranja) |
| 05 | Produto e Serviço | `#91307E` (magenta) |

## Regras de print (PDF)
- `html, body` têm `background: #F4F4F8` no CSS normal (previne fundo escuro no print)
- `@media print` com `-webkit-print-color-adjust: exact` em cada seção
- Abrir arquivo direto no Chrome via `file:///` → Ctrl+P → ativar "Gráficos de segundo plano" → Salvar

## Quando usar este template
- Novo banco de pautas mensais ou bimestrais
- Relatório de cobertura editorial
- Briefing de conteúdo para aprovação da Raquel

## Como duplicar para novo período
1. Copiar `template-documento-pautas.html`
2. Renomear para `pautas-[mes]-[ano].html`
3. Atualizar: título, data na stats bar, número de pautas, conteúdo dos cards
4. Manter estrutura de CSS e classes — não alterar tokens de cor
