---
name: conferir
description: Prova que uma entrega está pronta antes de dizer "pronto": cada critério de aceite com evidência produzida agora, status passou / falhou / não conferido, veredito PRONTO ou NÃO PRONTO. Use antes de concluir qualquer tarefa, ou quando invocarem /conferir, "confere", "tá tudo certo?", "revisa antes de entregar".
---

# Conferir

Antes de dizer "pronto", provar. Cada critério recebe evidência produzida **agora**: saída de comando, trecho de arquivo, número contado. "Deve estar passando" e "rodei há pouco" não são evidência. Entrada: task do `/lapidar`, relatório do `/tdd`, ou pedido direto. Saída: relatório e veredito. Flag `--corrigir`: corrigir o que falhou e reconferir, até 3 rodadas.

Regra central: **não conferido é diferente de passou.** O relatório diz o que passou, o que falhou e o que não foi conferido e por quê, com o mesmo peso.

## Fluxo

1. **Lista do que provar.** Critérios de aceite da task; senão a tabela do `/tdd`; senão derivar do pedido literal e mostrar a lista antes. Somar os **implícitos**: entregue é o pedido, sem escopo cortado em silêncio nem extra; nada pela metade (arquivo não salvo, "depois faço"); nada deixado para trás (log, `TODO`, temporário, comentário redundante); padrões da casa. Por tipo de entrega: `references/checagens/<tipo>.md`.
2. **Evidência, um critério por vez**, pela tabela abaixo. Não dá para conferir nesta sessão (acesso, outra pessoa, produção)? **Não conferido**, com o que seria preciso. Nunca "passou" por falta de meio.
3. **Ler o diff inteiro** em entrega com código: mudança fora do escopo, arquivo esquecido, exploração que ficou, segredo ou caminho local. Texto: reler do início ao fim como o leitor final.
4. **Veredito.** PRONTO só com tudo passou e nada não conferido. Qualquer falha ou não conferido é NÃO PRONTO com o que falta. Não existe "quase" nem "com ressalvas". Com `--corrigir`: corrigir (código pelo `/tdd`), reconferir só os afetados e "nada quebrou", máximo 3 rodadas.

| Critério | Evidência aceita | Não aceita |
|----------|------------------|------------|
| teste passa / suíte verde | comando rodado agora e a linha de resultado | "os testes existem" |
| arquivo/função/rota existe | trecho aberto agora, com caminho | "criei" |
| retorna Y quando Z | chamada executada e resposta colada | "a lógica cobre" |
| até N palavras/slides | contagem feita, com o número | "está curto" |
| primeira frase contém X | a frase citada | "está no começo" |
| nada de "não dizer" | busca por cada item, com resultado | "não coloquei" |
| nada quebrou | suíte inteira, lint, diff lido | "só mexi em um arquivo" |
| commit no padrão | `git log` da mensagem | "commitei certo" |

## Relatório

````markdown
## Conferência: <o que foi conferido>

| # | Critério | Status | Evidência |
|---|----------|--------|-----------|
| 1 | <critério> | passou | `pytest -q` → `47 passed` |
| 2 | <critério> | falhou | `GET /x` duplicado → 500, esperado 409 |
| 3 | <critério> | não conferido | precisa de acesso a homolog |

**Implícitos:** escopo íntegro (diff lido, N arquivos, todos da task) · nada pela metade · nada deixado para trás · padrões da casa (`git log -1` → `...`)

**Fora da lista, encontrado no diff:** <o que apareceu, ou "nada">

**Veredito: NÃO PRONTO.** Falta: <item 2>. Não conferido: <item 3, e o que seria preciso>.
````

Entrega pequena, relatório pequeno. Nunca omitir implícitos nem veredito.

## Sinais de arredondamento

| Pensamento | Realidade |
|-----------|-----------|
| "Rodei há cinco minutos" | Rodar de novo. Custa segundos. |
| "O arquivo de teste existe" | Existir não é passar. |
| "Não conferi X, mas o resto passou" | NÃO PRONTO. |
| "Falhou um detalhe, o grosso está feito" | Veredito é binário. |

## Não faz

Não escreve critérios além dos implícitos (`/lapidar`). Não corrige sem `--corrigir`. Não avalia qualidade subjetiva: confere o pedido contra o entregue.

## Referências

| Arquivo | Quando ler |
|---------|-----------|
| `references/checagens/<codigo\|texto\|apresentacao\|dados\|plano>.md` | No passo 1, só o tipo da entrega |
| `references/exemplos.md` | Só em dúvida sobre o que conta como evidência |
