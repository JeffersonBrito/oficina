---
name: registrar
description: No fim de uma task, grava o não-óbvio (decisão e porquê, armadilha, convenção, premissa errada) na memória ou no CLAUDE.md e docs do repositório. Use quando invocarem /registrar, "anota isso", "lembra disso", ou ao fechar task que revelou algo que o código e o git não contam.
---

# Registrar

O que custou caro para descobrir não pode custar de novo. Entrada: a task recém-fechada. Saída: zero, um ou poucos registros, cada um em um lugar só. Flags: `--memoria` só memória; `--projeto` só `CLAUDE.md` e `docs/`.

Regra central: **daqui a três meses, sem esta conversa, isso evita um erro ou uma pergunta?** Se não, não registra. Não registrar o que o código, o git ou a doc já contam: "o endpoint fica em `auth.controller.ts`" está no código; "não confirma e-mail porque o produto decidiu que o usuário nasce ativo" não está.

## Fluxo

1. **Colher candidatos** na task: decisões (premissas confirmadas, direção escolhida), armadilhas ("por que não foi pego antes" do `/depurar`, teste desonesto pego pelo `/conferir`), convenções descobertas (como roda, onde ficam as coisas, o que não muda), premissas erradas, feedback do usuário que vale para sempre.
2. **Filtrar** pelo teste dos três meses. Já existe registro? Atualizar, não duplicar. Registro antigo errado? Corrigir ou apagar.
3. **Destino**, um só por item:

| Sobre... | Vai para | Formato |
|----------|----------|---------|
| o usuário: preferência, correção | memória `feedback` ou `user` | fato + **Why** + **How to apply** |
| um projeto: onde fica, como funciona, o não-óbvio | memória `project` | fato + data absoluta |
| o que qualquer sessão neste repo precisa para não errar | `CLAUDE.md` | uma linha imperativa; até três; mais vira `docs/` com link |
| decisão com alternativas descartadas | `docs/decisions/AAAA-MM-DD-<slug>.md` | contexto, decisão, alternativas, consequências; meia página |
| link, dashboard, ticket | memória `reference` | URL + o que tem lá |

`CLAUDE.md` e `docs/` entram no diff e seguem o padrão de commit. Memória é do usuário; escrever direto.

4. **Escrever**: um fato por registro, frase que alguém sem contexto entende, datas absolutas, e sempre o porquê em `feedback` e `project`. Regra sem porquê é aplicada onde não cabe.
5. **Reportar**: o que foi registrado e onde; o que foi descartado e por quê. Uma linha cada.

## Sinais de desvio

| Pensamento | Realidade |
|-----------|-----------|
| "Anoto tudo que aconteceu" | Diário não é memória. |
| "Coloco no CLAUDE.md para garantir" | CLAUDE.md longo não é lido. Uma linha, ou `docs/`. |
| "Anoto a regra sem o motivo" | Vai ser aplicada errado. |
| "Registro depois" | Depois a conversa acabou. Agora. |

## Não faz

Não documenta código. Não registra o que não passou no teste dos três meses. Não muda `CLAUDE.md` compartilhado sem o item aparecer no diff.

## Referências

| Arquivo | Quando ler |
|---------|-----------|
| `references/exemplos.md` | Só em dúvida se um item merece registro |
