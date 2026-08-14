# MAP — lp-mentoria-ia

## Estrutura

```
lp-mentoria-ia/
├── public/           ← arquivos servidos publicamente
│   ├── index.html    ← página principal (mentoria)
│   ├── mentoria/
│   │   └── index.html  ← rota limpa /mentoria
│   ├── fonts/        ← woff2 self-hosted
│   ├── assets/       ← imagens e SVGs
│   └── diego.jpg     ← foto OG
├── scripts/          ← ferramentas de build (não servidas)
├── vendor/           ← dependências externas (não servidas)
├── CLOUDFLARE-PAGES.md
└── MAP.md
```

## URL
- Produção: `intushub.com.br/mentoria`
- Rota limpa via `public/mentoria/index.html`

## Stack
- HTML puro + CSS custom properties + JS vanilla
- Fontes self-hosted (woff2)
- Deploy: Cloudflare Pages / Vercel
