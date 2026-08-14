-- Habilita Row Level Security na tabela leads
ALTER TABLE public.leads ENABLE ROW LEVEL SECURITY;

-- Permite INSERT público (formulário da landing page usa chave publishable)
CREATE POLICY "allow_public_insert"
  ON public.leads
  FOR INSERT
  TO anon
  WITH CHECK (true);

-- Bloqueia SELECT, UPDATE, DELETE do público
-- (somente service_role / dashboard do Supabase consegue ler os leads)
