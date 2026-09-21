---
name: conferir
description: Verifica se uma entrega está pronta de verdade antes de dizer "pronto". Pega os critérios de aceite da task (do /lapidar, do relatório do /tdd, ou derivados do pedido) e confere cada um com evidência produzida na hora: comando rodado e saída, arquivo aberto e trecho, número contado. Reporta passou / falhou / não conferido, nunca arredonda, e termina com PRONTO ou NÃO PRONTO. Vale para código, texto, apresentação, dados ou qualquer entrega. Use antes de declarar qualquer tarefa concluída, quando o usuário invocar /conferir, disser "confere se ficou pronto", "revisa antes de entregar", "tá tudo certo?", ou pedir para validar uma entrega.
---

# Conferir

Antes de dizer "pronto", provar. Cada critério de aceite recebe uma evidência produzida **agora**, nesta sessão: a saída de um comando, o trecho de um arquivo, um número contado. "Deve estar passando" e "rodei há pouco" não são evidência.

Entrada: a task com critérios de aceite (do `/lapidar`), o relatório do `/tdd`, ou um pedido direto (`/conferir <o que conferir>`). Saída: relatório critério a critério e um veredito, PRONTO ou NÃO PRONTO.

| Flag | Efeito |
|------|--------|
| (nenhuma) | Confere e reporta. Não corrige nada. |
| `--corrigir` | Confere, corrige o que falhou, confere de novo. No máximo 3 rodadas; depois reporta o que sobrou. |

## Princípio

Não conferido é diferente de passou. A mentira mais comum de quem entrega, pessoa ou modelo, é arredondar "acho que está certo" para "está certo". Esta skill existe para separar os dois. O relatório diz o que passou, o que falhou, e **o que não foi conferido e por quê**, com o mesmo peso.

## Fluxo

### 1. Montar a lista do que provar

Fontes, em ordem de preferência:
1. Critérios de aceite da task do `/lapidar`, um por linha.
2. Tabela do relatório do `/tdd`.
3. Sem nenhum dos dois: derivar do pedido original. O que foi pedido, literalmente, vira um critério cada. Mostrar a lista antes de conferir.

Acrescentar sempre os **critérios implícitos**, que ninguém escreve mas todo mundo espera. Lista por tipo de entrega em `references/checagens.md`. Os universais:
- O que foi entregue é o que foi pedido, sem escopo cortado em silêncio e sem escopo extra.
- Nada ficou pela metade: arquivo não salvo, alteração só na memória, item "depois eu faço".
- Nada foi deixado para trás: log de debug, `TODO` sem dono, arquivo temporário, comentário que repete o código.
- Os padrões da casa foram seguidos (commits, código, formato pedido).

### 2. Produzir a evidência, um critério por vez

Para cada critério, executar a verificação **de verdade** e guardar a prova:

| Tipo de critério | Evidência aceita | Não aceita |
|------------------|------------------|------------|
| "teste X passa" / "suíte verde" | Comando rodado agora e a linha de resultado | "os testes existem", "passou no tdd" |
| "arquivo/função/rota existe" | Trecho do arquivo aberto agora, com caminho | "criei o arquivo" |
| "retorna Y quando Z" | Chamada executada e resposta colada | "a lógica cobre isso" |
| "até N palavras/slides/linhas" | Contagem feita, com o número | "está curto" |
| "primeira frase contém X" | A primeira frase, citada | "está no começo" |
| "nenhum item de 'não dizer' aparece" | Busca por cada item, com resultado | "não coloquei" |
| "nada quebrou" | Suíte **inteira** rodada, lint rodado, diff lido | "só mexi em um arquivo" |
| "commit no padrão" | `git log` da mensagem | "commitei certo" |

Se um critério **não dá para conferir** nesta sessão (precisa de acesso, de outra pessoa, de produção), marcar **não conferido** com o motivo e o que seria preciso. Nunca marcar passou por falta de meio.

### 3. Ler o diff inteiro

Para entrega com código ou arquivo versionado: ler o diff completo, não só os arquivos que "lembra" de ter mexido. Procurar: mudança fora do escopo, arquivo esquecido, código de exploração que ficou, segredo ou caminho local hardcoded. Para texto: reler do início ao fim uma vez, como o leitor final.

### 4. Veredito

- **PRONTO**: todo critério passou e nenhum está "não conferido". Sem exceção.
- **NÃO PRONTO**: qualquer critério falhou ou não foi conferido. O relatório diz exatamente o que falta. Não existe "quase pronto", "pronto com ressalvas" ou "pronto, só falta".

Com `--corrigir`: para cada critério que falhou, corrigir (se envolve código, pelo `/tdd`), e voltar à etapa 2 **só para os critérios afetados e para "nada quebrou"**. Máximo 3 rodadas. O que sobrar vai para o relatório como NÃO PRONTO.

## Formato do relatório

````markdown
## Conferência: <o que foi conferido>

| # | Critério | Status | Evidência |
|---|----------|--------|-----------|
| 1 | <critério> | passou | `pytest -q` → `47 passed` |
| 2 | <critério> | falhou | `GET /auth/register` duplicado → 500, esperado 409 |
| 3 | <critério> | não conferido | precisa de acesso ao ambiente de homolog |

**Implícitos:** escopo íntegro (diff lido, 6 arquivos, todos da task) · nada pela metade · nada deixado para trás · padrões da casa (`git log -1` → `Add register endpoint`)

**Fora da lista, encontrado no diff:** <o que apareceu e não estava na task, ou "nada">

**Veredito: NÃO PRONTO.** Falta: <item 2>. Não conferido: <item 3, e o que seria preciso>.
````

Relatório curto para entrega pequena: três critérios, três linhas. Nunca omitir a linha de implícitos nem o veredito.

## Sinais de que está arredondando

| Pensamento | Realidade |
|-----------|-----------|
| "Rodei os testes há cinco minutos" | Rodar de novo. Custa segundos; a mudança de depois pode ter quebrado. |
| "A mudança é trivial, não precisa conferir" | Trivial quebra. Conferir custa menos que explicar depois. |
| "O arquivo de teste existe, então está testado" | Existir não é passar. Rodar. |
| "O usuário pode conferir isso" | Ele pediu para você conferir. Se não dá, é "não conferido", não "passou". |
| "Não conferi X, mas o resto passou, então PRONTO" | Não conferido não é passou. NÃO PRONTO. |
| "Falhou um detalhe, mas o grosso está feito" | Veredito é binário. NÃO PRONTO, com o detalhe listado. |
| "Vou marcar passou e conferir no final" | Conferir é agora. Cada linha da tabela é escrita depois da evidência, não antes. |

## O que esta skill NÃO faz

- Não escreve critérios novos além dos implícitos: critério de aceite é do `/lapidar`.
- Não corrige sem `--corrigir`. Sem a flag, só reporta.
- Não faz revisão de qualidade subjetiva ("ficou bonito", "poderia ser melhor"). Confere o que foi pedido contra o que foi entregue.

## Referências

| Arquivo | Quando ler |
|---------|-----------|
| `references/checagens.md` | Na etapa 1, para os critérios implícitos e comandos por tipo de entrega |
| `references/exemplos.md` | Em dúvida sobre o que conta como evidência ou como escrever o veredito |
