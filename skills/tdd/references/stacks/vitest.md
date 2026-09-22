# Vitest

Mesmos padrões do Jest, com `vi` no lugar de `jest`:

| Ação | Comando |
|------|---------|
| Um arquivo | `npx vitest run src/x.test.ts` |
| Por nome | `npx vitest run -t "nome"` |
| Suíte inteira | `npx vitest run` |
| Watch | `npx vitest` |

`vi.fn()`, `vi.mock()`, `vi.useFakeTimers()`.
