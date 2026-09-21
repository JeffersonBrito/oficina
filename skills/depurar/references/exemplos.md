# Exemplo: valor errado no benchmark

Sintoma trazido: "o benchmark tá dando valor diferente do gabarito nos processos escaneados".

## Passo 0: congelar

- **O que acontece:** caso `0006817-82`, campo `valor_principal`: obtido `R$ 12.345,00`, gabarito `R$ 123.450,00`. Saída literal do benchmark colada.
- **Desde quando:** apareceu depois do commit que trocou o renderizador de página para imagem (há 4 dias). Antes disso o caso batia.
- **Onde reproduz:** só em processos com página transcrita de imagem. Nativos batem.

## Passo 1: reproduzir

```bash
python -m app.lawsuit.precatorio_v2.benchmark --caso 0006817-82
```
→ diverge toda vez. Teste de reprodução escrito: `tests/test_document_values.py::test_valor_principal_pagina_transcrita`, falhando.

## Passo 2: localizar

Bissecção no caminho: salvar o texto transcrito da página 214 antes de `enrich_from_document`. O texto contém `123 450,00` (espaço no lugar do ponto de milhar). O bug está **depois** da transcrição: no parser de valores, ou na própria transcrição que perdeu o ponto. Reduzir input: uma linha, `Principal corrigido: 123 450,00`, reproduz.

## Passo 3: hipóteses

| Hipótese | Se for isso, então | Resultado |
|----------|--------------------|-----------|
| 1. O parser de valores lê `123 450,00` como `12.345,00`, ignorando o espaço e perdendo um dígito | O parser com a string reduzida devolve `12345.00` | **confirmada**: `parse_valor("123 450,00")` → `12345.0`; regex captura `[\d.]+,\d{2}` e para no espaço |
| 2. A transcrição gera o espaço e antes gerava ponto | O texto de 4 dias atrás tem `123.450,00` | confirmada também: o renderizador novo tem resolução menor e o modelo de transcrição lê o ponto como espaço |
| 3. O gabarito está errado | `verificado_em` aponta para outra página | descartada: aponta para a página 214, valor confere no PDF |

## Passo 4: causa raiz

**Causa raiz:** o parser de valores só aceita ponto como separador de milhar, e a transcrição de imagem em resolução menor devolve espaço; o número perde um dígito silenciosamente.
**Por que não foi pego antes:** o teste do parser só cobria valores com ponto; nenhum caso escaneado no gabarito tinha valor acima de 100 mil até esse.

## Passo 5: corrigir pelo tdd

Correção mínima na causa: o parser aceita espaço, ponto ou nada como separador de milhar, e **rejeita** (devolve `None` com aviso) quando o resultado tem menos dígitos que a string original. Teste de reprodução passa; suíte `pytest -q` → 231 passed. A resolução do renderizador é registrada como task separada, não misturada.

## Passo 6: fechar

- Benchmark completo: caso `0006817-82` bate; nenhum nativo regrediu.
- Irmãos: `grep -rn "\\d+,\\d{2}" app/lawsuit/precatorio_v2/` encontra a mesma regex em `pricing.py` para ler valores do documento; mesmo bug em potencial, corrigido no mesmo diff com teste próprio.

## O que este exemplo mostra

- A evidência literal (o valor exato) apontou a natureza do erro: dígito perdido, não valor inventado.
- A bissecção no caminho decidiu em um passo se o problema era transcrição ou parser: eram os dois, e a correção foi no que era responsabilidade do código.
- Cada hipótese tinha uma previsão que podia dar errado.
- A causa raiz tem duas frases e nenhum "acho".
- A correção não foi `try/except` nem "ignorar espaço": foi aceitar o formato **e** detectar perda de dígito, porque a causa raiz era silêncio na perda.
