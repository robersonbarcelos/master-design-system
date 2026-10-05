# Skill: intus-hub-twitter-slide

Gera slides individuais do template **carrossel-twitter-post-style** para o Intus Hub (Diego Spanevello).
Pipeline completo: GPT Image → resize Pillow → avatar composite → scene composite.

> **Não é necessário perguntar a chave da OpenAI.** O `.env` já está configurado em `SKILLS/gpt-image2-skill/.env` e o CLI carrega automaticamente.

---

## CLI canônico

```
python clients/intus-hub/tools/gen_twitter_slide.py \
  --slide-num <N> \
  --hook "<hook line>" \
  --body "<linha 1\nlinha 2\nlinha 3>" \
  --scene "C:/caminho/para/NNN.png"
```

**Flags:**

| Flag | Obrigatória | Descrição |
|---|---|---|
| `--slide-num` | sim | Número do slide (ex: `2` ou `07`) — usado no nome do arquivo |
| `--hook` | sim | Primeira linha do slide (52px/900). Vai entre aspas. |
| `--body` | sim | Corpo do texto. Usar `\n` para quebras de linha. |
| `--scene` | não | Caminho absoluto da imagem de cena. Omitir para slides sem imagem. |
| `--output-dir` | não | Pasta de saída. Padrão: `clients/intus-hub/runs/YYYY-MM-DD/` |
| `--skip-gen` | não | Usa raw existente, só faz composite. Economiza API quando só o composite precisa de ajuste. |
| `--bold-red` | não | Palavra ou frase para aparecer em bold vermelho (#E53935) no body. Ex: `--bold-red AGENTE` |

**Saídas:**
- `slide<N>-raw.png` — imagem bruta do GPT (mantida para recomposição sem nova chamada de API)
- `slide<N>-FINAL.png` — slide final com avatar e cena compostos

---

## Fluxo de uso em uma nova sessão

1. **Receber o copy** do slide (hook + body) e o nome/caminho da imagem de cena
2. **Montar o comando** com os parâmetros (não gerar script separado — usar o CLI diretamente)
3. **Rodar via Bash** com `run_in_background=True` para slides independentes em paralelo
4. **Enviar o FINAL.png** para o usuário via SendUserFile quando completar

---

## Quando omitir `--scene` (slide sem imagem)

Quando o corpo do texto preenche mais de ~60% da altura útil do slide (4+ linhas longas no body), omitir `--scene`.
O espaço branco abaixo do texto é a solução correta — nunca forçar imagem.

---

## Tipografia canônica (não alterar)

| Elemento | Tamanho | Peso |
|---|---|---|
| Hook line (1ª linha) | 52px | 900 (black) |
| Body (demais linhas) | 28px | 400 (regular) |
| Bold inline no body | 28px | 700 — só peso, nunca tamanho diferente |
| Header nome | 26px | 600 (semibold) |
| Header handle | 22px | 400 |

**Cor única no body:** `#1A1A1A`. Exceção: `--bold-red` aplica `#E53935` na palavra indicada.

---

## Recomposição sem nova chamada de API

Se o problema for só no composite (avatar, cena, slot):
```
python clients/intus-hub/tools/gen_twitter_slide.py \
  --slide-num 2 \
  --hook "..." --body "..." --scene "..." \
  --skip-gen
```
Reutiliza o `slide02-raw.png` existente — não consome cota da OpenAI.

---

## Arquivos de referência

| Arquivo | O quê |
|---|---|
| `clients/intus-hub/references/TEMPLATE-SLIDE-TWITTER-POST.json` | Template completo com todas as zonas e regras |
| `clients/intus-hub/assets/avatar-diego.jpeg` | Avatar (já embutido no CLI) |
| `memory/project_intus-hub-slide-pipeline.md` | Histórico de erros resolvidos e regras canônicas |
| `.env` em `SKILLS/gpt-image2-skill/.env` | API key OpenAI (carregada automaticamente — não pedir ao usuário) |

---

## Regras fixas (nunca alterar)

- Output sempre 1080×1350px (gerado em 1088×1360, reduzido por Pillow LANCZOS)
- Avatar em posição fixa: x=66, y=61, size=120
- Retângulo de limpeza do avatar: `(56, 51, 196, 211)` — +30 embaixo (arco cinza do GPT)
- Slot detectado por `detect_slot()` — nunca coordenada fixa y
- Placeholder cinza (#E0E0E0) sempre incluído no prompt — necessário para detect_slot()
- Sem footer — @handle já está no header estilo Twitter
- Nunca travessão (—) no copy
