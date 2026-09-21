# Técnicas de localização

## Bissecção no tempo

```bash
git bisect start
git bisect bad                 # commit atual, com o bug
git bisect good <hash-bom>     # último commit sabidamente bom
# a cada parada: rodar a reprodução, depois
git bisect good   # ou
git bisect bad
git bisect reset
```

Com teste de reprodução automatizado: `git bisect run pytest tests/test_x.py::test_repro -q` faz tudo sozinho.

## Bissecção no caminho

Escolher um ponto no meio entre a entrada e a saída e perguntar: o estado aqui já está errado?

- Log com contexto, não `print("aqui")`: `print(f"[triage] pages={len(pages)} chars={total} budget={budget}")`.
- Assert temporário: `assert total <= budget, (total, budget)`.
- Salvar o estado intermediário em arquivo e inspecionar com calma.

Estado certo aqui → o bug está adiante. Errado → está atrás. Repetir naquele lado. Remover tudo no fim.

## Redução de input

Cortar o input pela metade e testar. Se ainda reproduz, cortar de novo. Se parou, a outra metade tem o gatilho. Chegar ao menor input que reproduz: ele costuma **mostrar** a causa (um caractere, um campo nulo, uma data no limite).

## Diferença entre ambientes

Reproduz na máquina A e não na B? Listar as diferenças, uma por linha, e eliminar uma por vez: versão da linguagem, dependências (`pip freeze`, `npm ls`), variáveis de ambiente, locale e timezone, dados, permissões de arquivo, arquitetura.

## Ler o stack trace

- Python: de baixo para cima; a última linha é o erro, a primeira linha **do seu código** (não de biblioteca) acima dela é onde olhar.
- Node: de cima para baixo; mesma regra, pular frames de `node_modules`.
- Ler os **argumentos** do frame quando o depurador mostra; o valor inesperado costuma estar ali.

## Depuradores

| Linguagem | Parar em um ponto | Rodar teste com depurador |
|-----------|-------------------|---------------------------|
| Python | `breakpoint()` na linha | `pytest -x --pdb` (para na primeira falha) · `pytest --lf` (só os que falharam) |
| Node/TS | `debugger;` + `node --inspect-brk` | `node --inspect-brk node_modules/.bin/jest --runInBand <arquivo>` |
| Shell | `set -x` | `bash -x script.sh` |

No depurador, três perguntas: qual o valor das variáveis aqui? De onde veio esse valor? O que eu esperava que fosse?

## Quando o bug é de dado

Comparar o registro que falha com um que funciona, campo a campo. A diferença é a hipótese 1. Buscar quantos registros compartilham a diferença: `grep -c`, `db.count()`. Isso diz se é um caso ou uma classe.

## Quando o bug é de concorrência ou tempo

- Tornar determinístico primeiro: relógio fixo (`freezegun`, `vi.useFakeTimers`), seed fixa, uma thread.
- Se sumiu ao serializar, é ordem ou estado compartilhado. Procurar o estado compartilhado (global, cache, singleton, conexão).

## Registrar enquanto depura

Manter uma lista curta no raciocínio: hipótese → previsão → resultado. Quando a terceira for descartada, a lista mostra o padrão do que ainda não foi questionado.
