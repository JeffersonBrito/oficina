---
name: entregar
description: Fecha trabalho em código no padrão da casa: exige PRONTO do /conferir, revisa o diff, commits em inglês sem prefixo nem atribuição, PR com objetivo, escopo excluído e como verificar. Use quando invocarem /entregar, "commita", "sobe", "abre o PR", "fecha a branch".
---

# Entregar

Commit e PR são o que os outros leem primeiro. Entrada: trabalho concluído na branch atual, com a task do `/lapidar` e o veredito do `/conferir`. Flags: nenhuma = confere, revisa e commita, sem push; `--push` = também push; `--pr` = push e PR, mostrando título e corpo e pedindo confirmação uma vez.

## Fluxo

1. **Pré-condições.** Veredito PRONTO do `/conferir` nesta sessão; sem ele, rodar agora; NÃO PRONTO não entrega. `git status` lido inteiro: arquivo sem motivo na task fica fora e é reportado; temporário, `.env`, log, saída de script, fora. Na branch principal, criar uma: nome curto em inglês, kebab-case, dizendo o quê (`register-endpoint`); seguir prefixo do repo se houver convenção em `git branch -r`.
2. **Ler o diff como revisor** (staged e não staged). Sai antes do commit: exploração, `print`, `console.log`, `debugger`, `TODO` sem dono, comentário que repete o código, caminho local, segredo, URL pessoal. Mudança fora do escopo: commit separado se necessária, fora se não.
3. **Commits.** Um por mudança que faz sentido sozinha; refactor preparatório antes da feature. Mensagem: frase curta em inglês, imperativo, capitalizada, sem prefixo, sem atribuição, até 72 caracteres; corpo só quando o porquê não cabe. `git add` por arquivo, com motivo. O hook bloqueia o que estiver fora; corrigir a mensagem, nunca contornar.
4. **Push e PR.** `git push -u origin <branch>`. Nunca `--force` em branch compartilhada; `--force-with-lease` só na própria e só se pedido. Com `--pr`: título e corpo pelo modelo em `references/pr.md`, mostrar, e `gh pr create` depois do "sim". Corpo em inglês, sem rodapé de atribuição.
5. **Reportar.** Hash e mensagem por commit, URL do PR, o que ficou fora e por quê.

## Sinais de desvio

| Pensamento | Realidade |
|-----------|-----------|
| "Commito tudo e depois arrumo" | Histórico é permanente. |
| "`git add .` é mais rápido" | Leva o `.env` junto. Por arquivo. |
| "Mensagem qualquer, depois squash" | O squash não acontece. |
| "O diff fala por si" | Não diz o que ficou de fora nem como verificar. |

## Não faz

Não decide se está pronto (`/conferir`). Não faz merge nem aprova. Não muda a convenção do repositório: segue a que existe, e a da casa quando não há.

## Referências

| Arquivo | Quando ler |
|---------|-----------|
| `references/pr.md` | No passo 4 |
