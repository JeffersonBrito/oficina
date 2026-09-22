# Dados e scripts

| Checagem | Como provar |
|----------|-------------|
| Amostra validada à mão | Rodar em 5 a 10 itens e comparar com o esperado, item a item |
| Idempotência | Rodar 2x e comparar saída/contagem |
| Contagens de entrada e saída fecham | Linhas lidas, linhas escritas, linhas descartadas com motivo |
| Custo dentro do teto | Número gasto vs teto da task |
| Não tocou o que não devia | Antes/depois do destino, além do esperado |
