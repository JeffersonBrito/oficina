# Padrões da casa

Valem para este repositório e para qualquer código, commit ou PR que as skills da oficina produzam. O hook `SessionStart` do plugin injeta este arquivo em toda sessão; o hook `PreToolUse` bloqueia commits e PRs fora do padrão.

## Commits

- Uma frase curta em inglês, no imperativo, capitalizada. Até 72 caracteres.
- Sem prefixo: nada de `feat:`, `fix:`, `chore:`, `refactor:`.
- Sem rodapé de atribuição: nada de `Co-Authored-By`, nada de "Generated with", nenhuma menção a Claude ou a outra ferramenta.
- Corpo opcional, só quando o porquê não cabe no título.

```
Add brainstorming skill
Reject duplicate email on register
Document commit and code conventions
```

## Pull requests

- Título no mesmo formato do commit.
- Corpo: objetivo, o que ficou fora, como verificar. Em inglês.
- Sem rodapé de atribuição.

## Código

- Clean code: o nome diz o que a coisa faz.
- Comentário só para um porquê que o código não consegue dizer. Comentário que repete o código é removido.
- Sem código morto, sem `TODO` sem dono, sem log de debug esquecido.
