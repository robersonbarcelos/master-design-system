# Skill: proposta-social-media

> Processo canônico para gerar proposta de social media para novo cliente.
> Aprovado em 23/07/2026 com o onboarding da Servitec Comercial e Locações.

---

## QUANDO USAR

Sempre que o usuário iniciar onboarding de novo cliente de social media.

---

## FLUXO CANÔNICO

### Fase 1 — Diagnóstico
1. Acessar Instagram, site e materiais do cliente (Claude in Chrome se necessário)
2. Documentar em `_checklist-onboarding.md` os 6 blocos
3. Registrar alertas imediatos (dados inconsistentes, links errados, erros de perfil)

### Fase 2 — Arquivos do cliente
Criar a pasta `clients/[nome-cliente]/` com a estrutura padrão:

```
clients/[cliente]/
├── CLAUDE.md                     — ativação automática
├── .agents/
│   └── social-media-context-sms.md  — personas, pilares, plataformas
├── brand-spec.md                 — paleta, tipografia, identidade
├── DESIGN.md                     — tokens CSS, grupos visuais, layouts
├── production-rules.md           — gatilho pré-copy, proibições, exemplos
├── content-system.md             — editorias, grade, copies, CTAs, hashtags
├── visual-system.md              — grupos visuais, JSON de prompt, negative prompts
├── _checklist-onboarding.md      — status dos 6 blocos
└── references/
    ├── copies-aprovadas.md
    ├── dados-ancora.md
    └── temas.md
```

### Fase 3 — Proposta HTML (para visualização pelo usuário)
Gerar `runs/[AAAA-MM-DD]/proposta-onboarding.html` com as seções:

| Seção | Conteúdo |
|---|---|
| 01 Diagnóstico | Tabela de indicadores + alertas imediatos |
| 02 Posicionamento | Declaração + proposta de valor |
| 03 Estratégia | Mix editorial (5 editorias com %) |
| 04 Formatos de produção | Feed (estático/carrossel/reels) + Stories (5 tipos) |
| 05 Calendário | 4 semanas do mês seguinte |
| 06 Exemplos de copy | 1 copy por editoria |
| 07 O que precisamos | Materiais + próximos passos |
| Resumo de produção | Bloco visual: semanal + mensal + total |
| Investimento | Valor/mês + condições + o que inclui |

**Regras de design da proposta:**
- Paleta do cliente no header + fundo claro nas seções
- Bloco de resumo: fundo navy escuro, números grandes em dourado
- Bloco de investimento: navy, valor em destaque, lista do que inclui
- Sem travessão ( — ) em nenhum lugar do texto
- Sem escrita de IA

**Referência de template:** `clients/servitec/runs/2026-07-23/proposta-onboarding.html`

### Fase 4 — Revisão e ajustes
O usuário lê o artifact publicado e pede ajustes. Aplicar e republicar no mesmo URL.

### Fase 5 — Gerar PDF (após aprovação)
Usar Chrome headless via PowerShell:

```powershell
$html = "CAMINHO_ABSOLUTO\proposta-onboarding.html"
$pdf  = "CAMINHO_ABSOLUTO\proposta-onboarding.pdf"
$chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"
$url = "file:///" + $html.Replace("\","/")

& $chrome --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="$pdf" "$url"
```

Copiar também para `C:\Users\Pichau\Downloads\` para acesso rápido.

---

## REGRAS DE ESCRITA (válidas para toda proposta)

- Sem travessão ( — ) — usar ponto, dois-pontos, vírgula ou ponto médio ( · )
- Sem termos de IA: "no contexto de", "ao longo de", "nesse sentido", "é importante ressaltar"
- Frases diretas, verbo ativo, dado concreto
- Tom: diagnóstico honesto + proposta clara + nenhum clickbait

---

## CSS CRÍTICO PARA PRINT

```css
* { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
```

Blocos com fundo escuro (navy) devem usar hex direto no inline style (`#001240`, `#002060`)
e ter classe para `break-inside: avoid` no `@media print`.

Cards e elementos que não podem quebrar entre páginas: adicionar classe e incluir na regra:
```css
@media print {
  .meu-card { break-inside: avoid; page-break-inside: avoid; }
}
```
