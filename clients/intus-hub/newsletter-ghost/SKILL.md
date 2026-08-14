---
name: intus-newsletter
description: >
  Skill completa de produção de conteúdo para a Intus Cripto News — newsletter e artigos
  publicados no Ghost CMS (https://newsletter-3.ghost.io). Use esta skill SEMPRE que o
  usuário mencionar: "newsletter", "artigo intus", "intus cripto news", "draft ghost",
  "notícias cripto", "links da semana", "edição intus", "publicar no ghost", "topicos.json",
  "artigo_content", "newsletter_content", "imagem artigo", "imagem newsletter", "bot.py",
  ou qualquer produção de conteúdo editorial para o canal Intus Cripto. Contém: fluxo
  completo newsletter e artigo, regras de escrita, templates HTML, sistema de imagens,
  deploy Ghost via API, scripts Python, regras de tipografia, paleta visual, emojis por
  categoria, tratamento de links bloqueados e todo o PRD do sistema.
  NUNCA produzir conteúdo para Intus Cripto sem consultar esta skill primeiro.
---

# INTUS CRIPTO NEWS — Production Skill

Skill completa de produção editorial para a Intus Cripto News.
Fundador: Diego Spanevello | Ghost: https://newsletter-3.ghost.io

---

## 0. FASE 0 — PESQUISA AUTÔNOMA (quando o usuário não traz links)

### Detecção

| Situação | Caminho |
|---|---|
| Usuário traz URLs / links | Pular FASE 0 → ir direto para a ⚠️ PERGUNTA OBRIGATÓRIA |
| Usuário diz "newsletter dessa semana", "o que rolou", "pesquisa pra mim", "sem links" | Executar FASE 0 completa |

---

### Passo 0.1 — Descoberta com last30days

Rodar `/last30days` nos tópicos-base da Intus Cripto, com os subreddits e canais mapeados:

```
/last30days AI crypto blockchain DeFi stablecoins regulation
  --subreddits CryptoCurrency,ethereum,defi,ethfinance,BitcoinMarkets,
               CryptoMarkets,singularity,AI_Agents
  --tiktok-hashtags bitcoin,ethereum,defi,cripto,stablecoin,regulacao
```

Tópicos a cobrir obrigatoriamente (adaptar a query para capturar todos):
- **Bitcoin / Macro** → preço, ETF, halving, institucional
- **Ethereum / Protocolo** → upgrades, L2, staking
- **DeFi / TVL** → novos protocolos, yields, exploits
- **Stablecoins** → USDC, USDT, regulação, volume
- **Regulação** → EUA (SEC, CFTC), Brasil (Banco Central), Europa (MiCA)
- **RWA / TradFi** → tokenização, bancos entrando em cripto
- **IA + Cripto** → agentes, pagamentos agenticos, protocolo x402
- **Riscos / Geopolítica** → sanções, hacks, congelamentos

---

### Passo 0.2 — Curadoria com newsletter-generation

Aplicar os critérios do pipeline `newsletter-generation` sobre o corpus do last30days:

| Critério | Filtro para Intus |
|---|---|
| **Recência** | Últimos 7 dias (máximo 10 para notícias de impacto) |
| **Autoridade** | Preferir CoinDesk, The Block, Decrypt, cointelegraph.com.br, Reuters, FT |
| **Relevância** | Impacto estrutural para cripto BR — evitar price speculation sem fundamento |
| **Acionabilidade** | Notícia deve ter implicação clara para investidor técnico intermediário/avançado |
| **Diversidade** | Mínimo 1 notícia por coluna temática (BTC, ETH, DeFi, Regulação, RWA/IA) |

Descartar automaticamente:
- Previsões de preço sem dado concreto ("BTC vai a 200k porque...")
- Memes / conteúdo de entretenimento sem impacto real
- Notícias duplicadas (mesmo evento coberto por fontes diferentes → manter a mais autoritative)
- Conteúdo com mais de 14 dias

---

### Passo 0.3 — Apresentar lista para aprovação

Apresentar ao Diego em formato compacto — **máximo 12 candidatos**:

```
📋 CANDIDATOS PARA NEWSLETTER — [data]
Baseado em: Reddit (N threads), HN (N), Web (N fontes)

1. 🏛️ [TÍTULO CURTO]
   Fonte: [publication] | Data: [DD/MM] | Engajamento: [N upvotes/pts]
   Ângulo: [1 frase — o que torna isso relevante para o leitor Intus]
   Link: [URL]

2. ⚡ [TÍTULO CURTO]
   ...

[continua até 12]

---
Recomendados para essa edição: [N1, N2, N3...] (6–10 itens ideais)
Aguardando sua aprovação. Pode remover, adicionar ou reordenar.
```

---

### Passo 0.4 — Transição para FASE 1

Após Diego aprovar a lista:
- Links aprovados entram como input do fluxo normal
- Aplicar **Regra 2 (TODAS AS NOTÍCIAS ENTRAM)** sobre os links aprovados — não filtrar mais
- Prosseguir para ⚠️ PERGUNTA OBRIGATÓRIA com os links em mãos

---

## ⚠️ PERGUNTA OBRIGATÓRIA AO INICIAR QUALQUER SESSÃO

**Antes de qualquer produção de conteúdo (links, tema, pedido de texto), perguntar PRIMEIRO:**

> "É uma **newsletter** (links de notícias da semana) ou um **artigo** (análise aprofundada de um tema)?"

- Nunca assumir que é newsletter só porque há links
- Nunca assumir que é artigo só porque é um tema único
- **Aguardar a resposta antes de prosseguir**

---

## 1. IDENTIDADE DO CANAL

| Campo | Valor |
|---|---|
| Nome | Intus Cripto News |
| Fundador | Diego Spanevello |
| Frequência | 2× por semana |
| Público | Investidores cripto brasileiros, nível técnico intermediário/avançado |
| Idioma | Português brasileiro |
| Tom | Técnico, analítico, causa-efeito, sem clickbait |
| Ghost URL | https://newsletter-3.ghost.io |

---

## 2. REGRA CRÍTICA: TODAS AS NOTÍCIAS ENTRAM

**Todas as notícias fornecidas pelo usuário DEVEM entrar na newsletter — sem exceção.**
- 10 links → 10 notícias. 6 links → 6 notícias.
- Nunca filtrar, selecionar ou reduzir
- Link inacessível: reportar ao usuário ANTES de prosseguir

---

## 3. REGRA DE IMAGENS — INQUEBRÁVEL

| Formato | Quantidade |
|---|---|
| **Newsletter** | **1 imagem por notícia** — 10 notícias = 10 imagens |
| **Artigo** | **Sempre 5 imagens** — IMAGEM_1 a IMAGEM_4 no corpo + IMAGEM_5 exclusiva para o CTA |

- IMAGEM_1: hero de abertura (logo após o cabeçalho)
- IMAGEM_2: após o gancho
- IMAGEM_3: após a seção principal de dados
- IMAGEM_4: após a seção final de análise, antes dos riscos
- IMAGEM_5: imagem do CTA — posicionada antes do bloco de oferta/produto

Arquivos salvos pelo usuário: `img1.jpg` … `img5.jpg`
Nunca reduzir ou redistribuir. Layout ou tamanho não justificam quebrar essa regra.

---

## 4. REGRA DE VERIFICAÇÃO DE LEITURA

Após ler todos os links, **obrigatoriamente reportar**:

> "Li X de Y fontes. [Lista das que não consegui acessar]."

- Todas lidas → confirmar e prosseguir
- Alguma falhou → **parar e perguntar** antes de continuar
- Nunca gerar conteúdo incompleto silenciosamente

---

## 5. REGRA DE LEITURA PARALELA

**Sempre ler todos os links em paralelo** — nunca um por um.
- Múltiplas chamadas WebFetch simultâneas
- Sites bloqueados: usar Claude in Chrome em paralelo com os demais
- Só processar após TODOS os links lidos ou reportados

---

## 6. PALETA VISUAL

| Elemento | Valor |
|---|---|
| Cor primária | `#796FFE` (roxo) |
| Fundo | `#FCFCFC` |
| Texto | `#1B1B1B` |
| Divisores | `3px solid #030712`, 50% width, centralizado |
| Gold accent (artigo) | `#c9a020` |
| Risk color | `#c44000` |
| Max-width | 670px (newsletter) / 680px (artigo) |

---

## 7. PADRÃO TIPOGRÁFICO

| Elemento | Font-family | Tamanho | Peso |
|---|---|---|---|
| H1 título principal | `'Trebuchet MS', Arial, sans-serif` | 28–32px | 900 |
| H2 seção | `'Trebuchet MS', Arial, sans-serif` | 20px | 800 |
| H3 sub-seção | `'Trebuchet MS', Arial, sans-serif` | 16px | 700 |
| Labels / metadados | `'Trebuchet MS', Arial, sans-serif` | 11–12px | 700 |
| Corpo — artigo | `'Georgia', serif` | 16–17px | 400 |
| Corpo — newsletter | `Helvetica, Arial, sans-serif` | 16px | 400 |

> Georgia no artigo = editorial, leitura longa. Helvetica na newsletter = limpa, email client.

---

## 8. CONTAINER DO ARTIGO

```html
<div style="max-width:680px;margin:0 auto;padding:0 16px;
            font-family:'Georgia',serif;color:#0a0a0a;
            background:#ffffff;box-sizing:border-box;">
```

`padding:0 16px` é o valor calibrado para equilibrar mobile e desktop no Ghost email. Valores maiores (28px+) sufocam o mobile; valores menores (0) encostam nas bordas.

---

## 9. EMOJIS POR CATEGORIA DE NOTÍCIA

| Emoji | Categoria |
|---|---|
| 🗽 | EUA / Agenda Macro |
| 🔷 | Ethereum / Protocolo |
| 🏛️ | RWA / Finanças Tradicionais |
| 📉 | Quedas / Preços |
| 📈 | Altas / Mercado positivo |
| ⚖️ | Regulação |
| ⚠️ | Riscos / Geopolítica |
| 🇧🇷 | Brasil |
| ❄️ | Congelamento / Sanções |
| 🔍 | Auditoria / Transparência |
| 💵 | Stablecoins / Dólares |
| ⚡ | Bitcoin / Macro |
| 🤖 | IA / Tecnologia |
| 🏦 | DeFi / Protocolos |

---

## 10. GRAMÁTICA — ARTIGO FEMININO DE PROTOCOLOS

| Errado | Correto |
|---|---|
| o Morpho / do Morpho | **a Morpho / da Morpho** |
| o Base / do Base | **a Base / da Base** |

Aplicar em todo conteúdo gerado.

---

## 11. SITES COM COMPORTAMENTO CONHECIDO

**Bloqueiam (403) — usar Claude in Chrome:**
- beincrypto.com ❌
- br.beincrypto.com ❌
- cryptopotato.com ❌
- theblock.co ❌ (escrever do conhecimento mesmo com Chrome)

**Funcionam bem com WebFetch:**
- cointelegraph.com.br ✅
- coindesk.com ✅
- yahoo finance ✅
- coinpaprika.com ✅
- decrypt.co ✅
- thedefiant.io ✅
- thetokendispatch.com ✅
- cryptoslate.com ✅

**Fluxo Claude in Chrome:**
1. `tabs_context_mcp` → pegar tabId
2. `navigate` → abrir o link
3. `get_page_text` → extrair conteúdo

---

## 12. TRATAMENTO DE LINKS INACESSÍVEIS

Quando um link bloquear, obrigatoriamente:

1. Informar qual link falhou e o motivo
2. Propor **2 caminhos**:
   - **Caminho A:** Extrair tema do slug e pesquisar na web
   - **Caminho B:** Usuário cola o conteúdo manualmente (Ctrl+A, Ctrl+C, colar no chat)
3. **Aguardar a escolha** antes de continuar
4. Nunca ignorar silenciosamente

---

## 13. INFRA TÉCNICA

### Arquivo .env (localização: pasta do projeto)

```
GHOST_URL=https://newsletter-3.ghost.io
GHOST_ADMIN_KEY=<id>:<secret_hex>
FREEPIK_API_KEY=...
IMGBB_API_KEY=...
GEMINI_API_KEY=...
XAI_API_KEY=...
FAL_API_KEY=...
GROQ_API_KEY=...
```

### Arquivos do projeto

| Arquivo | Função |
|---|---|
| `newsletter_template.html` | Template base da newsletter — nunca gerar HTML do zero |
| `newsletter_content.html` | Saída preenchida da newsletter |
| `artigo_template.html` | Template base do artigo |
| `artigo_content.html` | Saída preenchida do artigo |
| `topicos.json` | Prompts de imagem da newsletter (1 por notícia) |
| `artigo_topicos.json` | Prompts de imagem do artigo (sempre 4) |
| `bot.py` | Script principal de geração + deploy |
| `logos/` | Logos salvas para composição nas imagens |

---

## 14. GHOST ADMIN API — DEPLOY

### Autenticação JWT

```python
import jwt
from datetime import datetime, timezone

def ghost_token(GHOST_ADMIN_KEY):
    key_id, secret = GHOST_ADMIN_KEY.split(":")
    iat = int(datetime.now(timezone.utc).timestamp())
    payload = {"iat": iat, "exp": iat + 300, "aud": "/admin/"}
    return jwt.encode(payload, bytes.fromhex(secret), algorithm="HS256",
                      headers={"kid": key_id})
```

### Criar draft (POST)

```python
lexical = json.dumps({
    "root": {
        "children": [{"type": "html", "version": 1, "html": html}],
        "direction": None, "format": "", "indent": 0,
        "type": "root", "version": 1
    }
})
r = requests.post(
    f"{GHOST_URL}/ghost/api/admin/posts/",
    headers={"Authorization": f"Ghost {token}", "Content-Type": "application/json"},
    json={"posts": [{"title": "...", "lexical": lexical, "status": "draft"}]},
    timeout=30
)
post_id = r.json()["posts"][0]["id"]
```

> **CRÍTICO:** Nunca usar `"html": html` direto — o Ghost editor mostra vazio.
> Sempre usar o formato **lexical** acima.

### Atualizar draft existente (PUT)

```python
# 1. Buscar updated_at primeiro (evita 409 conflict)
r = requests.get(f"{GHOST_URL}/ghost/api/admin/posts/{POST_ID}/",
                 headers={"Authorization": f"Ghost {token}"})
updated_at = r.json()["posts"][0]["updated_at"]

# 2. PUT com updated_at
r = requests.put(
    f"{GHOST_URL}/ghost/api/admin/posts/{POST_ID}/",
    headers={"Authorization": f"Ghost {token}", "Content-Type": "application/json"},
    json={"posts": [{"title": "...", "lexical": lexical,
                     "status": "draft", "updated_at": updated_at}]}
)
```

### Upload de imagem

```python
with open(img_path, "rb") as f:
    files = {"file": ("nome.jpg", f, "image/jpeg"), "purpose": (None, "image")}
    r = requests.post(f"{GHOST_URL}/ghost/api/admin/images/upload/",
                      headers={"Authorization": f"Ghost {token}"},
                      files=files, timeout=30)
url = r.json()["images"][0]["url"]  # status 201 = sucesso
```

### Substituição de placeholders após upload

```python
tag = '<div style="padding:20px 0;"><img src="{url}" style="width:100%;max-width:680px;display:block;margin:0 auto;border-radius:6px;"/></div>'
for i, url in img_urls.items():
    html = html.replace(f"[IMAGEM_{i}]", tag.format(url=url))
```

---

## 15. FLUXO COMPLETO — NEWSLETTER

```
1. Usuário cola links
2. Claude lê TODOS em paralelo (WebFetch simultâneo)
3. Reporta: "Li X de Y fontes"
4. Preenche newsletter_template.html → salva newsletter_content.html
5. Cria topicos.json (1 prompt por notícia)
6. Usuário gera imagens → salva img1.jpg ... imgN.jpg na pasta
7. Claude faz upload + substitui [IMAGEM_N] + posta DRAFT no Ghost
8. Usuário revisa e publica
```

### Estrutura de cada edição

1. Cabeçalho — título com data + subtítulo roxo
2. Seção de Mercado — BTC, ETH, Market Cap + gauge Fear & Greed
3. N notícias — emoji + H3 + **[IMAGEM_N] obrigatório** + 2 parágrafos + divisor
4. Rodapé

### Estilo de escrita por notícia

- **Parágrafo 1:** Hook de contexto → dados concretos → o que aconteceu
- **Parágrafo 2:** Implicação estrutural → risco ou oportunidade → perspectiva macro
- Frases: "O paradoxo é claro...", "O que chama atenção...", "A variável decisiva..."
- Sempre números reais: %, valores USD, datas, nomes de projetos
- Nunca opiniões vagas — sempre ancoradas em dados

---

## 16. FLUXO COMPLETO — ARTIGO

```
1. Usuário envia link, texto ou tema
2. Claude lê o conteúdo
3. Claude propõe EXATAMENTE 3 ângulos
4. Usuário escolhe (aguardar antes de escrever)
5. Claude escreve artigo completo no artigo_template.html
6. Claude cria artigo_topicos.json (4 prompts)
7. Usuário gera imagens → salva img1.jpg ... img4.jpg
8. Claude faz upload + substitui [IMAGEM_N] + posta DRAFT no Ghost
```

### Formato dos 3 ângulos

```
ÂNGULO 1
Título:      [Emoji + CAPS + pergunta ou afirmação provocadora]
Subheadline: [Uma frase que entrega a tese — tom de revelação]
Gancho:      [3 linhas de amostra com analogia local — sem dado ainda]

ÂNGULO 2
...

ÂNGULO 3
...
```

**Regras dos ângulos:**
- Perspectivas radicalmente diferentes: ex. oportunidade / risco / paradoxo
- Títulos curtos, diretos — sem frases de IA ("muda para sempre", "ninguém está falando sobre isso")
- Subheadline sempre 1 frase, nunca lista
- Gancho é amostra real, já no tom do artigo

### Estrutura obrigatória do artigo

```
1. GANCHO (sem título de seção)
   5–8 linhas. Analogia brasileira/familiar. Cria imagem mental antes de qualquer dado.

2. [IMAGEM_1] — logo após o gancho

3. TL;DR — 5–7 <li> com pontos objetivos + dados concretos

4. SEÇÃO DE CONTEXTO
   Por que isso importa agora. Dado de abertura com "Tradução:".

5. SEÇÃO PRINCIPAL (pode ter sub-tópicos H3)
   Núcleo da análise. Dados + o que significam. Cada dado seguido de explicação.

6. [IMAGEM_2] — após seção principal

7. SEÇÃO DE DESDOBRAMENTOS
   O que muda a partir disso. Cenários possíveis.

8. [IMAGEM_3] — aqui

9. SEÇÃO ADICIONAL (se necessário)
   Detalhe técnico, histórico ou dado complementar.

10. [IMAGEM_4] — se artigo tiver 3.000+ palavras

11. ⚠️ VAMOS SER HONESTOS: OS RISCOS (obrigatória — sempre presente)
    Bloco laranja. Mínimo 2 riscos, máximo 4. Nunca amenizar.

12. 🎯 PALAVRAS FINAIS
    USAR FUNDO CLARO COM BORDA ESCURA (não fundo escuro — quebra em dark mode).
    Síntese + lista Oportunidade/Risco + pergunta retórica final.

13. DISCLAIMER (fixo do template — não alterar)
```

### PALAVRAS FINAIS — HTML correto (email-safe)

```html
<table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:40px 0;">
  <tr>
    <td bgcolor="#f5f3ee" style="background:#f5f3ee;border-left:6px solid #030712;
        border-radius:0 8px 8px 0;padding:28px 32px;">
      <h2 style="font-family:'Trebuchet MS',Arial,sans-serif;font-size:18px;
                 font-weight:800;color:#030712;margin:0 0 16px 0;">
        🎯 PALAVRAS FINAIS
      </h2>
      <p style="font-family:'Georgia',serif;font-size:16px;line-height:1.85;
                color:#1a1a1a;margin:0 0 16px 0;">[Síntese da tese]</p>
      <ol style="...">
        <li><strong style="color:#c9a020;">Oportunidade:</strong> [descrição]</li>
        <li><strong style="color:#e88080;">Risco:</strong> [descrição]</li>
      </ol>
      <p style="...color:#030712;border-top:2px solid #030712;">[Frase final itálica]</p>
    </td>
  </tr>
</table>
```

> `bgcolor` em `<td>` é suportado por 100% dos email clients.
> `background-color` em `<div>` pode ser ignorado por Outlook.
> Fundo escuro (#030712) torna texto invisível em dark mode — NUNCA usar.

---

## 17. REGRAS DE TOM — ARTIGO

| O que fazer | Exemplo |
|---|---|
| Analogia local antes do dado | "É como o Nubank em 2015 — todo mundo ria..." |
| Tradução explícita após dado | "Tradução: Solana gera 3x mais atividade por dólar que Ethereum" |
| Crédito ao ceticismo antes do bull case | "Os céticos estão certos nos problemas. Podem estar errados na conclusão." |
| Frase de corte curta isolada | "Wall Street não paga por hype. Paga por estrutura." |
| Inglês cripto preservado | yield, funding rate, stake, TVL, front-run — nunca traduzir |
| Pergunta retórica no final | "A questão não é SE vai acontecer. É QUEM vai dominar primeiro." |

**Títulos — evitar frases de IA clichê:**
- ❌ "E NINGUÉM ESTÁ FALANDO SOBRE ISSO"
- ❌ "MUDA PARA SEMPRE"
- ❌ "E ISSO IMPORTA"
- ✅ Curto, direto, provocador — ex: "BLOCKCHAIN GANHOU. DESCENTRALIZAÇÃO PERDEU."

---

## 18. SISTEMA DE IMAGENS

### Regra de prompt: específico > genérico

**NUNCA:** "crypto finance dark style"
**SEMPRE:** elemento principal reconhecível da notícia + contexto específico

### Formato do prompt

```
[ELEMENTO PRINCIPAL RECONHECÍVEL] + [CONTEXTO ESPECÍFICO DA NOTÍCIA] +
Style: cinematic, ultra-realistic, [paleta relevante],
dramatic lighting, no text, no logos, no watermarks, 16:9 widescreen, 2k resolution.
```

### Paletas por tema (artigo)

| Tema | Paleta |
|---|---|
| Blockchain / Protocolo | Deep navy and electric blue tones |
| TradFi entrando em cripto | Gold and dark charcoal corporate tones |
| Regulação / Governo | American red, white and blue — serious |
| DeFi / Inovação | Purple and cyan neon on dark |
| Risco / Crise | Dark red and black — tension |
| Bitcoin / Store of value | Dark gold and obsidian |
| Competição / Batalha | Arena lighting, dramatic shadows |
| IA / Tecnologia | Arctic blue and silver, cold precision |
| Stablecoins / Dólares | Deep navy and gold, institutional |

### Estilo visual padrão

- Fotorrealista, cinematográfico, blockbuster
- Sem texto, sem logos, sem marcas d'água
- 16:9 widescreen | Iluminação dramática | 2k resolution
- Para energia máxima: acrescentar "IMAX dramatic lighting, extreme chiaroscuro"

### Logos mapeadas (composição automática pelo bot)

| Domínio | Empresa |
|---|---|
| `robinhood.com` | Robinhood |
| `aave.com` | Aave |
| `circle.com` | Circle / USDC |
| `franklintempleton.com` | Franklin Templeton |
| `ondo.finance` | Ondo Finance |
| `chain.link` | Chainlink |
| `glassnode.com` | Glassnode |

### Nomenclatura das imagens salvas pelo usuário

- Newsletter: `img1.jpg`, `img2.jpg` ... `imgN.jpg`
- Artigo: `img1.jpg`, `img2.jpg`, `img3.jpg`, `img4.jpg`
- O bot aceita extensão dupla (`img1.jpg.jpeg`) — normal em downloads de browser

### Fluxo manual de imagens (quando API Freepik indisponível)

1. Claude apresenta os prompts do `topicos.json` / `artigo_topicos.json`
2. Usuário gera no site Freepik Premium (não API)
3. Usuário salva na pasta do projeto com nomes corretos
4. Claude faz upload via Ghost Admin API + substitui placeholders + atualiza draft

---

## 19. SCRIPT PYTHON — UPLOAD + DEPLOY COMPLETO

```python
import sys, json, requests, jwt
from datetime import datetime, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

# Carregar .env
env = {}
with open(".env") as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()

GHOST_URL       = env["GHOST_URL"]
GHOST_ADMIN_KEY = env["GHOST_ADMIN_KEY"]
POST_ID         = "ID_DO_DRAFT_EXISTENTE"  # ou None para criar novo

def ghost_token():
    key_id, secret = GHOST_ADMIN_KEY.split(":")
    iat = int(datetime.now(timezone.utc).timestamp())
    payload = {"iat": iat, "exp": iat + 300, "aud": "/admin/"}
    return jwt.encode(payload, bytes.fromhex(secret), algorithm="HS256",
                      headers={"kid": key_id})

# 1. Upload das imagens
img_urls = {}
for i in range(1, 5):  # ajustar range para newsletter
    for ext in [f"img{i}.jpg", f"img{i}.jpg.jpeg", f"img{i}.jpeg", f"img{i}.png"]:
        p = Path(ext)
        if p.exists():
            token = ghost_token()
            with open(p, "rb") as f:
                files = {"file": (f"intus-img{i}.jpg", f, "image/jpeg"),
                         "purpose": (None, "image")}
                r = requests.post(f"{GHOST_URL}/ghost/api/admin/images/upload/",
                                  headers={"Authorization": f"Ghost {token}"},
                                  files=files, timeout=30)
            if r.status_code == 201:
                img_urls[i] = r.json()["images"][0]["url"]
                print(f"OK img{i}")
            break

# 2. Substituir placeholders
html = open("artigo_content.html", encoding="utf-8").read()
tag = '<div style="padding:20px 0;"><img src="{url}" style="width:100%;max-width:680px;display:block;margin:0 auto;border-radius:6px;"/></div>'
for i, url in img_urls.items():
    html = html.replace(f"[IMAGEM_{i}]", tag.format(url=url))

lexical = json.dumps({
    "root": {
        "children": [{"type": "html", "version": 1, "html": html}],
        "direction": None, "format": "", "indent": 0,
        "type": "root", "version": 1
    }
})

# 3a. Criar novo draft
token = ghost_token()
r = requests.post(f"{GHOST_URL}/ghost/api/admin/posts/",
    headers={"Authorization": f"Ghost {token}", "Content-Type": "application/json"},
    json={"posts": [{"title": "TITULO AQUI", "lexical": lexical, "status": "draft"}]},
    timeout=30)
post = r.json()["posts"][0]
print(f"Draft: {GHOST_URL}/ghost/#/editor/post/{post['id']}")

# 3b. Atualizar draft existente (usar em vez do 3a se POST_ID definido)
# token = ghost_token()
# r_get = requests.get(f"{GHOST_URL}/ghost/api/admin/posts/{POST_ID}/",
#                      headers={"Authorization": f"Ghost {token}"})
# updated_at = r_get.json()["posts"][0]["updated_at"]
# token = ghost_token()
# r = requests.put(f"{GHOST_URL}/ghost/api/admin/posts/{POST_ID}/",
#     headers={"Authorization": f"Ghost {token}", "Content-Type": "application/json"},
#     json={"posts": [{"title": "TITULO", "lexical": lexical,
#                      "status": "draft", "updated_at": updated_at}]})
```

---

## 20. DADOS DE MERCADO — NEWSLETTER

O bot.py busca automaticamente via:

```python
# CoinGecko (BTC, ETH, Market Cap, Volume, Dominância)
r = requests.get("https://api.coingecko.com/api/v3/simple/price",
    params={"ids": "bitcoin,ethereum", "vs_currencies": "usd",
            "include_24hr_change": "true"}, timeout=10)

r2 = requests.get("https://api.coingecko.com/api/v3/global", timeout=10)

# Fear & Greed
r3 = requests.get("https://api.alternative.me/fng/?limit=1", timeout=10)
```

Quando rodando script manual (sem bot.py), buscar esses dados e substituir os placeholders:
`[BTC_PRECO]`, `[BTC_VARIACAO]`, `[ETH_PRECO]`, `[ETH_VARIACAO]`,
`[MARKET_CAP]`, `[VOLUME_24H]`, `[BTC_DOMINANCE]`, `[FNG_VALOR]`, `[FNG_LABEL]`, `[GAUGE_URL]`

---

## 21. COMANDO BOT.PY

```bash
# Newsletter
python bot.py --titulo "Intus Cripto News - DD/MM/AAAA" --topicos topicos.json

# Artigo
python bot.py \
  --html artigo_content.html \
  --titulo "Título do Artigo" \
  --subtitulo "Subheadline aqui" \
  --topicos artigo_topicos.json
```

---

## 22. PRD — PRODUCT REQUIREMENTS DOCUMENT

### Visão do Produto

Sistema de produção editorial semi-automatizado para a Intus Cripto News.
Produz 2 tipos de conteúdo por semana com qualidade editorial consistente,
deploy automatizado no Ghost e sistema de imagens geradas por IA.

### Problema que resolve

- Produção manual de newsletters cripto é lenta (2–4h por edição)
- Consistência de tom e formato difícil de manter sem sistema
- Deploy no Ghost era manual e sujeito a erros de formatação
- Imagens genéricas prejudicam engajamento

### Solução

Pipeline semi-automatizado: Claude lê fontes → gera HTML → cria prompts de imagem →
usuário gera imagens → Claude faz deploy automatizado no Ghost via API.

### Usuários

| Perfil | Diego Spanevello |
|---|---|
| Papel | Fundador, editor único |
| Frequência | 2× por semana |
| Skill técnico | Intermediário — usa Claude Code, Python básico |
| Objetivo | Produzir conteúdo de qualidade com mínimo de fricção |

### Requisitos funcionais

| ID | Requisito | Prioridade |
|---|---|---|
| RF01 | Ler N links em paralelo e reportar falhas | CRÍTICO |
| RF02 | Preencher templates HTML (newsletter e artigo) sem alterar estrutura | CRÍTICO |
| RF03 | Gerar prompts de imagem específicos por notícia/seção | CRÍTICO |
| RF04 | Deploy no Ghost via JWT + lexical format | CRÍTICO |
| RF05 | Upload de imagens via Ghost Admin API | CRÍTICO |
| RF06 | Substituir [IMAGEM_N] pelos URLs reais após upload | CRÍTICO |
| RF07 | Propor 3 ângulos para artigos antes de escrever | ALTO |
| RF08 | Buscar dados de mercado (BTC, ETH, F&G) automaticamente | ALTO |
| RF09 | Tratar links bloqueados com 2 caminhos alternativos | ALTO |
| RF10 | Derivar thread e carrossel a partir do artigo | MÉDIO |

### Requisitos não-funcionais

| ID | Requisito |
|---|---|
| RNF01 | Tom consistente: técnico, analítico, causa-efeito, sem clickbait |
| RNF02 | HTML compatível com todos os email clients (inline styles, sem classes CSS) |
| RNF03 | PALAVRAS FINAIS sempre com fundo claro (dark mode safe) |
| RNF04 | Imagens sempre 16:9, sem texto, sem logos, sem watermarks |
| RNF05 | Nenhuma notícia omitida sem autorização do usuário |
| RNF06 | JWT expira em 5 min — regenerar antes de cada chamada à API |

### Restrições técnicas

- Ghost usa formato **lexical** para conteúdo — HTML puro não funciona
- PUT no Ghost exige `updated_at` correto (evitar 409 conflict)
- Imagens devem ser JPEG para compatibilidade máxima
- `sys.stdout.reconfigure(encoding="utf-8")` obrigatório em scripts Python no Windows

### Fluxo de dados

```
Links do usuário
      ↓
WebFetch / Chrome (paralelo)
      ↓
Claude processa + gera HTML
      ↓
artigo_content.html / newsletter_content.html
      ↓
artigo_topicos.json / topicos.json (prompts)
      ↓
Usuário gera imagens (Freepik)
      ↓
img1.jpg ... imgN.jpg na pasta
      ↓
Script Python: upload → substituição → lexical → POST/PUT Ghost
      ↓
Draft no Ghost → Usuário revisa → Publica
```

### Evolução futura (backlog)

- [ ] Geração automática de imagens via API Freepik (bot.py já tem implementação)
- [ ] Derivação automática de thread Twitter após artigo
- [ ] Derivação automática de roteiro de carrossel após artigo
- [ ] Agendamento de publicações no Ghost
- [ ] Dashboard de métricas de engajamento por edição

---

## 23. EXEMPLOS DE PROMPTS DE IMAGEM APROVADOS

| Notícia | Prompt correto |
|---|---|
| Circle/Coinbase caem na bolsa | Red declining stock chart, Circle USDC coin crashing, Wall Street panic selling |
| Tether contrata Big Four | Financial auditor examining vault with USDT coins, magnifying glass on documents |
| Wallets congeladas (sanções) | Digital wallet frozen in ice, padlock, sanctions enforcement visualization |
| Bitcoin $71k + paz geopolítica | Golden Bitcoin stable on chart, diplomatic handshake between flags, ceasefire |
| Pix + Stablecoins Brasil | Brazilian Pix interface merging with stablecoins, Brazil flag colors, BRL |
| Hack / Exploit | Broken padlock on blockchain, hacker silhouette, smart contract vulnerability, red alert |
| Tokenização RWA | Physical asset dissolving into digital tokens on blockchain, institutional tones |
| DeFi TVL recorde | Decentralized finance ecosystem, liquidity pools, TVL counter, blockchain nodes |
| Regulação EUA | US Capitol or courthouse, gavel, regulatory framework glowing, American flag |
| IA + Cripto | AI agent with digital wallet, autonomous transactions, electric blue and silver |

---

*Intus Cripto Club · intuscripto.com.br · Fundador: Diego Spanevello*
