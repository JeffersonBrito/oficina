# Exemplos: antes e depois

Três exemplos de tamanhos e destinos diferentes de propósito. Nomes e referências são plausíveis; a etapa 2 (aterrar) deve sempre conferir contra o contexto real.

---

## Exemplo 1: comunicar (pequeno, leitor sem contexto)

### Antes

> escreve um e-mail pro cliente avisando que a entrega vai atrasar

### Depois

Tipo: **comunicar**. Premissas que mais pesam: existe uma data nova firme, e o cliente ainda não sabe do atraso.

```markdown
# Escrever e-mail à Ana (Contoso) avisando que o módulo de relatórios passa de 25/09 para 02/10

## Contexto
A entrega prometida para 25/09 não sai: uma dependência interna de infra atrasou. Ana perguntou do
status na semana passada e vai encaminhar a resposta ao diretor dela, então o e-mail precisa fazer
sentido para quem não acompanhou o projeto. O último e-mail para ela (12/09) é a referência de tom.

## Objetivo
Ana sabe a data nova e o motivo em 30 segundos e responde confirmando 02/10 ou propondo outra, sem ligar.

## Leitor
Ana, gerente de projeto da Contoso. Acompanha de perto e já cobrou uma vez.

## Tom e tamanho
Como o e-mail de 12/09: cordial e direto. Até 120 palavras, uma desculpa só, no início.

## O que não dizer
Quem ou qual equipe causou o atraso; que "pode atrasar de novo".

## Critérios de aceite
- [ ] A primeira frase traz a data nova (02/10).
- [ ] Assunto mais corpo de até 120 palavras.
- [ ] Nenhum item de "O que não dizer" aparece.
- [ ] Termina pedindo a confirmação da data.

## Como verificar
Contar as palavras e reler como o diretor da Ana, que só recebeu o encaminhamento: dá para dizer o que mudou e o que se pede?

## Premissas
- 02/10 é data firme. Se não for, o e-mail avisa do atraso e promete a data nova até um dia marcado.
- Ana não soube por outro canal. Se soube, abrir pelo que já está pronto e pelo pedido de confirmação.
```

Ficaram de fora, por não mudarem o trabalho: Escopo (ninguém faria bônus num e-mail de 120 palavras), Estrutura (quem escreve acerta a ordem), Abordagem, Entrega esperada (já dita nos critérios).

---

## Exemplo 2: criar (médio, leitor sem contexto)

### Antes

> monta uma apresentação sobre o motor de precatório pra diretoria

### Depois

Tipo: **criar**. Premissas que mais pesam: a diretoria não é técnica e a pergunta implícita é "isso vale o custo?".

```markdown
# Criar apresentação do motor de precatório v2 para a diretoria

## Contexto
O motor lê processos judiciais de precatório e devolve análise estruturada (valores, partes, situação).
Está em produção no `ms-content-server`, com benchmark contra gabarito humano e custo controlado por
processo. A diretoria ainda o vê como "projeto de IA" e vai decidir se amplia o uso para outros
tribunais; ninguém ali é técnico, e a dúvida de fundo é se o resultado paga o custo.

## Objetivo
Ao final, a diretoria sabe o que o motor entrega, quanto custa por processo, qual a taxa de acerto
medida, e decide se aprova a expansão.

## Formato e tamanho
Google Slides no template de `Resultados-Q2.pptx` (Drive do time), mesma densidade. 8 slides mais 1 de
apêndice, 15 minutos de fala + 10 de perguntas. Um número por slide quando houver número.

## Contrato (título de cada slide)
1. O problema: quanto tempo um analista gasta por processo hoje
2. O que o motor faz, em uma frase e um exemplo real (processo anonimizado)
3. Como sabemos que funciona: benchmark contra gabarito humano, taxa de acerto por campo
4. Onde ele erra, e o que acontece quando erra (revisão humana)
5. Custo por processo em BRL, com o teto configurado
6. O que muda com a expansão: tribunais, volume, custo projetado
7. Riscos e como estão sendo tratados (páginas escaneadas, mudanças de layout dos tribunais)
8. A decisão que estamos pedindo

## Casos difíceis
- "E se ele inventar um valor?": o slide 4 responde antes de perguntarem, com a validação determinística e a revisão humana.
- "Por que não usar o ChatGPT direto?": uma linha no slide 2 sobre contexto selecionado por regra e custo controlado.

## Escopo
**Inclui:** notas do apresentador com os números-fonte; apêndice de 1 slide com a metodologia do benchmark.
**Não inclui:** demo ao vivo; detalhes de arquitetura; comparação com fornecedores externos; roadmap além da expansão pedida.

## Requisitos
- Todo número tem fonte nas notas: saída do `benchmark.py` ou do `pricing.py`, com a data da rodada.
- Termo técnico vem traduzido na mesma frase ("LLM (o modelo de linguagem)").

## Restrições
- Taxa de acerto: só a medida no benchmark mais recente, nunca acima.
- Nome de modelo ou fornecedor só no apêndice.

## Insumos e referências
- Relatório da última rodada do benchmark — slides 3 e 4
- Teto de custo em `pricing.py` — slide 5
- Volume de processos por mês e por tribunal — slide 6; a obter com o time de operações

## Critérios de aceite
- [ ] 8 slides mais 1 de apêndice, no template do Q2.
- [ ] Cada número aparece com fonte e data nas notas do apresentador.
- [ ] O slide 8 tem uma pergunta única de decisão, com sim/não.
- [ ] Ensaio cronometrado fecha em até 15 minutos.

## Como verificar
Alguém de fora do time técnico lê só os slides, sem a fala, e diz o que o motor faz, quanto custa e o que está sendo pedido.

## Premissas
- A diretoria decide expansão, não continuidade. Se a dúvida for "manter ou desligar", o slide 1 muda para o custo do trabalho manual atual.
- Existe rodada de benchmark com menos de 30 dias. Se não, rodar antes; a apresentação não sai com número velho.

## Entrega esperada
Link do Google Slides e a lista dos números usados, com fonte e data de cada um.
```

Sem Abordagem sugerida: a ordem de montar um deck não é decisão de quem pediu.

---

## Exemplo 3: criar com `--executar` (executor é esta sessão)

A conversa já mostrou a rota, os testes em `tests/test_orders.py` e a paginação de `GET /customers`.

### Antes

> adiciona paginação no /orders --executar

### Depois

Tipo: **criar**. Premissa que mais pesa: a resposta deixa de ser lista e o único consumidor é o front deste repo.

```markdown
# Adicionar paginação ao GET /orders

## Objetivo
`GET /orders` aceita `page` e `per_page` e devolve `items`, `page`, `per_page` e `total`, no formato de `GET /customers`.

## Casos difíceis
Sem parâmetros → `page=1`, `per_page=20`. `page` além do fim → 200 com `items: []`. `per_page` fora de 1 a 100 → 422.

## Escopo
**Não inclui:** filtros, ordenação configurável, paginação por cursor, mexer em `/customers`.

## Critérios de aceite
- [ ] Sem parâmetros, devolve os 20 pedidos mais recentes e o `total` da tabela.
- [ ] `page=2&per_page=5` devolve do 6º ao 10º pedido.
- [ ] `page` além do fim devolve 200 com `items: []`.
- [ ] `per_page=0` e `per_page=101` devolvem 422.
- [ ] `web/src/api/orders.ts` lê `items` e a listagem do front continua abrindo.

## Como verificar
`pytest tests/test_orders.py -q` e `npm test -- orders` em `web/`.

## Premissas
- O único consumidor da rota é o front deste repo. Se houver consumidor externo, manter a lista como resposta e mandar o total no header `X-Total-Count`.
```

Executando a task acima.

Sem Contexto, Insumos nem Abordagem: tudo isso já está na conversa. O que a task acrescentou foram os casos de borda, o que não entra e a premissa sobre quem consome a rota.

---

## O que os três têm em comum

- Critérios de aceite que alguém marca sem interpretar, e um jeito de verificar que dá para executar.
- O porquê vem em prosa no Contexto, quando o leitor não o tem.
- Premissas dizem **o que fazer se estiverem erradas**, não só que existem.
- Cada seção presente muda o que o executor faria; as ausentes não fariam falta.
- O e-mail tem um terço da apresentação. Proporcional.
