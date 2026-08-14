# DESIGN-corporate.md — INTUS HUB / Intus IA Corporate

Referência visual: institucional premium, dark, estrutura azul + núcleo dourado.
Design skill: `impeccable` (não `bold`) — esta linha não usa o playbook de impacto/viral do Super Agente.

> Este arquivo aplica a paleta institucional de `brand-spec.md` especificamente à linha B2B Intus IA Corporate.
> O `DESIGN.md` original continua sendo a referência do Super Agente (campanha laranja) — nunca misturar os dois.

---

## Filosofia visual

**POV:** Produto técnico sério, mas nunca frio. Enquanto o Super Agente grita pra parar o scroll, o Corporate convence um decisor de empresa em silêncio — através de acabamento, estrutura e prova, não de urgência visual. Cada pixel deve transmitir: "isso é operado por gente séria, e já está rodando de verdade."

**Princípios:**
1. Estrutura antes de impacto — hierarquia clara, respiro generoso, nunca "grita" como criativo de social
2. Azul é a base, dourado é o momento — 70% azul / 20% dourado / 10% branco (proporção institucional oficial), nunca inverter
3. Prova > adjetivo — cada claim (skin in the game, segurança, escassez) tem elemento visual de apoio, não fica só em texto
4. Escuro total no fundo — Hub Night (#050D1F), nunca branco, nunca cinza claro genérico de SaaS
5. Assimetria com propósito — layout nunca centrado/simétrico igual aos concorrentes mapeados (Epic Labs, Flowgrammers, KapexIA são todos hero centrado + 3 cards iguais)

---

## Tipografia aplicada

**Headlines:**
- Família: Inter 700/900 (nunca abaixo de 700 em título) — esta é a fonte de display real usada no site institucional em produção (mentoria.intushub.com.br), confirmada por inspeção direta do CSS do site. **Syne está proibida nesta linha de produto**: é a fonte usada nos materiais de social media, tem assinatura visual de template genérico gerado por IA, e não corresponde à identidade real do site.
- Cor: White Ice #F0F4FF, com palavra-chave em Bright Gold #F0B429 quando houver claim central
- Tracking: -0.02em
- **Nunca Inter Tight aqui** — essa é a variante compacta, exclusiva da campanha Super Agente. A Inter padrão (700/900) é a correta para esta linha.

**Subtítulos/corpo:**
- Família: Space Grotesk 400-500
- Cor corpo: rgba(240,244,255,0.75)
- Tamanho: 16-18px corpo, 20-28px subhead
- Linha: 1.6

**Dados, tags, categoria do produto:**
- Família: JetBrains Mono 400-500, all-caps, letter-spacing 0.08em
- Cor: Light Blue #3399FF (estrutura) ou Bright Gold #F0B429 (destaque pontual)
- Uso: badges de fase (01/02/03/04), tag de categoria ("Consultoria de IA aplicada"), labels técnicos de segurança

---

## Cores aplicadas por seção da LP

**Hero:**
- Fundo: Hub Night #050D1F, sem gradiente decorativo (nada de roxo/azul genérico de "IA")
- Headline: White Ice, com 1 palavra ou frase curta em Bright Gold
- CTA: fundo Electric Blue #0055FF, texto White Ice, hover com glow azul sutil

**Seção de prova/skin in the game:**
- Fundo: leve variação — #0A1330 (mais claro que o hero, ainda escuro)
- Foto/elemento real (Diego, Aspira/Clóvis) — nunca ilustração genérica
- Nome/cargo em JetBrains Mono, Light Blue

**Seção de segurança/dados sensíveis:**
- Fundo: Hub Night, borda sutil Intus Blue (rgba(0,51,170,0.3))
- Ícones: line style, monocromático branco ou azul — nunca cadeado genérico de stock
- Este bloco deve parecer o mais "sóbrio" de toda a página — é o argumento de confiança, não de energia

**Seção de escassez/CTA final:**
- Fundo: Hub Night
- Número/dado de capacidade (ex: vagas do mês) em Bright Gold, JetBrains Mono, grande
- Border do card de escassez: 1px solid rgba(240,180,41,0.3) — dourado, não azul, pra destacar do resto da página

**Formulário de aplicação:**
- Fundo do card: #0A1330
- Inputs: borda Intus Blue em foco, nunca borda laranja (herança do padrão antigo)

---

## Elementos visuais recorrentes

**Glow azul (estrutura):**
- box-shadow: 0 0 40px rgba(0,85,255,0.2)
- Usado em: CTA primário, bordas de card ativo

**Glow dourado (momento/prova):**
- box-shadow: 0 0 32px rgba(240,180,41,0.18)
- Usado em: número de escassez, selo de segurança, claim de skin in the game — sempre pontual, nunca em mais de 1 elemento por dobra

**Borda sutil:**
- border: 1px solid rgba(51,153,255,0.2) — padrão
- border: 1px solid rgba(240,180,41,0.3) — variante de destaque (usar com moderação, é o "momento dourado")

**Linha divisória entre seções:**
- Gradiente: transparent → #0033AA → transparent
- Altura: 1px

**Hexágono marca:**
- Elemento decorativo de fundo, opacity 0.04-0.08, sempre em azul (nunca dourado sólido de fundo)

---

## Estéticas PROIBIDAS (além das globais de marca)

- Paleta laranja/preto da campanha Super Agente (Inter Tight, #E84000) — linhas nunca se misturam
- Gradiente roxo/azul genérico de "IA" (diferente do azul institucional sólido — ver nota abaixo)
- Hero centrado + 3 cards idênticos abaixo (é o padrão visual de Epic Labs/Flowgrammers/KapexIA — precisamos destoar)
- Ícones emoji, glassmorphism sem propósito, fundo claro
- Fonte Syne em qualquer peça desta linha — não é a fonte do site real, e carrega assinatura visual de "gerado por IA"/template genérico. Display font é sempre Inter 700/900.
- Mais de 1 elemento com glow dourado por dobra (dilui o "momento" de destaque)
- Foto de stock corporativo genérico ("aperto de mão", "pessoas sorrindo em reunião")

**Nota sobre azul:** a proibição de "gradiente roxo/azul genérico de IA" (herdada do `DESIGN.md` original) se refere ao gradiente roxo→azul clichê de produtos de IA (tipo OpenAI/Midjourney default). Isso é diferente do **Intus Blue institucional sólido**, que é cor de marca, não efeito decorativo — aplicado como bloco de cor ou glow sutil, nunca como gradiente multicolor de fundo.

---

## Referências de estilo

**Benchmark de acabamento:** Templo (institucional, premium, sem cair em curso genérico)
**Benchmark de mecânica de conversão:** Epic Labs (escassez real, "aplicar" não "comprar", metáfora simples pro processo)
**O que evitar de ambos:** hero centrado, cards simétricos, tom "startup jovem" (linguagem coloquial demais, gírias) — o Corporate fala direto mas sério
