---
name: depurar
description: Investiga um bug ou comportamento errado até a causa raiz antes de corrigir. Congela o sintoma com evidência literal, reproduz de forma determinística, localiza por bissecção (no tempo, no caminho, nos dados), testa no máximo 3 hipóteses com previsão verificável, explica a causa em uma frase, e só então corrige pelo /tdd. Vale para código, número que não bate, processo que falha, script que dá resultado errado. Use quando o usuário invocar /depurar, disser "tá quebrando", "dá erro", "não funciona", "resultado errado", "por que isso acontece", "flaky", ou quando uma task do /lapidar for do tipo corrigir.
---

# Depurar

Nenhuma correção sem uma frase que explique **por que** o bug acontece. Mudar coisas até o sintoma sumir não é depurar, é esconder: o bug volta com outra cara.

Entrada: um sintoma (erro, valor errado, comportamento inesperado), de preferência a task do `/lapidar` tipo `corrigir`. Saída: causa raiz explicada, correção feita pelo `/tdd`, e um relatório com o que foi testado e descartado.

| Flag | Efeito |
|------|--------|
| (nenhuma) | Investiga até a causa raiz e corrige |
| `--so-causa` | Para na causa raiz, sem corrigir. Para quando a correção é decisão de outra pessoa ou de outra task |

## Princípio

Bug é uma diferença entre o que você acha que o código faz e o que ele faz. Depurar é encontrar **qual crença está errada**. Por isso a regra central é: uma mudança por vez, com uma previsão antes de cada mudança. Se mudou três coisas e passou, não sabe qual foi, e vai carregar duas mudanças inúteis para sempre.

## Fluxo

### 0. Congelar o sintoma

Antes de tocar em qualquer coisa, escrever:
- **O que acontece**, com a evidência literal: mensagem de erro inteira, stack trace, valor obtido vs esperado, log. Nunca resumir; colar.
- **Desde quando**, e o que mudou nesse intervalo: `git log` do período, deploy, dependência atualizada, dado novo, configuração.
- **Onde reproduz e onde não**: ambiente, usuário, input. A diferença entre os dois é a primeira pista.

Ler a mensagem de erro **inteira**, do início ao fim, literalmente. Metade dos bugs está escrita nela.

### 1. Reproduzir

Um comando ou sequência de passos que faz o bug aparecer **toda vez**. Sem isso, não dá para saber se uma correção funcionou.

- Intermitente? Rodar em loop até medir a taxa (`for i in $(seq 20)`); flaky é bug, não azar.
- Não reproduz? A task muda: agora é "obter reprodução", não "corrigir". Coletar mais evidência (logs, input real, ambiente) antes de qualquer hipótese.
- Reproduziu? Escrever o teste que reproduz, se for código. Ele vai falhar agora e passar no fim; é o teste de regressão do `/tdd`.

### 2. Localizar

Cortar o espaço pela metade, repetidamente, até a falha caber em uma tela:

- **No tempo:** `git bisect` entre o último commit bom e o primeiro ruim. Custa minutos e aponta o diff exato.
- **No caminho:** entrada → saída; verificar o estado no meio (log, assert, print com contexto). O bug está no lado onde o estado já está errado. Repetir naquele lado.
- **Nos dados:** reduzir o input ao menor que ainda reproduz. Um processo de 400 páginas vira uma página; um JSON de 2 MB vira 3 campos.

Técnicas e comandos por linguagem em `references/tecnicas.md`.

### 3. Hipóteses com previsão

No máximo 3, ordenadas da mais provável para a menos. Cada uma com:
- **Se for isso, então**: uma previsão observável que só é verdadeira se a hipótese for.
- **Como descartar**: o que rodar ou olhar, o mais barato primeiro.

Testar uma por vez. Registrar o resultado antes de passar para a próxima. Hipótese descartada é progresso: o espaço encolheu.

Três hipóteses descartadas? Parar. Listar o que "sei" que está certo e não conferi (o ambiente, o dado, a versão, a premissa de que o framework está certo). Uma dessas certezas está errada. Voltar ao passo 2 com ela.

### 4. Causa raiz

Uma frase: "acontece porque X, que faz Y, e Z não trata". Se tem "acho que", "provavelmente" ou "deve ser", ainda não é causa raiz; voltar ao 3.

Mais uma frase: **por que não foi pego antes**. Faltava teste? O caso não foi previsto? A validação deixou passar? Isso vira item do relatório e, quando cabe, um teste a mais.

### 5. Corrigir pelo `/tdd`

Teste de reprodução falhando (passo 1) → correção **mínima** que ataca a causa raiz → suíte inteira verde. Uma mudança. Correção que é `try/except`, `retry`, `sleep`, `if not None` ou "roda de novo" sem a causa raiz por trás é sintoma escondido, não correção.

Desfazer tudo que foi tentado e não ajudou (prints, mudanças experimentais). O diff final tem só a correção e o teste.

### 6. Fechar

- Rodar o cenário **original** do sintoma (não só o teste) e confirmar que sumiu.
- Procurar **irmãos**: o mesmo padrão em outros lugares do código (`grep` pelo padrão da causa). Corrigir junto se é o mesmo bug; registrar se é outra task.
- Relatório no formato abaixo. Entregar para o `/conferir`.

## Formato do relatório

````markdown
## Depuração: <sintoma em poucas palavras>

**Sintoma:** <evidência literal, resumida em uma linha, com a citação>
**Reprodução:** `<comando>` → <o que aparece>
**Localizado em:** <arquivo:função ou etapa>, por <bissecção no tempo/caminho/dados>

| Hipótese | Se for isso, então | Resultado |
|----------|--------------------|-----------|
| 1. <…> | <previsão> | descartada: <o que se viu> |
| 2. <…> | <previsão> | confirmada: <o que se viu> |

**Causa raiz:** <uma frase, sem "acho">
**Por que não foi pego antes:** <uma frase>
**Correção:** <o que mudou, em uma linha> · teste de regressão `<caminho::nome>` · suíte `<comando>` → <resultado>
**Irmãos:** <onde o mesmo padrão aparece, ou "nenhum encontrado">
````

## Sinais de que está chutando

| Pensamento | Realidade |
|-----------|-----------|
| "Vou mudar X e ver o que acontece" | Sem previsão, não é experimento. Escrever "se X for a causa, então Y" antes. |
| "Coloco um try/except e segue" | Sintoma escondido. O erro vai aparecer em outro lugar, sem stack trace. |
| "Deve ser cache / rede / o framework" | O framework raramente está errado. Provar antes de culpar. |
| "Roda de novo que passa" | Flaky é bug com taxa. Medir a taxa e reproduzir. |
| "Mudei três coisas e passou" | Qual delas? Desfazer duas e descobrir. |
| "Não reproduz, mas sei o que é" | Sem reprodução, não sabe se corrigiu. Reproduzir primeiro. |
| "É um caso raro, ignora" | Raro em teste é frequente em produção. |
| "Já gastei 2 horas, vou corrigir o sintoma" | 2 horas sem causa raiz = uma crença errada não examinada. Listar as certezas. |

## O que esta skill NÃO faz

- Não corrige sem causa raiz: correção é o passo 5, nunca o 1.
- Não escreve a task: sintoma vago vira `/lapidar` tipo `corrigir` antes.
- Não substitui o `/tdd` na correção nem o `/conferir` no fechamento.

## Referências

| Arquivo | Quando ler |
|---------|-----------|
| `references/tecnicas.md` | No passo 2, para bissecção, redução de input, logging e depuradores por linguagem |
| `references/exemplos.md` | Em dúvida sobre como escrever hipóteses com previsão ou o relatório |
