# Texto (e-mail, post, doc, mensagem)

| Checagem | Como provar |
|----------|-------------|
| Tamanho | `wc -w` ou contagem; colar o número |
| Primeira frase carrega a informação principal | Citar a primeira frase |
| Itens de "não dizer" ausentes | Buscar cada um (`grep -i`); colar resultado |
| Leitor consegue agir | Reler como o leitor: dá para responder/decidir sem perguntar nada? Dizer o que ele faria |
| Nomes, datas, números batem com a fonte | Conferir cada um contra a task ou o arquivo de origem |
| Tom pedido | Comparar com a referência de estilo citada na task |
| Sem placeholder | `grep -nE "\[.*\]|TODO|XXX|lorem"` |
