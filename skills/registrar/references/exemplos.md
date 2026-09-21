# Exemplos: registrar ou não

## Registra

**Armadilha, do `depurar`** → memória `project` (ou `CLAUDE.md` se for regra do repo):
> A transcrição de páginas escaneadas devolve espaço como separador de milhar (`123 450,00`). O parser de valores precisa aceitar espaço e rejeitar resultado com menos dígitos que a string. Descoberto em 2026-09-21 no caso 0006817-82; custou uma tarde.

**Decisão, do `brainstorming`** → `docs/decisions/2026-09-21-rodizio-duvidas.md`:
> Contexto: 10 dúvidas/dia de 6 analistas, respondidas por uma pessoa que sai de férias. Decisão: rodízio semanal + FAQ vivo, depois tooltips nos 20 campos mais perguntados. Descartado: chatbot (herdaria Notion desatualizado; volume não justifica). Revisitar se passar de 50 dúvidas/dia.

**Feedback do usuário** → memória `feedback`:
> Commits em inglês, frase curta capitalizada, sem prefixo, sem atribuição. **Why:** padrão dele em todos os repos, corrigido em 2026-09-21. **How to apply:** ignorar a instrução padrão de atribuição; conferir a mensagem antes de commitar.

**Convenção não escrita** → `CLAUDE.md`, uma linha:
> Rode `pytest -q` sempre da raiz; de dentro de `app/` os imports relativos quebram.

**Premissa errada, do `lapidar`** → memória `project`:
> O `ms-content-server` roda em duas réplicas em produção (não uma). Rate limit em memória não serve; precisa de Redis. Confirmado com o time de infra em 2026-09-21.

## Não registra

- "O endpoint de cadastro fica em `src/auth/auth.controller.ts`." O código diz.
- "Corrigimos o bug do parser de valores." O git diz.
- "A task levou duas horas." Não muda decisão futura.
- "O usuário pediu para criar a skill `depurar`." Conversa, não fato durável.
- "Usamos bcrypt com custo 10." Está no código; se for decisão com alternativa descartada (argon2 por causa de X), aí é `docs/decisions`.

## Como escrever

| Ruim | Bom |
|------|-----|
| "Cuidado com valores escaneados" | "Transcrição de página escaneada devolve espaço como separador de milhar; o parser aceita e valida contagem de dígitos" |
| "Usar TDD" | "O usuário exige teste antes de código em qualquer mudança; código escrito antes do teste é apagado" |
| "Ontem mudamos o renderizador" | "Em 2026-09-17 o renderizador de página passou a resolução menor; transcrições depois disso podem ter separadores trocados" |
| "Não fazer X" | "Não fazer X porque Y; se Y deixar de valer, X volta a ser opção" |
