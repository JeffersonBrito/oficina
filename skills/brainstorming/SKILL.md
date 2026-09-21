---
name: brainstorming
description: Explora um problema antes de decidir a solução. Pega uma ideia ou pedido ("quero um app de X", "como resolvo Y", "estou pensando em fazer Z") e devolve 3 a 5 direções materialmente diferentes, com prós, contras, custo e risco, mais uma recomendação; a direção escolhida vira entrada do /lapidar. Vale para qualquer domínio: produto, código, texto, carreira, processo. Use quando o usuário invocar /brainstorming, disser "vamos pensar em", "quais opções eu tenho", "não sei se faço A ou B", "me ajuda a decidir como", ou trouxer uma ideia ainda vaga antes de pedir execução.
---

# Brainstorming

Pega um problema ou uma ideia ainda crua e devolve direções diferentes de verdade, com uma recomendação. Termina quando o usuário escolhe uma direção, e essa escolha sai pronta para virar task no `/lapidar`.

O pedido vem em `$ARGUMENTS` ou na mensagem do usuário. Flags opcionais no final:

| Flag | Efeito |
|------|--------|
| (nenhuma) | Conduz o brainstorm e entrega o resumo da direção escolhida |
| `--salvar` | Também grava o resumo em `.claude/brainstorms/AAAA-MM-DD-<slug>.md` (ou `~/.claude/brainstorms/` fora de um projeto) |
| `--lapidar` | Depois da escolha, chama `/lapidar` com a direção escolhida, sem parar |

## Princípio

A primeira solução que aparece raramente é a melhor, mas é a que vira código, texto ou e-mail se ninguém parar para olhar as outras. Esta skill obriga a **separar o problema da solução que já veio junto**, e a olhar pelo menos três caminhos diferentes antes de escolher. O tamanho é proporcional: dúvida de 5 minutos vira 3 direções em 20 linhas; decisão de produto vira 5 direções com tabela.

## Fluxo

### 1. Separar problema de solução

O pedido do usuário quase sempre já traz uma solução embutida ("quero um dashboard" é solução; o problema é "não sei o que está acontecendo com X"). Escrever em uma frase cada um:

- **Problema**: o que dói ou o que se quer alcançar, sem dizer como.
- **Solução que veio junto**: o que o usuário já imaginou, se imaginou. Ela entra como uma das direções, nunca como a única.
- **Por que agora**: o que mudou para isso virar pauta.

Se não dá para escrever o problema sem a solução, é sinal de que falta a pergunta da etapa 3.

### 2. Aterrar no que existe (curto, no máximo uns 2 minutos)

Conversa atual, arquivos mencionados, memória do usuário, repositório se envolver código, e o que já foi tentado antes para o mesmo problema. Registrar restrições reais: prazo, orçamento, o que não pode mudar, quem decide.

### 3. Perguntar, uma de cada vez

Só perguntas que **mudam a direção**. Se a resposta não eliminaria nenhuma direção, não perguntar; assumir e registrar. No máximo 5 perguntas no brainstorm inteiro, **uma por vez**, de preferência com opções (AskUserQuestion). Uma pergunta de cada vez porque a resposta da primeira normalmente elimina a segunda.

Ordem que costuma funcionar: para quem é → o que "resolvido" significa → o que não pode mudar → quanto tempo/dinheiro há → o que já foi tentado. Banco de perguntas por tipo de problema em `references/perguntas.md`.

Parar de perguntar assim que der para propor direções. Em sessão autônoma, assumir a leitura mais provável e registrar.

### 4. Divergir: 3 a 5 direções

Cada direção precisa ser **materialmente diferente**. Teste: se cada uma virasse uma task no `/lapidar`, as tasks seriam diferentes? Se duas dariam a mesma task com um parâmetro diferente, são uma direção só.

Sempre incluir:
- **A direção óbvia** (a que o usuário trouxe ou a primeira que vem à cabeça).
- **A direção mínima**: o menor esforço que resolve o problema hoje, mesmo que feio. Inclui "não fazer nada" quando fizer sentido.
- **Pelo menos uma direção que ataca o problema por outro ângulo**: muda o "quem", o "quando" ou o "onde" em vez do "como".

Para cada direção, o formato da seção "Formato das direções". Prós e contras são fatos, não adjetivos: "exige Redis, que o projeto não tem" e não "mais complexo".

### 5. Convergir: recomendar e pedir a escolha

Uma recomendação só, com o motivo em uma frase e **a condição em que outra direção venceria**. Depois, a única pergunta que trava: "qual direção?" (AskUserQuestion com as direções como opções). O usuário pode misturar duas; nesse caso, escrever a direção combinada antes de seguir.

### 6. Entregar

O resumo da direção escolhida no formato fixo abaixo, em um bloco ```markdown. A última linha do bloco é o comando `/lapidar` pronto. Sem flag, parar aí. Com `--lapidar`, invocar a skill `lapidar` em seguida com a linha do "Próximo passo" como pedido.

## Formato das direções

````markdown
### <Letra>. <Nome curto da direção>
**Em uma frase:** <o que é>
**Como funciona:** <2 a 4 linhas, o suficiente para alguém imaginar o resultado>
**A favor:** <fatos>
**Contra:** <fatos>
**Esforço:** <horas, dias ou semanas, e o que consome>
**Risco principal:** <o que pode dar errado e o sinal de que deu>
**Vence quando:** <a condição em que esta é a melhor escolha>
````

Com 4 ou mais direções, acrescentar uma tabela direções × (esforço, risco, reversível?, resolve o problema inteiro?) antes da recomendação.

## Formato do resumo final

````markdown
# Brainstorm: <tema em poucas palavras>

## Problema
<uma frase, sem solução embutida>

## Direção escolhida
<nome + "em uma frase" + como funciona, copiados da direção>

## Decisões tomadas
- <cada resposta do usuário e cada premissa assumida que fecha uma porta>

## Alternativas descartadas
- **<Nome>**: <motivo em uma linha>

## Riscos assumidos
- <risco da direção escolhida e o sinal de que ele se materializou>

## Perguntas em aberto
- <o que ainda não se sabe e não travou a escolha>

## Próximo passo
/lapidar <pedido de uma linha que descreve a direção escolhida com as decisões acima>
````

## Checklist de qualidade

Antes de entregar as direções, conferir. Um "não" = voltar e corrigir.

- [ ] O **Problema** está escrito sem nenhuma solução dentro.
- [ ] Há pelo menos 3 direções e no máximo 5.
- [ ] As direções passam no teste: virariam tasks diferentes no `/lapidar`.
- [ ] Existe a direção mínima (ou "não fazer nada") e uma que muda o ângulo.
- [ ] Todo "A favor" e "Contra" é um fato verificável, não um adjetivo.
- [ ] A recomendação diz em que condição outra direção venceria.
- [ ] Nenhuma pergunta foi feita cuja resposta não eliminaria uma direção.
- [ ] O tamanho é proporcional à decisão.

## Sinais de que está saindo do trilho

| Pensamento | O que fazer |
|-----------|-------------|
| "O usuário já disse o que quer, é só fazer" | Ele disse a solução. Escrever o problema antes; a solução dele é a direção A. |
| "Só existe um jeito de fazer isso" | Achar o jeito mínimo e o jeito que muda o ângulo. Sempre existem. |
| "Vou perguntar tudo de uma vez para ganhar tempo" | Uma por vez. A primeira resposta mata metade das outras perguntas. |
| "Essa direção é claramente pior, nem vou listar" | Listar com o contra em fato. Direção descartada com motivo tem valor; omitida não. |
| "Já sei a resposta, vou direto para a recomendação" | Recomendar sem direções é opinião. Três direções, depois a recomendação. |
| "Vou já escrever a task / o código / o texto" | Não é papel desta skill. O resumo termina em `/lapidar`. |

## O que esta skill NÃO faz

- Não escreve a task final: isso é `/lapidar`.
- Não executa nada: nem código, nem texto, nem e-mail.
- Não decide pelo usuário: recomenda e pergunta.
- Não faz pesquisa longa: se decidir exige levantar dados, a direção recomendada pode ser "investigar X primeiro", e isso vira o `/lapidar`.

## Referências

| Arquivo | Quando ler |
|---------|-----------|
| `references/perguntas.md` | Na etapa 3, para escolher a pergunta que mais elimina direções |
| `references/exemplos.md` | Em dúvida sobre o nível de detalhe ou sobre o que é "materialmente diferente" |
