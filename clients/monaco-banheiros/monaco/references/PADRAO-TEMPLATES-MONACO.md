# Padrão de Templates de Card : Mônaco

> Todo template novo da Mônaco segue esta lógica. Referência: `TEMPLATE-BORDAS-MONACO.json` (primeiro template, 13 out 2026).

## Nome e arquivo
- `TEMPLATE-[NOME]-MONACO.json` em `monaco/references/`.
- Variações dentro do arquivo: `card-01-...`, `card-02-...` (estilo BNB), com `indice_rapido` no fim (estilo CTG).
- Arquivo de teste preenchido: `TESTE-[NOME]-MONACO.json`.

## As 4 regras
1. **Imagem livre.** A foto é sempre anexada (IMAGEM 1) e pode ser qualquer cena: trailer, interior, casa, rua, evento ou pessoas. O prompt nunca descreve a cena. Ele só manda preservar tudo, sem redesenhar, trocar, remover ou acrescentar nada, e aplicar tratamento de cor editorial, upscale de nitidez e recurso de legibilidade na área do texto.
2. **Logo em local definido.** A logo é anexada (IMAGEM 2: `logo/monaco-simbolo-marinho.png`, ou o símbolo branco sobre fundo escuro) e aplicada exatamente como enviada, em coordenadas fixas. Plano B: colar o PNG por cima.
3. **Dados fixos travados.** Header "MÔNACO MOBILE TOILET / EVENTOS · PRODUÇÕES", telefone (11) 97628-4782 e site www.banheirosmonaco.com.br, com texto, fonte, cor e posição definidos.
4. **Copy em campos.** Onde vai texto, o template define posição, fonte, tamanho, cor e limite de caracteres. O texto entra por `{{CAMPO}}` a cada post. Campo opcional vazio = elemento removido.

## Blocos obrigatórios em todo template
`template`, `status`, `description`, `logica_padrao_templates_monaco`, `anexos`, `instrucao_para_colar_antes`, `logo`, `tratamento_da_foto`, `estrutura_do_layout`, `elementos_fixos`, `slots_variaveis`, `regras_fixas`, `negative_rules_globais`, `variacoes` (cada uma com `preencher` + `json_exemplo` neutro), `indice_rapido`.

## Templates
| Arquivo | Uso | Status |
|---|---|---|
| TEMPLATE-BORDAS-MONACO.json | Foto com moldura, headline 2 cores, local opcional, faixa de contato | aguardando teste |
| TEMPLATE-HOTSPOTS-MONACO.json | Foto full-bleed com lente circular, barra UI de vidro, hotspots em objetos reais, Poppins | aguardando teste |

## Como escolher o template pela imagem
Quando o Diego carregar uma foto e perguntar, analisar a imagem e responder com: template + variação recomendados, por quê, 2 opções de copy (título, subtítulo, destaque, hotspots ou local) e o JSON completo em bloco se ele pedir.

| A foto tem... | Template | Variação |
|---|---|---|
| Lugar marcante e céu/área limpa em cima | BORDAS | card-01 (com local) |
| Interior ou detalhe com área limpa em cima, 0 a 1 objeto de destaque | BORDAS | card-02 (sem local) |
| 4 objetos reais bem visíveis e espalhados (interior completo) | HOTSPOTS | card-01 (4 hotspots) |
| 1 a 2 objetos claros, trailer por fora, foto limpa ou com rostos | HOTSPOTS | card-02 (2 hotspots) |
| Foto escura, desfocada, cortada no trailer ou sem área para texto | avisar e sugerir outra foto ou recorte | |

Regras de título: curto (até ~10 caracteres por linha) = tamanho padrão do template; longo (14 a 20) = reduzir (HOTSPOTS 82px, destaque só na palavra-chave); acima de 20 = reescrever.

## Regra de CAPA 9:16 (Reels), definida pelo Diego em 14 out 2026
- Toda capa 9:16 é montada a partir de um template 4:5 salvo (BORDAS, HOTSPOTS...), adaptado.
- O card 4:5 (1080x1350) fica CENTRALIZADO dentro do canvas 1080x1920. Atrás dele vai a MESMA foto, ampliada e bem desfocada (blur forte, levemente escurecida), preenchendo o 9:16.
- Assim a capa funciona na grade do perfil (recorte 4:5) e no feed de Reels (9:16) sem cortar nada importante.
- Copy da capa: CURTA e grande (headline de 2 a 3 linhas, no máximo um eyebrow ou local). SEM rodapé: nada de site, telefone ou faixa de contato na capa.
- Referência aprovada: capa "Banheiros Mônaco na 55ª Convenção Nacional da Unimed" (criações/Banheiros Mônaco na Convenção Unimed.png).
- Antes de gerar, sempre propor 3 ideias de copy da capa e esperar a escolha.
