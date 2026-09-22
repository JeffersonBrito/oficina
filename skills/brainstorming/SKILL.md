---
name: brainstorming
description: Explora um problema antes de decidir a solução, devolve 3 a 5 direções diferentes com prós, contras e risco, e recomenda uma; a escolha vira entrada do /lapidar. Use quando invocarem /brainstorming, disserem "vamos pensar em", "quais opções", "não sei se A ou B", ou trouxerem uma ideia ainda vaga.
---

# Brainstorming

Problema ou ideia crua entra; saem direções diferentes de verdade, uma recomendação, e a escolha do usuário pronta para o `/lapidar`. Pedido em `$ARGUMENTS` ou na mensagem. Flags: `--salvar` grava o resumo em `.claude/brainstorms/AAAA-MM-DD-<slug>.md` (ou `~/.claude/brainstorms/`); `--lapidar` chama o `/lapidar` logo após a escolha.

Regra central: separar o problema da solução que veio junto, e olhar pelo menos três caminhos antes de escolher. Tamanho proporcional: dúvida de 5 minutos são 3 direções em 20 linhas; decisão de produto, 5 direções com tabela.

## Fluxo

1. **Separar problema de solução.** Uma frase cada: o **problema** (o que dói, sem dizer como), a **solução que veio junto** (vira uma direção, nunca a única), e **por que agora**. Se o problema não sai sem a solução, falta a pergunta do passo 3.
2. **Aterrar** (até uns 2 minutos): conversa, arquivos, memória, repositório se envolver código, o que já foi tentado. Anotar restrições reais: prazo, orçamento, o que não muda, quem decide.
3. **Perguntar, uma por vez, no máximo 5**, só se a resposta elimina uma direção; senão assumir e registrar. Preferir opções (AskUserQuestion). Ordem que funciona: para quem → o que é "resolvido" → o que não pode mudar → tempo e dinheiro → o que já foi tentado. Banco em `references/perguntas.md`. Parar assim que der para propor direções. Sessão autônoma: assumir e registrar.
4. **Divergir em 3 a 5 direções** materialmente diferentes. Teste: virariam tasks diferentes no `/lapidar`? Sempre incluir a **óbvia**, a **mínima** (menor esforço que resolve hoje, ou "não fazer nada") e uma que **muda o ângulo** (quem, quando ou onde, em vez do como). Prós e contras são fatos, não adjetivos: "exige Redis, que o projeto não tem". Com 4 ou mais, tabela direções × (esforço, risco, reversível, resolve inteiro) antes da recomendação.
5. **Convergir.** Uma recomendação, o motivo em uma frase, e a condição em que outra venceria. Depois a única pergunta que trava: qual direção (AskUserQuestion com as direções). Mistura de duas vira uma direção combinada, escrita antes de seguir.
6. **Entregar** o resumo abaixo em bloco ```markdown; a última linha é o comando `/lapidar` pronto. Sem flag, parar aí. Com `--lapidar`, invocar `lapidar` com essa linha.

## Formato de cada direção

````markdown
### <Letra>. <Nome curto>
**Em uma frase:** <o que é>
**Como funciona:** <2 a 4 linhas>
**A favor:** <fatos>
**Contra:** <fatos>
**Esforço:** <horas, dias ou semanas, e o que consome>
**Risco principal:** <o que pode dar errado e o sinal de que deu>
**Vence quando:** <a condição em que esta é a melhor>
````

## Formato do resumo final

````markdown
# Brainstorm: <tema>

## Problema
<uma frase, sem solução embutida>

## Direção escolhida
<nome, "em uma frase" e como funciona>

## Decisões tomadas
- <respostas do usuário e premissas que fecham uma porta>

## Alternativas descartadas
- **<Nome>**: <motivo em uma linha>

## Riscos assumidos
- <risco e o sinal de que se materializou>

## Perguntas em aberto
- <o que não travou a escolha>

## Próximo passo
/lapidar <pedido de uma linha com a direção e as decisões acima>
````

## Checklist

- [ ] Problema escrito sem solução dentro.
- [ ] 3 a 5 direções que virariam tasks diferentes; há a mínima e a que muda o ângulo.
- [ ] Todo "a favor" e "contra" é fato verificável.
- [ ] Recomendação diz quando outra venceria.
- [ ] Nenhuma pergunta feita cuja resposta não eliminaria uma direção.

## Sinais de desvio

| Pensamento | Realidade |
|-----------|-----------|
| "O usuário já disse o que quer" | Disse a solução. Escrever o problema; a dele é a direção A. |
| "Só existe um jeito" | Achar o mínimo e o que muda o ângulo. Sempre existem. |
| "Pergunto tudo de uma vez" | A primeira resposta mata metade das perguntas. Uma por vez. |
| "Já sei, vou direto à recomendação" | Sem direções é opinião. Três, depois recomendar. |

## Não faz

Não escreve a task (`/lapidar`), não executa, não decide pelo usuário. Se decidir exige levantar dados, a recomendação pode ser "investigar X primeiro", e isso vira o `/lapidar`.

## Referências

| Arquivo | Quando ler |
|---------|-----------|
| `references/perguntas.md` | No passo 3, para a pergunta que mais elimina direções |
| `references/exemplos.md` | Só em dúvida sobre o que é "materialmente diferente" |
