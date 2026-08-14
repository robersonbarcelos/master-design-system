ALTER TABLE public.leads
  ADD COLUMN IF NOT EXISTS ferramentas_ia    text,
  ADD COLUMN IF NOT EXISTS economia_esperada text,
  ADD COLUMN IF NOT EXISTS disposicao_investir text;
