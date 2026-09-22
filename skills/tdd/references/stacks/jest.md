# Jest (Node/TypeScript)

| Ação | Comando |
|------|---------|
| Um arquivo | `npx jest src/auth/auth.service.spec.ts` |
| Um teste por nome | `npx jest -t "retorna 409"` |
| Suíte inteira | `npm test` (conferir o script) |
| Watch | `npx jest --watch` |
| Só os relacionados a arquivos alterados | `npx jest -o` |

Padrões:
- Arquivo ao lado: `x.spec.ts` (NestJS) ou `x.test.ts`; ou `__tests__/`. Seguir o que o projeto já faz.
- `describe('<unidade>')` + `it('<comportamento em frase>')`.
- Asserção específica: `toBe`, `toEqual`, `toStrictEqual`, `toHaveLength(2)`. Evitar `toBeTruthy`/`toBeDefined` como asserção principal.
- Erro esperado: `await expect(fn()).rejects.toThrow(ConflictException)`.
- Mock: `jest.fn()` injetado pelo construtor ou pelo módulo de teste do Nest (`Test.createTestingModule` com `useValue`). `jest.mock('modulo')` só para fronteira externa.
- RED legítimo: asserção falhou, `TypeError: x is not a function` de método novo. RED falso: erro de compilação TS não relacionado, `Cannot find module`.
