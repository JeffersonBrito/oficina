---
name: lapidar
description: Transforma um pedido curto em uma task estruturada (contexto, objetivo, escopo, critérios de aceite, premissas), para qualquer domínio. Use quando invocarem /lapidar ou pedirem para estruturar, detalhar ou expandir um pedido, prompt ou tarefa.
---

# Lapidar

Pedido bruto entra; sai uma task que outra sessão, um subagente ou uma pessoa executa sem adivinhar. O pedido vem em `$ARGUMENTS` ou na mensagem. Flags no final: `--salvar` grava em `.claude/prompts/AAAA-MM-DD-<slug>.md` (ou `~/.claude/prompts/` fora de projeto); `--executar` gera e, na mesma resposta, executa.

Regra central: nenhuma decisão importante fica implícita, e o tamanho é proporcional ao pedido. E-mail de três linhas vira task de 15 linhas; apresentação para diretoria vira 60. Nunca inflar.

## Fluxo

1. **Classificar** pelo resultado final: `criar` (algo novo) · `corrigir` (algo que existe voltar a funcionar) · `transformar` (mesmo conteúdo, outra forma) · `investigar` (resposta com evidência) · `decidir` (recomendação entre opções) · `planejar` (passos no tempo) · `comunicar` (mensagem para alguém). Ler **só** `references/tipos/<tipo>.md` para as seções extras. Híbrido usa o tipo do resultado final.
2. **Aterrar** (no máximo uns 2 minutos): conversa atual, arquivos citados, memória, repositório se envolver código, e o que já existe do mesmo tipo (e-mail anterior, doc no padrão). A task cita nomes, números e caminhos reais. Sem contexto, cada lacuna vira premissa.
3. **Lacunas**: o que o pedido não diz e muda o trabalho. Dá para assumir → Premissa, com o que fazer se estiver errada. Leituras diferentes dariam trabalhos materialmente diferentes (o executor perderia mais de 20% do esforço) → pergunta, no máximo 3, em uma rodada (AskUserQuestion). Em sessão autônoma, assumir a mais provável e registrar.
4. **Escrever** no formato abaixo. Seção vazia é removida, nunca "N/A". Idioma do pedido; código e nomes próprios como estão.
5. **Checklist**; corrigir o que falhar antes de entregar.
6. **Entregar**: uma linha com o tipo e as 1-2 premissas que mais pesam, depois a task em um bloco ```markdown. Sem flag: nada depois do bloco e **não executar**. `--salvar`: gravar e mostrar o caminho. `--executar`: logo após o bloco escrever "Executando a task acima." e executar como se fosse o pedido do usuário, seguindo Requisitos, Restrições e Premissas; ao fim, reportar item a item contra os Critérios de aceite e dizer quais premissas se confirmaram. Parar só se uma Pergunta em aberto travar o início.

## Formato da task

````markdown
# <Verbo no imperativo + objeto concreto + para quem, se houver>

## Contexto
<2 a 5 linhas: o que existe hoje, por que a tarefa existe, o que dói. Nomes e referências reais.>

## Objetivo
<1 a 2 frases. Estado final observável: "X passa a fazer/ter/ser Y", não "melhorar X".>

## Escopo
**Inclui:** <o que entra>
**Não inclui:** <o que alguém faria "de bônus" e não deve>

## Requisitos
- <o que o resultado precisa ter ou fazer, um por linha, verificável>

## Restrições
- <o que não pode mudar ou ultrapassar: prazo, tamanho, tom, orçamento, dependências>

## Insumos e referências
- <arquivo, link, dado, pessoa, exemplo anterior> — por que importa

## Abordagem sugerida
1. <passos em ordem, cada um com resultado observável>

Sugerida, não obrigatória: caminho melhor ao executar vale, dizendo por quê.

## Critérios de aceite
- [ ] <afirmação binária e testável: "o teste X passa", "o e-mail cabe em uma tela de celular">

## Como verificar
<comando exato, checklist de leitura, comparar com o exemplo Y, ou quem revisa>

## Premissas
- <o que foi assumido, e o que fazer se estiver errado>

## Perguntas em aberto
- <só as que não travam o início>

## Entrega esperada
<formato, tamanho, destino, para quem, e o que reportar: o que ficou de fora e por quê>
````

## Checklist

- [ ] Objetivo é um estado final observável, não uma intenção.
- [ ] Todo critério de aceite é binário: "passou" ou "não passou" sem interpretar.
- [ ] Toda referência citada existe ou está marcada "a obter" / "a criar".
- [ ] "Como verificar" é executável neste contexto; "revisar com cuidado" não vale.
- [ ] "Não inclui" tem pelo menos um item em `criar`, `transformar` e `planejar`.
- [ ] "Entrega esperada" diz formato, tamanho e destino.
- [ ] Nenhuma frase proibida. Toda lacuna virou Premissa ou Pergunta.
- [ ] Nada acrescentado que o usuário não pediu; tamanho proporcional.

## Frases proibidas

Cada uma empurra uma decisão para quem executa. Substituir pela decisão.

`seguir boas práticas` · `garantir qualidade` · `de forma clara e objetiva` · `profissional` · `robusto` · `de forma eficiente` · `se necessário` · `conforme apropriado` · `etc.` · `entre outros` · `tratar adequadamente` · `o público-alvo` · `os stakeholders` · `revisar com cuidado`

Exemplo: "de forma clara e objetiva" → "até 120 palavras, primeira frase diz a data nova, uma desculpa só".

## Não faz

Não executa sem `--executar`. Não inventa requisitos: escopo extra vai para "Não inclui". A abordagem sugerida é ponto de partida, não contrato.

## Referências

| Arquivo | Quando ler |
|---------|-----------|
| `references/tipos/<tipo>.md` | Sempre, só o tipo detectado |
| `references/exemplos.md` | Só em dúvida sobre o nível de detalhe |
