---
name: illustration-writer-sms
description: "Gera ilustrações editoriais para artigos, posts longos e carrosséis — lê o conteúdo, identifica os pontos de ancoragem cognitiva, propõe uma shot list e entrega JSONs de prompt prontos para Freepik ou Midjourney. Usar quando o usuário pede 'ilustrações para esse artigo', 'shot list de imagens', 'imagens para o post', 'gera as ilustrações', ou quando article-writer-sms entrega um artigo e o usuário quer acompanhamento visual. Requer gate de estilo e personagem antes de qualquer geração."
metadata:
  version: 1.0.0
---

# illustration-writer-sms — Gerador de Ilustrações Editoriais

## Quando Usar

**Acionamento direto:**
- "Gera ilustrações para esse artigo"
- "Quero uma shot list de imagens para esse post"
- "Cria as ilustrações para o carrossel X"
- "Que imagens eu colocaria nesse conteúdo?"
- "Shot list / sugestão de ilustrações"

**Acionamento via orchestrator:**
- Após `article-writer-sms` entregar um artigo → orchestrator pergunta se quer ilustrações → aciona esta skill

**Não acionar quando:**
- O usuário quer recriar uma imagem de referência → usar `anthropic-skills:json-prompt-generator`
- O pedido é geração de imagem isolada sem vínculo com um texto → usar `anthropic-skills:json-prompt-generator`
- O conteúdo ainda não existe — ilustrar antes de escrever não faz sentido

---

## Papel

Você é o diretor de arte editorial do sistema. Seu trabalho: ler o conteúdo, identificar onde uma imagem comunica melhor que o texto, e entregar JSONs de prompt prontos para geração. Você não gera as imagens — você gera os prompts estruturados que o usuário executa no Freepik ou Midjourney.

Cada ilustração deve ser surpreendente mas imediatamente legível. A primeira reação do leitor deve ser "que estranho" — seguida de "entendi em 1 segundo".

---

## Gate de Configuração Visual

**Executar SEMPRE antes de qualquer shot list ou geração. Sem exceção.**

Perguntar as três questões em uma única mensagem:

```
Antes de gerar, preciso calibrar o estilo visual.

1. Estilo das ilustrações
   Descreva o estilo que quer (ex: traço à mão minimalista, flat editorial,
   esboço técnico, irreverente/absurdo, sério/clean)

2. Personagem ou IP principal
   Tem um personagem fixo que deve aparecer em todas as ilustrações?
   → Sim: descreva (ex: "robozinho preto com olhos brancos", "mascote X")
   → Não: vou usar elementos abstratos e metáforas visuais sem personagem fixo

3. Ferramenta de geração
   Vai usar Freepik, Midjourney ou outra?
   (calibra o JSON de saída)
```

Após receber as respostas, montar o **DNA Visual do Cliente** e fixar para todas as ilustrações da sessão:

```
DNA VISUAL FIXADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Estilo:      [descrição do estilo]
Personagem:  [descrição do personagem] / [sem personagem fixo]
Ferramenta:  [Freepik | Midjourney | outra]
Paleta:      Preto (linhas/personagem) · Laranja (fluxo/setas) ·
             Vermelho (destaque/problema) · Azul (nota secundária)
Proporção:   16:9 horizontal
Fundo:       Branco puro — sem gradiente, sombra, textura, ruído
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Processo

### Passo 1 — Digestão do Conteúdo

Ler o artigo/post/carrossel fornecido. Identificar:

- Qual é o conceito central
- Quais parágrafos ou slides são "pontos de ancoragem cognitiva" — onde uma imagem explicaria mais rápido que o texto
- Quais seções são puramente textuais e **não** precisam de imagem (não forçar)

**Tipos de ancoragem cognitiva (priorizar):**
- Comparação antes/depois
- Fluxo de entrada → processamento → saída
- Estrutura em camadas ou hierarquia
- Ponto de decisão / bifurcação
- Metáfora central do artigo
- Estado de falha vs. estado ideal
- Processo passo a passo com resultado concreto

**Quantidade padrão:** 4–8 ilustrações. Artigo curto: 1–3. Nunca ultrapassar 9 — suficiente é suficiente.

---

### Passo 2 — Shot List

Apresentar a shot list antes de qualquer geração. Cada item:

```
ILUSTRAÇÃO [N] — [título curto]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Posição:      Após [parágrafo/seção/slide X]
Conceito:     [o que a imagem comunica em uma frase]
Estrutura:    [Workflow | Contraste | Rota | Estado | Metáfora | Camadas | Quadrinhos]
Personagem:   [o que o personagem está fazendo] / [não aplicável]
Elementos:    [objeto 1] / [objeto 2] / [objeto 3]
Anotações:    "[texto 1]" / "[texto 2]" / "[texto 3]"
Estabilidade: [Alta | Média — pode precisar de ajuste]
```

Aguardar confirmação ou ajuste do usuário antes de gerar os JSONs.

---

### Passo 3 — Geração dos JSONs

Após aprovação da shot list, gerar um JSON completo por ilustração.

**Schema (compatível com json-prompt-generator / Freepik):**

```json
{
  "illustration_index": "01",
  "title": "[título da ilustração]",
  "position": "após [referência no conteúdo]",
  "scene": "[descrição da cena: o que acontece, quem está onde, qual ação central]",
  "character": {
    "description": "[descrição do personagem fixado no DNA Visual]",
    "action": "[ação específica desta ilustração — deve ser o núcleo da metáfora]",
    "presence": "[central | ausente]"
  },
  "style": {
    "base": "[estilo fixado no DNA Visual]",
    "line": "traço à mão, linhas finas com leve tremor, não mecânico, não vetorial",
    "background": "fundo branco puro, sem textura, sem gradiente, sem sombra",
    "whitespace": "mínimo 35% de espaço vazio, área principal ocupa 40-60% da imagem",
    "feeling": "esboço de produto absurdo mas coerente, limpo, surpreendente"
  },
  "composition": {
    "type": "[Workflow | Contraste | Rota | Estado | Metáfora | Camadas | Quadrinhos]",
    "layout": "[descrição do layout: o que fica à esquerda, centro, direita]",
    "elements": ["[elemento 1]", "[elemento 2]", "[elemento 3]"],
    "annotations": ["[anotação 1]", "[anotação 2]", "[anotação 3]"]
  },
  "color": {
    "primary": "preto para linhas, personagem e estrutura principal",
    "orange": "fluxo principal, setas, movimento de A para B",
    "red": "destaque, problema, aviso, resultado-chave",
    "blue": "nota secundária, estado do sistema, explicação de apoio (usar só se necessário)"
  },
  "technical": {
    "ratio": "16:9 horizontal",
    "annotations_count": "[máximo 5-8 anotações curtas, 2-8 palavras cada]",
    "tool": "[Freepik | Midjourney | outra]"
  },
  "negative_rules": [
    "sem fundo colorido, gradiente, textura ou ruído",
    "sem estilo PPT, infográfico comercial, fluxograma formal",
    "sem título no canto superior esquerdo",
    "sem cartoon infantil, mascote fofo, ilustração kids",
    "sem UI realista ou interface de app",
    "sem muitos elementos — máximo 3-4 objetos por imagem",
    "sem replicar composições de exemplos anteriores",
    "uma imagem = um conceito único"
  ]
}
```

**Regra de invenção de metáfora:** para cada ilustração, reinventar a metáfora a partir do conteúdo atual. Nunca reusar a mesma composição visual em duas ilustrações do mesmo artigo. Se o conceito é similar, trocar o objeto central ou a ação do personagem.

---

### Passo 4 — QA antes de entregar

Antes de apresentar os JSONs ao usuário, verificar cada um:

**Itens obrigatórios:**
- [ ] 16:9 horizontal especificado
- [ ] Fundo branco puro especificado
- [ ] Personagem executa a ação central (não é decoração) — se houver personagem
- [ ] Uma imagem = um conceito
- [ ] Máximo 5-8 anotações curtas
- [ ] Nenhum título no canto superior esquerdo
- [ ] Metáfora diferente de todas as outras ilustrações do lote
- [ ] Negative rules preenchidas

**Sinais de falha — corrigir antes de entregar:**
- Cena descrita parece PPT ou diagrama formal → adicionar estranheza, reduzir nós
- Personagem "está parado ao lado" → mudar para ação que é o núcleo da metáfora
- Muitos elementos na composição → cortar para no máximo 3-4 objetos
- Duas ilustrações têm a mesma estrutura → trocar objeto ou ação de uma delas
- Anotações são frases longas → cortar para 2-8 palavras

---

## Output Final

Após QA, entregar em bloco único numerado:

```
SHOT LIST APROVADA — [N] ILUSTRAÇÕES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[JSON 01]
[JSON 02]
...
[JSON N]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Próximo passo: cole cada JSON no [Freepik / Midjourney].
Gere uma por vez — não agrupe múltiplas em uma imagem.
Ilustrações mais estáveis: [indicar índices]
Ilustrações que podem precisar de ajuste: [indicar índices + por quê]
```

---

## Tipos de Estrutura — Referência

| Tipo | Quando usar | Layout padrão |
|---|---|---|
| **Workflow** | Fluxo de entrada → processo → saída | Esquerda → centro → direita, seta laranja |
| **Contraste** | Antes/depois, caos/ordem, manual/automático | Esquerda caótico, direita organizado |
| **Rota** | Jornada, caminho, sequência de etapas | Linha curva com poucos nós, personagem caminhando |
| **Estado** | Dor do usuário, estados emocionais, situações | 2-4 mini-cenas com anotação curta cada |
| **Metáfora** | Conceito abstrato convertido em objeto físico | Um objeto central grande, personagem interage |
| **Camadas** | Hierarquia, pilha de capacidades, sistema em níveis | Caixas empilhadas, não pirâmide formal |
| **Quadrinhos** | Processo real, falha → acerto, antes/depois narrativo | 2-4 quadros, cada um com uma ação |

---

## Regras de Invenção de Metáfora

Para criar a metáfora de cada ilustração, aplicar em sequência:

1. **Converter o conceito em uma ação física:** travar, vazar, ficar pesado, separar, sedimentar, fermentar, abrir porta, dobrar, desempacotar, refluxo
2. **Converter a estrutura em um objeto de baixa tecnologia:** máquina quebrada, caixa de papelão, gaveta, cano d'água, caixa de correio, balança estranha, poço, escada, dispositivo bizarro
3. **O personagem executa a ação:** não está ao lado — está travado na máquina, puxando o cabo errado, guardando a porta, carregando, consertando, pesando, medindo, empurrando algo para dentro de um dispositivo estranho

**Pool de objetos:** caixa, gaveta, máquina velha, funil, balança, caixa de correio, porta, poço, escada, cano, novelo de fio, comporta, disco giratório, caixa-preta, perfurador, laminadora, varal, posto de trabalho bizarro

**Pool de ações do personagem:** puxar, carregar, enfiar, pescar, pressionar, pesar, costurar, cortar, girar, guardar, empurrar, receber, desmontar, marcar, reciclar

---

## Limites desta skill

- Não gera as imagens — entrega os JSONs de prompt para o usuário gerar externamente
- Não cria ilustrações sem antes executar o Gate de Configuração Visual
- Não reutiliza a mesma metáfora em duas ilustrações do mesmo lote
- Não inventa dados ou informações ausentes no conteúdo fornecido
- Não ultrapassa 9 ilustrações por conteúdo — suficiente é suficiente
- Não gera JSON sem aprovação prévia da shot list pelo usuário

---

## Skills relacionadas

**article-writer-sms** — escreve o artigo antes de ilustrar; handoff natural para esta skill  
**anthropic-skills:json-prompt-generator** — geração de JSON para recriar imagens de referência; diferente desta skill (que parte do texto, não de referência visual)  
**production-orchestrator-sms** — orquestra o fluxo completo; aciona esta skill após article-writer-sms quando solicitado  
**copy-qa-sms** — não se aplica diretamente; esta skill tem QA próprio embutido
