---
name: adaptacao-referencia-sms
description: "Adapta um conteúdo de referência (carrossel, post, roteiro, legenda) de outra marca para qualquer cliente do sistema, mantendo a base da mensagem e reescrevendo tom de voz, gancho e escrita. Usar SEMPRE que o usuário mandar uma referência para 'adaptar', 'replicar', 'recriar', 'absorver a referência', 'fazer igual pro cliente', 'seguir a mesma base'. Roda antes da skill de criação do formato (carousel-writer-sms, post-writer-sms, video-script-sms etc.) e entrega a ela a modelagem slide a slide."
metadata:
  version: 1.0.0
---

# Adaptação de Referência

## Princípio

Referência dá a **ideia**, nunca o **texto**.

| Mantém da referência | Muda para o cliente |
|---|---|
| Mensagem central e tese | Tom de voz (production-rules.md do cliente) |
| Tópicos e a lógica da sequência (a ordem pode mudar um pouco para não ficar na cara que veio da referência) | Gancho da capa (3 opções novas) |
| Função de cada slide (capa, contexto, item, virada, fechamento) | Escrita de cada frase, reescrita do zero |
| Tipo de frase (antes x agora, dado + implicação, lista, contraste) | Nicho, exemplos e vocabulário do cliente |
| Ritmo e quantidade de slides | Virada e CTA padrão do cliente |
| | Template visual: sempre os templates oficiais do cliente |

## Nunca

- Copiar frase da referência, nem com troca de 1 ou 2 palavras
- Inventar argumento, cena, tópico ou implicação que a referência não tem
- Cortar tópico da referência sem avisar
- Usar dado da referência sem fonte: marcar `[DADO A CONFIRMAR]` e perguntar se busca fonte ou tira o número
- Herdar travessão, termos proibidos ou CTA da referência

## Fluxo

1. **Ler a referência na ordem certa.** Carrossel: arquivos terminados em _0 (capa), _1, _2... Ler todos antes de qualquer proposta.
2. **Mapa da referência.** Tabela por slide: função · ideia (1 linha, com palavras minhas) · layout. Apontar problemas que não podem vir junto (travessão, dado sem fonte, erro de data).
3. **Encaixe visual.** Consultar os templates oficiais do cliente (ex.: BNB `references/*-BNB.json`) e propor um card por slide. Nunca inventar template a partir da referência.
4. **3 ganchos** no padrão do cliente, mantendo a tese da capa da referência.
5. **Storytelling adaptado, sempre em 2 versões.** Tabela por versão: slide · ideia da referência · texto do cliente (reescrito). Aguardar aprovação.
   - **Versão BASE:** mesma lógica e mesmos tópicos da referência; ordem pode trocar levemente para disfarçar a origem.
   - **Versão ADAPTADA:** mantém a tese, mas troca ou ajusta alguns conceitos para o contexto do cliente (ex.: um tópico vira outro mais próximo da operação do cliente). Sinalizar o que mudou em relação à base. O usuário escolhe se quer usar.
6. **Handoff** para a skill de criação do formato (carousel-writer-sms etc.), que roda Gate CTA, copy-qa-sms e entrega final.

## Checklist antes de entregar

- [ ] Cada slide do cliente corresponde a uma ideia da referência (nenhum a mais, nenhum a menos sem aviso)
- [ ] Nenhuma frase igual ou quase igual à da referência
- [ ] Voz conferida no production-rules.md do cliente
- [ ] Dados sem fonte marcados
- [ ] Zero travessão
- [ ] Templates oficiais do cliente usados
