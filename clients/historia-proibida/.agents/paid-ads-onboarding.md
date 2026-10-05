# Paid Ads Onboarding — [Nome do Cliente]
# Roteiro de coleta de dados para execução via API

> **Para quem é isso:** este arquivo é preenchido uma vez por cliente.
> Depois de completo, as skills de execução (meta-ads-ratos, google-ads-ratos, ga4-ratos)
> leem automaticamente para criar campanhas, monitorar métricas e gerar relatórios reais.
>
> **Tempo estimado para preencher:** 15–30 minutos (com os acessos em mãos).
> **Nível técnico:** não precisa saber programar — só seguir os passos de cada seção.

---

## ════════════════════════════════════════
## BLOCO 1 — IDENTIDADE DO CLIENTE
## ════════════════════════════════════════

```yaml
cliente:
  nome: ""                          # Nome do cliente / marca
  responsavel: ""                   # Nome de quem você fala (dono, gestor de tráfego)
  nicho: ""                         # Ex: infoprodutos / e-commerce moda / serviço local / SaaS
  site_principal: ""                # Ex: https://meusite.com.br
  data_onboarding: ""               # Ex: 2026-05-22
```

---

## ════════════════════════════════════════
## BLOCO 2 — META ADS
## ════════════════════════════════════════

```yaml
meta_ads:

  # ── Conta de anúncios ─────────────────────────────────
  ad_account_id: ""                 # Ex: act_905545132380980
                                    # 📍 ONDE ACHAR: ver tutorial A abaixo

  # ── Facebook Page ─────────────────────────────────────
  page_id: ""                       # Ex: 108234567890123
                                    # 📍 ONDE ACHAR: ver tutorial B abaixo

  # ── Instagram ─────────────────────────────────────────
  instagram_id: ""                  # Ex: 17841400123456789 (ID numérico, não o @)
  instagram_username: ""            # Ex: @minhamarca
                                    # 📍 ONDE ACHAR: ver tutorial C abaixo

  # ── Pixel / Rastreamento ──────────────────────────────
  pixel_id: ""                      # Ex: 905545132380980
  capi_ativo: false                 # true / false
  emq_score: null                   # Ex: 7.2 — ou deixar null se não souber
  evento_conversao_principal: ""    # Ex: Lead / Purchase / CompleteRegistration
  url_confirmacao: ""               # Ex: https://site.com/obrigado (página pós-conversão)
                                    # 📍 ONDE ACHAR: ver tutorial D abaixo

  # ── Budget e metas ────────────────────────────────────
  budget_mensal_brl: 0              # Ex: 3000 (em reais, sem R$)
  cpa_meta_brl: 0                   # Ex: 25.00 (custo por resultado desejado)
  roas_meta: null                   # Ex: 3.5 — ou null se for campanha de CPL
  objetivo_principal: ""            # leads / vendas / trafego / awareness

  # ── Landing pages ─────────────────────────────────────
  landing_pages:
    captura: ""                     # Ex: https://site.com/captura
    vendas: ""                      # Ex: https://site.com/vendas
    checkout: ""                    # Ex: https://pay.hotmart.com/...
    confirmacao: ""                 # Ex: https://site.com/obrigado

  # ── Convenção UTM ─────────────────────────────────────
  utm_convention:
    source: "facebook"              # Padrão: facebook
    medium: "cpc"                   # Padrão: cpc
    campaign_pattern: ""            # Ex: {objetivo}-{publico}-{mes} → leads-frio-maio26
    content_pattern: ""             # Ex: {formato}-{variacao} → video-v1 / static-v2
```

---

## ════════════════════════════════════════
## BLOCO 3 — GOOGLE ADS
## ════════════════════════════════════════

> Preencher apenas se o cliente usar Google Ads.
> Se não usar, deixar tudo em branco ou remover o bloco.

```yaml
google_ads:

  # ── Conta ─────────────────────────────────────────────
  customer_id: ""                   # Ex: 1234567890 (sem hífens)
  mcc_id: ""                        # Ex: 9876543210 (se tiver MCC/conta gerenciadora)
                                    # 📍 ONDE ACHAR: ver tutorial E abaixo

  # ── Developer token ────────────────────────────────────
  developer_token: ""               # Gerado na Central de API do Google Ads
                                    # 📍 ONDE ACHAR: ver tutorial E abaixo

  # ── Budget e metas ────────────────────────────────────
  budget_mensal_brl: 0
  cpa_meta_brl: 0
  roas_meta: null

  # ── Tipos de campanha ativos ───────────────────────────
  tipos_campanha:
    - search: false
    - pmax: false
    - display: false
    - youtube_ads: false
```

---

## ════════════════════════════════════════
## BLOCO 4 — GOOGLE ANALYTICS 4 (GA4)
## ════════════════════════════════════════

```yaml
ga4:

  property_id: ""                   # Ex: 123456789 (sem "properties/")
                                    # 📍 ONDE ACHAR: ver tutorial F abaixo

  auth_mode: "service_account"      # service_account (recomendado) ou oauth2

  # Se service_account:
  credentials_path: ""              # Ex: ~/.claude/skills/ga4-ratos/credentials.json

  # Eventos de conversão configurados no GA4
  eventos_conversao:
    - nome: ""                      # Ex: generate_lead
    - nome: ""                      # Ex: purchase
```

---

## ════════════════════════════════════════
## BLOCO 5 — ACESSO À META APP (API)
## ════════════════════════════════════════

> Necessário para a execução via meta-ads-ratos.
> Configurado uma vez no .env da skill — não fica aqui no cliente.
> Apenas anote se o app já está configurado.

```yaml
meta_app:
  app_configurado: false            # true se já fez o setup do meta-ads-ratos
  app_id: ""                        # Ex: 905545132380980
  app_modo: ""                      # development / live (precisa ser live para criar anúncios)
  token_tipo: ""                    # user_token / system_token
  token_expira: ""                  # Data de expiração — tokens de usuário expiram!
                                    # 📍 ONDE ACHAR: ver tutorial G abaixo
```

---

## ════════════════════════════════════════════════════════
## TUTORIAIS — COMO ENCONTRAR CADA INFORMAÇÃO
## ════════════════════════════════════════════════════════

---

### 📋 TUTORIAL A — ID da Conta de Anúncios (Meta)

**O que é:** identificador único da conta de anúncios do cliente no Meta.
**Formato:** act_XXXXXXXXXXXXXXXXX

**Passo a passo:**
1. Acesse [business.facebook.com](https://business.facebook.com) → faça login
2. No menu lateral, clique em **Contas de anúncios**
3. O ID aparece abaixo do nome da conta no formato `act_XXXXXXXXX`
4. **Alternativa:** abra o Gerenciador de Anúncios → a URL contém o ID:
   `https://www.facebook.com/adsmanager/manage/...?act=XXXXXXXXX`
5. Copie o número COM o prefixo `act_`

> ⚠️ Atenção: clientes com múltiplas contas — confirmar qual conta é a correta antes de preencher.

---

### 📋 TUTORIAL B — Page ID (Página do Facebook)

**O que é:** ID numérico da Página do Facebook que vai aparecer nos anúncios.
**Formato:** número com 15–16 dígitos

**Passo a passo:**
1. Acesse a Página do Facebook do cliente
2. Clique em **Sobre** (na barra lateral da página)
3. Role até o final → procure por **ID da Página**
4. **Alternativa rápida:** acesse [findmyfbid.in](https://www.findmyfbid.in) e cole a URL da página

> 💡 Dica: se o cliente tiver o Business Manager configurado, vá em:
> Configurações do Business → Contas → Páginas → clique na página → o ID aparece na URL

---

### 📋 TUTORIAL C — Instagram ID numérico

**O que é:** identificador único do perfil no Instagram (diferente do @username).
**Formato:** número com 17–18 dígitos

**Passo a passo:**
1. Acesse [stormlikes.net/tools/instagram-id](https://stormlikes.net/tools/instagram-id)
   **ou** [findinstagramid.com](https://www.findinstagramid.com)
2. Digite o @username do cliente (sem o @)
3. Clique em **Find ID** → copie o número retornado

**Alternativa via Business Manager:**
1. Business Manager → Configurações → Contas do Instagram
2. Clique no perfil → ID aparece na URL ou nos detalhes

> ⚠️ O @ (username) muda — o ID numérico nunca muda. Sempre use o ID.

---

### 📋 TUTORIAL D — Pixel ID e configuração de conversão

**O que é:** código de rastreamento do Meta instalado no site do cliente.
**Formato:** número com 15–16 dígitos

**Encontrar o Pixel ID:**
1. Gerenciador de Anúncios → menu de hambúrguer (≡) → **Eventos**
2. Clique em **Gerenciador de Eventos**
3. A lista mostra todos os pixels — copie o ID do pixel ativo

**Verificar qual evento de conversão está configurado:**
1. No Gerenciador de Eventos → clique no pixel
2. Vá em **Atividade de eventos** → veja quais eventos chegam
3. O evento principal é geralmente: `Lead` (geração de leads) ou `Purchase` (vendas)

**URL de confirmação:**
- É a página que o cliente abre APÓS converter (ex: "Obrigado pelo cadastro")
- Confirme com o cliente qual é essa URL
- Se não houver página de obrigado → ative o evento via botão (Conversions API)

**Verificar EMQ Score:**
1. Gerenciador de Eventos → clique no pixel → **Qualidade dos eventos**
2. O número ao lado de cada evento é o EMQ Score (0–10)
3. Acima de 7.0 = bom | Abaixo de 5.0 = problema crítico

---

### 📋 TUTORIAL E — Google Ads Customer ID e Developer Token

**Customer ID (ID da Conta):**
1. Acesse [ads.google.com](https://ads.google.com) → faça login
2. O ID aparece no canto superior direito no formato `XXX-XXX-XXXX`
3. Remova os hífens: `1234567890`

**Developer Token:**
1. No Google Ads → clique no ícone de ferramentas (🔧) → **API Center** (Central de API)
2. Se não aparecer: você não tem acesso de administrador — peça ao cliente para compartilhar
3. Copie o **Token de desenvolvedor** da página
4. Status deve ser **Aprovado para acesso de teste** (mínimo) ou **Aprovado para acesso padrão**

> ⚠️ Token em **Aprovado para acesso de teste** só funciona em contas de teste.
> Para produção real, solicitar **Acesso padrão** no mesmo painel.

---

### 📋 TUTORIAL F — GA4 Property ID

**O que é:** identificador da propriedade GA4 vinculada ao site.
**Formato:** número com 9 dígitos (ex: 123456789)

**Passo a passo:**
1. Acesse [analytics.google.com](https://analytics.google.com)
2. Selecione a conta do cliente (canto superior esquerdo)
3. Selecione a propriedade GA4 (atenção: não confunda com Universal Analytics)
4. Vá em **Admin** (engrenagem no canto inferior esquerdo)
5. Em **Propriedade** → **Configurações da propriedade**
6. O **ID da propriedade** aparece no topo (ex: `123456789`)
7. **NÃO** incluir o prefixo "properties/" — só o número

**Criar Service Account (autenticação recomendada):**
1. Acesse [console.cloud.google.com](https://console.cloud.google.com)
2. Selecione ou crie um projeto
3. Menu → **IAM e administração** → **Contas de serviço**
4. Clique em **+ Criar conta de serviço**
5. Dê um nome (ex: `ga4-ratos-cliente`) → clique em **Criar e continuar**
6. Conceda a função: **Visualizador** → clique em **Concluir**
7. Clique na conta criada → aba **Chaves** → **Adicionar chave** → **JSON**
8. Baixe o arquivo JSON → salve em `~/.claude/skills/ga4-ratos/credentials-[cliente].json`
9. **Autorizar no GA4:**
   - Volte ao GA4 → Admin → **Gerenciamento de acesso da propriedade**
   - Clique em **+** → **Adicionar usuários**
   - Cole o e-mail da service account (ex: `ga4-ratos@meu-projeto.iam.gserviceaccount.com`)
   - Função: **Visualizador** → salve

---

### 📋 TUTORIAL G — Meta App Token (para meta-ads-ratos)

> Este passo configura a skill meta-ads-ratos, não é específico por cliente.
> Fazer uma vez — o token fica no `.env` da skill.

**Passo a passo:**
1. Acesse [developers.facebook.com](https://developers.facebook.com) → **Meus Apps**
2. Crie um novo app (tipo: **Business**) ou use um existente
3. **IMPORTANTE:** o app precisa estar em **modo Live** para criar anúncios reais
   - No painel do app → toggle no topo: **Desenvolvimento → Ativo (Live)**
4. Vá em **Ferramentas** → **Graph API Explorer**
5. Selecione seu app → clique em **Gerar token de acesso**
6. Marque as permissões:
   - `ads_management`
   - `ads_read`
   - `business_management`
   - `pages_read_engagement`
   - `instagram_basic`
7. Copie o token gerado
8. Abra `~/.claude/skills/meta-ads-ratos/.env` e preencha:
   ```
   META_ADS_TOKEN=seu_token_aqui
   META_APP_ID=seu_app_id
   META_AD_ACCOUNT_ID=act_XXXXXXXXX  (conta padrão)
   ```

> ⚠️ Tokens de usuário expiram em 60 dias. Para token permanente → gerar **System User Token**
> no Business Manager → Configurações → Usuários do sistema.

---

## ════════════════════════════════════════
## CHECKLIST DE VALIDAÇÃO
## ════════════════════════════════════════

Antes de marcar o onboarding como completo, confirme cada item:

### Meta Ads
- [ ] ID da conta de anúncios preenchido (`act_XXXXXXXXX`)
- [ ] Page ID preenchido
- [ ] Instagram ID numérico preenchido
- [ ] Pixel ID preenchido
- [ ] Evento de conversão principal definido
- [ ] URL de confirmação preenchida
- [ ] EMQ Score verificado (meta: > 7.0)
- [ ] Budget mensal e CPA meta definidos
- [ ] URLs de todas as landing pages preenchidas
- [ ] Convenção UTM definida
- [ ] App Meta em modo Live ✓

### Google Ads (se usar)
- [ ] Customer ID preenchido (sem hífens)
- [ ] Developer Token obtido
- [ ] Budget e CPA meta definidos

### GA4
- [ ] Property ID preenchido
- [ ] Service Account criada e autorizada na propriedade
- [ ] Arquivo JSON de credenciais salvo em `~/.claude/skills/ga4-ratos/`
- [ ] Pelo menos 1 evento de conversão configurado no GA4

### Teste de conexão
Após preencher, rode os testes de cada skill:
```bash
# Meta Ads
python3 ~/.claude/skills/meta-ads-ratos/scripts/setup.py
# → deve listar contas disponíveis

# Google Ads
python3 ~/.claude/skills/google-ads-ratos/scripts/setup.py test
# → deve listar campanhas

# GA4
python3 ~/.claude/skills/ga4-ratos/scripts/read.py account --property [PROPERTY_ID]
# → deve retornar nome e timezone da propriedade
```

---

## ════════════════════════════════════════
## REGISTRO DE ONBOARDING
## ════════════════════════════════════════

```yaml
onboarding:
  realizado_por: ""                 # Seu nome
  data: ""                          # Data de conclusão
  status: "pendente"                # pendente / em_andamento / completo
  observacoes: ""                   # Qualquer nota relevante

  # Itens pendentes (preencher o que ainda falta)
  pendencias:
    - ""
```
