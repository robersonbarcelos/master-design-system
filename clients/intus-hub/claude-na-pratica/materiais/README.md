# Claude na Prática — Repositório do Curso

Minicurso do [Intus Hub](https://intushub.com.br) que ensina o **sistema completo do Claude** (Anthropic) em menos de 2 horas: do Chat básico até squads de agentes de IA. Sem enrolação, sem teoria solta — cada aula tem 1 objetivo, 1 demo prático e 1 ação para o aluno executar.

**Preço de lançamento: R$47 · Ticket pós-lançamento: R$67–R$97 · Vitalício · Hotmart/Lastlink**

---

## O que é o curso

**Claude na Prática** é a porta de entrada para o ecossistema Intus Hub. É o único minicurso no mercado que cobre os 5 modos do Claude (Chat, Cowork, Code, Skills e Squads) em 1h52 de conteúdo 100% prático, com foco em negócios digitais — infoprodutores, criadores, gestores e empreendedores.

**Funil de produto:**
- Entrada: Claude na Prática · R$47
- Upsell 1: Domínio Claude (curso completo) · R$497
- Upsell 2: Mentoria / Squad Intus Hub · R$1.800+

**Para quem é:**
- João, 32 anos — infoprodutor/creator que usa ChatGPT mas não tira o máximo do Claude
- Ana, 28 anos — gestora/empreendedora que quer automatizar sem depender de tutoriais fragmentados

**Posicionamento:** *"1h30 para aprender o sistema completo do Claude — do Chat ao squad de agentes. Sem enrolação: você sai do curso com projetos funcionando."*

---

## Estrutura do repositório

```
curso-claude-na-pratica/
├── aulas/          → Conteúdo base de cada aula em Markdown
├── materiais/      → HTMLs interativos entregues ao aluno + portal de navegação
├── roteiros/       → Roteiros de gravação (texto + versão visual)
├── referencias/    → Documentos internos de orientação da produção
├── prd-claude-na-pratica.html  → PRD completo do produto
└── README.md
```

---

## Para que serve cada pasta

### `aulas/`
Conteúdo estruturado de cada aula em Markdown, organizado por módulo. É o documento-base que define o que é ensinado: objetivos, pontos principais, prompts de exemplo e entregáveis. Uma subpasta por módulo, um `.md` por aula.

### `materiais/`
Os HTMLs interativos entregues ao aluno após cada aula. Cada arquivo contém o roteiro resumido, prompts prontos para copiar, exemplos práticos e recursos complementares — tudo offline, sem servidor necessário.

A subpasta `materiais-alunos/index.html` é o **portal do aluno**: interface completa com menu lateral por módulo, atalhos no topo (M0–M5), botão de início, navegação anterior/próxima e barra de progresso.

### `roteiros/`
Roteiros completos para gravação de cada aula em dois formatos:
- `.md` — texto puro para edição e revisão
- `.html` — versão visual formatada para usar como teleprompter durante a gravação

### `referencias/`
Documentos internos de orientação da produção:

| Arquivo | Para que serve |
|---------|---------------|
| `analise-competitiva.md` | Mapeamento de cursos concorrentes, preços e diferencial do Claude na Prática |
| `brand-guide-curso.md` | Paleta de cores, tipografia, tom de voz e identidade visual do curso |
| `cursos-oficiais-anthropic.md` | Levantamento do conteúdo educacional oficial da Anthropic (evitar repetição, identificar gaps) |
| `regras-materiais-html.md` | Checklist e padrões obrigatórios para produção e manutenção dos HTMLs |

### `prd-claude-na-pratica.html`
PRD (Product Requirements Document) completo. Define estrutura de módulos, posicionamento, personas, preço, benchmark de concorrentes e funil de upsell. É o documento de referência principal para qualquer decisão de produto — abrir no navegador.

---

## Módulos e aulas (1h 52min total)

| Módulo | Tempo | Aulas | Conteúdo |
|--------|-------|-------|----------|
| M0 · Boas-vindas | 5 min | 1 | Como aproveitar o curso ao máximo |
| M1 · Bases do Claude | 18 min | 3 | Claude vs. ChatGPT · Os 3 modos · Setup inicial e Projetos |
| M2 · Claude Chat | 20 min | 3 | Artifacts · Projetos com memória · Conectores (Calendar, Gmail, Airtable) |
| M3 · Claude Cowork | 20 min | 3 | Missões completas · Plugins oficiais · Criação de arquivos reais (Excel, Word, PDF) |
| M4 · Claude Code | 22 min | 3 | Desktop App · Landing page sem código · Skills e pack exclusivo |
| M5 · Agentes de IA | 27 min | 4 | O que são agentes · Demo squad pesquisador+escritor · MCPs · Recap e upsell |

**Regra de ouro:** cada aula tem 1 objetivo único, 1 demo ou exercício prático, e termina com 1 ação clara. Câmera na tela, mão na massa.

---

## Como usar o portal do aluno

Abra `materiais/materiais-alunos/index.html` em qualquer navegador. Funciona 100% offline:

- Menu lateral com todos os módulos e aulas
- Atalhos no topo para cada módulo (M0–M5)
- Logo ou ícone de casa para voltar ao início
- Botões anterior/próxima para seguir a sequência
- Barra de progresso com aulas visitadas

Cada HTML de aula também funciona de forma independente — útil para compartilhar uma aula específica.

---

*Intus Hub © 2025 — Todos os direitos reservados.*
