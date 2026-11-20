# F. Brasil Academy: Contexto de Produção

> Lido automaticamente pelo Claude Code ao abrir esta pasta. Perfil criado em 20/11/2026 a partir do briefing de 17/10/2026, do dossiê, das artes da Camila e do site no ar.

---

## Ativação automática

Você está trabalhando com o cliente **F. Brasil Academy** (Fabiano Brasil, head hunter de Curitiba).

Ao iniciar qualquer sessão nesta pasta, leia em sequência:

1. `.agents/social-media-context-sms.md`: voz, pilares, público, papéis, concorrência
2. `brand-spec.md`: logo, cores, tipografia, contraste
3. `DESIGN.md`: referência visual do site e do quiz
4. `production-rules.md`: gatilho pré-copy, padrões proibidos, exemplos antes e depois
5. `content-system.md`: editorias, grade, CTAs, UTM, funil
6. `visual-system.md`: grupos visuais, JSON de imagem, regras de prompt

Confirme em uma linha: *"Trabalhando com F. Brasil Academy. O que vamos produzir hoje?"*

## Sob demanda

- `site-e-quiz.md`: copy e estrutura da landing e do quiz no ar, as 10 perguntas, faixas, rastreio
- `references/dados-ancora.md`: números, produto, LinkedIn, concorrência
- `references/temas.md`: banco de pautas
- `references/copies-aprovadas.md`: voz do Fabiano e textos do site
- `assets/logo/`, `assets/fotos/`, `assets/artes-camila-referencia/`

## Regras que mandam em tudo

1. **Autoria é do Fabiano.** Textos, roteiros, artigos e vídeos são dele. Tudo que sair daqui é rascunho para aprovação (prazo dele: 48 h). Não mudar conteúdo autoral sem o ok.
2. **Sem anúncios** na fase 1. Orgânico, com UTM em todo link. Não pedir acesso a contas de anúncio.
3. **Nunca prometer** entrevista, aprovação em ATS ou contratação. Todo exemplo é marcado "fictício" ou "ilustrativo".
4. **Bases (28 mil WhatsApp, 6 milhões de currículos):** NÃO usar para oferta. Depende de avaliação LGPD.
5. **Cargo:** "Head Hunter" primeiro, em todos os lugares.
6. **Números de autoridade** (34 anos, 66 mil, 13 mil horas) ainda precisam da confirmação do Fabiano.
7. Sem travessão (—) na copy. Acentuação PT-BR completa.
8. Logo e foto do Fabiano usados como vieram, sem recriar.
9. Quem faz o quê: Fabiano (conteúdo), Camila (redes e identidade visual), Roberson (páginas, quiz, funil, integrações).

## Estado do projeto (20/11/2026)

**No ar:** landing `/`, quiz `/quiz` (+ `/raio-x`, `/curriculo-ia`), domínio `fbrasilacademy.com.br`, RD Station, Google Analytics `G-HQFNXFDY5F`, DNS do e-mail (SPF, CNAMEs, `_dmarc`).
**Pendente:**
- Plataforma de venda e checkout (link `COURSE_URL` ainda `#`).
- Botão "Faça o teste gratuito" da landing aponta para `#`; deveria ir para `/quiz`.
- Roteiros das 10 aulas e dos 8 vídeos verticais (curso gravado de 15 vídeos chegou em 14/11; falta mapear às aulas).
- Casos e depoimentos autorizados.
- Logo em vetor, nomes das fontes, dourado oficial e manual de marca (pedir à Camila).
- Política de privacidade; aviso de cookies; remover `noindex` e o aviso "página de exemplo" no go-live.
- Telegram do `/api/lead` não configurado; sequência de e-mails por faixa do quiz.
- Confirmar com o Fabiano: revisão individual/mentoria (não está no briefing), parcelamento, política de reembolso, segundo curso.

## Salvamento de artefatos

Salvar em `runs/AAAA-MM-DD/` com kebab-case: `carrossel-[tema].md`, `roteiro-[tema].md`, `post-[tema].md`, `lp-briefing-[tema].md`, `json-capas-[tema].md`.

## Antes de produzir

- Nunca escrever copy sem o Gatilho Pré-Copy de `production-rules.md`.
- Passar por `copy-qa-sms` antes de entregar (regra global de copy).
- Se algum arquivo tiver placeholder não preenchido, avisar antes de produzir.
