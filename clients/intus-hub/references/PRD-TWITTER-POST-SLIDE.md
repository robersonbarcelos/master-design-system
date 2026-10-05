# PRD: Geração de Slides — Twitter Post Template

> **Ler integralmente antes de gerar qualquer slide neste template.**
> CLI canônico: `clients/intus-hub/tools/gen_twitter_slide.py`
> Saída: 1080×1350px · 4:5 portrait

---

## PRÉ — Antes do primeiro slide em qualquer sessão

**Avatar pode estar ausente em worktrees.** Verificar antes de rodar:

```powershell
# Verificar se existe
Test-Path "clients\intus-hub\assets\avatar-diego.jpeg"

# Se não existir, copiar do repo principal
cp "C:\Users\Pichau\Downloads\intus-newsletter\SKILLS\Master-social-design-system\clients\intus-hub\assets\avatar-diego.jpeg" `
   ".\clients\intus-hub\assets\avatar-diego.jpeg"
```

---

## 01 — O Comando (PowerShell obrigatório)

**Nunca usar Bash (Git Bash).** Bash no Windows corrompe acentos PT-BR. Sempre PowerShell.

```powershell
python clients/intus-hub/tools/gen_twitter_slide.py `
  --slide-num 2 `
  --hook "Primeira linha do slide." `
  --body "Linha 1`nLinha 2`nLinha 3" `
  --scene "C:\ARQUIVOS\...\002.png"
```

Em PowerShell, quebras de linha no `--body` usam **backtick-n** (`` `n ``), nunca `\n`.

| Flag | Obrigatória | Descrição |
|---|---|---|
| `--slide-num` | Sim | Número do slide (usado no nome do arquivo) |
| `--hook` | Sim | Primeira linha — 52px / 900 weight |
| `--body` | Sim | Corpo do texto com `` `n `` para quebras |
| `--scene` | Não | Caminho da imagem de cena. Omitir para slides sem imagem |
| `--skip-gen` | Não | Reutiliza raw existente — só refaz composite |
| `--bold-red` | Não | Palavra em bold vermelho #E53935 no body |

---

## 02 — Header e Avatar

O GPT gera um círculo cinza placeholder. O composite apaga esse cinza e cola o avatar circular real.

**Coordenadas canônicas (pós-resize 1080×1350):**

```
AVT_X = 66 · AVT_Y = 61 · AVT_SIZE = 120

Clearing rect:  (56, 51, 196, 211)
                 ↑         ↑
                 x2=196     y2 = 61+120+30 = 211  ← +30, nunca +10
```

**Por que +30 embaixo:** GPT gera o placeholder ligeiramente maior que 120px. Com +10, o arco inferior fica exposto. Com +30, é coberto antes de colar o avatar.

| Campo header | Valor |
|---|---|
| Nome | Diego Spanevello \| Inteligência Artificial ✓ |
| Handle | @diego.spanevello |
| Fonte nome | 26px / semibold 600 / #1A1A1A |
| Fonte handle | 22px / regular 400 / #888888 |

---

## 03 — Copy — Tipografia canônica

| Elemento | Tamanho | Peso | Cor |
|---|---|---|---|
| Hook line (1ª linha) | 52px | 900 (black) | #1A1A1A |
| Body (demais linhas) | 28px | 400 (regular) | #1A1A1A |
| Bold inline no body | 28px | 700 | #1A1A1A |

**Regras absolutas:**
- Cor única no body: `#1A1A1A`. Exceção: `--bold-red` aplica `#E53935`
- Sem travessão (—) em nenhuma linha
- Bold inline: marcar com `**palavra**` no texto — GPT renderiza como bold

---

## 04 — Slot de Imagem — detect_slot()

**O prompt DEVE incluir o placeholder cinza.** É necessário para detect_slot() encontrar a posição real. A imagem cobre 100% do placeholder — nada aparece ao usuário.

**Trecho obrigatório no prompt:**
```
IMAGE PLACEHOLDER SLOT (directly below the last body line, 24px gap,
44px side margins, 44px bottom margin):
  A solid uniform light gray (#E0E0E0) filled rounded rectangle,
  16:9 landscape proportions, border-radius 18px.
  The slot must start AFTER the last line of body text.
  Empty inside — no icons, no label text, no gradient.
```

**Por que não coordenada fixa y=748:** O GPT posiciona o slot após o texto. Quando o hook ocupa 2 linhas, o texto desce e y=748 fica dentro do bloco de texto → sobreposição.

**Por que não find_image_slot() antigo:** Capturava texto @handle (~200px) e retornava 825×123px errado.

**detect_slot() por largura mínima (canônico):** Filtra por linhas com ≥50% de pixels cinzas uniformes. @handle (~200px) não passa. Slot real (~992px) passa.

---

## 05 — Slide sem imagem

Quando o body tiver 4+ linhas longas (texto > ~60% da altura útil), **omitir `--scene`**.

Espaço branco abaixo do texto é correto. Nunca forçar imagem — sobrepõe o texto.

---

## 06 — Recomposição sem gastar API

Quando o problema for só no composite (avatar, cena, slot) e não no texto:

```powershell
python clients/intus-hub/tools/gen_twitter_slide.py `
  --slide-num 2 --hook "..." --body "..." --scene "..." `
  --skip-gen  # usa raw existente, economiza cota
```

---

## 07 — Modos de falha conhecidos

| Sintoma | Causa | Fix |
|---|---|---|
| Arco cinza abaixo do avatar | Clearing rect com +10 embaixo | Usar (56, 51, 196, **211**) |
| Texto sobrepõe a imagem | Coordenada fixa y=748 | Usar detect_slot() |
| Slot detectado como 825×123px | Capturou texto @handle estreito | min_width_ratio=0.5 filtra @handle |
| Avatar não encontrado | worktree sem assets/ | Copiar avatar antes do primeiro slide |
| Acentos corrompidos | Chamada via Bash | Usar PowerShell com backtick-n |
| Slot não detectado (fallback) | Placeholder cinza removido do prompt | Manter trecho do placeholder no prompt |

---

## REF — Arquivos canônicos

| Arquivo | Papel |
|---|---|
| `clients/intus-hub/tools/gen_twitter_slide.py` | CLI — pipeline completo, API key automática |
| `clients/intus-hub/references/TEMPLATE-SLIDE-TWITTER-POST.json` | Especificação de zonas e tipografia |
| `clients/intus-hub/assets/avatar-diego.jpeg` | Avatar — copiar para worktrees |
| `skills/intus-hub-twitter-slide/SKILL.md` | Skill para novas sessões |
| `memory/project_intus-hub-slide-pipeline.md` | Histórico de erros e regras |
| `SKILLS/gpt-image2-skill/.env` | API key OpenAI — carregada automaticamente |
