# Anti-padrões de teste

Cada um destes já produziu suíte verde com bug em produção. Ler ao criar mock, fixture ou helper.

## 1. Testar o mock

```python
servico.enviar = Mock()
processar(pedido)
servico.enviar.assert_called_once()   # prova que chamou; não prova que o que chamou está certo
```

O teste passa se `processar` chamar `enviar` com qualquer coisa. Trocar por asserção sobre o **efeito**: o que foi enviado, o estado depois, o valor retornado. `assert_called_with(...)` com os argumentos exatos é o mínimo aceitável, e só quando o efeito real é inobservável.

## 2. Mockar o que está sendo testado

Mockar `calcular_total` para testar `fechar_pedido`, que só existe para chamar `calcular_total`. O teste vira tautologia. Mock é para a **fronteira**: rede, relógio, aleatoriedade, banco externo, serviço pago, sistema de arquivos quando for lento. O resto roda de verdade.

## 3. Método só-para-teste no código de produção

`reset_for_tests()`, `_set_clock()`, `if TESTING:`. O código de produção passa a ter dois comportamentos, e o testado é o que ninguém usa. Trocar por injeção de dependência: o relógio, a conexão, o cliente HTTP entram pelo construtor ou por parâmetro.

## 4. Snapshot como asserção principal

`expect(resultado).toMatchSnapshot()` sem ler o snapshot congela o que saiu, certo ou errado, e a primeira execução sempre passa. Aceitável para saídas grandes e estáveis (HTML renderizado) **depois** de uma asserção explícita do que importa. Nunca como único teste.

## 5. Teste que espelha a implementação

```python
def test_desconto():
    assert calcular(100, "premium") == 100 * 0.9
```

Se a regra mudar para `0.85`, o teste continua "certo" ao ser atualizado junto, e nunca teria pego um bug em `0.9`. Escrever o valor esperado como fato: `== 90`. Teste é especificação, não cópia.

## 6. Ordem entre testes

Teste B só passa se A rodou antes (deixou registro no banco, mudou variável global). Rodar em ordem aleatória (`pytest -p randomly`, `jest --randomize`) pega isso. Cada teste monta e desmonta o próprio estado.

## 7. Fixture gigante compartilhada

Um `conftest.py` que cria 40 objetos para todo teste. Ninguém sabe o que cada teste precisa, e mudar a fixture quebra testes sem relação. Fixture pequena por necessidade; composição em vez de uma fixture-mundo.

## 8. `sleep` para esperar assíncrono

`time.sleep(1)` / `await new Promise(r => setTimeout(r, 1000))` no teste. Lento e intermitente. Trocar por `await` no que se espera, fake timers, ou polling com timeout curto sobre a condição real.

## 9. Engolir exceção

```python
try:
    resultado = funcao()
except Exception:
    pass
assert True
```

Passa sempre. Deixar o erro subir. Erro esperado usa `pytest.raises` / `toThrow` com o tipo e, quando importa, a mensagem.

## 10. Cobertura como meta

100% de linhas cobertas com asserções fracas é pior que 70% com asserções honestas: dá confiança sem base. Cobertura aponta o que **não** foi testado; não diz nada sobre o que foi. A pergunta continua sendo "se eu quebrar isso, algum teste falha?".
