# Referência — Cursos Oficiais Anthropic Academy
**Fonte:** anthropic.skilljar.com · Capturado em Julho 2026
**Uso:** Base técnica para elaboração dos .md e roteiros das aulas do curso "Claude na Prática"

---

## 1. Claude 101
**URL:** anthropic.skilljar.com/claude-101
**Formato:** 12 aulas · 1h · Gratuito · claude.ai (usuário final)
**Público:** Quem quer usar Claude no dia a dia — sem código

### Currículo
**Seção: Meet Claude**
- What is Claude?
- Your first conversation with Claude
- Getting better results
- Claude desktop app: Chat, Cowork, Code

**Seção: Organizing your work and knowledge**
- Introduction to projects
- Creating with artifacts
- Working with skills

**Seção: Expanding Claude's reach**
- Connecting your tools
- Enterprise search
- Research mode for deep dives

**Seção: Putting it all together**
- Claude in action: use-cases by role
- Other ways to work with Claude

### Insights relevantes para nosso curso
- "Creating with artifacts" — tema que NÃO temos no nosso currículo. Artifacts são os outputs visuais/interativos gerados pelo Claude (HTML, SVG, código, tabelas). Vale mencionar em M2.
- "Research mode for deep dives" — função de pesquisa profunda do Claude. Pode ser citado em M2 aula 2.1 ou M3.
- A progressão Chat → Desktop App → Skills segue a mesma lógica do nosso curso.

---

## 2. Introduction to Claude Cowork
**URL:** anthropic.skilljar.com/introduction-to-claude-cowork
**Formato:** ~10 aulas · 0.5h vídeo · Gratuito
**Público:** Knowledge workers que movem informação entre arquivos, apps e ferramentas

### Objetivos de aprendizado (literais do curso oficial)
- Set up Claude Cowork with a working folder, connectors, and the right permissions
- Run your first end-to-end task — clarify, steer mid-run, and review the deliverable
- Give Claude standing context with global instructions, projects, skills, and plugins
- Set up scheduled tasks and Dispatch for recurring work
- Bring Claude into the browser with Claude in Chrome
- Work inside Word, Excel, PowerPoint, and Outlook with the Microsoft 365 integration
- Test the skills you build and share plugins with your team safely

### Currículo por seção
**Seção 1: Meet Claude Cowork (4 aulas)**
- O que é Cowork e como difere do Chat
- Setup: pasta de trabalho, conectores, permissões
- Primeira tarefa end-to-end: descrever, clarificar, ajustar no meio, revisar entrega
- Conectores: quais ferramentas o Cowork pode acessar por tarefa

**Seção 2: Make Claude Cowork yours (4 aulas)**
- Global instructions e Projetos para contexto permanente
- Construir Skills e instalar Plugins
- Anatomia de uma Skill: pasta com SKILL.md + referências + assets
- Dois formatos de Plugin: toolkit de função vs pipeline end-to-end

**Seção 3: Use Claude wherever you work (2 aulas)**
- Claude in Chrome: Claude lê dashboards e páginas durante uma tarefa Cowork
- Microsoft 365: Word, Excel, PowerPoint, Outlook

**Seção 4: Sharing and safety in Claude Cowork (4 aulas)**
- Revisar planos e outputs antes de executar
- Validar skills antes de depender delas
- Compartilhar plugins com o time com segurança
- Caminhos de distribuição de plugins por tipo de organização

### Insights relevantes
- "Steer mid-run" — é possível intervir durante uma tarefa Cowork sem cancelar. Tópico importante para M3.
- Dispatch = Cowork pelo celular via Telegram. Citado como feature para tarefas recorrentes.
- Scheduled tasks = agendamento de tarefas automáticas no Cowork. Bom teaser para M3 ou M5.
- Anatomia do prompt Cowork: "fontes de entrada + entregável real no final" — exatamente o que ensinamos em M3 aula 3.1.
- Plugin ≠ Skill: plugin pode ser um "toolkit de função" (conjunto de skills) OU um "pipeline end-to-end" (fluxo completo). Confirma nossa distinção Skill vs Plugin em M4 aula 4.3.

---

## 3. Introduction to Subagents
**URL:** anthropic.skilljar.com/introduction-to-subagents
**Formato:** 4 aulas · 20 min · Gratuito · Claude Code
**Público:** Usuários de Claude Code que querem sessões mais longas e paralelas

### O que são subagentes (descrição oficial)
"Sub-agents are one of the most practical ways to get more out of longer Claude Code sessions. They let Claude spin up a separate context window, hand it a focused task, and get back a clean summary."

### Currículo
- What are subagents?
- Creating a subagent (comando `/agents`)
- Designing effective subagents
- Using subagents effectively

### O que o curso ensina (detalhe oficial)
- **Como funcionam:** Claude Code abre uma janela de contexto separada, recebe inputs e retorna resumo
- **Criando subagentes customizados:** comando `/agents` para criar agentes como code-reviewers, documentadores, etc.
- **Design eficaz:** formatos de output estruturado, obstacle reporting, checkpoints
- **Quando usar (e quando NÃO usar):** padrões anti-produtivos a evitar

### Insights relevantes
- O comando `/agents` cria subagentes customizados. Mencionar em M5 aula 5.1.
- "Separate context window" é a analogia certa: cada agente tem seu próprio "cérebro limpo" para uma tarefa específica.
- Anti-padrões existem — não é sempre melhor usar subagentes. Honestidade pedagógica.
- Output estruturado + checkpoint são padrões profissionais que diferenciam uso iniciante de uso avançado (bom teaser para Domínio Claude).

---

## 4. Introduction to Agent Skills
**URL:** anthropic.skilljar.com/introduction-to-agent-skills
**Formato:** 6 aulas · 30 min · Gratuito · Claude Code
**Público:** Quem quer parar de repetir instruções e ensinar o Claude uma vez só

### Descrição oficial
"Learn how to stop repeating yourself and start teaching Claude once. You'll define reusable markdown instructions that travel with your project, configure multi-file skills, and share them with your team by committing them to a git repository — so every collaborator gets the same, consistent Claude behavior."

### Currículo
- What are skills?
- Creating your first skill
- Configuration and multi-file skills
- Skills vs. other Claude Code features
- Sharing skills
- Troubleshooting skills

### Insights relevantes
- Definição oficial: Skills = "reusable markdown instructions that travel with your project" — usar essa frase em M4 aula 4.3.
- Skills multi-arquivo: uma skill pode ter SKILL.md + arquivos de referência + assets adicionais.
- Skills são compartilhadas via **git repository** — cada colaborador recebe o mesmo comportamento.
- "Skills vs. other Claude Code features" — o próprio curso oficial separa Skills de outras features. Valida nossa abordagem de ensinar a diferença Skill vs Plugin.
- Troubleshooting é parte do curso oficial — skills podem dar errado, é esperado.

---

## 5. Claude Code 101
**URL:** anthropic.skilljar.com/claude-code-101
**Formato:** 12 aulas · 1.5h vídeo · Gratuito · Claude Code
**Público:** Developers novos e experientes que querem workflows com IA

### Currículo por seção
**Seção 1: What is Claude Code? (2 aulas)**
- O que está acontecendo quando o Claude Code roda
- Loop agêntico: gather context → take action → verify results

**Seção 2: Your first prompt (2 aulas)**
- Instalar e rodar no terminal, VS Code, JetBrains, Claude in Chrome

**Seção 3: Daily workflows (3 aulas)**
- Ritmo: **Explore → Plan → Code → Commit**
- Comandos: `/compact`, `/clear`, `/context`
- Spawning de subagente code-reviewer

**Seção 4: Customizing Claude Code (5 aulas)**
- CLAUDE.md: arquivo de memória do projeto
- Conectar Claude Code a MCP server (ex: Linear)
- Configurar hooks em `.claude/settings.json`

### Insights relevantes — IMPORTANTES para nosso curso
- **Loop agêntico oficial:** gather context → take action → verify results. Usar como base de explicação em M4 aula 4.1.
- **CLAUDE.md** = arquivo de memória/instruções do projeto para o Claude Code. Análogo ao "Projeto com instruções" do Chat, mas para o Code. Mencionar em M4 aula 4.1.
- **Ritmo Explore → Plan → Code → Commit** — fluxo de trabalho profissional. Bom para mencionar como "próximo nível" na aula 4.1 ou no upsell de M5.4.
- `/compact` = compacta o contexto quando está cheio. `/clear` = limpa e recomeça. Atalhos táticos importantes.
- **Claude in Chrome** é ensinado também neste curso (não só no Cowork) — confirma que é feature cross-produto.
- Hooks (`.claude/settings.json`) = configurações avançadas. Bom teaser para Domínio Claude.

---

## 6. Introduction to Model Context Protocol
**URL:** anthropic.skilljar.com/introduction-to-model-context-protocol
**Formato:** 16 aulas · 1h · Gratuito · MCP
**Público:** ENGENHEIROS — requer Python, async/await, APIs

### O que é (definição oficial)
"MCP é um protocolo para conectar Claude a serviços externos e fontes de dados sem escrever toneladas de boilerplate."

### Currículo
**Seção 1: MCP fundamentals & server development (8 aulas)**
- Arquitetura MCP: diagrama cliente-servidor
- Python SDK para definir tools num servidor MCP
- MCP Inspector para testar servidores

**Seção 2: MCP client implementation & advanced features (8 aulas)**
- Implementar cliente MCP com session management
- Resources e prompts
- Fluxo completo de aplicação com integração MCP

### Como usar no nosso curso (M5 aula 5.3)
- Definição para leigos: "MCP é como um adaptador universal — conecta o Claude a qualquer ferramenta ou banco de dados externo sem você precisar programar a integração do zero."
- Exemplos não-técnicos: Claude conectado ao Notion via MCP, ao Airtable, ao Perplexity para busca em tempo real.
- **NÃO ensinar** setup técnico (Python SDK) — isso é Domínio Claude ou curso avançado.
- Mencionar MCP Inspector como "painel de controle" para quem quiser aprofundar.
- Diferença prática para o aluno: **Conector** (Google Calendar, Gmail) → nativo no Claude.ai. **MCP** → extensão técnica para o Claude Code. Essa distinção é o que M5 aula 5.3 deve deixar clara.

---

## Gaps identificados nos cursos oficiais vs nosso currículo

| Tópico oficial Anthropic | Está no nosso curso? | Ação |
|---|---|---|
| Artifacts (outputs visuais) | ❌ Não | Mencionar rapidamente em M2 aula 2.1 |
| CLAUDE.md (memória do projeto Code) | ❌ Não | Incluir em M4 aula 4.1 |
| Loop agêntico gather→act→verify | ❌ Não | Base de explicação M4 aula 4.1 |
| Explore→Plan→Code→Commit | ❌ Não | Teaser em M4 ou M5.4 |
| /compact /clear /context | ❌ Não | Mencionar como atalhos táticos M4 |
| Dispatch (Cowork pelo celular) | ⚠️ Só como teaser M5.4 | Manter como teaser |
| Scheduled tasks | ❌ Não | Mencionar em M3 ou M5.4 |
| Steer mid-run (intervir no Cowork) | ❌ Não | Incluir em M3 aula 3.1 |
| Anatomia prompt Cowork (fontes+entregável) | ✅ M3 aula 3.1 | Já coberto |
| Plugin = toolkit OU pipeline | ⚠️ Vago em M3 | Clarificar em M3 aula 3.2 |

---

## Definições oficiais para usar nos roteiros

> **Claude Cowork:** "Claude working directly with your files, folders, and apps — reading, editing, and producing real deliverables."

> **Skills:** "Reusable markdown instructions that travel with your project — teach Claude once, use everywhere."

> **Subagents:** "Claude Code spins up a separate context window, hands it a focused task, and gets back a clean summary."

> **MCP:** "A protocol for connecting Claude to external services and data sources without writing tons of boilerplate."

> **Loop agêntico:** "Gather context → take action → verify results."
