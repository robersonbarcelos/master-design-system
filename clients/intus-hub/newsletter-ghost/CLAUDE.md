# Intus Cripto — Regras para o Claude

---

## ⚠️ PERGUNTA OBRIGATÓRIA AO INICIAR QUALQUER SESSÃO DE CONTEÚDO

**Sempre que o usuário iniciar uma sessão de geração de conteúdo (enviando links, pedindo para escrever algo, ou mencionando "newsletter"), perguntar PRIMEIRO:**

> "É uma **newsletter** (links de notícias da semana) ou um **artigo** (análise aprofundada de um tema)?"

- Nunca assumir que é newsletter só porque há links
- Nunca assumir que é artigo só porque é um tema único
- **Aguardar a resposta antes de prosseguir**

---

## REGRA DE IMAGENS POR FORMATO — INQUEBRÁVEL ⚠️

| Formato | Quantidade de imagens |
|---|---|
| **Newsletter** | **1 imagem por notícia** — se são 10 notícias, são 10 imagens. Sem exceção. |
| **Artigo** | **Sempre 4 imagens** distribuídas ao longo do conteúdo (IMAGEM_1 a IMAGEM_4). |

**Nunca reduzir ou distribuir de forma diferente** — layout, tamanho da newsletter ou qualquer outro critério não justifica quebrar essa regra.

---

## REGRA: VERIFICAÇÃO DE LEITURA ANTES DE ESCREVER ⚠️

Após ler todos os links e textos fornecidos pelo usuário, **obrigatoriamente reportar**:

> "Li X de Y fontes. [Lista das que não consegui acessar, se houver]."

- Se todas foram lidas: confirmar e prosseguir
- Se alguma falhou: **parar e perguntar** se o usuário quer fornecer o conteúdo manualmente antes de continuar
- **Nunca gerar conteúdo incompleto silenciosamente** — o usuário sempre decide o que fazer com fontes inacessíveis

---

## REGRA DE GRAMÁTICA — ARTIGO FEMININO DE PROTOCOLOS/BLOCKCHAINS ⚠️

Alguns nomes de protocolos e blockchains são **femininos** em português:

| Forma errada | Forma correta |
|---|---|
| o Morpho / do Morpho / no Morpho | **a Morpho / da Morpho / na Morpho** |
| o Base / do Base / no Base | **a Base / da Base / na Base** |

Aplicar em todo o conteúdo gerado — artigos, newsletters e qualquer outro formato.

---

## Identidade da Newsletter
- Nome: Intus Cripto News
- Frequência: 2x por semana
- Público: investidores cripto brasileiros, nível técnico intermediário/avançado
- Idioma: Português brasileiro
- Tom: técnico, analítico, causa-efeito, sem clickbait

---

## REGRA CRÍTICA: Todas as notícias entram na newsletter ⚠️

**Todas as notícias fornecidas pelo usuário DEVEM entrar na newsletter — sem exceção.**
- Nunca filtrar, selecionar ou reduzir o número de notícias
- Se o usuário passa 10 links → newsletter tem 10 notícias
- Se o usuário passa 6 links → newsletter tem 6 notícias
- A única exceção é link inacessível (ver seção abaixo) — mas nesse caso reportar ao usuário ANTES de prosseguir

---

## Estrutura de cada edição

1. **Cabeçalho** — título com data + subtítulo roxo
2. **Seção de Mercado** — BTC, ETH, Market Cap + gauge Fear & Greed (placeholders automáticos)
3. **N notícias** — cada uma com emoji + H3 + **[IMAGEM_N] obrigatório** + 2 parágrafos + divisor (10 notícias = 10 imagens, sem exceção)
4. **Rodapé** — © Intus Cripto

> **Usar o template base:** `newsletter_template.html` — nunca gerar HTML do zero.
> Preencher apenas os slots `<!-- SLOT_MERCADO_EXTRA -->` e `<!-- NOTICIA_N -->`.

---

## Estilo de escrita (por notícia)

- **Parágrafo 1:** Hook de contexto → dados/números concretos → o que aconteceu
- **Parágrafo 2:** Implicação estrutural → risco ou oportunidade → perspectiva macro
- Frases analíticas: "O paradoxo é claro...", "O que chama atenção...", "A variável decisiva..."
- Sempre incluir números reais: %, valores em USD, datas, nomes de projetos
- Nunca opiniões vagas — sempre ancoradas em dados

---

## Emojis por categoria de notícia

| Emoji | Categoria |
|-------|-----------|
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

## Paleta visual (HTML)

- Cor primária: `#796FFE` (roxo)
- Fundo: `#FCFCFC`
- Texto: `#1B1B1B`
- Divisores: `3px solid #030712`, largura 50%, centralizado
- Fonte body: Helvetica, 16px, line-height 26px
- Fonte títulos: Trebuchet MS, H3 = 20px, H1 = 36px
- Max-width: 670px

---

## PADRÃO TIPOGRÁFICO — Válido para TODOS os formatos ⚠️

Aplicar nas newsletters, artigos e qualquer outro HTML gerado.

| Elemento | Font-family | Tamanho | Peso |
|---|---|---|---|
| H1 (título principal) | `'Trebuchet MS', Arial, sans-serif` | 28–32px | 900 |
| H2 (seção) | `'Trebuchet MS', Arial, sans-serif` | 20px | 800 |
| H3 (sub-seção) | `'Trebuchet MS', Arial, sans-serif` | 16px | 700 |
| Labels / metadados | `'Trebuchet MS', Arial, sans-serif` | 11–12px | 700 |
| Corpo de texto — artigo | `'Georgia', serif` | 16–17px | 400 |
| Corpo de texto — newsletter | `Helvetica, Arial, sans-serif` | 16px | 400 |

> Georgia no artigo = mais editorial, melhor para leitura longa.
> Helvetica na newsletter = mais limpa, melhor para e-mail client.

---

## CONTAINER DO ARTIGO — Margem lateral obrigatória ⚠️

O container externo do artigo **sempre** deve incluir `padding:0 24px` para evitar que o texto encoste nas bordas da página.

```html
<div style="max-width:680px;margin:0 auto;padding:0 24px;
            font-family:'Georgia',serif;color:#0a0a0a;
            background:#ffffff;box-sizing:border-box;">
```

Sem `padding:0 24px` → texto encosta nas bordas (bug confirmado no Ghost).

---

## ESTILO DO ARTIGO — Regras de HTML para email ⚠️

> Aplicar sempre ao preencher `artigo_content.html`.

### Cabeçalho do artigo

| Campo | Valor correto |
|---|---|
| Label superior | `INTUS CRIPTO · NEWSLETTER` |
| Autor | `Por Diego Spanevello · Intus Cripto` |
| H1 font-family | `Arial, Helvetica, sans-serif` |
| H1 font-size | `28px` |
| H1 font-weight | `900` |
| H1 line-height | `1.6` |
| H1 letter-spacing | `0px` |
| H1 color | `#030712` |

### Bloco "Palavras Finais" (conclusão)

**NÃO usar fundo escuro** — email clients em dark mode tornam o texto invisível mesmo com `color:#ffffff` forçado.

Usar fundo claro com borda escura:

```html
<table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:40px 0;">
  <tr>
    <td bgcolor="#f5f3ee" style="background:#f5f3ee;border-left:6px solid #030712;border-radius:0 8px 8px 0;padding:28px 32px;">
      <h2 style="...color:#030712;">🎯 PALAVRAS FINAIS</h2>
      <p style="...color:#1a1a1a;">...</p>
      <!-- Oportunidade em #c9a020, Risco em #c44000, texto corrido em #1a1a1a -->
      <p style="...color:#c9a020;border-top:2px solid #030712;">Frase final itálica</p>
    </td>
  </tr>
</table>
```

**Por que table e não div:** `bgcolor` em `<td>` é suportado por 100% dos email clients. `background-color` em `<div>` pode ser ignorado por Outlook e outros.

---

## REGRA DE IMAGENS — CRÍTICA ⚠️

**Cada imagem deve ser imediatamente reconhecível pelo tema da notícia.**
NÃO gerar imagens genéricas de "crypto/finance dark style".

### Formato do prompt correto:

```
[ELEMENTO PRINCIPAL RECONHECÍVEL DA NOTÍCIA] + [CONTEXTO ESPECÍFICO] +
Style: cinematic, ultra-realistic, [cores relevantes ao tema],
dramatic lighting, no text, no logos, no watermarks, 16:9 widescreen.
```

### REGRA DE LOGOS — obrigatória ⚠️

Quando a notícia menciona uma empresa ou protocolo com logo mapeada:
- **Sempre incluir o domínio no campo `logos` do `topicos.json`**
- A logo será composited sobre a imagem gerada pelo bot (não é mencionada no prompt)
- O prompt deve descrever o contexto visual SEM mencionar logos (o bot adiciona automaticamente)

**Empresas/protocolos mapeados (logos já salvas em `logos/`):**

| Domínio | Empresa |
|---------|---------|
| `robinhood.com` | Robinhood |
| `aave.com` | Aave |
| `circle.com` | Circle / USDC |
| `franklintempleton.com` | Franklin Templeton |
| `ondo.finance` | Ondo Finance |
| `chain.link` | Chainlink |
| `glassnode.com` | Glassnode |

Para adicionar nova empresa: salvar logo em `logos/` + adicionar entrada no `LOGO_MAP` do `bot.py`.

### Exemplos corretos:

| Notícia | Prompt base correto |
|---------|-------------------|
| Circle/Coinbase caem na bolsa | Red declining stock chart, Circle USDC coin crashing, Wall Street panic selling, financial crisis |
| Tether contrata Big Four | Financial auditor examining large vault with USDT gold coins, magnifying glass on documents, corporate audit |
| Carteiras congeladas (sanções) | Digital cryptocurrency wallet frozen in ice, padlock, Iran map silhouette, sanctions enforcement |
| Bitcoin $71k + paz geopolítica | Golden Bitcoin coin stable on chart, diplomatic handshake between US and Middle East flags, ceasefire |
| Pix + Stablecoins Brasil | Brazilian Pix interface merging with stablecoins, Brazil flag colors, digital payment flows, BRL |
| Polymarket + regulação EUA | US federal courthouse with gavel, prediction market screens, 11 states map highlighted |
| ARK Invest compra Circle | Cathie Wood / ARK logo, contrarian investor buying the dip, Circle stock chart |
| DeFi TVL recorde | Decentralized finance ecosystem, liquidity pools, TVL counter, blockchain nodes glowing |
| Mineração Bitcoin | Bitcoin mining rig hardware, energy consumption visualization, hash rate data |
| Hack / Exploit | Broken padlock on blockchain, hacker silhouette, smart contract vulnerability, red alert |

### Estilo visual padrão (sempre aplicar):
- Fotorrealista, cinematográfico
- Sem texto, sem logos, sem marcas d'água
- 16:9 widescreen
- Iluminação dramática
- Alta resolução (2k)
- Modelo Freepik Mystic: `realism`

---

## Links que costumam bloquear (403)

- beincrypto.com ❌ → usar Claude in Chrome
- theblock.co ❌ → bloqueado mesmo no Chrome (escrever do conhecimento)
- cryptopotato.com ❌ → usar Claude in Chrome

## Links que funcionam bem

- cointelegraph.com.br ✅
- coindesk.com ✅
- yahoo finance ✅
- coinpaprika.com ✅
- decrypt.co ✅
- thedefiant.io ✅

---

## Scraping — Como acessar páginas bloqueadas

Usar **Claude in Chrome** (MCP) para navegar como um humano real.
Fluxo:
1. `tabs_context_mcp` → pegar tabId
2. `navigate` → abrir o link
3. `get_page_text` → extrair o conteúdo completo

Sites que funcionam com Claude in Chrome (antes bloqueavam com WebFetch):
- beincrypto.com ✅
- br.beincrypto.com ✅
- cryptopotato.com ✅

**Sempre tentar Claude in Chrome antes de declarar link inacessível.**

---

## REGRA: Links inacessíveis (403 ou erro)

Quando um ou mais links bloquearem o acesso, OBRIGATORIAMENTE:

1. **Informar claramente** quais links não foram acessados e o motivo (403, timeout, etc.)

2. **Propor 2 caminhos para cada link bloqueado:**

   **Caminho A — Pesquisa pelo título/URL:**
   Extraio o tema do slug/título do link e pesquiso na web para reconstruir a notícia com dados reais.
   Exemplo: `beincrypto.com/tether-circle-freeze-wallex-iran-wallet` → pesquiso "Tether Circle freeze Wallex Iran wallet 2026"

   **Caminho B — Usuário cola o conteúdo:**
   Peço para o usuário abrir o link no navegador, selecionar tudo (Ctrl+A), copiar (Ctrl+C) e colar aqui no chat.

3. **Aguardar a escolha** antes de gerar o conteúdo daquela notícia.

4. **Nunca ignorar silenciosamente** um link bloqueado — sempre reportar e propor solução.

---

## REGRA: Leitura paralela de links ⚡

**Sempre ler todos os links em paralelo** — nunca um por um.
- Usar múltiplas chamadas WebFetch simultâneas (ou Agent com múltiplos fetches)
- Para links bloqueados (beincrypto, cryptopotato): usar Claude in Chrome em paralelo com os demais
- Só processar o conteúdo após TODOS os links estarem lidos (ou reportados como inacessíveis)

Isso reduz o tempo de pesquisa de ~2min para ~20s em edições com 10 links.

---

---

## FLUXO DE ARTIGO — Análise aprofundada

> Usar quando o usuário confirmar que quer um **artigo**, não uma newsletter.

### Passo 1 — Receber o conteúdo

O usuário pode enviar:
- Um link (ler via WebFetch / Chrome)
- Texto colado diretamente
- Tema descrito em palavras

### Passo 2 — Propor 3 ângulos

Após ler/entender o conteúdo, apresentar **exatamente 3 ângulos** no formato:

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
- Cada ângulo deve ter perspectiva radicalmente diferente (ex: oportunidade / risco / paradoxo)
- Títulos no formato Diego: Emoji + CAPS + pergunta OU afirmação forte
- Subheadline sempre em 1 frase, nunca lista
- Gancho é amostra real — já no tom do artigo

### Passo 3 — Aguardar escolha

Perguntar: *"Qual ângulo você prefere? Posso ajustar título ou subheadline antes de começar."*
Só desenvolver após confirmação.

### Passo 4 — Escrever o artigo completo

Usar o template `artigo_template.html` como base. Preencher os slots:

| Slot | O que preencher |
|---|---|
| `<!-- SLOT_TITULO -->` | Título sem emoji (o emoji vai no lexical do Ghost) |
| `<!-- SLOT_SUBTITULO -->` | Subheadline escolhida |
| `<!-- SLOT_TEMPO_LEITURA -->` | "7 minutos" ou "8 minutos" |
| `<!-- SLOT_TLDR -->` | 5-7 `<li>` com pontos objetivos + dados |
| `<!-- SLOT_CONTEUDO -->` | Todas as seções HTML conforme guia interno do template |

**Estrutura obrigatória do conteúdo:**

```
1. GANCHO (sem título de seção)
   5-8 linhas. Analogia do mundo real brasileiro/familiar.
   Cria imagem mental antes de qualquer dado.
   "Imagina...", "Em 2015...", "Pensa numa torneira..."

2. SEÇÃO DE CONTEXTO
   Por que isso importa agora. Dado de abertura com tradução.

3. SEÇÃO PRINCIPAL (pode ter sub-tópicos)
   O núcleo da análise. Dados duros + o que significam.
   Cada dado sempre seguido de "Tradução:" ou frase explicando ao leitor.

4. [IMAGEM_2] — inserir após seção principal

5. SEÇÃO DE DESDOBRAMENTOS
   O que muda a partir disso. Cenários possíveis.

6. [IMAGEM_3] — inserir aqui

7. SEÇÃO ADICIONAL (se necessário)
   Detalhe técnico, comparativo histórico, ou dado complementar.

8. [IMAGEM_4] — inserir se artigo tiver 3.000+ palavras

9. ⚠️ VAMOS SER HONESTOS: OS RISCOS (obrigatória — sempre presente)
   Usando o bloco laranja do template.
   Mínimo 2 riscos, máximo 4.
   Nunca amenizar — crédito real ao ceticismo.

10. 🎯 PALAVRAS FINAIS (conclusão no bloco escuro)
    Síntese + lista numerada Oportunidade/Risco + pergunta retórica final.

11. DISCLAIMER (fixo do template — não alterar)
```

### Regras de tom para artigos

| O que fazer | Exemplo |
|---|---|
| Analogia local antes do dado | "É como o Nubank em 2015 — todo mundo ria..." |
| Tradução explícita após dado | "Tradução: Solana gera 3x mais atividade por dólar que Ethereum" |
| Crédito ao ceticismo antes do bull case | "Os céticos estão certos nos problemas. Podem estar errados na conclusão." |
| Frase de corte curta isolada | "Wall Street não paga por hype. Paga por estrutura." |
| Inglês cripto preservado | yield, funding rate, stake, TVL, front-run — nunca traduzir |
| Pergunta retórica no final | "A questão não é SE vai acontecer. É QUEM vai dominar primeiro." |

### Criação do artigo_topicos.json

Após escrever o HTML, criar `artigo_topicos.json` com **3-4 entradas** (uma por `[IMAGEM_N]`):

```json
[
  {
    "descricao": "Imagem de abertura — tema central do artigo",
    "logos": ["dominio.com"],
    "logo_source": "ddg",
    "prompt": "Descrição visual cinematográfica relacionada ao tema central. Style: cinematic, ultra-realistic, [paleta], dramatic lighting, no text, no logos, no watermarks, 16:9 widescreen, 2k resolution."
  }
]
```

**Regra de paletas para artigos** (mais longa que newsletter — atmosfera mais consistente):

| Tema do artigo | Paleta |
|---|---|
| Blockchain / Protocolo | Deep navy and electric blue tones |
| TradFi entrando em cripto | Gold and dark charcoal corporate tones |
| Regulação / Governo | American red, white and blue — serious |
| DeFi / Inovação | Purple and cyan neon on dark |
| Risco / Crise | Dark red and black — tension |
| Bitcoin / Store of value | Dark gold and obsidian |
| Competição / Batalha de mercado | Arena lighting, dramatic shadows |

### Comando para rodar o bot com artigo

```bash
python bot.py \
  --html artigo_content.html \
  --titulo "Título do Artigo" \
  --subtitulo "Subheadline aqui" \
  --topicos artigo_topicos.json
```

O bot gera as imagens, compõe logos, e posta como DRAFT no Ghost — mesmo fluxo da newsletter.

---

## GERAÇÃO DE IMAGENS — STATUS E FLUXO MANUAL ⚠️

### Situação atual da API Freepik (abril/2026)

O plano **Freepik Premium** (site de assets) é **diferente** do plano **Freepik API** (developers.freepik.com).
- O bot usa a API de desenvolvedor — plano separado com cota própria
- Quando a cota da API esgota, o bot retorna `429` ou mensagem de trial expirado
- **Verificar saldo em:** `freepik.com/developers/dashboard/billing`

### Fluxo manual de imagens (quando a API não estiver disponível)

Usar este fluxo em vez de rodar o `bot.py` normalmente:

**Passo 1 — Claude gera os prompts**
Claude apresenta os 4 prompts prontos para copiar (já estão no `artigo_topicos.json`).

**Passo 2 — Usuário gera as imagens no Freepik (site)**
- Acessar o site Freepik com o plano Premium
- Usar o gerador de imagens AI do site (não a API)
- Usar os prompts exatamente como fornecidos

**Passo 3 — Usuário salva as imagens na pasta do projeto**
- Salvar em `C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub\newsletter-ghost\imagens-publicacao\`
- Nomes obrigatórios: `img1.jpg`, `img2.jpg`, `img3.jpg`, `img4.jpg` (ou `img1.jpeg` etc.)
- ⚠️ O browser pode salvar com extensão dupla (`img1.jpg.jpeg`) — isso é normal, o script aceita

**Passo 4 — Claude faz upload e posta o draft**
Claude roda um script Python que:
1. Faz upload das 4 imagens direto para o Ghost via Admin API
2. Substitui os `[IMAGEM_N]` no HTML pelos URLs do Ghost
3. Posta o draft usando **formato lexical** (obrigatório — HTML direto não funciona no Ghost)

### Formato correto para postar no Ghost via API ⚠️

**NUNCA** usar `"html": html` direto no payload — o Ghost editor mostrará vazio.
**SEMPRE** usar o formato lexical:

```python
lexical = json.dumps({
    "root": {
        "children": [{"type": "html", "version": 1, "html": html}],
        "direction": None, "format": "", "indent": 0,
        "type": "root", "version": 1
    }
})
body = {"posts": [{"title": "...", "lexical": lexical, "status": "draft"}]}
```

### Script de upload manual + post Ghost

```python
import sys, json, requests, jwt
from datetime import datetime, timezone
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

# Carregar .env manualmente (não usar load_dotenv em scripts inline)
env = {}
with open(".env") as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()

GHOST_URL       = env["GHOST_URL"]
GHOST_ADMIN_KEY = env["GHOST_ADMIN_KEY"]

def ghost_token():
    key_id, secret = GHOST_ADMIN_KEY.split(":")
    iat = int(datetime.now(timezone.utc).timestamp())
    payload = {"iat": iat, "exp": iat + 300, "aud": "/admin/"}
    return jwt.encode(payload, bytes.fromhex(secret), algorithm="HS256", headers={"kid": key_id})

# Upload das imagens
img_urls = {}
for i in range(1, 5):
    for ext in ["img%d.jpg" % i, "img%d.jpg.jpeg" % i]:
        path = Path(ext)
        if path.exists():
            token = ghost_token()
            with open(path, "rb") as f:
                files = {"file": (f"intus-artigo-img{i}.jpg", f, "image/jpeg"), "purpose": (None, "image")}
                r = requests.post(f"{GHOST_URL}/ghost/api/admin/images/upload/",
                                  headers={"Authorization": f"Ghost {token}"}, files=files, timeout=30)
            if r.status_code == 201:
                img_urls[i] = r.json()["images"][0]["url"]
                print(f"OK img{i}")
            break

# Substituir placeholders
html = open("artigo_content.html", encoding="utf-8").read()
tag = '<div style="padding:20px 0;"><img src="{url}" style="width:100%;max-width:680px;display:block;margin:0 auto;border-radius:6px;"/></div>'
for i, url in img_urls.items():
    html = html.replace(f"[IMAGEM_{i}]", tag.format(url=url))

# Postar draft (formato lexical obrigatório)
lexical = json.dumps({
    "root": {
        "children": [{"type": "html", "version": 1, "html": html}],
        "direction": None, "format": "", "indent": 0,
        "type": "root", "version": 1
    }
})
token = ghost_token()
r = requests.post(f"{GHOST_URL}/ghost/api/admin/posts/",
    headers={"Authorization": f"Ghost {token}", "Content-Type": "application/json"},
    json={"posts": [{"title": "TITULO AQUI", "lexical": lexical, "status": "draft"}]},
    timeout=30)
post = r.json()["posts"][0]
print(f"Draft: {GHOST_URL}/ghost/#/editor/post/{post['id']}")
```

---

## Plataforma de publicação

- **Ghost**
- URL: `https://newsletter-3.ghost.io`
- API Admin: funciona via JWT (PyJWT)
- Draft criado em: `{GHOST_URL}/ghost/api/admin/posts/`
- Revisar e publicar em: `https://newsletter-3.ghost.io/ghost/`

---

## Fluxo de trabalho

1. Usuário cola links das notícias
2. **Claude lê TODOS os links em paralelo** (WebFetch simultâneo)
3. Claude preenche o template `newsletter_template.html` com o conteúdo → salva em `newsletter_content.html`
4. Claude cria `topicos.json` com prompts de imagem ESPECÍFICOS + logos mapeadas
5. Rodar: `python bot.py --titulo "Intus Cripto News - DD/MM/AAAA" --topicos topicos.json`
6. Bot auto-fetcha F&G (alternative.me) + mercado (CoinGecko) → gera imagens em paralelo → upload Ghost → posta DRAFT
7. Usuário revisa em `https://newsletter-3.ghost.io/ghost/` e publica quando quiser
