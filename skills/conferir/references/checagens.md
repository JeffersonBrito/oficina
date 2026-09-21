# Checagens por tipo de entrega

Critérios implícitos e como produzir a evidência. Acrescentar aos critérios da task, não substituir.

## Código

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

## Texto (e-mail, post, doc, mensagem)

| Checagem | Como provar |
|----------|-------------|
| Tamanho | `wc -w` ou contagem; colar o número |
| Primeira frase carrega a informação principal | Citar a primeira frase |
| Itens de "não dizer" ausentes | Buscar cada um (`grep -i`); colar resultado |
| Leitor consegue agir | Reler como o leitor: dá para responder/decidir sem perguntar nada? Dizer o que ele faria |
| Nomes, datas, números batem com a fonte | Conferir cada um contra a task ou o arquivo de origem |
| Tom pedido | Comparar com a referência de estilo citada na task |
| Sem placeholder | `grep -nE "\[.*\]|TODO|XXX|lorem"` |

## Apresentação

| Checagem | Como provar |
|----------|-------------|
| Número de slides | Contar |
| Cada número tem fonte | Listar número → fonte; qualquer um sem fonte falha |
| Ordem dos slides = contrato da task | Comparar título a título |
| Tempo | Ensaio cronometrado, ou estimativa de 1 a 2 min por slide declarada como estimativa |
| Termos técnicos traduzidos | Buscar os termos e conferir se há explicação na mesma frase |

## Dados e scripts

| Checagem | Como provar |
|----------|-------------|
| Amostra validada à mão | Rodar em 5 a 10 itens e comparar com o esperado, item a item |
| Idempotência | Rodar 2x e comparar saída/contagem |
| Contagens de entrada e saída fecham | Linhas lidas, linhas escritas, linhas descartadas com motivo |
| Custo dentro do teto | Número gasto vs teto da task |
| Não tocou o que não devia | Antes/depois do destino, além do esperado |

## Plano ou decisão

| Checagem | Como provar |
|----------|-------------|
| Cada item tem dono e data | Ler a lista; qualquer um sem, falha |
| Esforço cabe na capacidade | Somar e comparar com o declarado |
| Recomendação única com condição de reversão | Citar a frase |
| Alternativas descartadas com motivo | Contar |

## Quando não dá para conferir

Marcar **não conferido** e dizer o que seria preciso: "precisa de acesso ao S3 de homolog", "precisa que a Ana confirme a data", "precisa de um caso real escaneado". O veredito fica NÃO PRONTO até isso ser resolvido ou o usuário aceitar explicitamente o risco.
