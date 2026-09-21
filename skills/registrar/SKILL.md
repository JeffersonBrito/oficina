---
name: registrar
description: No fim de uma task, grava o que foi não-óbvio para não ser redescoberto: decisão tomada e por quê, armadilha encontrada, convenção do projeto, premissa que se revelou errada. Vai para a memória (fatos sobre o usuário e seus projetos) ou para o CLAUDE.md e docs do repositório (o que qualquer sessão naquele projeto precisa saber). Use quando o usuário invocar /registrar, disser "anota isso", "lembra disso", "guarda para a próxima", ou ao fechar uma task do /lapidar, do /depurar ou do /tdd que revelou algo que o código e o git não contam.
---

# Registrar

O que custou caro para descobrir não pode custar de novo. Esta skill pega o que ficou de não-óbvio no fim de uma task e grava no lugar onde a próxima sessão vai encontrar.

Entrada: a task recém-fechada e o que aconteceu nela. Saída: zero, um ou poucos registros, cada um em um lugar só.

| Flag | Efeito |
|------|--------|
| (nenhuma) | Decide o destino de cada item |
| `--memoria` | Só a memória do usuário |
| `--projeto` | Só `CLAUDE.md` e `docs/` do repositório |

## Princípio

Registrar demais é tão ruim quanto registrar de menos: `CLAUDE.md` de 300 linhas não é lido, memória com 80 fatos não é lembrada. O teste para cada item: **daqui a três meses, sem esta conversa, isso evita um erro ou uma pergunta?** Se não, não registra.

Não registrar o que o código, o git ou a doc já contam. "O endpoint fica em `auth.controller.ts`" está no código. "O endpoint de cadastro não confirma e-mail porque o produto decidiu que o usuário nasce ativo" não está.

## Fluxo

### 1. Colher candidatos

Perguntar à task recém-fechada:
- **Decisões:** o que foi escolhido entre alternativas, e por quê. (Premissas do `lapidar` que se confirmaram; direção escolhida no `brainstorming`.)
- **Armadilhas:** o que quebrou, custou tempo ou surpreendeu. ("Por que não foi pego antes" do `depurar`; teste desonesto pego pelo `conferir`.)
- **Convenções descobertas:** como o projeto faz algo que não está escrito. (Padrão de teste, como roda, onde ficam as coisas, o que não pode mudar.)
- **Premissas erradas:** o que se assumiu e não era assim.
- **Sobre o usuário:** preferência ou correção que ele deu e que vale para sempre.

### 2. Filtrar

Para cada candidato, o teste dos três meses. Depois: já existe registro sobre isso? Atualizar em vez de duplicar. O registro antigo está errado? Corrigir ou apagar.

### 3. Destino

| O item é sobre... | Vai para | Formato |
|-------------------|----------|---------|
| O usuário: preferência, correção, jeito de trabalhar | Memória, tipo `feedback` ou `user` | Fato + **Why** + **How to apply** |
| Um projeto do usuário: onde fica, como funciona, o que não é óbvio | Memória, tipo `project` | Fato + data absoluta quando houver |
| O que qualquer sessão neste repositório precisa saber para não errar | `CLAUDE.md` do repositório | Uma linha imperativa, ou até três; mais que isso vira arquivo em `docs/` com link |
| Uma decisão de design com alternativas descartadas | `docs/decisions/AAAA-MM-DD-<slug>.md` | Contexto, decisão, alternativas, consequências. Meia página |
| Link, dashboard, ticket, doc externa | Memória, tipo `reference` | URL + o que tem lá |

`CLAUDE.md` e `docs/` são arquivos do repositório: entram no diff, seguem o padrão de commit, e o usuário vê antes de subir. Memória é do usuário; escrever direto.

### 4. Escrever

Um fato por registro. Frase que alguém sem contexto entende. Datas absolutas ("em 2026-09-21"), não "ontem". Para `feedback` e `project`, sempre o porquê: fato sem porquê é regra sem critério, e vai ser aplicada errado.

### 5. Reportar

Lista do que foi registrado e onde, e do que foi descartado e por quê. Uma linha cada.

## Sinais de que está registrando errado

| Pensamento | Realidade |
|-----------|-----------|
| "Vou anotar tudo que aconteceu" | Diário não é memória. Só o que muda uma decisão futura. |
| "Coloco no CLAUDE.md para garantir" | CLAUDE.md longo não é lido. Uma linha, ou vai para docs/. |
| "Isso o código já diz, mas anoto assim mesmo" | Duplicado envelhece diferente do código. Não. |
| "Anoto a regra sem o motivo" | Sem motivo, a regra vai ser aplicada onde não cabe. |
| "Não vale registrar, foi um caso raro" | Raro que custou 2 horas vale. |
| "Registro depois" | Depois a conversa acabou e o detalhe se perdeu. Agora. |

## O que esta skill NÃO faz

- Não escreve documentação do código: isso é outra task.
- Não registra o que não passou pelo teste dos três meses.
- Não muda `CLAUDE.md` de repositório compartilhado sem o item aparecer no diff para o usuário ver.

## Referências

| Arquivo | Quando ler |
|---------|-----------|
| `references/exemplos.md` | Em dúvida se um item merece registro, ou como escrever |
