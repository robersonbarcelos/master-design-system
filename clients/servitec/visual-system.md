# Visual System — Servitec Comercial e Locações

> Especificações técnicas, grupos visuais e regras de prompt para geração de imagens.

---

## 01 | ESPECIFICAÇÕES TÉCNICAS POR PLATAFORMA

| Plataforma | Formato | Dimensões | Proporção | Observação |
|---|---|---|---|---|
| Instagram Feed | Post único | 1080 × 1080 px | 1:1 | Padrão — maioria dos posts |
| Instagram Feed | Retrato | 1080 × 1350 px | 4:5 | Ocupa mais espaço no feed — usar para destaque |
| Instagram Stories | Vertical | 1080 × 1920 px | 9:16 | Zona segura: deixar 250px de margem top/bottom |
| Instagram Carrossel | Feed | 1080 × 1080 px | 1:1 | Mesmo padrão, múltiplos slides |
| Facebook Post | Feed | 1200 × 630 px | 1.91:1 | Formato landscape |

---

## 02 | GRUPOS VISUAIS

### Grupo A — Oferta Direta (Ofertas da Semana)
**Quando usar:** posts de produto com preço ou condição de locação/venda
**Características:**
- Fundo: azul marinho (#003087) ou gradiente azul escuro
- Título: amarelo vibrante (#FFD100), caixa alta, fonte bold condensada
- Produto: foto real em destaque, fundo removido ou integrado ao fundo azul
- Badge: "OFERTA ESPECIAL" ou "DISPONÍVEL PARA LOCAÇÃO" em amarelo
- Rodapé: logo Servitec sempre presente
- Energia: urgência + clareza

### Grupo B — Produto em Campo (Soluções em Campo)
**Quando usar:** equipamento sendo usado em obra ou contexto industrial
**Características:**
- Foto real do equipamento em ambiente de uso (obra, indústria)
- Overlay leve de azul ou amarelo para destacar texto
- Texto: especificação técnica principal em destaque
- Tom: sério, profissional, técnico
- Badge: categoria de produto (ex: "Plataforma Elevatória | 16m")

### Grupo C — Educativo (Servitec Explica)
**Quando usar:** posts com dicas, comparativos, tutoriais, normas
**Características:**
- Fundo mais claro — azul médio ou branco com elementos visuais da marca
- Ícones ou elementos gráficos que illustram o conceito
- Tipografia hierárquica clara: pergunta no topo, resposta estruturada
- Tom: editorial, didático, com espaço para leitura
- Mascote pode aparecer como "guia"

### Grupo D — Institucional (Legado & Bastidores)
**Quando usar:** posts de história da empresa, equipe, eventos, conquistas
**Características:**
- Fotografia real quando possível (equipe, loja, evento)
- Paleta mais equilibrada — azul + amarelo + espaço em branco
- Texto mais discreto — a imagem faz o trabalho
- Data, número de anos ou dado histórico em destaque tipográfico
- Tom: orgulho, pertencimento, humanidade

### Grupo E — Campanhas (Datas & Campanhas)
**Quando usar:** Julho Amarelo, Junho Vermelho, Fenasucro, datas do setor
**Características:**
- Cor da campanha como acento (ex: amarelo e verde para Julho Amarelo)
- Mascote de capacete como porta-voz do cuidado
- Mensagem curta e direta — saúde ou segurança como protagonista
- Logo da campanha + logo Servitec no rodapé

---

## 03 | JSON PADRÃO PARA GERAÇÃO DE IMAGEM

```json
{
  "scene": "[Descrição da cena — equipamento em uso / ambiente industrial / ambiente de obra]",
  "style": "commercial photography, industrial, professional, high resolution, cinematic lighting",
  "technical": {
    "ratio": "1:1",
    "resolution": "2k",
    "model": "realism"
  },
  "materials": "[Metal, concreto, equipamento industrial, obra em andamento]",
  "composition": "[Produto em destaque / trabalhador em ação / ambiente de fundo]",
  "quality": "ultra-detailed, sharp focus, professional product photography",
  "negative": "text, watermark, logo, blurry, distorted, cartoon, illustration, oversaturated"
}
```

---

## 04 | NEGATIVE PROMPTS FIXOS

Sempre aplicar em geração de imagem:
- Sem texto na imagem
- Sem logos ou marcas visíveis
- Sem marca d'água
- Sem pessoas com rosto distorcido ou irrealista
- Sem cenário genérico de stock photo (fundo branco puro)
- Sem equipamentos que pareçam brinquedo ou miniatura

---

## 05 | REGRAS DE PROMPT POR GRUPO

| Grupo | Elementos obrigatórios no prompt | Paleta de iluminação |
|---|---|---|
| A — Oferta | produto isolado ou sobre fundo azul profundo, iluminação de estúdio | Azul profundo + destaque amarelo |
| B — Campo | ambiente real de obra ou indústria, ação implícita | Natural industrial, luz de dia |
| C — Educativo | clean, organizado, pode ter ícones ou elementos gráficos | Azul médio + branco |
| D — Institucional | ambiente da loja ou externo, pessoas reais quando possível | Natural, acolhedor |
| E — Campanha | cor da campanha como dominante | Conforme tema (amarelo/verde, vermelho) |

---

## 06 | ELEMENTOS VISUAIS PROIBIDOS

- Fundo branco puro sem elemento visual (parece genérico demais)
- Tipografia manuscrita ou ornamental — foge do tom industrial
- Ilustração cartoon excessiva (o mascote é exceção controlada)
- Cores fora da paleta primária sem aprovação: verde, laranja, roxo
- Emojis na capa do post (só na legenda)
- Mais de 3 logos de parceiros no mesmo post
