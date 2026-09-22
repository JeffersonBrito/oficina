# Exemplos: antes e depois

Três exemplos de domínios diferentes e tamanhos diferentes de propósito. Nomes e referências são plausíveis; a etapa 2 (aterrar) deve sempre conferir contra o contexto real.

---

## Exemplo 1: comunicar (pequeno)

### Antes

> escreve um e-mail pro cliente avisando que a entrega vai atrasar

### Depois

Tipo: **comunicar**. Premissas que mais pesam: o cliente ainda não sabe do atraso, e existe uma data nova para oferecer.

```markdown
# Escrever e-mail à Contoso avisando do atraso da entrega do módulo de relatórios

## Contexto
A entrega prometida para 25/09 não vai acontecer. A causa é interna (dependência de infra que
atrasou). O cliente é a Contoso, contato Ana (gerente de projeto), que já perguntou do status na
semana passada. Último e-mail trocado com ela: 12/09, tom cordial e direto.

## Objetivo
Ana lê o e-mail, sabe a nova data e o motivo em 30 segundos, e aprova sem precisar ligar.

## Leitor
Ana, gerente de projeto da Contoso. Já acompanha de perto, vai reportar para o diretor dela.
Precisa de algo que ela consiga encaminhar sem editar.

## O que ela deve fazer depois
Responder confirmando que a nova data (02/10) funciona, ou propor outra.

## Tom e tamanho
Direto, sem cerimônia, no padrão do e-mail de 12/09. Até 120 palavras. Uma desculpa, no início, sem repetir.

## O que não dizer
- Nome da equipe ou pessoa responsável pelo atraso interno.
- Que "pode atrasar de novo". Se houver risco, dizer o que está sendo feito para não atrasar.

## Estrutura
1. Primeira frase: a entrega de 25/09 passa para 02/10.
2. Motivo em uma linha, sem jargão.
3. O que já está pronto e o que falta.
4. Pedido: confirmar a data ou sugerir outra.

## Critérios de aceite
- [ ] A primeira frase contém a data nova.
- [ ] Até 120 palavras.
- [ ] Nenhum item de "O que não dizer" aparece.
- [ ] Termina com um pedido claro de resposta.

## Como verificar
Ler em voz alta como se fosse a Ana encaminhando para o diretor: precisa fazer sentido sem contexto extra.

## Premissas
- Existe uma data nova firme (02/10). Se não houver, o e-mail muda: avisa do atraso e promete data até dia X.
- Ana não foi avisada por outro canal. Se já foi, cortar a estrutura para os itens 3 e 4.

## Entrega esperada
Texto do e-mail com assunto, pronto para colar. Sem versões alternativas.
```

---

## Exemplo 2: criar (médio)

### Antes

> monta uma apresentação sobre o motor de precatório pra diretoria

### Depois

Tipo: **criar**. Premissas que mais pesam: a diretoria não é técnica e a pergunta implícita é "isso vale o custo?".

```markdown
# Criar apresentação do motor de precatório v2 para a diretoria

## Contexto
O motor lê processos judiciais de precatório e devolve análise estruturada (valores, partes, situação).
Está em produção no `ms-content-server`, com benchmark contra gabarito humano e custo controlado por
processo. A diretoria ainda o vê como "projeto de IA" e vai decidir se amplia o uso para outros tribunais.

## Objetivo
Ao final, a diretoria sabe o que o motor entrega, quanto custa por processo, qual a taxa de acerto
medida, e decide se aprova a expansão.

## Formato e tamanho
Google Slides, 8 slides, 15 minutos de fala + 10 de perguntas. Texto grande, um número por slide quando houver número.

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
- "E se ele inventar um valor?": slide 4 precisa responder antes de perguntarem. Mostrar a camada determinística de validação e a revisão humana.
- "Por que não usar o ChatGPT direto?": uma linha no slide 2 sobre contexto selecionado por regra e custo controlado.

## Referência de estilo
Apresentação de resultados do Q2 (arquivo `Resultados-Q2.pptx` no Drive do time): mesmo template, mesma densidade.

## Escopo
**Inclui:** os 8 slides, notas do apresentador com os números-fonte, um apêndice de 1 slide com a metodologia do benchmark.
**Não inclui:** demo ao vivo; detalhes de arquitetura; comparação com fornecedores externos; roadmap além da expansão pedida.

## Requisitos
- Todo número tem fonte: saída do `benchmark.py` ou do `pricing.py`, com a data da rodada.
- Nenhum termo técnico sem tradução na mesma frase ("LLM (o modelo de linguagem)").
- Exemplo real do slide 2 é anonimizado.

## Restrições
- Não prometer taxa de acerto acima da medida no benchmark mais recente.
- Não citar nome de modelo ou fornecedor nos slides principais (vai para o apêndice).

## Insumos e referências
- Última rodada do benchmark (rodar ou pegar o relatório mais recente) — slides 3 e 4
- Configuração de teto de custo em `pricing.py` — slide 5
- Volume atual de processos por mês e por tribunal — slide 6, a obter com o time de operações
- `Resultados-Q2.pptx` — template

## Abordagem sugerida
1. Levantar os números (benchmark, custo, volume) e anotar a fonte de cada um.
2. Escrever as notas do apresentador de cada slide antes dos slides: se a nota não fecha, o slide não fecha.
3. Montar os slides no template.
4. Ensaiar em 15 minutos cronometrados; cortar o que passar.

## Critérios de aceite
- [ ] 8 slides mais 1 de apêndice, no template do Q2.
- [ ] Cada número aparece com a fonte nas notas do apresentador.
- [ ] O slide 8 tem uma pergunta única de decisão, com sim/não.
- [ ] Ensaiado em até 15 minutos.

## Como verificar
Alguém de fora do time técnico lê só os slides, sem a fala, e consegue dizer o que o motor faz, quanto custa e o que está sendo pedido.

## Premissas
- A diretoria decide expansão, não continuidade. Se a dúvida for "manter ou desligar", o slide 1 muda para o custo do trabalho manual atual.
- Existe rodada de benchmark recente (menos de 30 dias). Se não, rodar antes; a apresentação não sai com número velho.

## Entrega esperada
Link do Google Slides com notas preenchidas, e uma lista dos números usados com a fonte e a data de cada um.
```

---

## O que os dois têm em comum

- Nenhuma referência genérica: cada arquivo, pessoa ou número citado tem motivo.
- Critérios de aceite que alguém marca sem interpretar.
- "Não inclui" segura o escopo.
- Premissas dizem **o que fazer se estiverem erradas**, não só que existem.
- O e-mail é um terço da apresentação. Proporcional.
