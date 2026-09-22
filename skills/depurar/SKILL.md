---
name: depurar
description: Investiga um bug até a causa raiz antes de corrigir: sintoma literal, reprodução, bissecção, até 3 hipóteses com previsão, causa em uma frase, correção pelo /tdd. Use quando invocarem /depurar, disserem "dá erro", "tá quebrando", "valor errado", "flaky", ou em task do /lapidar tipo corrigir.
---

# Depurar

Nenhuma correção sem uma frase que explique **por que** o bug acontece. Mudar coisas até o sintoma sumir é esconder, não depurar. Entrada: um sintoma, de preferência a task `corrigir` do `/lapidar`. Saída: causa raiz, correção pelo `/tdd`, relatório. Flag `--so-causa`: parar na causa raiz, sem corrigir.

Regra central: bug é uma crença errada sobre o que o código faz. Uma mudança por vez, com previsão antes. Mudou três coisas e passou? Não sabe qual foi.

## Fluxo

0. **Congelar o sintoma.** Evidência literal colada, nunca resumida: erro inteiro, stack trace, valor obtido vs esperado. Desde quando e o que mudou (`git log`, deploy, dependência, dado). Onde reproduz e onde não: a diferença é a primeira pista. Ler a mensagem de erro inteira; metade dos bugs está nela.
1. **Reproduzir** toda vez, com um comando ou passos. Intermitente: rodar em loop e medir a taxa; flaky é bug. Não reproduz: a task vira "obter reprodução", sem hipótese antes. Reproduziu e é código: escrever o teste que reproduz; ele é a regressão do `/tdd`.
2. **Localizar** cortando o espaço pela metade: no **tempo** (`git bisect`), no **caminho** (estado no meio: certo → bug adiante, errado → atrás), nos **dados** (menor input que ainda reproduz). Técnicas em `references/tecnicas.md`.
3. **Hipóteses**, no máximo 3, da mais provável para a menos, cada uma com "**se for isso, então** <previsão observável>" e como descartar, o mais barato primeiro. Uma por vez; registrar o resultado. Três descartadas: parar e listar as certezas não conferidas (ambiente, dado, versão, "o framework está certo"); uma está errada. Voltar ao 2 com ela.
4. **Causa raiz** em uma frase: "acontece porque X, que faz Y, e Z não trata". Com "acho", "provavelmente" ou "deve ser", voltar ao 3. Mais uma frase: **por que não foi pego antes** (faltava teste? caso não previsto?).
5. **Corrigir pelo `/tdd`**: teste de reprodução falhando → correção mínima na causa → suíte verde. `try/except`, `retry`, `sleep`, `if not None` sem causa por trás é sintoma escondido. Desfazer prints e tentativas: o diff final tem só correção e teste.
6. **Fechar.** Rodar o cenário original, não só o teste. Procurar **irmãos** (`grep` pelo padrão da causa): corrigir junto se é o mesmo bug, registrar se é outra task. Relatório abaixo, entregue ao `/conferir`.

## Relatório

````markdown
## Depuração: <sintoma>

**Sintoma:** <evidência literal em uma linha>
**Reprodução:** `<comando>` → <o que aparece>
**Localizado em:** <arquivo:função ou etapa>, por <bissecção no tempo/caminho/dados>

| Hipótese | Se for isso, então | Resultado |
|----------|--------------------|-----------|
| 1. <…> | <previsão> | descartada: <o que se viu> |
| 2. <…> | <previsão> | confirmada: <o que se viu> |

**Causa raiz:** <uma frase>
**Por que não foi pego antes:** <uma frase>
**Correção:** <o que mudou> · regressão `<caminho::nome>` · suíte `<comando>` → <resultado>
**Irmãos:** <onde o padrão aparece, ou "nenhum">
````

## Sinais de chute

| Pensamento | Realidade |
|-----------|-----------|
| "Vou mudar X e ver" | Sem previsão não é experimento. |
| "Coloco um try/except e segue" | O erro reaparece em outro lugar, sem stack trace. |
| "Deve ser cache / rede / o framework" | O framework raramente está errado. Provar. |
| "Roda de novo que passa" | Flaky é bug com taxa. |
| "Já gastei 2 horas, corrijo o sintoma" | Uma crença não examinada. Listar as certezas. |

## Não faz

Não corrige sem causa raiz. Não escreve a task (`/lapidar corrigir`). Não substitui `/tdd` na correção nem `/conferir` no fechamento.

## Referências

| Arquivo | Quando ler |
|---------|-----------|
| `references/tecnicas.md` | No passo 2 |
| `references/exemplos.md` | Só em dúvida sobre hipóteses com previsão |
