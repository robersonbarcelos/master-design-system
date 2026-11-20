# Site e Quiz: F. Brasil Academy

> Estado do que está no ar em 20/11/2026. Código: `C:\Users\Pichau\Downloads\clones\lp-push` (branch `main`, repositório GitHub com deploy automático na Vercel).

## Endereços

| Caminho | O que é |
|---|---|
| `fbrasilacademy.com.br/` | Landing de vendas do curso |
| `/quiz` | Quiz "Seu currículo está preparado para a era da IA?" |
| `/raio-x` | Mesmo quiz (rewrite para `/quiz`) |
| `/curriculo-ia` | Atalho que abre a landing do curso (rewrite para `/`) |
| `/quiz/nota` | Página interna "Seu currículo está preparado para a era da IA?" |
| `/api/lead` | Grava o lead no Google Sheets (Telegram previsto, não configurado) |

Domínio no Registro.br, zona DNS em Modo avançado: `A` 76.76.21.21 (Vercel), `www` por CNAME, SPF e 5 CNAMEs do RD Station (e-mail SendGrid) e TXT `_dmarc`.

## Tecnologia

TypeScript (TSX) em Next.js 16 e React 19, Tailwind CSS 4, CSS próprio (`lp.css`, `quiz.css`), `lucide-react` para ícones, shadcn e `@base-ui/react`. Fontes Bebas Neue e Outfit via `next/font`. Hospedagem Vercel.

## Medição e rastreio

- **RD Station:** loader no `layout.tsx` (`strategy="afterInteractive"`, `account_id` 1200432). Só rastreia visitas; o quiz grava no Google Sheets, não no RD.
- **Google Analytics 4:** `G-HQFNXFDY5F`, tag no `layout.tsx` desde 19/11/2026. Status inicial "coleta pendente" (até 48 h).
- `noindex` ativo nas páginas (remover no go-live).

## Landing de vendas: estrutura

1. Menu: O curso, Método, Bônus, Quem ensina, Dúvidas, botão "Quero o curso".
2. Abertura (gradiente navy, foto do Fabiano em máscara curva): "Curso com o head hunter Fabiano Brasil" + título "O currículo de sucesso na era da IA." + subtítulo + botões "Quero o curso" e "Faça o teste gratuito" + "R$ 97 · garantia de 7 dias · bônus com 5 prompts de IA".
3. Faixa rolante: Clareza, Verdade, Contexto, Contribuição, Estratégia, IA com fatos reais, Direto ao ponto.
4. Autoridade: "Experiência dos dois lados da mesa. Quem contrata sabe o que lê." + contadores 34 anos, 66 mil, 13 mil+ horas.
5. "Você se reconhece?": seis perguntas do público com resposta curta.
6. Método: "Um bom currículo responde quatro perguntas rápido".
7. "Seis aulas, direto ao ponto": Aula 01 O currículo na era da IA; 02 ATS e candidaturas digitais; 03 Os erros que enfraquecem o currículo; 04 Experiências e resultados; 05 IA aplicada ao currículo; 06 Checklist final e plano de ação.
8. Antes e depois (exemplo ilustrativo).
9. Quatro pilares do "Método Direto ao Ponto": Clareza, Consistência, Verdade, Estratégia.
10. Bônus e oferta: caderno com 5 prompts + "Curso completo R$97, 6 aulas curtas e diretas ao ponto, caderno bônus, garantia de 7 dias" + ressalva de que não promete entrevista nem contratação.
11. Quem ensina: Fabiano Brasil, head hunter + link para o LinkedIn.
12. Perguntas frequentes (4).
13. Convite ao teste: "Quer saber se seu currículo está pronto antes de comprar?"
14. Rodapé: "© F. Brasil Academy. Este curso não promete entrevista, aprovação em sistemas ATS ou contratação. Página de exemplo para aprovação, textos sujeitos a revisão do Fabiano."

**Pendências na landing:** botão "Faça o teste gratuito" ainda aponta para `#` (deveria ir para `/quiz`); link de checkout (`COURSE_URL`) é placeholder `#`; página lista 6 aulas contra 10 do plano; números 34 / 66 mil / 13 mil precisam de confirmação; falta política de privacidade; "Página de exemplo" no rodapé deve sair no go-live.

## Quiz: fluxo

1. **Abertura:** "TESTE DE 10 PERGUNTAS" + "SEU CURRÍCULO ESTÁ PREPARADO PARA A ERA DA IA?" + "Responda 10 perguntas sobre o seu currículo, exatamente como ele está hoje. Descubra sua nota de 0 a 100 e identifique os pontos que precisam de atenção para melhorar sua apresentação profissional." + botão + aviso "Teste educativo. Não mede a chance de contratação e não certifica compatibilidade com nenhum ATS." Animações: currículo em raio-x e nota girando.
2. **10 perguntas** (uma por tela), cada uma com três respostas: **Não (0)**, **Parcialmente (5)**, **Sim (10)**. Legenda: "Responda pensando no currículo que você usa hoje".
3. **Captura:** "SEU RESULTADO ESTÁ PRONTO. Informe seus dados para ver a nota, a faixa e os pontos que mais pedem atenção." Campos: nome, e-mail, WhatsApp (obrigatório, DDD e número), consentimento. Texto do consentimento: "Autorizo a F. Brasil Academy a entrar em contato por e-mail e WhatsApp com meu resultado e conteúdos do Fabiano Brasil. Posso cancelar quando quiser." Nota: "Seus dados ficam com a F. Brasil Academy e não são vendidos nem compartilhados."
4. **Resultado:** nota de 0 a 100 + faixa colorida + texto da faixa; "SUA NOTA EM CADA PONTO" (barra por pergunta); "POR ONDE COMEÇAR" (as 3 perguntas de menor nota, com o erro e a explicação, "Prioridade 1, 2, 3"); "TRANSFORME ESSE RESULTADO EM MELHORIAS PRÁTICAS" + botão "Conhecer o curso" (link do curso, hoje `#`); rodapé com o aviso educativo; "Refazer o teste".

## Quiz: as 10 perguntas (texto do PDF do Fabiano, sem alteração)

| # | Área | Pergunta |
|---|---|---|
| 1 | Clareza do objetivo | Meu currículo apresenta claramente as áreas e posições profissionais para as quais possuo qualificação. |
| 2 | Resumo profissional | O resumo inicial demonstra minha especialidade, senioridade e principais diferenciais, sem recorrer apenas a frases genéricas. |
| 3 | Resultados comprováveis | Minhas experiências apresentam conquistas, melhorias ou resultados concretos, sempre que possível com números e indicadores. |
| 4 | Palavras-chave relevantes | Meu currículo utiliza naturalmente termos técnicos, competências e expressões relevantes para as posições que busco. |
| 5 | Estrutura e legibilidade | O documento possui organização clara, títulos identificáveis e formatação que favorece a leitura humana e a extração de texto. |
| 6 | Compatibilidade com ATS | Evito depender de elementos gráficos complexos, imagens ou informações essenciais em formatos que possam dificultar a leitura por sistemas. |
| 7 | Aderência à vaga | Antes de me candidatar, verifico os requisitos e ajusto a ênfase das informações do currículo sem alterar os fatos. |
| 8 | Experiência e evolução | Minha trajetória demonstra responsabilidades, escopo de atuação, progressão e contexto profissional de maneira objetiva. |
| 9 | Uso responsável da IA | Quando utilizo IA, reviso cuidadosamente o conteúdo para evitar exageros, informações inventadas e linguagem artificial. |
| 10 | Revisão final e coerência | Meu currículo está atualizado, sem erros relevantes, com datas coerentes e informações alinhadas ao meu LinkedIn. |

Cada pergunta corresponde a um erro: 1 Objetivo impreciso, 2 Resumo genérico, 3 Responsabilidades sem resultados, 4 Linguagem distante da vaga, 5 Formatação confusa, 6 Dependência de recursos gráficos, 7 Candidaturas sem critério, 8 Trajetória sem contexto, 9 Texto produzido por IA sem revisão, 10 Inconsistências e desatualização.

## Quiz: faixas

| Nota | Faixa | Texto | Cor |
|---|---|---|---|
| 0 a 39 | Revisão urgente | Há fragilidades importantes. Priorize estrutura, conteúdo e posicionamento antes de intensificar candidaturas. | `#E8806A` |
| 40 a 59 | Melhorias necessárias | Existe uma base aproveitável, mas o currículo pode não comunicar adequadamente qualificação e diferenciais. | `#CB9A5A` |
| 60 a 79 | Bem estruturado | Seu documento apresenta uma boa base. Ajustes direcionados podem melhorar clareza, aderência e resultados. | `#7FB4E0` |
| 80 a 100 | Preparação consistente | Sua autoavaliação indica uma estrutura sólida. Continue adaptando o documento às oportunidades e revisando sua eficácia. | `#6CC28C` |

## Formato de escrita do site e do quiz

- **Títulos:** caixa alta condensada (Bebas Neue), com uma palavra de destaque em dourado (`<em>`): "SEU CURRÍCULO ESTÁ PREPARADO PARA A ERA DA **IA?**".
- **Capa em pergunta:** "Quer saber se seu currículo está pronto antes de comprar?", "Você se reconhece?".
- **Etiqueta acima do título** em bronze: "Teste de 10 perguntas", "Método", "Bônus e oferta".
- **Frases curtas**, uma ideia por bloco, palavras do dia a dia.
- **Dor em voz do público** entre aspas e resposta curta e honesta ("Pode haver fatores de mercado. Aqui o foco é o que está ao seu alcance").
- **Ressalva em todo bloco de oferta:** "Não promete entrevista nem contratação".
- **Exemplo sempre marcado:** "Exemplo ilustrativo, apenas para demonstrar o método."
- **CTA com verbo e destino:** "Quero o curso", "Faça o teste gratuito", "Fazer o teste do currículo", "Conhecer o curso".
- **Resultado do quiz:** tom de diagnóstico, sem julgamento; sempre mostra o que fazer em seguida.
- Sem travessão na copy.
