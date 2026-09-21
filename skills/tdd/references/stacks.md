# Comandos e padrões por stack

Conferir sempre contra o projeto real: `pyproject.toml`, `pytest.ini`, `package.json` (`scripts.test`), `jest.config.*`, `vitest.config.*`. O que está aqui é o padrão quando o projeto não diz nada.

## pytest (Python)

| Ação | Comando |
|------|---------|
| Um teste só | `pytest tests/test_x.py::test_nome -q` |
| Um arquivo | `pytest tests/test_x.py -q` |
| Suíte inteira | `pytest -q` |
| Parar na primeira falha | `pytest -x -q` |
| Só os que falharam da última vez | `pytest --lf -q` |
| Por palavra no nome | `pytest -k "email" -q` |
| Mostrar prints | `pytest -s` |

Padrões:
- Arquivo `tests/test_<modulo>.py`, função `test_<comportamento>()`. Classes `TestX` só para agrupar.
- Fixtures em `conftest.py` no nível mais baixo que as usa.
- Asserção: `assert resultado == esperado`. Erro esperado: `with pytest.raises(ValueError, match="texto"):`.
- Mock: `unittest.mock.patch("modulo.onde.é.usado")`, não onde é definido. Preferir injetar a dependência a fazer `patch`.
- Parametrizar bordas: `@pytest.mark.parametrize("entrada,esperado", [...])`, um caso por linha, com `ids=`.
- RED legítimo: `AssertionError`, `NameError`/`ImportError` de função que ainda não existe, `AttributeError` de método novo. RED falso: `SyntaxError`, `fixture 'x' not found`, `ModuleNotFoundError` de dependência.

## Jest (Node/TypeScript)

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

## Vitest

Mesmos padrões do Jest, com `vi` no lugar de `jest`:

| Ação | Comando |
|------|---------|
| Um arquivo | `npx vitest run src/x.test.ts` |
| Por nome | `npx vitest run -t "nome"` |
| Suíte inteira | `npx vitest run` |
| Watch | `npx vitest` |

`vi.fn()`, `vi.mock()`, `vi.useFakeTimers()`.

## Outros

Sem reconhecer a stack: procurar o script de teste no manifesto do projeto e a pasta de testes existente; rodar um teste que já existe para aprender o comando; anotar os dois comandos antes de escrever o primeiro teste.
