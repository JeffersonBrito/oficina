# Exemplos

## Exemplo 1: código, com uma falha

Task do `/lapidar`: endpoint de cadastro com 409 para e-mail duplicado. O `/tdd` reportou tudo verde.

```markdown
## Conferência: endpoint POST /auth/register

| # | Critério | Status | Evidência |
|---|----------|--------|-----------|
| 1 | Os 4 testes existem e passam | passou | `npx jest src/auth` → `Tests: 4 passed, 4 total` |
| 2 | POST válido retorna 201 sem campo password | passou | `curl -s -X POST localhost:3000/auth/register -d '{...}'` → `201 {"id":"c1f...","email":"a@b.com","createdAt":"..."}` |
| 3 | Repetir o mesmo POST retorna 409 | falhou | segundo curl → `500 Internal Server Error`; log: `QueryFailedError: duplicate key`. O índice único existe, mas a exceção não é traduzida para 409 |
| 4 | Lint e suíte inteira passam | passou | `npm run lint` → 0 problems · `npm test` → `Tests: 51 passed` |
| 5 | Swagger mostra 201, 400 e 409 | passou | `GET /api-json` → `paths./auth/register.post.responses` tem `201`, `400`, `409` |

**Implícitos:** escopo íntegro (`git diff --stat`: 6 arquivos, todos da task) · nada pela metade · nada deixado para trás (`grep console.log` no diff: 0) · padrões da casa (`git log -1` → `Add register endpoint`)

**Fora da lista, encontrado no diff:** nada.

**Veredito: NÃO PRONTO.** Falta: item 3, a violação do índice único vira 500 em vez de 409. O teste de 409 passa porque mocka o repositório; a chamada real não passa pelo mock.
```

O que este exemplo mostra: o `/tdd` estava verde e mesmo assim a entrega não estava pronta. O teste era desonesto (mock do repositório escondia o comportamento real), e só a chamada de verdade no critério 2 e 3 revelou. Conferir não é repetir o relatório do tdd; é produzir evidência independente.

## Exemplo 2: texto, pronto

Task: e-mail ao cliente sobre atraso, até 120 palavras, data nova na primeira frase, sem citar o responsável.

```markdown
## Conferência: e-mail de atraso para a Ana (Contoso)

| # | Critério | Status | Evidência |
|---|----------|--------|-----------|
| 1 | Primeira frase contém a data nova | passou | "Ana, a entrega do módulo de relatórios, prevista para 25/09, passa para 02/10." |
| 2 | Até 120 palavras | passou | `wc -w` → 97 |
| 3 | Nenhum item de "não dizer" | passou | busca por "equipe", "infra", "atrasar de novo", nome do responsável → 0 ocorrências |
| 4 | Termina com pedido claro de resposta | passou | última frase: "Consegue me confirmar se 02/10 funciona para vocês, ou sugerir outra data?" |

**Implícitos:** é o que foi pedido (assunto + corpo, sem versões alternativas) · sem placeholder (`grep "\["` → 0) · nomes e datas batem com a task

**Veredito: PRONTO.**
```

## Exemplo 3: não dá para conferir

```markdown
| 3 | Rodar 2x não duplica registros no Mongo de homolog | não conferido | sem acesso ao Mongo de homolog nesta sessão; precisa da URI ou de alguém rodar `db.processos.countDocuments()` antes e depois |

**Veredito: NÃO PRONTO.** Não conferido: item 3. Para fechar: rodar a contagem em homolog, ou o usuário aceitar explicitamente entregar sem essa prova.
```
