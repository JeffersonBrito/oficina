# Código

| Checagem | Como provar |
|----------|-------------|
| Suíte inteira verde | `pytest -q` / `npm test` rodado agora; colar a linha de resumo |
| Lint e tipos | `ruff check .`, `mypy`, `npm run lint`, `tsc --noEmit`, o que o projeto tiver; colar resultado |
| Diff é só o escopo | `git diff --stat` e leitura do diff; cada arquivo tem motivo na task |
| Nada deixado para trás | `git diff \| grep -nE "print\(\|console\.log\|TODO\|FIXME\|debugger\|breakpoint"` |
| Sem segredo ou caminho local | `git diff \| grep -nE "/Users/\|/home/\|password\|secret\|token"` |
| Tudo salvo e no git | `git status --porcelain` vazio ou só o esperado |
| Commit no padrão | `git log -1 --format=%s%n%b`: inglês, capitalizado, sem prefixo, sem atribuição |
| Comportamento real, não só teste | Chamar a rota/função uma vez de verdade (curl, REPL, script) e colar a resposta |
| Sem comentário que repete o código | Ler o diff procurando comentários; cada um explica um porquê ou sai |
