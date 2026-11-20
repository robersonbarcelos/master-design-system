# Brand Spec: ABS Moto Peças e Serviços

last_updated: 2026-10-14

> Fonte principal: `ABS_Memoria_Editorial.md` (seções 5, 6 e 7). Hex das cores da marca vêm dessa memória editorial; confirmar com o cliente se existir manual oficial.

---

## Logo

**Arquivo principal:** `assets/logo-abs.png` (337x89, RGBA, fundo transparente)
**Variações disponíveis:**
- [x] Versão horizontal (`assets/logo-abs.png`)
- [x] Versão com fundo branco (`assets/logo-abs-fundo-branco.png`, 320x320)
- [ ] Versão vetorial (SVG/PDF): pendente, pedir ao cliente (as atuais têm baixa resolução)
- [ ] Versão branca para fundo escuro: pendente
- [ ] Favicon / símbolo isolado: pendente

**Descrição:** "ABS" em itálico com bandeira quadriculada à esquerda; A vermelho, B amarelo, S verde; assinatura "MOTO PEÇAS" em caixa alta espaçada abaixo.

**Uso do logo:**
- Fundos permitidos: claros (off-white, branco, cinza claro) e escuros com contorno preservado
- Nunca: esticar, rotacionar, alterar as cores, adicionar sombra

---

## Cores

### Paleta funcional

| Papel | Nome | Hex | Uso |
|---|---|---|---|
| Base clara | Off-white | #FAFAF8 | Fundo principal (70 a 80% do feed) |
| Base neutra | Cinza claro | #E9ECEF | Fundo técnico, boxes |
| Texto / base escura | Grafite | #1F1F1F | Texto principal e fundo dark (20 a 30% do feed) |
| Marca 1 | Amarelo ABS | #FFD100 | Destaque, labels, CTAs, informação importante |
| Marca 2 | Vermelho ABS | #E53935 | Alerta, urgência, falha, problema, promoção |
| Marca 3 | Verde ABS | #009444 | Solução, resultado, aprovação, confiança |

**Regra:** evitar vermelho, amarelo e verde com o mesmo peso visual no mesmo card. A cor tem função, não decoração (vermelho = problema, amarelo = processo ou atenção, verde = resultado).

### Variáveis CSS
```css
:root {
  --abs-bg-light: #FAFAF8;
  --abs-bg-neutral: #E9ECEF;
  --abs-ink: #1F1F1F;
  --abs-yellow: #FFD100;
  --abs-red: #E53935;
  --abs-green: #009444;
}
```

---

## Tipografia

| Papel | Família | Observação |
|---|---|---|
| Display / Headline | Anton, Bebas Neue ou Oswald | Condensada, forte, alto impacto |
| Body / apoio | Montserrat, Inter ou Poppins | Sans serif limpa |

**Hierarquia:** 1) headline curta e grande, 2) palavra-chave destacada, 3) informação técnica de apoio, 4) CTA discreto.

---

## Estilo visual geral

**Referência visual:** técnico, moderno, confiável, forte, organizado, fotográfico, mais claro que as referências de concorrentes e menos "panfleto de motopeças". Um único sistema ABS com cinco famílias editoriais.

**Estilo de fotografia:** fotografia real da oficina como protagonista (bancada, mãos do mecânico, peça gasta x nova, motor, óleo, equipe). Evitar banco de imagens genérico e renderizações que deixem a oficina artificial.

**Atmosfera:** profissional, ativa, técnica, próxima. Não precisa parecer luxuosa.

---

## Notas de aplicação

- Dark é recurso (alerta, risco, desgaste severo), não identidade padrão
- Elementos recorrentes: labels, selos, boxes leves, ícones lineares, setas, checklists, comparativos, faixas finas de cor, assinatura da logo
- Detalhes completos por família em `visual-system.md` e `ABS_Memoria_Editorial.md`
