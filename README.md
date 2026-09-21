# oficina

Skills pessoais para o [Claude Code](https://claude.com/claude-code), em português. Ferramentas de pensamento para usar **antes** de pedir código, texto ou análise: transformar um pedido vago em uma task que qualquer um executa sem adivinhar.

## Instalação

Dentro do Claude Code:

```
/plugin marketplace add JeffersonBrito/oficina
/plugin install oficina@oficina
```

Para atualizar depois: `/plugin update oficina`.

## Skills

| Skill | O que faz | Como usar |
|-------|-----------|-----------|
| **lapidar** | Pega um pedido curto e vago e devolve uma task estruturada: contexto, objetivo, escopo, critérios de aceite verificáveis, abordagem, premissas explícitas. Vale para qualquer domínio: e-mail, apresentação, análise, plano, decisão, código. | `/lapidar <pedido>` |

### lapidar

```
/lapidar escreve um e-mail pro cliente avisando que a entrega vai atrasar
/lapidar monta uma apresentação sobre o motor pra diretoria --salvar
/lapidar o benchmark tá dando valor diferente do gabarito --executar
```

| Flag | Efeito |
|------|--------|
| (nenhuma) | Só gera a task, para você revisar e usar onde quiser |
| `--salvar` | Gera e grava em `.claude/prompts/AAAA-MM-DD-<slug>.md` |
| `--executar` | Gera, mostra, e executa a task na mesma resposta |

O que ela faz de diferente de "pedir ao modelo para melhorar o prompt":

- **Classifica o pedido** em sete tipos pelo resultado esperado: `criar`, `corrigir`, `transformar`, `investigar`, `decidir`, `planejar`, `comunicar`. Cada tipo exige seções próprias (um e-mail exige "Leitor" e "O que não dizer"; uma decisão exige "Critérios de comparação"; um bug exige "Reprodução" e "Hipóteses").
- **Aterra no que existe**: conversa, arquivos, memória, repositório. A task cita nomes, números e caminhos reais, nunca "o documento relevante".
- **Premissas com plano B**: cada suposição diz o que fazer se estiver errada. Pergunta ao usuário só quando leituras diferentes mudam o trabalho de verdade, no máximo três perguntas.
- **Tamanho proporcional**: um e-mail vira task de 15 linhas, uma apresentação vira task de 60. Nunca infla.
- **Frases proibidas**: "boas práticas", "de forma clara e objetiva", "o público-alvo", "se necessário" são barradas pelo checklist e trocadas pela decisão concreta.

Exemplos completos de antes e depois em [`skills/lapidar/references/exemplos.md`](skills/lapidar/references/exemplos.md).

## Em breve

- **brainstorming**: explorar o problema e as alternativas antes de lapidar. Saída: 2 a 4 direções com prós e contras e uma recomendação, que vira entrada do `/lapidar`.

## Criar uma skill nova

Veja [`docs/como-criar-uma-skill.md`](docs/como-criar-uma-skill.md) e o modelo em [`templates/SKILL-template.md`](templates/SKILL-template.md).

## Inspiração

A ideia de skills como processos de pensamento vem do [Superpowers](https://github.com/obra/superpowers). A oficina é uma coleção própria, em português, com foco em tasks e não só em código.

## Licença

MIT
