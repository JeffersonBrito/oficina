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
| **brainstorming** | Separa o problema da solução que veio junto, faz até 5 perguntas (uma por vez), propõe 3 a 5 direções materialmente diferentes com prós, contras, esforço e risco em fatos, recomenda uma e pede a escolha. A escolha sai como comando `/lapidar` pronto. | `/brainstorming <ideia ou dúvida>` |
| **lapidar** | Pega um pedido curto e vago e devolve uma task estruturada: contexto, objetivo, escopo, critérios de aceite verificáveis, abordagem, premissas explícitas. Vale para qualquer domínio: e-mail, apresentação, análise, plano, decisão, código. | `/lapidar <pedido>` |
| **tdd** | Implementa código com teste primeiro. Lista de testes derivada dos critérios de aceite, ciclo RED (ver falhar pelo motivo certo) → GREEN mínimo → REFACTOR, fatias verticais ponta a ponta, testes honestos. Código escrito antes do teste é apagado. Bug começa por um teste que reproduz. | `/tdd <o que implementar>` ou automático ao executar uma task com código |
| **conferir** | Prova que a entrega está pronta antes de dizer "pronto". Cada critério de aceite recebe evidência produzida na hora (comando e saída, trecho, contagem); reporta passou / falhou / não conferido sem arredondar; veredito binário PRONTO ou NÃO PRONTO. Vale para código, texto, apresentação, dados. | `/conferir` ou automático antes de concluir |
| **depurar** | Investiga um bug até a causa raiz antes de corrigir. Congela o sintoma com evidência literal, reproduz, localiza por bissecção (tempo, caminho, dados), testa até 3 hipóteses com previsão, explica a causa em uma frase sem "acho", corrige pelo `tdd` e procura irmãos do bug. | `/depurar <sintoma>` ou automático em task `corrigir` |

O fluxo pensado: **`/brainstorming` → escolhe a direção → `/lapidar` → task pronta → `/tdd` implementa → `/conferir` prova.** Para bug, a task `corrigir` do `lapidar` passa pelo **`/depurar`** antes do `tdd`. Cada skill para onde a próxima começa: os critérios de aceite do `lapidar` são a lista de testes do `tdd` e a lista de provas do `conferir`.

### brainstorming

```
/brainstorming quero colocar um chatbot no sistema pra responder as dúvidas dos analistas
/brainstorming não sei se aviso o cliente por e-mail ou ligo --lapidar
```

| Flag | Efeito |
|------|--------|
| (nenhuma) | Conduz o brainstorm e entrega o resumo da direção escolhida, terminando no comando `/lapidar` |
| `--salvar` | Também grava o resumo em `.claude/brainstorms/AAAA-MM-DD-<slug>.md` |
| `--lapidar` | Depois da escolha, chama o `/lapidar` na sequência |

Regras que a diferenciam de "me dá umas ideias":

- **Problema antes da solução.** "Quero um chatbot" é solução; a skill escreve o problema ("analistas param para tirar dúvida com a mesma pessoa") e o chatbot vira uma direção entre outras.
- **Direções materialmente diferentes.** Teste: cada uma viraria uma task diferente no `/lapidar`? Sempre inclui a mínima (ou "não fazer nada") e uma que muda o ângulo (quem, onde, quando) em vez do como.
- **Uma pergunta por vez, no máximo cinco.** Só perguntas cuja resposta elimina uma direção.
- **Prós e contras em fatos.** "Exige Redis, que o projeto não tem", não "mais complexo".
- **Recomenda e diz quando outra venceria.** Depois pergunta qual. Não decide sozinha, não executa nada.

Exemplos completos em [`skills/brainstorming/references/exemplos.md`](skills/brainstorming/references/exemplos.md).

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

### tdd

```
/tdd endpoint POST /auth/register com 409 para e-mail duplicado
/lapidar cria o endpoint de cadastro --executar      # a execução entra no /tdd sozinha
```

Três regras que não se negociam:

- **Teste antes, sempre.** Código de produção escrito antes do teste é apagado, não "guardado de referência".
- **Fatia vertical, não camada.** Cada ciclo entrega um comportamento inteiro, da entrada ao resultado observável.
- **Teste honesto.** Antes de fechar um item: "se eu quebrar a implementação de propósito, este teste falha?". Tabela de sinais de teste desonesto (`toBeTruthy`, asserção sobre o mock, snapshot sem ler) com a troca certa.

O ciclo exige **ver o RED pelo motivo certo** (asserção que não bateu ou função que não existe; erro de sintaxe ou fixture faltando não conta) e trata teste que passa de primeira como suspeito. Vem com tabela de racionalizações, tabela de "quando travar", relatório final critério a critério, e referências de comandos para pytest, Jest e Vitest e de anti-padrões de teste.

### conferir

```
/conferir
/conferir o e-mail que você escreveu --corrigir
```

| Flag | Efeito |
|------|--------|
| (nenhuma) | Confere e reporta. Não corrige. |
| `--corrigir` | Confere, corrige o que falhou, confere de novo. Até 3 rodadas. |

O que a diferencia de "revisa aí":

- **Evidência produzida agora.** "Rodei há cinco minutos" e "o arquivo de teste existe" não valem. Comando rodado, saída colada, trecho citado, número contado.
- **Não conferido ≠ passou.** O que não deu para provar aparece com esse nome e o que seria preciso, e derruba o veredito.
- **Critérios implícitos.** Escopo íntegro (diff lido inteiro), nada pela metade, nada deixado para trás, padrões da casa. Tabela por tipo de entrega em `references/checagens.md`.
- **Veredito binário.** PRONTO ou NÃO PRONTO com o que falta. Sem "quase", sem "com ressalvas".
- **Evidência independente do `tdd`.** O exemplo em `references/exemplos.md` mostra uma suíte verde com teste desonesto que só a chamada real pegou.

### depurar

```
/depurar o benchmark tá dando valor diferente do gabarito nos processos escaneados
/depurar POST /auth/register devolve 500 em vez de 409 --so-causa
```

| Flag | Efeito |
|------|--------|
| (nenhuma) | Investiga até a causa raiz e corrige pelo `tdd` |
| `--so-causa` | Para na causa raiz, sem corrigir |

O que a diferencia de "tenta mudar e vê":

- **Uma mudança por vez, com previsão antes.** "Se X for a causa, então Y aparece." Mudou três coisas e passou? Desfaz duas.
- **Reproduzir antes de qualquer hipótese.** Não reproduz? A task vira "obter reprodução".
- **Bissecção** no tempo (`git bisect`), no caminho (estado no meio) e nos dados (menor input que reproduz). Técnicas e depuradores por linguagem em `references/tecnicas.md`.
- **Três hipóteses descartadas = parar** e listar as certezas não conferidas. Uma delas está errada.
- **Causa raiz sem "acho"**, mais "por que não foi pego antes". `try/except`, `retry` e `sleep` sem causa por trás não são correção.
- **Irmãos do bug**: o mesmo padrão em outro lugar é corrigido junto ou registrado.

## Padrões da casa

Commits em inglês, frase curta capitalizada, sem prefixo, sem rodapé de atribuição. PRs no mesmo formato. Código sem comentários que repetem o código. Tudo em [`docs/padroes.md`](docs/padroes.md).

O plugin faz cumprir, não só recomenda:

| Hook | O que faz |
|------|-----------|
| `SessionStart` | Injeta `docs/padroes.md` no contexto de toda sessão |
| `PreToolUse` (Bash) | Bloqueia `git commit` e `gh pr create/edit` com prefixo, minúscula inicial, mais de 72 caracteres, português ou rodapé de atribuição, e explica o motivo. Testes em `hooks/test_check_commit.py` |

```
oficina bloqueou o commit. Padrão: frase curta em inglês, capitalizada, sem prefixo, sem atribuição.
- prefixo proibido em "feat: add brainstorming skill": use uma frase, sem "tipo:"
```

## Criar uma skill nova

Veja [`docs/como-criar-uma-skill.md`](docs/como-criar-uma-skill.md) e o modelo em [`templates/SKILL-template.md`](templates/SKILL-template.md).

## Inspiração

A ideia de skills como processos de pensamento vem do [Superpowers](https://github.com/obra/superpowers), e o rigor do `tdd` (ver o teste falhar, apagar código escrito antes do teste) vem da skill de TDD de lá. A fatia vertical e os testes honestos vêm da skill de TDD do [Matt Pocock](https://www.aihero.dev/skill-test-driven-development-claude-code). A oficina é uma coleção própria, em português, com foco em tasks e não só em código.

## Licença

MIT
