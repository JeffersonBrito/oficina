---
name: tdd
description: Implementa código com teste primeiro: lista de testes dos critérios de aceite, RED visto pelo motivo certo, GREEN mínimo, REFACTOR, fatias verticais, testes honestos. Use ao implementar qualquer feature, correção ou mudança de comportamento, ao executar task do /lapidar com código, ou quando invocarem /tdd ou pedirem "teste primeiro".
---

# TDD

Nenhum código de produção sem um teste que falhou antes. Entrada: task do `/lapidar` (critérios de aceite viram a lista de testes) ou pedido direto. Saída: código, testes e relatório critério a critério.

Três regras que não se negociam:

1. **Teste antes.** Código de produção escrito antes do teste é apagado, não guardado "de referência".
2. **Fatia vertical, não camada.** Cada ciclo entrega um comportamento inteiro, da entrada ao resultado observável.
3. **Teste honesto.** Só vale se falha quando o comportamento quebra.

Exceções só com aval explícito do usuário: protótipo descartável, código gerado, configuração.

## Fluxo

0. **Preparar.** Descobrir o comando que roda um teste só e o que roda a suíte (`references/stacks/<stack>.md` se não souber). Ler dois testes existentes e seguir o padrão. Rodar a suíte: se já está vermelha, parar e reportar. Sem suíte, criar a mínima.
1. **Lista de testes**, em texto, um comportamento por linha, antes do primeiro teste. Fonte: critérios de aceite; sem task, os requisitos mais as bordas (vazio, nulo, duplicado, sem permissão, limite). Ordem: caminho feliz mais fino ponta a ponta, depois bordas, depois erros. Mostrar a lista e só então começar.
2. **Ciclo, um item por vez.**
   - **RED:** um teste, nome que descreve o comportamento (`retorna_409_quando_email_ja_existe`). Rodar só ele e confirmar que falhou **pelo motivo certo**: asserção que não bateu ou função que não existe. Erro de sintaxe, import ou fixture é teste quebrado, não RED. Colar a linha da falha. Passou de primeira? Suspeito: ou o comportamento já existia (item sai da lista) ou o teste não testa nada (reescrever).
   - **GREEN:** o mínimo que passa esse teste; nada para o próximo item. Hard-code vale se o próximo teste força a generalização. Rodar o teste e a suíte inteira.
   - **REFACTOR:** só com suíte verde; sem mudar ou adicionar comportamento; rodar de novo. Vermelho? Desfazer, não "consertar" adicionando código.
   
   Código e teste em clean code: nomes que dispensam comentário. Commit por fatia se o usuário pediu commits: frase curta em inglês, capitalizada, sem prefixo, sem atribuição.
3. **Fechar.** Toda linha da lista tem teste visto falhar e depois passar; suíte inteira verde com o comando exato; relatório abaixo.

## Testes honestos

Antes de fechar um item: **se eu quebrar a implementação de propósito, este teste falha?** Na dúvida, quebrar e ver.

| Sinal de teste desonesto | Troca por |
|--------------------------|-----------|
| `assert result` / `toBeTruthy()` | asserção do valor exato |
| asserção sobre o mock (`mock.called`) | asserção sobre o resultado observável |
| snapshot sem ler | asserção explícita do que importa |
| teste que replica a implementação | testar pela interface pública |
| `try/except` engolindo no teste | deixar subir; `raises`/`toThrow` quando o erro é o esperado |
| "e" no nome do teste | dois testes |

Mock só do que está **fora** do que se testa (rede, relógio, banco externo, serviço pago). Precisou mockar tudo? Acoplamento; injetar a dependência é o refactor.

**Bug** começa por um teste que reproduz e falha. Sem reprodução, isso é a task (`/lapidar` tipo `corrigir`), não a correção.

## Racionalizações

| Pensamento | Realidade |
|-----------|-----------|
| "Simples demais para testar" | Simples quebra. 30 segundos. |
| "Testo depois" | Passa de primeira, não prova nada. Depois é "o que faz?"; antes é "o que deve fazer?". |
| "Guardo o código de referência" | Vai adaptar; adaptar é testar depois. Apagar. |
| "Já gastei horas, apagar é desperdício" | As horas já foram. Código sem teste que falhou é dívida. |
| "É difícil de testar" | Difícil de testar é difícil de usar. O teste aponta o design. |
| "Esse caso é diferente" | Não é. |

## Quando travar

| Problema | Fazer |
|---------|-------|
| Não sei como testar | Escrever a asserção primeiro, com a API que gostaria que existisse. |
| Teste enorme ou 5 mocks | Design grande ou acoplado. Simplificar interface, injetar dependências. |
| Setup repetido | Fixture ou helper; se continua grande, o design ainda está grande. |

## Relatório final

````markdown
## TDD: <o que foi implementado>

| Critério / comportamento | Teste | RED visto | GREEN |
|--------------------------|-------|-----------|-------|
| <critério> | `tests/x_test.py::nome` | sim: <motivo da falha> | sim |

**Suíte inteira:** `<comando>` → <N passed>
**Fora da lista:** <comportamentos que apareceram e não entraram, com motivo>
**Design que o teste apontou:** <mudanças de interface, se houve>
````

## Não faz

Não escreve critérios de aceite (`/lapidar`); sem eles, deriva a lista do pedido e mostra antes. Não "adiciona cobertura" a código pronto. Não decide se TDD se aplica: aplica-se, exceção é do usuário.

## Referências

| Arquivo | Quando ler |
|---------|-----------|
| `references/stacks/<pytest\|jest\|vitest>.md` | Na etapa 0, só a stack do projeto |
| `references/antipadroes.md` | Ao criar mock, fixture ou helper |
