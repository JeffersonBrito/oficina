---
name: entregar
description: Fecha um trabalho em código no padrão da casa: confere que está pronto, revisa o diff, faz commits em inglês sem prefixo e sem atribuição, e abre o PR com objetivo, o que ficou fora e como verificar, derivados da task. Use quando o usuário invocar /entregar, disser "commita", "sobe", "abre o PR", "fecha a branch", "manda para revisão", ou ao terminar uma task do /lapidar que envolveu código.
---

# Entregar

Commit e PR são a parte da entrega que outras pessoas leem primeiro. Esta skill garante que eles contam a história certa, no padrão da casa, sem nada sobrando e sem nada faltando.

Entrada: trabalho concluído na branch atual, de preferência com a task do `/lapidar` e o veredito do `/conferir`. Saída: commits, e opcionalmente push e PR.

| Flag | Efeito |
|------|--------|
| (nenhuma) | Confere, revisa o diff e commita. Não faz push. |
| `--push` | Também faz push da branch |
| `--pr` | Push e abre o PR. Mostra título e corpo antes de criar e pede confirmação uma vez |

## Princípio

Ninguém entrega o que não conferiu, e ninguém commita o que não leu. As duas leituras acontecem aqui, mesmo que pareçam redundantes: o `conferir` prova os critérios; o `entregar` lê o diff como revisor.

## Fluxo

### 1. Pré-condições

- Veredito **PRONTO** do `/conferir` nesta sessão. Sem ele, rodar o `/conferir` agora. NÃO PRONTO não entrega.
- `git status` lido inteiro: cada arquivo modificado ou novo tem motivo na task. Arquivo sem motivo não entra no commit (e é reportado). Arquivo temporário, `.env`, log, saída de script: fora.
- Branch: se estiver na branch principal, criar uma. Nome curto em inglês, kebab-case, dizendo o quê: `register-endpoint`, `fix-scanned-value-parser`. Seguir prefixo do repositório se ele tiver convenção visível no `git branch -r`.

### 2. Ler o diff como revisor

`git diff` completo (staged e não staged). Procurar, e corrigir antes de commitar:
- Código de exploração, `print`, `console.log`, `debugger`, `TODO` sem dono.
- Comentário que repete o código.
- Caminho local, segredo, URL de ambiente pessoal.
- Mudança fora do escopo da task. Se for necessária, vira commit separado com sua própria mensagem; se não, sai.

### 3. Commits

Um commit por mudança que faz sentido sozinha. Feature pequena é um commit. Feature com refactor preparatório são dois: primeiro o refactor, depois a feature.

Mensagem no padrão da casa (`docs/padroes.md`): frase curta em inglês, imperativo, capitalizada, sem prefixo, sem rodapé de atribuição, até 72 caracteres. Corpo só quando o porquê não cabe no título; nunca para repetir o diff.

```
Add register endpoint with duplicate email check
Reject values that lose digits when parsing scanned pages
```

O hook `PreToolUse` do plugin bloqueia o que estiver fora do padrão. Se bloquear, corrigir a mensagem, não contornar o hook.

### 4. Push e PR

Com `--push` ou `--pr`: `git push -u origin <branch>`. Nunca `--force` em branch compartilhada; `--force-with-lease` só na própria branch e só se o usuário pediu.

Com `--pr`: montar título e corpo pelo modelo em `references/pr.md`, mostrar ao usuário, e criar com `gh pr create` depois do "sim". Corpo em inglês, derivado da task: objetivo, o que mudou, o que ficou de fora e por quê, como verificar. Sem rodapé de atribuição.

### 5. Reportar

Uma linha por commit com o hash e a mensagem; a URL do PR se houver; o que ficou fora do commit e por quê.

## Sinais de que está entregando errado

| Pensamento | Realidade |
|-----------|-----------|
| "Commito tudo e depois arrumo" | Histórico é permanente. Arrumar antes. |
| "`git add .` é mais rápido" | E leva o `.env`, o log e o arquivo de teste manual junto. `git add` por arquivo, com motivo. |
| "O conferir foi há pouco, não precisa de novo" | Se mudou algo depois, precisa. Se não mudou, custa segundos. |
| "Mensagem qualquer, depois faço squash" | O squash não acontece. Mensagem certa agora. |
| "O PR pode ficar sem descrição, o diff fala" | O diff não diz o que ficou de fora nem como verificar. |
| "Force push resolve" | Resolve para você e quebra para os outros. |

## O que esta skill NÃO faz

- Não decide se está pronto: isso é o `/conferir`.
- Não faz merge nem aprova PR.
- Não muda a convenção de branch ou de commit do repositório onde está: segue a que existe, e a da casa quando não há.

## Referências

| Arquivo | Quando ler |
|---------|-----------|
| `references/pr.md` | No passo 4, para o modelo de título e corpo do PR |
