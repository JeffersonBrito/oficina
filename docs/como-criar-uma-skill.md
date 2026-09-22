# Como criar uma skill na oficina

## Estrutura

```
skills/
  nome-da-skill/
    SKILL.md            # obrigatório: frontmatter + instruções
    references/         # opcional: detalhe carregado sob demanda
      tipos/            # um arquivo por tipo; o modelo lê só o que a task pede
        criar.md
        corrigir.md
      exemplos.md       # lido só em dúvida
```

Copie `templates/SKILL-template.md` para `skills/<nome>/SKILL.md` e preencha.

## Regras que valem para todas as skills daqui

1. **A `description` do frontmatter decide tudo.** É o único texto que o Claude lê antes de escolher carregar a skill. Ela deve dizer o que a skill faz e listar as palavras que o usuário usaria ao pedir. Descrição vaga = skill nunca carregada.
2. **`SKILL.md` curto, `references/` longo.** O `SKILL.md` deve caber em uma leitura (até ~2.000 tokens). Tabelas por tipo vão para `references/<grupo>/<tipo>.md`, um arquivo por tipo, para o modelo ler só o que a task pede. Exemplos vão para `references/exemplos.md` e só são lidos em dúvida.
3. **`description` com até 60 tokens.** Ela entra em toda sessão, para todas as skills, mesmo sem uso. Diz o que a skill faz e os gatilhos; a explicação fica no corpo.
4. **Toda etapa tem critério de parada.** "Explorar o projeto" não; "explorar por até 2 minutos e citar caminhos reais" sim.
5. **Saída em formato fixo.** Quem usa a skill duas vezes deve receber a mesma estrutura.
6. **Checklist de qualidade binário.** Cada item responde sim ou não.
7. **Seção "O que esta skill NÃO faz".** Evita que uma skill invada outra (ex.: `lapidar` não executa, `brainstorming` não escreve a task final).
8. **Português por padrão.** Nomes de código, comandos e termos técnicos ficam como estão.

## Testar localmente antes de publicar

Aponte a pasta local da skill para dentro de `~/.claude/skills/` com um link simbólico. Assim edições no repositório valem na hora, sem reinstalar o plugin:

```bash
ln -s ~/Projects/oficina/skills/nome-da-skill ~/.claude/skills/nome-da-skill
```

Depois, em uma sessão do Claude Code, invoque `/nome-da-skill <pedido>` e confira:

- A skill foi carregada? (a resposta deve seguir o formato fixo)
- Um pedido pequeno gerou saída pequena?
- Nenhuma frase proibida sobrou?

## Padrões da casa

Em [`padroes.md`](padroes.md). O hook `SessionStart` injeta o arquivo em toda sessão e o `PreToolUse` bloqueia commits e PRs fora do padrão, então editar aquele arquivo muda o comportamento do plugin inteiro.

## Publicar uma nova versão

1. Atualizar `version` em `.claude-plugin/plugin.json` e em `.claude-plugin/marketplace.json` (os dois).
2. Adicionar a skill na tabela do `README.md`.
3. Commit e push. Quem instalou pelo marketplace atualiza com `/plugin update oficina`.

## Como as skills se encadeiam

`brainstorming` termina em um comando `/lapidar`; `lapidar` termina em uma task pronta para executar; `tdd` pega os critérios de aceite dessa task como lista de testes e termina em código com relatório critério a critério; `conferir` prova cada critério com evidência independente e termina em PRONTO ou NÃO PRONTO. Para bug, `depurar` entra entre o `lapidar` (tipo `corrigir`) e o `tdd`, e termina em causa raiz explicada. `entregar` fecha com commit e PR; `registrar` guarda o não-óbvio. `usar-oficina` é a tabela que diz por onde entrar, e é injetada em toda sessão: skill nova precisa de uma linha lá. Skill nova deve dizer onde entra nessa cadeia e onde para, na seção "O que esta skill NÃO faz".
