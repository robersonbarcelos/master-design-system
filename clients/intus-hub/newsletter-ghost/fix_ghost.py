import sys, requests, json, jwt
from datetime import datetime, timezone
sys.stdout.reconfigure(encoding='utf-8')

GHOST_URL = 'https://roberson-barcelos.ghost.io'
GHOST_ADMIN_KEY = '69c54c1b309b100001e5ff95:a89b51138d4c3985fbf82fb764d709d612d068ca6b504538e8a3958e49c719b1'
POST_ID = '69c54fa5309b100001e5ff9d'
UPDATED_AT = '2026-03-26T15:24:21.000Z'

HTML = """
<div style="max-width:670px;margin:0 auto;font-family:Helvetica,Arial,sans-serif;color:#1B1B1B;">

  <div style="display:flex;gap:20px;padding:20px 0;">
    <div style="flex:1;">
      <p style="font-size:15px;font-weight:bold;margin:0 0 8px;">&#9889; Sentiment:</p>
      <p style="font-size:15px;line-height:24px;margin:0;">
        BTC: <strong>$71.019</strong> (+0,9% 24h)<br>
        ETH: <strong>$2.164</strong> (-9,2% semana)<br>
        Petroleo Brent: <strong>$99,55</strong><br>
        Circle (CRCL): <strong style="color:#cc0000;">-20,11%</strong>
      </p>
    </div>
    <div style="width:3px;background:#030712;align-self:stretch;"></div>
    <div style="flex:1;">
      <p style="font-size:15px;font-weight:bold;margin:0 0 8px;">&#128200; Market Cap:</p>
      <p style="font-size:15px;line-height:24px;margin:0;">
        Total: <strong>~$2.4T</strong><br>
        USDT cap: <strong>$184B</strong><br>
        Coinbase: <strong style="color:#cc0000;">-11%</strong><br>
        Plano paz EUA-Ira: <strong style="color:#006600;">15 pontos</strong>
      </p>
    </div>
  </div>

  <div style="border-top:3px solid #030712;width:50%;margin:20px auto;"></div>

  <div style="padding:10px 0 20px;">
    <h3 style="font-family:Trebuchet MS,sans-serif;font-size:20px;color:#1B1B1B;margin:0 0 14px;">&#128181; Circle -20% e Coinbase -11%: o Clarity Act que apagou bilhoes em um pregao</h3>
    <img src="https://i.ibb.co/Q3DgGZfP/intus-20260326-img1.png" alt="Circle stock crash" style="width:100%;border-radius:6px;display:block;margin:14px 0;"/>
    <p style="font-size:16px;line-height:26px;margin:12px 0;">Em um unico pregao, a Circle Internet Group (CRCL) despencou 20,11% de $126,64 para $101,17, enquanto a Coinbase recuou 11%. O gatilho foi o Clarity Act, proposta legislativa americana que redesenha a estrutura regulatoria para stablecoins e jogou incerteza direta sobre os modelos de receita das duas empresas.</p>
    <p style="font-size:16px;line-height:26px;margin:12px 0;">O paradoxo e claro: quanto mais o setor cripto tenta se institucionalizar, mais fica exposto as mesmas forcas que regulam o sistema financeiro tradicional. A variavel decisiva agora e o texto final do Clarity Act e quao agressivo ele sera na limitacao dos rendimentos distribuidos por emissores de stablecoins.</p>
  </div>

  <div style="border-top:3px solid #030712;width:50%;margin:10px auto 30px;"></div>

  <div style="padding:10px 0 20px;">
    <h3 style="font-family:Trebuchet MS,sans-serif;font-size:20px;color:#1B1B1B;margin:0 0 14px;">&#128269; Tether contrata Big Four: a auditoria que o mercado esperava ha anos</h3>
    <img src="https://i.ibb.co/nW9YbBr/intus-20260326-img2.png" alt="Tether Big Four auditoria" style="width:100%;border-radius:6px;display:block;margin:14px 0;"/>
    <p style="font-size:16px;line-height:26px;margin:12px 0;">A Tether anunciou que contratou uma das quatro maiores firmas de auditoria do mundo para realizar a primeira auditoria financeira independente e completa das reservas do USDT. Com $184 bilhoes em capitalizacao, o USDT e a maior stablecoin do mundo e historicamente a mais questionada quanto a transparencia das reservas.</p>
    <p style="font-size:16px;line-height:26px;margin:12px 0;">O que chama atencao e o timing: enquanto a Circle desaba na bolsa por pressao regulatoria, a Tether proativamente busca credibilidade com auditores de nivel maximo. Se a auditoria confirmar integridade total das reservas, o efeito sobre a confianca no USDT e em todo o mercado de stablecoins sera consideravel.</p>
  </div>

  <div style="border-top:3px solid #030712;width:50%;margin:10px auto 30px;"></div>

  <div style="padding:10px 0 20px;">
    <h3 style="font-family:Trebuchet MS,sans-serif;font-size:20px;color:#1B1B1B;margin:0 0 14px;">&#10052; Tether e Circle congelam carteiras da Wallex: stablecoins como ferramenta geopolitica</h3>
    <p style="font-size:16px;line-height:26px;margin:12px 0;">Em acao coordenada, Tether e Circle congelaram carteiras associadas a exchange iraniana Wallex, em cumprimento as sancoes impostas pelos EUA. A medida reforca um padrao que vem se consolidando: emissores centralizados de stablecoins operam como extensao do sistema de compliance financeiro ocidental, com poder de congelar ativos a qualquer momento.</p>
    <p style="font-size:16px;line-height:26px;margin:12px 0;">A pergunta estrutural e direta: stablecoins sao neutras? A resposta pratica ja esta dada. Para quem busca resistencia a censura, o recado e inequivoco: USDT e USDC nao oferecem essa protecao. O debate sobre stablecoins descentralizadas nunca esteve tao relevante.</p>
  </div>

  <div style="border-top:3px solid #030712;width:50%;margin:10px auto 30px;"></div>

  <div style="padding:10px 0 20px;">
    <h3 style="font-family:Trebuchet MS,sans-serif;font-size:20px;color:#1B1B1B;margin:0 0 14px;">&#9889; Bitcoin segura $71k enquanto petroleo cai abaixo de $100 e EUA propoe paz com o Ira</h3>
    <img src="https://i.ibb.co/kVcZQx75/intus-20260326-img4.png" alt="Bitcoin $71k macro" style="width:100%;border-radius:6px;display:block;margin:14px 0;"/>
    <p style="font-size:16px;line-height:26px;margin:12px 0;">O Bitcoin operou a $71.019 (+0,9% em 24h) em meio ao primeiro alivio macro em semanas. O Brent recuou 4,7% para $99,55, abaixo dos $100 pela primeira vez desde o inicio do conflito, depois que Washington apresentou ao Ira um plano de 15 pontos via Paquistao. Equidades asiaticas subiram 1,9%, dolar enfraqueceu e futuros americanos apontaram para cima.</p>
    <p style="font-size:16px;line-height:26px;margin:12px 0;">Para o cripto, o BTC demonstrou mais resiliencia do que os ativos de risco tradicionais. A queda semanal de 6,4% ainda pesa, mas o suporte em $71k se manteve mesmo durante os picos de tensao geopolitica. Se o plano de paz avancar, a pressao vendedora deve ceder. Se travar, o petroleo volta a $116 e o BTC enfrenta novo teste.</p>
  </div>

  <div style="border-top:3px solid #030712;width:50%;margin:10px auto 30px;"></div>

  <div style="padding:10px 0 20px;">
    <h3 style="font-family:Trebuchet MS,sans-serif;font-size:20px;color:#1B1B1B;margin:0 0 14px;">&#127463;&#127479; Visa, Pix e Stablecoins: o dinheiro programavel esta chegando ao Brasil</h3>
    <img src="https://i.ibb.co/n8rdjy1v/intus-20260326-img5.png" alt="Pix Stablecoins Brasil" style="width:100%;border-radius:6px;display:block;margin:14px 0;"/>
    <p style="font-size:16px;line-height:26px;margin:12px 0;">A Visa movimentou US$ 4,5 bilhoes em liquidacoes anuais com stablecoins ate dezembro de 2025. Eduardo Abreu, VP de Novos Negocios da Visa no Brasil, resume o novo paradigma: "O dinheiro passa a ser um software programavel". A convergencia entre Pix, stablecoins e contratos inteligentes nao e ruptura, e evolucao da infraestrutura financeira global, com o Brasil em posicao privilegiada.</p>
    <p style="font-size:16px;line-height:26px;margin:12px 0;">O Pix ja provou que adocao em massa acontece quando infraestrutura aberta encontra experiencia simples. A proxima camada, pagamentos programaveis e stablecoins em reais, pode seguir o mesmo caminho. Para o mercado cripto brasileiro, a demanda por ativos digitais denominados em BRL nao e tendencia futura. E presente que ainda nao chegou em escala.</p>
  </div>

  <div style="border-top:3px solid #030712;width:50%;margin:10px auto 30px;"></div>

  <div style="padding:10px 0 20px;">
    <h3 style="font-family:Trebuchet MS,sans-serif;font-size:20px;color:#1B1B1B;margin:0 0 14px;">&#9878; 11 estados americanos vs. Polymarket: a batalha que pode redesenhar o DeFi</h3>
    <img src="https://i.ibb.co/dwr88YYL/intus-20260326-img6.png" alt="Polymarket regulacao EUA" style="width:100%;border-radius:6px;display:block;margin:14px 0;"/>
    <p style="font-size:16px;line-height:26px;margin:12px 0;">Onze estados americanos, incluindo Nevada, Arizona e Pensilvania, entraram em confronto com plataformas como Kalshi e Polymarket. Nevada impôs bloqueio de 14 dias. O Arizona apresentou acusacoes criminais por operacao ilegal de apostas. O combustivel: um grupo lucrou ~US$ 1 milhao apostando em ataques dos EUA ao Ira, com forte suspeita de insider trading.</p>
    <p style="font-size:16px;line-height:26px;margin:12px 0;">O que esta em jogo vai alem de apostas em eleicoes. A batalha entre estados e CFTC vai definir como plataformas financeiras descentralizadas serao tratadas nos EUA. Se os estados vencerem, o escopo regulatorio sobre DeFi pode se expandir de forma agressiva. O precedente que sair dessa disputa vai ecoar por anos.</p>
  </div>

  <div style="border-top:3px solid #030712;width:50%;margin:20px auto;"></div>

  <div style="text-align:center;padding:20px 0;">
    <p style="font-size:14px;color:#1B1B1B;margin:0 0 6px;">&#169; 2026 Newsletter Intus Cripto</p>
    <p style="font-size:12px;color:#BAC2CE;margin:0;">Powered by Ghost</p>
  </div>

</div>
"""

key_id, secret = GHOST_ADMIN_KEY.split(':')
iat = int(datetime.now(timezone.utc).timestamp())
token_payload = {'iat': iat, 'exp': iat + 300, 'aud': '/admin/'}
token = jwt.encode(token_payload, bytes.fromhex(secret), algorithm='HS256', headers={'kid': key_id})

headers = {'Authorization': f'Ghost {token}', 'Content-Type': 'application/json'}

lexical = json.dumps({
    "root": {
        "children": [{"type": "html", "version": 1, "html": HTML}],
        "direction": None, "format": "", "indent": 0,
        "type": "root", "version": 1
    }
})

body = {"posts": [{"title": "Intus Cripto News - 25/03/2026", "lexical": lexical, "status": "draft", "updated_at": UPDATED_AT}]}

r = requests.put(f'{GHOST_URL}/ghost/api/admin/posts/{POST_ID}/', headers=headers, json=body, timeout=30)
result = r.json()
if result.get('posts'):
    p = result['posts'][0]
    print(f'SUCESSO! Post atualizado.')
    print(f'Admin: {GHOST_URL}/ghost/#/editor/post/{POST_ID}')
    print(f'URL publica: {p.get("url")}')
else:
    print('ERRO:', json.dumps(result, indent=2, ensure_ascii=False)[:600])
