# pytest (Python)

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
