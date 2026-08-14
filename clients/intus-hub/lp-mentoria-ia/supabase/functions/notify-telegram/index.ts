import { serve } from 'https://deno.land/std@0.168.0/http/server.ts'

const TG_TOKEN = '8758318754:AAGCstM0fA9kDSUZIXjWuo-mm-BGHQprEFA'
const TG_CHAT  = '688498346'

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
}

serve(async (req) => {
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders })
  }

  try {
    const body = await req.json()
    // suporta payload direto ou via database webhook (body.record)
    const r = body.record || body

    const msg = `🔔 *Novo Lead — Mentoria INTUS HUB*

👤 *Nome:* ${r.nome || '—'}
🏢 *Empresa:* ${r.empresa || '—'}
📧 *Email:* ${r.email || '—'}
📱 *WhatsApp:* ${r.whatsapp || '—'}
🏷 *Segmento:* ${r.segmento || '—'}
💼 *Cargo:* ${r.cargo || '—'}
💰 *Faturamento:* ${r.faturamento || '—'}
👥 *Time:* ${r.time_empresa || '—'}
⚡ *Urgência:* ${r.urgencia || '—'}
✅ *Decisor:* ${r.decisor || '—'}
🎯 *Desafios:* ${r.area || '—'}
📝 *Observação:* ${r.gargalo || '—'}
🤖 *Ferramentas de IA:* ${r.ferramentas_ia || '—'}
📈 *Economia esperada (12m):* ${r.economia_esperada || '—'}
💡 *Disposição a investir:* ${r.disposicao_investir || '—'}`

    const tgRes = await fetch(`https://api.telegram.org/bot${TG_TOKEN}/sendMessage`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ chat_id: TG_CHAT, text: msg, parse_mode: 'Markdown' })
    })

    const tgJson = await tgRes.json()
    return new Response(JSON.stringify({ ok: true, tg: tgJson }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      status: 200
    })
  } catch (e) {
    return new Response(JSON.stringify({ error: e.message }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      status: 500
    })
  }
})
