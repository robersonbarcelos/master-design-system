# Master Social Design System — Regras Globais

> Este arquivo é lido automaticamente ao abrir qualquer pasta deste projeto.
> Estas regras se aplicam a TODOS os clientes e sessões de produção.

---

## REGRA CRÍTICA — JSON de Imagem (obrigatório)

**Sempre que o usuário enviar uma imagem de referência com intenção de gerar um prompt ou JSON para IA generativa (Freepik, Midjourney, ChatGPT Image, etc.), OBRIGATORIAMENTE:**

1. **Perguntar antes de gerar:**
   > "Quer que eu use a skill `json-prompt-generator` para analisar esta referência? Ela gera um JSON estruturado com campos `scene`, `style`, `technical`, `materials`, `composition` e `quality` — schema completo e pronto para usar."

2. **Se o usuário confirmar** (ou já tiver pedido explicitamente):
   - Acionar a skill `json-prompt-generator` localizada em `skills/design/json-prompt-generator/`
   - Seguir o workflow da skill: Analysis → JSON Prompt → Tweaks
   - Nunca usar o schema simplificado `{ "prompt": "...", "negative_prompt": "...", "aspect_ratio": "..." }`

3. **Nunca gerar JSON de imagem sem passar pela skill** quando há imagem de referência presente.

### Quando esta regra se aplica
- Usuário envia imagem + pede "recriar", "replicar", "fazer igual", "prompt disto", "JSON disto"
- Usuário envia imagem + pede variações com paleta do cliente
- Usuário envia imagem + pede "3 ideias" que resultarão em JSONs

### Exceção
- Se o usuário disser explicitamente "não precisa usar a skill" ou "usa o formato simples" → pode usar o schema básico

---

## REGRA CANÔNICA — Widget HTML vs JSON completo

**Widget HTML é APENAS para:**
- Teste de seleção de fontes (font-test-sheet, especificações de fonte lado a lado)
- Teste de variação em sites e landing pages

**Para capa/imagem DEFINITIVA (carrossel, post, thumbnail, qualquer peça final de imagem), NUNCA montar widget HTML.**
Sempre gerar o **JSON completo por variação**, usando o template base de zonas definido para o cliente (`header`/`image`/`content`/`footer`), com:
- Título/nome da variação especificando a combinação de fonte usada
- `zones.image.asset_prompt` com a análise de imagem via `json-prompt-generator` (quando houver referência) integrada dentro do próprio schema de zonas — nunca como JSON solto separado
- `negative_rules` reforçando as regras fixas do cliente (ex: sem travessão, sem avatar, posição da headline, overlay correto por variação, etc.)

Essa regra vale para todos os clientes deste sistema, não só para peças de teste de fonte.

### Sempre colar os JSONs completos no chat

Além de salvar em `runs/[data]/`, sempre colar o conteúdo completo de cada JSON gerado diretamente na resposta do chat — nunca apenas referenciar o caminho do arquivo.

---

## REGRA CRÍTICA — Gate de Skill de Criação (obrigatório para todos os clientes e todos os formatos)

**Sempre que o pedido envolver produzir qualquer peça de copy — carrossel, artigo/long-form, post, thread, legenda, hook ou roteiro de vídeo — em qualquer cliente, é OBRIGATÓRIO acionar a skill de criação correspondente (`carousel-writer-sms`, `article-writer-sms`, `post-writer-sms`, `thread-writer-sms`, `caption-writer-sms`, `hook-writer-sms`, `video-script-sms`) — nunca escrever ângulos, slides, parágrafos, hooks ou falas manualmente "por fora" dela.**

### Tabela de mapeamento formato → skill obrigatória

| Formato pedido | Skill obrigatória |
|---|---|
| Carrossel (qualquer plataforma) | `carousel-writer-sms` |
| Artigo / long-form / X Article / newsletter | `article-writer-sms` |
| Post único / post longo | `post-writer-sms` |
| Thread multi-post | `thread-writer-sms` |
| Legenda visual (caption) | `caption-writer-sms` |
| Hook / linha de abertura | `hook-writer-sms` |
| Roteiro de vídeo / script / reel | `video-script-sms` |
| Repurpose de conteúdo existente | `content-repurposer-sms` |

### Por que essa regra existe
Em 2026-07-21, um carrossel do Intus Hub foi produzido escrevendo ângulos manualmente (arquivo `angulos-[tema].md`) sem passar pela skill. Isso pulou a ETAPA 0 (oferta do `narrative-framework-sms` — os 5 frameworks: Value-Stack, Problem-Proof, Hack List, Rant Callout, Demo Walkthrough), a FASE 0.5 (pesquisa de contexto estruturada) e todos os demais gates da skill. A convenção de nomenclatura de artefatos (`angulos-[tema].md`, `carrossel-[tema].md` etc, definida no `CLAUDE.md` de cada cliente) descreve **onde salvar o resultado**, não substitui o processo da skill. O mesmo risco existe para qualquer outro formato de copy — não é exclusivo de carrossel — por isso a regra foi generalizada.

### O que fazer sempre que o pedido for de copy em qualquer formato
1. Acionar a skill de criação correspondente (ferramenta Skill) — não produzir texto livre "por fora"
2. A skill decide sozinha, em seu próprio gate inicial, se oferece o `narrative-framework-sms` antes da fase de execução
3. Seguir todos os gates da skill em sequência, sem pular etapa
4. Toda skill de criação deve executar o `copy-qa-sms` (Voice Gate + AI Pattern Gate + padrões estruturais) antes de entregar o copy final — se a skill acionada não tiver esse gate, é falha da skill, não uma etapa opcional
5. Salvar os artefatos finais em `clients/[cliente]/runs/[data]/` seguindo a convenção de nomes do `CLAUDE.md` daquele cliente — isso continua valendo, é só o *empacotamento final*, não substitui o processo

### Onde essa regra vale
Este arquivo (`CLAUDE.md` raiz) é lido automaticamente ao abrir qualquer pasta do sistema — a regra acima já se aplica a **todos os clientes** (Intus Hub, Carol, Aurum Lingerie, Mercurius, Michele Fara, Motofácil, NovaDAX, White Label, etc.) e a **todos os formatos de copy**, sem precisar duplicar em cada `CLAUDE.md` individual. Não é necessário (nem recomendado) recriar esta regra nos arquivos de cliente — isso criaria risco de divergência se as skills forem atualizadas.

### Exceção
- Se o usuário disser explicitamente "não quer passar pela skill, quer só um rascunho rápido" → pode prosseguir em modo manual, mas sinalizar: `[⚠️ COPY SEM GATE DA SKILL — não passou por narrative-framework-sms nem pelos QA Gates de copy-qa-sms]`

---

## Estrutura do Projeto

```
Master-social-design-system/
├── clients/          — Um subdiretório por cliente, cada um com CLAUDE.md próprio
├── skills/           — Skills compartilhadas entre todos os clientes
│   └── design/
│       └── json-prompt-generator/   ← USAR PARA TODO JSON DE IMAGEM COM REFERÊNCIA
```

---

## REGRA CANÔNICA — Repositório é a fonte única de skills (proibido stub com caminho absoluto)

**O repositório `master-design-system` é a fonte canônica de todo `SKILL.md`. A pasta global do usuário (`~/.claude/skills/` ou `C:\Users\<usuario>\.claude\skills\`) é apenas um destino de instalação local — nunca o inverso.**

### O que NUNCA fazer
- Nunca substituir o conteúdo real de um `SKILL.md` dentro de `skills/` por um stub "movido para" que aponte para um caminho absoluto de máquina (`C:\Users\User\...`, `C:\Users\Pichau\...`, `/home/usuario/...` etc.)
- Nunca tratar a pasta global do Claude Code como "fonte única" de uma skill — ela é local a uma máquina e a um usuário do sistema operacional, e não é versionada nem portável

### Por que essa regra existe
Em 2026-07-14, uma consolidação anterior moveu o conteúdo de 22 skills para `C:\Users\User\.claude\skills\` e deixou, no lugar delas dentro do repositório, apenas um stub apontando para esse caminho absoluto. Isso funcionava nessa máquina, mas ao instalar o repositório em outro computador (`C:\Users\Pichau\`), o caminho não existia — a skill ficava vazia e inutilizável. Isso foi corrigido em 2026-07-27: o conteúdo real de todas as skills afetadas foi restaurado dentro de `skills/` a partir da pasta global desta máquina, e o repositório passou a ser a única fonte de verdade.

### O que fazer sempre
1. Editar o comportamento de uma skill **direto no arquivo dentro do repositório** (`skills/.../SKILL.md`)
2. Se for necessário instalar/sincronizar localmente em `~/.claude/skills/`, isso é uma cópia de instalação — pode ser feita por script de setup, nunca por edição manual divergente
3. Antes de qualquer commit, verificar se nenhum `SKILL.md` dentro de `skills/` foi substituído por um stub ou contém referência a caminho absoluto de máquina (`grep -r "C:\\\\Users\\\\" skills/` deve retornar vazio)
4. Se encontrar um stub desses, restaurar o conteúdo real antes de prosseguir — nunca commitar/push um stub

---

## REGRA — Gate de Referência de Fontes e Paletas

> Catálogo de fontes: `reference/fonts/fonts-index.md`
> Catálogo de paletas: `reference/colors/paletas-index.md` + `reference/colors/palettes-visual/`

### Quando consultar e oferecer opções do catálogo (gate ATIVO)

| Momento | O que fazer |
|---------|-------------|
| **Onboarding de novo cliente** | Consultar catálogo de paletas e fontes — sugerir combinações compatíveis com o posicionamento antes de preencher `brand-spec.md` e `visual-system.md` |
| **Criação ou revisão de brand guide** | Abrir `fonts-index.md` e `paletas-index.md` — apresentar opções organizadas por categoria e mood antes de definir tipografia e paleta do cliente |
| **Elaboração de sistema de criativos** (estrutura como `visual-system.md`, `paletas-variacao.md`, `fontes-variacao.md`) | Consultar catálogo e propor combinações — o output final entra nos arquivos do cliente |
| **Criação de novo template de carrossel ou estático** | Verificar se as fontes e paletas do template estão no catálogo — se não estiverem, sugerir equivalentes antes de montar o template |

### Quando NÃO acionar (gate SILENCIOSO)

| Situação | Por quê |
|----------|---------|
| **Execução em template já definido** (ex: carrossel com estrutura de zonas já aprovada) | Fonte e paleta já estão definidas no template — não interromper o fluxo |
| **Geração de copy** (carousel-writer-sms, post-writer-sms, etc.) | Escopo tipográfico já está no `visual-system.md` do cliente |
| **Atualização de runs existentes** | Identidade já está travada — sem reabrir definições |
| **Pedido explícito sem curadoria** | Se o usuário trouxer fonte/paleta específica e pedir para usar diretamente, aplicar sem gate |

### Como apresentar as opções quando o gate está ativo

1. Ler `fonts-index.md` e `paletas-index.md`
2. Filtrar por categoria/mood compatível com o posicionamento do cliente
3. Apresentar no máximo **3 combinações font + paleta** com justificativa de 1 linha cada
4. Aguardar aprovação antes de registrar em `visual-system.md` ou `fontes-variacao.md` do cliente

---

## Regras Gerais de Produção

- Ao iniciar sessão em qualquer pasta de cliente, ler o CLAUDE.md daquele cliente primeiro
- Nunca misturar paleta, copy ou identidade visual entre clientes diferentes
- Sempre confirmar qual cliente está ativo antes de produzir qualquer conteúdo
