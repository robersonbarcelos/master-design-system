# PRD — Pipeline de Scoring de Leads Instagram

## Objetivo

Enriquecer leads capturados via ManyChat com dados do Instagram (bio, seguidores, sinal de negócio) e subir ao Supabase para qualificação e priorização no pipeline de vendas.

## Arquitetura atual

### Fonte de leads
- **Planilha:** Base Unificada 6 (`1qQSFlaZai7dWUEn8QAk0mM8GO1EpLVmNiu-2GE-g45s`), aba `leads_v6`
- **Colunas relevantes:** `ig_username`, `unified_lead_id`, `has_lastlink`, `has_whatsapp_group`, `batch`, `lastlink_produto_1..5`
- **Export:** Arquivo > Fazer download > CSV (valores separados por vírgula)

### Enriquecimento (ScrapeCreators)

Fluxo de 2 etapas por lead:

1. `GET /v1/instagram/search?query={handle}` — 1 crédito → retorna lista de usuários; pegar o `id` do resultado com `username` exato
2. `GET /v1/instagram/basic-profile?userId={id}` — 1 crédito → retorna `biography`, `follower_count`, `is_business`, `is_private`

**Por que esse fluxo:** O endpoint `/v1/instagram/profile?handle=X` falha (retorna sem dados) para perfis privados. O caminho search→userId→basic-profile funciona para perfis públicos E privados.

**Custo:** 2 créditos/lead. 200 leads = 400 créditos.

### Scoring (local, sem API)

Campos calculados a partir da bio:
- `has_business_signal`: True se bio contém palavras-chave do `BUSINESS_KEYWORDS` (ceo, founder, consultor, etc.)
- `matched_keywords`: lista das palavras encontradas

### Supabase

Tabela `leads`. PK = `id` = `ig_username`.

Colunas escritas pelo pipeline:

| Coluna | Tipo | Fonte |
|---|---|---|
| `bio` | text | basic-profile.biography |
| `followers` | int | basic-profile.follower_count |
| `business` | bool | basic-profile.is_business |
| `kw` | text[] | matched keywords da bio |
| `error` | bool | True se houve erro de scraping |
| `error_reason` | text | Mensagem do erro (ex: "perfil privado") |
| `score` | int | Calculado separadamente |
| `tags` | text[] | Tags de produto (ex: lastlink:intus-cri) |
| `in_pipeline` | bool | True quando movido para pipeline |
| `pipeline_added_at` | timestamptz | Set automaticamente por trigger |

### Tags de produto (Apps Script)

Lidas da planilha (colunas `lastlink_produto_1..5`) via Google Apps Script.
Script ID: `1-sE4ZBcsLK6Swj-WQHNSVgfz6FOlCdM0UbAJVfW4XGoWfNyOJi6EaHP-`
Função: `lote5Completo()` — lê tags, pinta linhas de roxo (#D9B8FF), exporta mapeamento para aba temporária `lote5_tags_export`.

## Sequência de execução para novo lote

1. Exportar handles não pintados via Apps Script (`exportarLoteN()`) → aba `loteN_export`
2. Baixar CSV da aba exportada → `leads_loteN_input.csv`
3. `python lead_scoring.py leads_loteN_input.csv --out leads_loteN_scored.csv`
4. Checar CSV scored: quantos com erro, quais tipos
5. `python upload_loteN_supabase.py` — UPSERT no Supabase (usar POST com `Prefer: resolution=merge-duplicates`, nunca PATCH)
6. Rodar `pintarLoteN()` no Apps Script para pintar planilha com `#D9B8FF`
7. Verificar dashboard em `https://dashboard-crm-intus.vercel.app/`

## Critérios de ordenação no pipeline

Leads entram no pipeline ordenados por `pipeline_added_at ASC NULLS LAST` — os mais antigos primeiro, novos sempre ao final da fila. Isso é garantido por trigger no Supabase (`trg_pipeline_added_at`).
