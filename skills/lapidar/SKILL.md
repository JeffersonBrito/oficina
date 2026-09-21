---
name: lapidar
description: Transforma um pedido curto e vago ("escreve um e-mail pro cliente", "monta uma apresentação sobre X", "analisa esse contrato", "corrige o benchmark") em uma task estruturada e valiosa — contexto, objetivo, escopo, critérios de aceite verificáveis, abordagem e premissas explícitas. Vale para qualquer domínio, não só código. Use quando o usuário invocar /lapidar, pedir para "estruturar", "expandir", "detalhar" ou "melhorar" um prompt/pedido/tarefa, ou quiser um brief pronto para executar em outra sessão, por um subagente ou por uma pessoa.
---

# Lapidar

Pega um pedido bruto e devolve uma task que outra sessão, um subagente, uma pessoa da equipe, ou você mesmo daqui a dez minutos consegue executar **sem adivinhar nada**.

O pedido bruto vem em `$ARGUMENTS` ou na mensagem do usuário. Flags opcionais no final:

| Flag | Efeito |
|------|--------|
| (nenhuma) | Só gera a task |
| `--salvar` | Gera e grava em `.claude/prompts/AAAA-MM-DD-<slug>.md` (ou `~/.claude/prompts/` fora de um projeto) |
| `--executar` | Gera, mostra, e **na mesma resposta** executa a task como se fosse o pedido do usuário |

## Princípio

Uma task boa não é uma task longa. É uma task onde **nenhuma decisão importante ficou implícita**: quem é o público, o que é "pronto", o que fica de fora, o que foi assumido. O tamanho é proporcional ao pedido: um e-mail de três linhas vira task de 15 linhas; uma apresentação para diretoria vira task de 60. Nunca inflar para parecer completo.

## Fluxo

### 1. Ler e classificar

Tipo do pedido, pelo que o usuário quer no final:

| Tipo | O resultado é... | Exemplos |
|------|-----------------|----------|
| `criar` | algo novo que não existia | texto, apresentação, planilha, código, design, curso |
| `corrigir` | algo que existe voltar a funcionar | bug, texto com erro, processo que falha, planilha errada |
| `transformar` | o mesmo conteúdo em outra forma | resumir, traduzir, reescrever, refatorar, converter formato |
| `investigar` | uma resposta com evidência | análise, pesquisa, diagnóstico, "por que X acontece" |
| `decidir` | uma recomendação entre opções | comparar ferramentas, escolher abordagem, "vale a pena?" |
| `planejar` | uma sequência de passos no tempo | roadmap, cronograma, semana, projeto, estudo |
| `comunicar` | uma mensagem que chega a alguém | e-mail, post, anúncio, feedback, apresentação para pessoas |

Cada tipo acrescenta seções próprias ao formato base. Ler `references/tipos.md` para o tipo identificado. Pedido híbrido (ex.: "analisa e me diz o que fazer") usa o tipo do resultado final (`decidir`) e pega emprestado o que precisar.

### 2. Aterrar no que existe (exploração curta, no máximo uns 2 minutos)

Antes de escrever, juntar o que já está disponível:
- **A conversa atual**: o que o usuário já disse, mostrou ou decidiu antes deste pedido.
- **Arquivos mencionados ou anexados**: ler o suficiente para citar trechos, nomes e números reais.
- **Memória do usuário**: projetos, preferências e contexto já conhecidos.
- **Repositório**, se o pedido envolve código e há um aberto: `CLAUDE.md`, estrutura, como testa e roda.
- **O que já existe do mesmo tipo**: e-mail anterior ao mesmo cliente, apresentação anterior, doc no mesmo padrão. Serve de referência de estilo e evita recomeçar.

Meta: a task cita **nomes reais, números reais, referências reais**. Nunca "o documento relevante" ou "o público-alvo". Sem contexto disponível, registrar cada lacuna em Premissas.

### 3. Detectar lacunas

Listar o que o pedido não diz e que muda o trabalho. Para cada lacuna:
- Dá para assumir com segurança → assume e registra em **Premissas**, com o que fazer se a premissa estiver errada.
- Leituras diferentes levam a trabalhos materialmente diferentes → vira pergunta. **No máximo 3 perguntas, em uma rodada só** (AskUserQuestion). Em sessão autônoma, escolher a leitura mais provável e registrar.

Teste para decidir: "se eu assumir errado, quem executa perde mais de 20% do esforço?" Se sim, pergunta. Se não, premissa.

As lacunas mais comuns, por tipo: `comunicar` → quem lê e qual tom; `criar` → formato e tamanho; `investigar` → o que conta como resposta; `decidir` → critérios de comparação; `planejar` → prazo e horas disponíveis; `corrigir` → como reproduzir; `transformar` → o que não pode mudar.

### 4. Escrever a task

Formato fixo abaixo. Seção sem conteúdo é **removida**, não deixada com "N/A". Idioma: o mesmo do pedido (padrão pt-BR); nomes próprios, termos técnicos e código ficam como estão.

### 5. Passar pelo checklist

Ver "Checklist de qualidade" no fim. Item que falha é corrigido antes de entregar.

### 6. Entregar

- Padrão (sem flag): uma linha dizendo o tipo detectado e as 1-2 premissas que mais pesam; depois a task em um bloco ```markdown pronto para copiar. Nada depois do bloco. **Não executar a task.**
- `--salvar`: igual ao padrão, mais gravar o arquivo e mostrar o caminho.
- `--executar`: igual ao padrão, e **na mesma resposta, logo depois do bloco**, escrever a linha "Executando a task acima." e começar a executar. A task recém-escrita passa a ser o pedido do usuário: seguir os Requisitos, Restrições e Premissas dela. Ao terminar, reportar item a item contra os Critérios de aceite da própria task, dizendo quais premissas se confirmaram. Parar só se uma Pergunta em aberto travar o início; nesse caso, perguntar e continuar depois da resposta.

## Formato da task

````markdown
# <Verbo no imperativo + objeto concreto + para quem, se houver>

## Contexto
<2 a 5 linhas: o que existe hoje, por que a tarefa existe, o que dói ou o que se quer alcançar. Com nomes e referências reais.>

## Objetivo
<1 a 2 frases. Estado final observável. Não é "melhorar X"; é "X passa a fazer/ter/ser Y".>

## Escopo
**Inclui:** <o que entra>
**Não inclui:** <o que alguém tentaria fazer "de bônus" e não deve>

## Requisitos
- <o que o resultado precisa ter ou fazer, um por linha, cada um verificável>

## Restrições
- <o que não pode mudar, não pode ser usado, não pode ultrapassar: prazo, tamanho, tom, orçamento, dependências, compatibilidade>

## Insumos e referências
- <arquivo, link, trecho, dado, pessoa a consultar, exemplo anterior a seguir como padrão> — por que importa

## Abordagem sugerida
1. <passos em ordem, cada um com resultado observável>

Sugerida, não obrigatória: se ao executar surgir caminho melhor, seguir o melhor e dizer por quê.

## Critérios de aceite
- [ ] <afirmação binária e testável: "o e-mail cabe em uma tela de celular", "o teste X passa", "a tabela tem as 3 opções com custo mensal">

## Como verificar
<o que fazer para provar que ficou pronto: comando exato, checklist de leitura, comparar com o exemplo Y, alguém específico revisar>

## Premissas
- <o que foi assumido porque o pedido não dizia, e o que fazer se estiver errado>

## Perguntas em aberto
- <só as que não travam o início; as que travam já foram perguntadas>

## Entrega esperada
<formato, tamanho, onde vai parar, para quem, e o que reportar: o que ficou de fora e por quê>
````

## Checklist de qualidade

Antes de entregar, conferir cada item. Um "não" = voltar e corrigir.

- [ ] O **Objetivo** descreve um estado final que dá para observar, não uma intenção.
- [ ] Todo **critério de aceite** é binário: alguém consegue dizer "passou" ou "não passou" sem interpretar.
- [ ] Toda referência citada (arquivo, pessoa, número, link) **existe** ou está marcada como "a obter" / "a criar".
- [ ] **Como verificar** é executável neste contexto, não genérico ("revisar com cuidado" não vale).
- [ ] **Não inclui** tem pelo menos um item quando o tipo é `criar`, `transformar` ou `planejar`.
- [ ] **Entrega esperada** diz formato, tamanho e destino. "Um documento" não basta; "um `.md` de até 1 página no canal #produto" basta.
- [ ] Nenhuma **frase proibida** (lista abaixo) sobrou no texto.
- [ ] Toda lacuna do pedido virou Premissa ou Pergunta. Nenhuma foi ignorada em silêncio.
- [ ] O tamanho é proporcional ao pedido.
- [ ] Nada foi acrescentado que o usuário não pediu. Escopo extra vai para "Não inclui", não para Requisitos.

## Frases proibidas

Cada uma destas é uma decisão que foi empurrada para quem vai executar. Substituir pela decisão concreta.

`seguir boas práticas` · `garantir qualidade` · `de forma clara e objetiva` · `profissional` · `robusto` · `de forma eficiente` · `se necessário` · `conforme apropriado` · `etc.` · `entre outros` · `tratar adequadamente` · `o público-alvo` · `os stakeholders` · `revisar com cuidado`

Exemplos de substituição:
- "de forma clara e objetiva" → "até 120 palavras, primeira frase diz a data nova, sem pedir desculpas mais de uma vez"
- "o público-alvo" → "a diretoria comercial, que não sabe o que é LLM e decide orçamento"
- "tratar erros adequadamente" → "quando o PDF não abre, registrar aviso com o id e seguir; não abortar o lote"

## O que esta skill NÃO faz

- Não executa a tarefa, salvo com `--executar`.
- Não inventa requisitos. Escopo extra que pareça útil vai para "Não inclui" para o usuário decidir depois.
- Não substitui o planejamento durante a execução: a "Abordagem sugerida" é um ponto de partida, não um contrato.

## Referências

| Arquivo | Quando ler |
|---------|-----------|
| `references/tipos.md` | Sempre, depois de classificar: seções extras por tipo |
| `references/exemplos.md` | Quando estiver em dúvida sobre o nível de detalhe esperado |
