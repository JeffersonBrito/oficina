---
name: tdd
description: Implementa código com Test-Driven Development de verdade: lista de testes derivada dos critérios de aceite, ciclo RED (ver falhar pelo motivo certo) → GREEN (mínimo) → REFACTOR, fatias verticais ponta a ponta, testes honestos que falham quando o comportamento quebra. Código escrito antes do teste é apagado. Use ao implementar qualquer feature, correção de bug ou mudança de comportamento; ao executar uma task do /lapidar que envolve código; quando o usuário invocar /tdd, disser "faz com TDD", "teste primeiro", "escreve os testes antes", ou pedir para corrigir um bug (reproduzir com teste antes de corrigir).
---

# TDD

Nenhum código de produção sem um teste que falhou antes. Se você não viu o teste falhar, não sabe se ele testa alguma coisa.

Entrada: uma task do `/lapidar` (os critérios de aceite viram a lista de testes) ou um pedido direto (`/tdd <o que implementar>`). Saída: código, testes, e um relatório critério a critério.

## Princípio

Três regras que não se negociam:

1. **Teste antes, sempre.** Escreveu código de produção antes do teste? Apaga e recomeça. Não guarda "de referência": você vai adaptar, e adaptar é testar depois.
2. **Fatia vertical, não camada.** Cada ciclo entrega um comportamento inteiro, do ponto de entrada até o resultado observável. Nunca "todos os models, depois todos os services, depois o controller".
3. **Teste honesto.** Um teste só vale se falha quando o comportamento quebra. Teste que passa com a implementação errada não é teste, é enfeite.

Exceções, só com aval explícito do usuário: protótipo descartável, código gerado, arquivo de configuração.

## Fluxo

### 0. Preparar (antes de qualquer teste)

- Descobrir o **comando exato** que roda um teste só e o que roda a suíte inteira. Anotar os dois. Se não souber, `references/stacks.md` tem os de pytest, Jest e Vitest.
- Olhar dois testes existentes do projeto e seguir o padrão deles: pasta, nome, fixtures, estilo de asserção.
- Rodar a suíte inteira uma vez. Se já está vermelha, parar e reportar antes de começar: TDD sobre suíte quebrada não prova nada.
- Sem suíte nenhuma? Criar a mínima (um teste trivial que roda) e seguir.

### 1. Lista de testes

Antes de escrever o primeiro teste, escrever a lista inteira em texto, um comportamento por linha. Fonte: os critérios de aceite da task; sem task, os requisitos do pedido mais as bordas que o pedido não citou (vazio, nulo, duplicado, sem permissão, limite).

Ordenar por **fatia vertical**: primeiro o caminho feliz mais fino que atravessa tudo (entrada → resultado), depois as bordas, depois os erros. Cada linha vai virar exatamente um teste. Mostrar a lista ao usuário e só então começar.

### 2. Ciclo, um item por vez

**RED**
- Escrever **um** teste para o próximo item. Nome descreve o comportamento: `retorna_409_quando_email_ja_existe`, não `test_register_2`.
- Rodar só esse teste. **Confirmar que falhou pelo motivo certo**: uma asserção que não bateu, ou um erro de "função não existe". Erro de sintaxe, import errado ou fixture faltando não é RED, é teste quebrado; consertar o teste e rodar de novo.
- Colar a linha da falha no raciocínio. Se não consegue dizer por que falhou, não avançar.
- **Teste passou de primeira?** Suspeito. Ou o comportamento já existia (então o item sai da lista) ou o teste não testa nada (reescrever). Nunca seguir sem saber qual dos dois.

**GREEN**
- Escrever o **mínimo** que faz esse teste passar. Nada para o próximo item, nada "já que estou aqui". Hard-code é aceitável neste passo se o próximo teste vai forçar a generalização.
- Rodar o teste; depois rodar a suíte inteira. Tudo verde antes de seguir.

**REFACTOR**
- Só com a suíte verde. Limpar duplicação, nome ruim, estrutura, no código de produção e nos testes. Sem mudar comportamento, sem adicionar comportamento.
- Rodar a suíte de novo. Verde? Próximo item. Vermelho? Desfazer o refactor, não "consertar" adicionando código.

Código de produção e de teste seguem clean code: nomes que dispensam comentário; comentário só para um porquê que o código não diz. Commit por fatia, se o projeto usa commits pequenos e o usuário pediu commits: uma frase curta em inglês, capitalizada, sem prefixo, sem rodapé de atribuição.

### 3. Fechar

- Toda linha da lista tem um teste que **você viu falhar e depois passar**.
- Suíte inteira verde, com o comando exato que rodou.
- Relatório no formato abaixo.

## Testes honestos

Antes de dar um item por concluído, uma pergunta: **se eu quebrar a implementação de propósito, este teste falha?** Se a resposta é "não sei", quebrar e ver. Sinais de teste desonesto:

| Sinal | Por que é desonesto | Troca por |
|------|---------------------|-----------|
| `assert result` / `toBeTruthy()` | Passa com qualquer coisa não vazia | Asserção do valor exato |
| Asserção sobre o mock (`mock.called`) | Testa que você chamou o mock, não o comportamento | Asserção sobre o resultado observável |
| Snapshot sem ler o snapshot | Congela o que saiu, certo ou errado | Asserção explícita do que importa |
| Teste que replica a implementação | Muda o código, muda o teste, nunca falha de verdade | Testar pela interface pública |
| `try/except` engolindo no teste | Esconde a falha | Deixar o erro subir; usar `raises`/`toThrow` quando o erro é o esperado |
| Um teste com "e" no nome | Duas coisas; quando falha, não se sabe qual | Dois testes |

Regra de mock: mocka-se o que está **fora** do que se testa (rede, relógio, banco externo, serviço pago). Nunca o que está sendo testado. Precisou mockar tudo para testar? O código está acoplado demais; injetar a dependência é o refactor.

## Bug é teste primeiro

Bug reportado → primeiro passo é um teste que reproduz o bug e **falha**. Só então corrigir. O teste fica como regressão. Correção sem teste de reprodução não é aceita nesta skill. Sem conseguir reproduzir? Isso é a task, não a correção: voltar ao `/lapidar` com tipo `corrigir`.

## Racionalizações

Cada uma destas já apareceu na sua cabeça. Resposta pronta:

| Pensamento | Realidade |
|-----------|-----------|
| "É simples demais para testar" | Simples quebra. O teste leva 30 segundos. |
| "Escrevo os testes depois" | Teste que passa de primeira não prova nada. Depois = "o que isso faz?"; antes = "o que isso deve fazer?". |
| "Já testei na mão" | Sem registro, sem repetição. Na próxima mudança testa tudo de novo na mão. |
| "Vou guardar o código como referência" | Vai adaptar. Adaptar é testar depois. Apagar é apagar. |
| "Já gastei horas nisso, apagar é desperdício" | As horas já foram. Código sem teste que falhou é dívida, não ativo. |
| "Preciso explorar antes" | Pode. Exploração se joga fora; depois começa pelo teste. |
| "É difícil de testar" | Difícil de testar é difícil de usar. O teste está apontando um problema de design. |
| "TDD vai me atrasar" | Mais lento que debugar em produção? Não. |
| "Esse caso é diferente porque..." | Não é. |

## Quando travar

| Problema | O que fazer |
|---------|-------------|
| Não sei como testar isso | Escrever a asserção primeiro, com a API que você gostaria que existisse. Depois o resto do teste. |
| O teste ficou enorme | O design está grande. Simplificar a interface antes de simplificar o teste. |
| Preciso mockar 5 coisas | Acoplamento. Injetar dependências; testar a unidade menor. |
| O setup se repete em todo teste | Fixture ou helper. Se continua grande, o design ainda está grande. |
| Não sei o próximo item | Voltar à lista. Se a lista acabou, acabou. |

## Formato do relatório final

````markdown
## TDD: <o que foi implementado>

| Critério / comportamento | Teste | RED visto | GREEN |
|--------------------------|-------|-----------|-------|
| <critério de aceite> | `tests/x_test.py::nome` | sim: <motivo da falha> | sim |

**Suíte inteira:** `<comando>` → <N passed>
**Fora da lista:** <comportamentos que apareceram e não foram implementados, com motivo>
**Design que o teste apontou:** <mudanças de interface feitas porque o teste ficou difícil, se houve>
````

## O que esta skill NÃO faz

- Não escreve a task nem os critérios de aceite: isso é `/lapidar`. Sem critérios, ela os deriva do pedido e mostra a lista antes de começar.
- Não "adiciona cobertura" a código pronto. Isso é outra atividade, e a skill diz isso em vez de fingir que é TDD.
- Não decide se TDD se aplica. Aplica-se. Exceção é decisão do usuário, não da skill.

## Referências

| Arquivo | Quando ler |
|---------|-----------|
| `references/stacks.md` | Na etapa 0, para os comandos e o padrão de pytest, Jest e Vitest |
| `references/antipadroes.md` | Ao criar um mock, fixture ou helper de teste; ou quando um teste "passa mas não confia" |
