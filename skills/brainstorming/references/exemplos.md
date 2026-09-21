# Exemplos

Dois exemplos de tamanhos diferentes. O primeiro é uma dúvida rápida; o segundo, uma decisão de produto.

---

## Exemplo 1: dúvida rápida

### Pedido

> /brainstorming não sei se aviso o cliente do atraso por e-mail ou ligo

### Etapa 1

- **Problema:** o cliente precisa saber do atraso e aprovar a nova data sem que a relação piore.
- **Solução que veio junto:** e-mail ou ligação (duas direções já dadas).
- **Por que agora:** a data original é semana que vem.

### Pergunta feita (uma só)

"Esse cliente já reclamou de atraso antes?" → "Sim, uma vez, e ficou chateado por saber tarde."

### Direções

### A. E-mail direto
**Em uma frase:** e-mail curto com a data nova na primeira linha.
**Como funciona:** assunto claro, 100 palavras, pedido de confirmação.
**A favor:** fica registrado; o cliente encaminha para o chefe sem editar.
**Contra:** ele já ficou chateado uma vez; texto frio pode reabrir isso.
**Esforço:** 15 minutos.
**Risco principal:** ele lê como descaso. Sinal: responde seco ou não responde.
**Vence quando:** a relação é operacional e o atraso é pequeno.

### B. Ligar, depois e-mail
**Em uma frase:** ligação de 5 minutos para avisar e ouvir, e-mail em seguida formalizando.
**Como funciona:** liga, explica, pergunta se a data nova serve; e-mail registra o combinado.
**A favor:** ele ouve o tom de voz; dá para ajustar a data na hora.
**Contra:** exige que ele esteja disponível hoje; 2 passos.
**Esforço:** 30 minutos.
**Risco principal:** ligação pega ele no pior momento. Sinal: não atende ou corta.
**Vence quando:** a relação já está sensível, como aqui.

### C. Não avisar ainda, entregar parcial
**Em uma frase:** entregar o que está pronto na data original e avisar do restante junto.
**Como funciona:** separa o que fecha até a data, entrega, e o aviso do atraso vem com algo na mão.
**A favor:** o cliente recebe algo; a conversa começa com entrega, não com pedido de desculpa.
**Contra:** só funciona se o parcial tem valor sozinho; adiar o aviso repete o erro de "saber tarde".
**Esforço:** depende do que dá para separar; meio dia para avaliar.
**Risco principal:** o parcial não serve e o aviso chega ainda mais tarde.
**Vence quando:** existe uma parte com valor próprio e o atraso do resto é curto.

### Recomendação
**B.** O cliente já disse que o problema foi saber tarde; ligar hoje ataca isso diretamente. **A** venceria se ele fosse difícil de alcançar por telefone. **C** só se houver parte pronta com valor real, o que não se sabe.

### Escolha do usuário: B

### Resumo final

```markdown
# Brainstorm: avisar cliente do atraso

## Problema
O cliente precisa saber do atraso e aprovar a nova data sem que a relação piore.

## Direção escolhida
Ligar, depois e-mail. Ligação de 5 minutos hoje para avisar e ouvir; e-mail em seguida registrando a data combinada.

## Decisões tomadas
- Avisar hoje, não esperar ter mais informação: o histórico é de reclamação por saber tarde.
- O e-mail vem depois da ligação e só formaliza; não é o primeiro contato.

## Alternativas descartadas
- **E-mail direto**: frio para um cliente que já se chateou uma vez.
- **Entregar parcial**: não se sabe se existe parte com valor próprio; adiaria o aviso.

## Riscos assumidos
- Ele não atender hoje. Sinal: duas tentativas sem retorno até 16h → mandar o e-mail (direção A) e registrar que tentou ligar.

## Perguntas em aberto
- Existe uma nova data firme? Se não, a ligação promete data até dia X.

## Próximo passo
/lapidar preparar roteiro de ligação de 5 minutos e e-mail de formalização para avisar o cliente do atraso, com a data nova na primeira frase
```

---

## Exemplo 2: decisão de produto

### Pedido

> /brainstorming quero colocar um chatbot no sistema pra responder as dúvidas dos analistas

### Etapa 1

- **Problema:** analistas param o trabalho para tirar dúvidas sobre o sistema, e quem responde é sempre a mesma pessoa.
- **Solução que veio junto:** chatbot.
- **Por que agora:** a pessoa que responde vai sair de férias.

### Perguntas feitas (três, uma por vez)

1. "Que tipo de dúvida é a mais comum?" → "Onde fica tal função e como interpretar tal campo. Quase nunca é bug."
2. "Quantas dúvidas por dia?" → "Umas 10, de 6 analistas."
3. "Existe documentação escrita?" → "Um Notion desatualizado que ninguém abre."

### Direções (resumidas; no uso real cada uma tem o formato completo)

- **A. Chatbot sobre a documentação** (a direção que veio junto). Exige documentação atualizada primeiro, senão responde errado. Esforço: 2 a 3 semanas contando a doc. Vence quando: o volume crescer e a doc já existir.
- **B. Atualizar o Notion e linkar de dentro do sistema** (mínima). Cada tela com um "?" que abre a página certa. Esforço: 3 dias. Vence quando: as dúvidas são de "onde fica" e "o que significa", como aqui.
- **C. Rodízio de quem responde + FAQ vivo** (muda o "quem"). Cada semana um analista responde e registra a dúvida e a resposta numa página. Esforço: 1 hora para combinar. Vence quando: o gargalo é uma pessoa só, não a falta de informação.
- **D. Tooltips e textos de ajuda dentro do sistema** (muda o "onde"). Ataca "como interpretar tal campo" no lugar onde a dúvida nasce. Esforço: 1 semana para os 20 campos mais perguntados. Vence quando: a dúvida se repete nos mesmos campos.

### Tabela

| | Esforço | Risco | Reversível | Resolve inteiro |
|---|---|---|---|---|
| A. Chatbot | 2-3 sem | Responde errado com doc ruim | Sim | Só com doc boa |
| B. Notion linkado | 3 dias | Ninguém abre, como hoje | Sim | Parcial |
| C. Rodízio + FAQ | 1 h | Depende de disciplina | Sim | Parcial |
| D. Tooltips | 1 sem | Não cobre "onde fica" | Sim | Parcial |

### Recomendação
**C agora, D em seguida.** C resolve as férias em uma hora e gera o FAQ que qualquer direção futura precisa. D ataca metade das dúvidas na origem. **A** venceria se houvesse 50 dúvidas por dia ou se a doc já estivesse boa; hoje o chatbot herdaria o Notion desatualizado.

### Escolha do usuário: C + D

### Próximo passo (última linha do resumo)

```
/lapidar montar rodízio semanal de quem responde dúvidas dos analistas com FAQ registrado, e em seguida adicionar textos de ajuda nos 20 campos mais perguntados do sistema
```

---

## O que os dois têm em comum

- O problema foi escrito sem a solução, e a solução que veio junto virou uma direção entre outras.
- Cada direção viraria uma task diferente.
- Sempre existe a mínima e a que muda o ângulo (quem, onde, quando).
- A recomendação diz quando outra venceria.
- Termina em `/lapidar`, não em execução.
