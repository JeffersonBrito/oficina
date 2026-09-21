# Seções extras por tipo

O formato base do `SKILL.md` vale para todos os tipos. Cada tipo abaixo **acrescenta** seções ou muda a ênfase. Inserir as seções extras logo depois de "Objetivo", antes de "Escopo".

---

## criar

O resultado é algo novo: texto, apresentação, planilha, código, design, curso, campanha.

### Formato e tamanho
Qual é o artefato final, concretamente: "deck de 8 slides em Google Slides", "função Python com assinatura X", "post de 300 palavras no LinkedIn", "planilha com 3 abas". Se o usuário não disse, propor e marcar como premissa.

### Contrato
Só quando faz sentido: a interface que o artefato expõe antes de existir. Em código: assinatura, rota, schema. Em texto: estrutura de seções com uma linha cada. Em apresentação: título de cada slide.

### Casos difíceis
Os inputs ou situações em que o artefato precisa ter comportamento definido: em código, vazio/nulo/duplicado/concorrente; em texto, o leitor cético ou o que já leu a versão anterior; em apresentação, a pergunta incômoda que vão fazer.

### Referência de estilo
Um exemplo existente que o resultado deve parecer. Se não existe, dizer isso.

Ênfase: "Não inclui" é obrigatório. `criar` é onde mais aparece escopo de bônus.

---

## corrigir

Algo existe e está errado: bug, texto com problema, processo que falha, número que não bate.

Substituir "Contexto" por três seções:

### Sintoma
O que acontece hoje, com a evidência: mensagem exata, print, valor errado, reclamação literal. Se o usuário não deu, a primeira etapa da Abordagem é obter.

### Esperado
O que deveria acontecer. Uma frase.

### Reprodução
Como fazer o problema aparecer de novo. Se não existe reprodução, o primeiro critério de aceite é "existe uma forma de reproduzir".

Acrescentar:

### Hipóteses
No máximo 3, cada uma com **como descartar** (o que olhar, rodar ou perguntar). Da mais provável para a menos.

Regras fixas:
- Restrição obrigatória: "não corrigir sem antes reproduzir".
- Critério de aceite obrigatório: "o problema reproduzido antes não reproduz depois".
- Entrega esperada inclui a **causa raiz** em uma frase, não só o que mudou.

---

## transformar

O mesmo conteúdo em outra forma: resumir, traduzir, reescrever, simplificar, refatorar, converter formato, adaptar para outro público.

### Invariantes
O que **não pode mudar**: fatos, números, decisões, comportamento, tom da marca. E como provar: "cada número do original aparece no resumo", "todos os testes passam sem alteração", "o glossário do cliente é respeitado".

### O que muda
Explicitamente: tamanho, idioma, estrutura, nível técnico, forma.

### Motivação
Por que mexer no que já existe. Uma dor concreta.

Regras fixas:
- "Não inclui" obrigatório: "corrigir erros de conteúdo encontrados no caminho" (registrar e separar, não misturar).
- Critério de aceite obrigatório: um teste de invariante concreto.

---

## investigar

O resultado é uma resposta com evidência: análise, pesquisa, diagnóstico.

Substituir "Requisitos" e "Critérios de aceite" por:

### Pergunta central
Uma pergunta só, respondível. "Por que as vendas caíram?" não; "qual canal perdeu mais receita entre março e agosto, e a queda começou antes ou depois da mudança de preço?" sim.

### Fontes a consultar
Arquivos, dados, logs, docs, pessoas, sites. Em ordem de prioridade, com o que cada uma pode responder.

### O que conta como resposta
Formato (tabela, ranking, sim/não com evidência, texto de N parágrafos) e o nível de confiança mínimo. "Depende" não é resposta: se depender, dizer de quê e qual é o caso mais comum.

### Critérios de aceite
- [ ] A resposta cita a evidência (fonte, número, trecho).
- [ ] Alternativas descartadas aparecem com o motivo.
- [ ] Termina com uma recomendação, mesmo que seja "não fazer nada".

---

## decidir

O resultado é uma recomendação entre opções.

### Opções em jogo
As candidatas, nomeadas. Se o usuário deu só uma ("vale a pena X?"), a segunda é sempre "não fazer nada / manter como está".

### Critérios de comparação
No máximo 5, com peso ou ordem. Custo, prazo, risco, esforço, reversibilidade. Sem critério explícito, a comparação vira opinião.

### Quem decide e até quando
Quem bate o martelo e o prazo. Muda o nível de detalhe da recomendação.

Critérios de aceite obrigatórios:
- [ ] Tabela opções × critérios preenchida com fatos, não adjetivos.
- [ ] Uma recomendação única, com a condição em que ela deixaria de valer.
- [ ] O que seria preciso para reverter a decisão depois.

---

## planejar

O resultado é uma sequência de passos no tempo: roadmap, cronograma, semana, projeto, plano de estudo.

### Horizonte e capacidade
Até quando, e quantas horas ou pessoas por semana. Sem isso, o plano é uma lista de desejos.

### Marcos
Os 2 a 5 pontos onde dá para dizer "chegamos aqui". Cada um com o que fica visível ou entregue.

### Dependências e riscos
O que precisa acontecer antes de quê, e o que pode atrasar tudo. Para cada risco, o plano B em uma linha.

### Como acompanhar
Onde o plano vive (arquivo, board, calendário) e com que frequência é revisto.

Critérios de aceite obrigatórios:
- [ ] Cada item tem dono (mesmo que seja "eu") e data ou semana.
- [ ] A soma do esforço cabe na capacidade declarada.
- [ ] O primeiro passo pode começar hoje.

---

## comunicar

O resultado é uma mensagem que chega a alguém: e-mail, post, anúncio, feedback, apresentação para pessoas.

### Leitor
Quem lê, o que já sabe, o que sente sobre o assunto hoje. "Cliente que já reclamou do atraso duas vezes" é diferente de "cliente novo".

### O que o leitor deve fazer ou sentir depois
Uma frase. "Aprovar a nova data sem ligar", "entender que o risco é baixo", "responder com a informação X até sexta". Esse é o critério de aceite principal.

### Tom e tamanho
Direto ou cerimonioso; limite de palavras, slides ou minutos. Se existe mensagem anterior à mesma pessoa, apontar como referência.

### O que não dizer
Informação que não deve aparecer: preço interno, nome de quem errou, promessa que não dá para cumprir.

### Estrutura
Os blocos em ordem, com uma linha do que vai em cada. Primeira frase sempre carrega a informação principal.

Critérios de aceite obrigatórios:
- [ ] A primeira frase responde "o que aconteceu / o que eu quero de você".
- [ ] Nenhum item de "O que não dizer" aparece.
- [ ] Cabe no tamanho declarado.
