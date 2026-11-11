---
name: lapidar
description: Transforma um pedido curto em uma task estruturada (contexto, objetivo, escopo, critérios de aceite, premissas), para qualquer domínio. Use quando invocarem /lapidar ou pedirem para estruturar, detalhar ou expandir um pedido, prompt ou tarefa.
---

# Lapidar

Pedido bruto entra; sai uma task que outra sessão, um subagente ou uma pessoa executa sem adivinhar. O pedido vem em `$ARGUMENTS` ou na mensagem. Flags no final: `--salvar` grava em `.claude/prompts/AAAA-MM-DD-<slug>.md` (ou `~/.claude/prompts/` fora de projeto); `--executar` gera e, na mesma resposta, executa.

## Princípio

A task acrescenta **decisões** ao pedido, não texto: o que conta como pronto, como provar, o que fica de fora, o que foi assumido. Decisão implícita é tomada por quem executa, sem o contexto de quem pediu. Linha que repete o pedido, ou diz o que um executor capaz já faria, dilui as que importam e sai. Por isso o tamanho segue o pedido: e-mail de três linhas vira task de 15 linhas; apresentação para diretoria vira 60.

Quanto escrever depende de quem executa. Sem flag ou com `--salvar`, o leitor não viu esta conversa: a task carrega sozinha o contexto e o porquê. Com `--executar`, o executor é esta sessão: o que já está na conversa não se reescreve; o ganho é fixar o que é pronto e virar lacunas em premissas e perguntas.

## Fluxo

1. **Classificar** pelo resultado final: `criar` (algo novo) · `corrigir` (algo que existe voltar a funcionar) · `transformar` (mesmo conteúdo, outra forma) · `investigar` (resposta com evidência) · `decidir` (recomendação entre opções) · `planejar` (passos no tempo) · `comunicar` (mensagem para alguém). Ler **só** `references/tipos/<tipo>.md`, que traz as decisões próprias do tipo. Híbrido usa o tipo do resultado final.
2. **Aterrar** (no máximo uns 2 minutos): conversa atual, arquivos citados, memória, repositório se envolver código, e o que já existe do mesmo tipo (e-mail anterior, doc no padrão). A task cita nomes, números e caminhos reais. Sem contexto, cada lacuna vira premissa.
3. **Lacunas**: o que o pedido não diz e muda o trabalho. Dá para assumir → Premissa, com o que fazer se estiver errada. Leituras diferentes dariam trabalhos materialmente diferentes (o executor perderia mais de 20% do esforço) → pergunta, no máximo 3, em uma rodada (AskUserQuestion). Em sessão autônoma, assumir a mais provável e registrar.
4. **Escrever** no formato abaixo. Idioma do pedido; código e nomes próprios como estão.
5. **Checklist**; corrigir o que falhar antes de entregar.
6. **Entregar**: uma linha com o tipo e as 1-2 premissas que mais pesam, depois a task em um bloco ```markdown. Sem flag: nada depois do bloco, e a task fica sem executar. `--salvar`: gravar e mostrar o caminho. `--executar`: logo após o bloco escrever "Executando a task acima." e executar como se fosse o pedido do usuário, respeitando o que a task fixou; ao fim, reportar item a item contra os Critérios de aceite e dizer quais premissas se confirmaram. Parar só se uma Pergunta em aberto travar o início.

## Formato da task

Objetivo, Critérios de aceite e Como verificar entram sempre: sem elas ninguém sabe quando parar.

````markdown
# <Verbo no imperativo + objeto concreto + para quem, se houver>

## Contexto
<Um parágrafo em prosa, não lista: o que existe hoje, por que a tarefa existe, o que dói e para quem. Nomes e referências reais.>

## Objetivo
<1 a 2 frases. Estado final observável: "X passa a fazer/ter/ser Y", não "melhorar X".>

## Critérios de aceite
- [ ] <afirmação binária e testável: "o teste X passa", "o e-mail cabe em uma tela de celular">

## Como verificar
<comando exato, checklist de leitura, comparar com o exemplo Y, ou quem revisa>
````

**Contexto** entra sempre que o leitor não viu a conversa: é o porquê que deixa o executor decidir bem o que a task não previu. As demais entram quando mudam o trabalho, com estes nomes: Premissas, Perguntas em aberto e Entrega esperada depois de Como verificar; as outras, e as do tipo, antes de Critérios de aceite. Em task pequena, uma linha cada.

| Seção | Entra quando |
|-------|--------------|
| Escopo (`**Inclui:**` / `**Não inclui:**`) | há um "bônus" que alguém faria e não deve; `Inclui` só se o Objetivo não delimita |
| Requisitos | o resultado precisa ter ou fazer algo que os critérios não cobrem; um por linha |
| Restrições | há o que não pode mudar ou ultrapassar: prazo, tamanho, tom, orçamento, dependência |
| Insumos e referências | há arquivo, link, dado, pessoa ou exemplo que o executor não acharia sozinho; cada um com o motivo |
| Abordagem sugerida | o caminho já foi decidido (usuário, brainstorming, tentativa que falhou) ou há uma ordem que só o contexto revela; com o porquê. Fora isso, omitir: passo sugerido vira passo seguido, e quem executa escolhe melhor com o material na frente |
| Premissas | algo foi assumido; cada uma com o que fazer se estiver errada |
| Perguntas em aberto | ficou dúvida que não trava o início |
| Entrega esperada | formato, tamanho, destino ou o que reportar ainda não foram ditos |

## Checklist

- [ ] Objetivo é um estado final observável, não uma intenção.
- [ ] Todo critério de aceite é binário: "passou" ou "não passou" sem interpretar.
- [ ] "Como verificar" é executável neste contexto.
- [ ] Toda referência citada existe ou está marcada "a obter" / "a criar".
- [ ] "Não inclui" tem pelo menos um item em `criar`, `transformar` e `planejar`.
- [ ] Formato, tamanho e destino da entrega estão ditos em alguma seção (em código, o Objetivo basta).
- [ ] Toda lacuna virou Premissa com plano B ou Pergunta. Nenhuma frase proibida.
- [ ] Nenhuma seção repete o pedido, outra seção ou a conversa; nada que o usuário não pediu.

## Frases proibidas

Cada uma empurra uma decisão para quem executa. Substituir pela decisão.

`seguir boas práticas` · `garantir qualidade` · `de forma clara e objetiva` · `profissional` · `robusto` · `de forma eficiente` · `se necessário` · `conforme apropriado` · `etc.` · `entre outros` · `tratar adequadamente` · `o público-alvo` · `os stakeholders` · `revisar com cuidado`

Exemplo: "de forma clara e objetiva" → "até 120 palavras, primeira frase diz a data nova, uma desculpa só".

## Não faz

Só executa com `--executar`. Não inventa requisitos: escopo extra vai para "Não inclui". Não escolhe o caminho pelo executor: fixa a chegada e a prova.

## Referências

| Arquivo | Quando ler |
|---------|-----------|
| `references/tipos/<tipo>.md` | Sempre, só o tipo detectado |
| `references/exemplos.md` | Só em dúvida sobre o nível de detalhe |
