# Intus Hub — Pipeline de Scoring de Leads

Pipeline completo: planilha → scrape Instagram → Supabase (dashboard) → pintura na planilha.

---

## Visão geral do fluxo

```
Planilha Google (Base Unificada 6)
  → Apps Script: exportar N handles não pintados → aba lote6_export
  → CSV local: leads_loteN_input.csv
  → lead_scoring.py: scrape ScrapeCreators (2 steps)
  → leads_loteN_scored.csv
  → upload_loteN_supabase.py: UPSERT no Supabase (INSERT + update)
  → Apps Script: pintar linhas processadas com #D9B8FF na planilha
```

---

## Credenciais (.env — nunca commitar)

```
SCRAPECREATORS_API_KEY=...
SUPABASE_SECRET_KEY=...        # chave secreta — nunca em código commitado
```

> `SUPABASE_URL` é hardcoded: `https://klsifkkixxcriacojdtd.supabase.co`
> A URL não é segredo e não vai no .env.

---

## Planilha

- **Nome:** Base Unificada 6
- **ID:** `1qQSFlaZai7dWUEn8QAk0mM8GO1EpLVmNiu-2GE-g45s`
- **Aba de trabalho:** `Cópia de leads_v6`
- **Coluna de Instagram:** coluna 7 (`instagram_handle_1`)
- **Cor de processado:** `#D9B8FF` (roxo claro) — linha inteira (colunas 1–20)
- **Apps Script ID:** `1-sE4ZBcsLK6Swj-WQHNSVgfz6FOlCdM0UbAJVfW4XGoWfNyOJi6EaHP-`

---

## Passo 1 — Exportar handles não processados via Apps Script

No editor Apps Script (`script.google.com`), usar `SpreadsheetApp.openById()` — **nunca** `getActiveSpreadsheet()` (retorna null em scripts standalone).

```javascript
function exportarLoteN() {
  var SHEET_ID = "1qQSFlaZai7dWUEn8QAk0mM8GO1EpLVmNiu-2GE-g45s";
  var LIMIT = 400;  // quantidade do lote
  var ss = SpreadsheetApp.openById(SHEET_ID);
  var sheet = ss.getSheetByName('Cópia de leads_v6');
  var lastRow = sheet.getLastRow();
  var handles = [];
  var BATCH = 1000;

  for (var start = 2; start <= lastRow && handles.length < LIMIT; start += BATCH) {
    var end = Math.min(start + BATCH - 1, lastRow);
    var count = end - start + 1;
    var vals = sheet.getRange(start, 7, count, 1).getValues();
    var bgs  = sheet.getRange(start, 1, count, 1).getBackgrounds();
    for (var r = 0; r < count && handles.length < LIMIT; r++) {
      var h = (vals[r][0] || '').toString().trim().replace(/^@/, '');
      var bg = (bgs[r][0] || '').toString().toLowerCase();
      if (h && bg !== '#d9b8ff') handles.push(h);
    }
  }

  // Salvar na aba loteN_export
  var expSheet = ss.getSheetByName('loteN_export') || ss.insertSheet('loteN_export');
  expSheet.clearContents();
  expSheet.getRange(1,1).setValue('ig_username');
  if (handles.length > 0) {
    expSheet.getRange(2, 1, handles.length, 1).setValues(handles.map(h => [h]));
  }
  Logger.log('Exportados: ' + handles.length);
}
```

Após executar, exportar a aba `loteN_export` como CSV e salvar como `leads_loteN_input.csv` nesta pasta.

> **Alternativa para exportar o CSV:** o Apps Script pode logar os handles com `Logger.log(JSON.stringify(handles))` — capturar via JavaScript no DOM do editor quando o export direto falha por autenticação.

---

## Passo 2 — Scrape dos perfis

```bash
python lead_scoring.py leads_loteN_input.csv \
  --out leads_loteN_scored.csv \
  --username-col ig_username \
  --delay 2
```

### Como funciona (2 créditos por lead)

1. **Step 1** — `GET /v1/instagram/search?query={handle}` → retorna `userId`
2. **Step 2** — `GET /v1/instagram/basic-profile?userId={id}` → retorna bio, followers, is_business

Funciona para perfis **públicos e privados**.

### Custo de créditos por lote

| Situação | Créditos |
|---|---|
| Sucesso completo | 2 por lead |
| Erro no step 1 (perfil inexistente, timeout na busca) | 1 por lead |
| Erro no step 2 (timeout no basic-profile) | 2 por lead |

Lote de 400 leads ≈ **~790 créditos**.

### Tratamento de erros

O script captura `requests.exceptions.Timeout` e `requests.exceptions.RequestException` em ambos os steps — timeouts são registrados como `error_reason` no CSV em vez de crashar o run.

---

## Passo 3 — Upload para Supabase (UPSERT)

```bash
python upload_loteN_supabase.py
```

### CRÍTICO: usar UPSERT (POST), não PATCH

- **PATCH** com `?id=eq.{handle}` retorna 204 mesmo se a linha não existe → silencioso, não insere nada
- **POST** com `Prefer: resolution=merge-duplicates` faz INSERT ou UPDATE conforme o `id` já exista

### Campos obrigatórios no INSERT (estrutura da tabela `leads`)

```json
{
  "id": "ig_username",
  "u": "ig_username",
  "instagram_link": "https://instagram.com/ig_username",
  "bio": "...",
  "followers": 0,
  "business": false,
  "kw": [],
  "tags": [],
  "followups": [],
  "error": false,
  "error_reason": "",
  "status": "novo",
  "in_pipeline": false,
  "batch": "lote-N",
  "phone": ""
}
```

> **`kw` é array no Postgres** — nunca passar como string. Converter com `.split(",")` antes de enviar.

### Headers corretos

```python
headers = {
    "apikey": SECRET_KEY,
    "Authorization": f"Bearer {SECRET_KEY}",
    "Content-Type": "application/json",
    "Prefer": "resolution=merge-duplicates,return=minimal",
}
```

### Verificar se o upload funcionou

```python
r = requests.get(
    f"{SUPABASE_URL}/rest/v1/leads",
    params={"id": "eq.{handle}", "select": "id,bio,followers"},
    headers={"apikey": SECRET_KEY, "Authorization": f"Bearer {SECRET_KEY}"},
)
# Se retornar [] → lead não existe (PATCH falhou silenciosamente)
# Se retornar [{...}] → lead inserido com sucesso
```

---

## Passo 4 — Pintar linhas na planilha

No Apps Script, usar a função de pintura para marcar as linhas do lote como processadas (`#D9B8FF`).

```javascript
function pintarLoteN() {
  var SHEET_ID = "1qQSFlaZai7dWUEn8QAk0mM8GO1EpLVmNiu-2GE-g45s";
  var LOTE_IDS = ["handle1", "handle2", ...];  // lista do CSV de input

  var processedSet = {};
  LOTE_IDS.forEach(function(id) { processedSet[id.toLowerCase()] = true; });

  var ss = SpreadsheetApp.openById(SHEET_ID);  // openById — nunca getActiveSpreadsheet()
  var sheet = ss.getSheetByName('Cópia de leads_v6');
  var lastRow = sheet.getLastRow();
  var BATCH = 1000;
  var painted = 0;

  for (var start = 2; start <= lastRow; start += BATCH) {
    var end = Math.min(start + BATCH - 1, lastRow);
    var count = end - start + 1;
    var vals = sheet.getRange(start, 7, count, 1).getValues();
    var bgs  = sheet.getRange(start, 1, count, 1).getBackgrounds();

    for (var r = 0; r < count; r++) {
      var handle = (vals[r][0] || '').toString().trim().replace(/^@/, '').toLowerCase();
      var bg = (bgs[r][0] || '').toString().toLowerCase();
      if (handle && processedSet[handle] && bg !== '#d9b8ff') {
        sheet.getRange(start + r, 1, 1, 20).setBackground('#D9B8FF');
        painted++;
      }
    }
  }
  Logger.log('Pintado: ' + painted + ' linhas');
}
```

### Como executar no Apps Script via Claude in Chrome

1. Injetar o código no Monaco editor via `javascript_tool` na aba do Apps Script
2. Salvar com o botão "Salvar projeto no Drive" (jsname `UFPec`)
3. Abrir o dropdown de funções (role=`listbox`) e selecionar a função
4. Clicar em "Executar a função selecionada" (jsname `XvjrTb`)
5. Aguardar "Execução concluída" no log (pode levar 2–4 min para 20k linhas)

---

## Contagem de leads restantes

```javascript
function contarLeadsNaoProcessados() {
  var SHEET_ID = "1qQSFlaZai7dWUEn8QAk0mM8GO1EpLVmNiu-2GE-g45s";
  var ss = SpreadsheetApp.openById(SHEET_ID);
  var sheet = ss.getSheetByName('Cópia de leads_v6');
  var lastRow = sheet.getLastRow();
  var BATCH = 1000;
  var totalComIG = 0, jaProcessados = 0;

  for (var start = 2; start <= lastRow; start += BATCH) {
    var end = Math.min(start + BATCH - 1, lastRow);
    var count = end - start + 1;
    var vals = sheet.getRange(start, 7, count, 1).getValues();
    var bgs  = sheet.getRange(start, 1, count, 1).getBackgrounds();
    for (var r = 0; r < count; r++) {
      if ((vals[r][0] || '').toString().trim()) {
        totalComIG++;
        if ((bgs[r][0] || '').toString().toLowerCase() === '#d9b8ff') jaProcessados++;
      }
    }
  }
  Logger.log('Total com IG: ' + totalComIG + ' | Já processados: ' + jaProcessados + ' | Faltam: ' + (totalComIG - jaProcessados));
}
```

---

## Erros conhecidos e soluções

| Erro | Causa | Solução |
|---|---|---|
| `TypeError: Cannot read properties of null (reading 'getSheetByName')` | `getActiveSpreadsheet()` em script standalone | Usar `openById(SHEET_ID)` |
| PATCH retorna 204 mas lead não aparece no dashboard | PATCH não insere linhas novas | Usar POST com `Prefer: resolution=merge-duplicates` |
| `malformed array literal: "advogada"` | Coluna `kw` é array no Postgres, string enviada | Converter para lista Python antes do JSON |
| `Could not find the 'lote' column` | Coluna não existe na tabela | Usar `batch` (nome correto na tabela) |
| `23502 NOT NULL violation` | Campos obrigatórios ausentes no INSERT | Incluir: `id, u, instagram_link, status, in_pipeline, tags, followups, phone` |
| Script crashou no meio do scrape | `requests.exceptions.ReadTimeout` não capturado | Envolver `requests.get()` em try/except Timeout |
| Função não aparece no dropdown do Apps Script | Editor ainda carregando | Salvar com botão UFPec e aguardar listbox atualizar |
| Dashboard mostra menos leads que o esperado (ex: 241 de 400) | Supabase REST API tem **limite padrão de 1000 rows** — sem `limit` explícito retorna só as primeiras 1000 linhas alfabéticas | `boot()` do `index.html` já pagina em loop com `.range(from, from+999)` — não remover essa lógica em atualizações futuras |

---

## Estado atual dos lotes

| Lote | Leads | Status |
|---|---|---|
| lote-1 a lote-5 | 746 | ✅ Scraped + Supabase + planilha pintada |
| lote-6 | 400 | ✅ Scraped + Supabase + planilha pintada |
| lote-7 | 400 | ✅ Scraped + Supabase + planilha pintada |
| **Total processado** | **1.546** | |
| Faltam na planilha | ~12.244 | (de ~13.790 com IG) |
