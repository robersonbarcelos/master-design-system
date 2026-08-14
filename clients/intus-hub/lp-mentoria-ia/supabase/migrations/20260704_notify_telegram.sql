CREATE OR REPLACE TRIGGER notify_telegram_on_lead
  AFTER INSERT ON public.leads
  FOR EACH ROW
  EXECUTE FUNCTION supabase_functions.http_request(
    'https://evtchedskwnwpioatjet.supabase.co/functions/v1/notify-telegram',
    'POST',
    '{"Content-Type":"application/json","Authorization":"Bearer sb_publishable_PrzJanVd9LnY4RXTpOw1JA_3HguATrj"}',
    '{}',
    '5000'
  );
