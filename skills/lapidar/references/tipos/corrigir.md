# corrigir

Algo existe e está errado: bug, texto com problema, processo que falha, número que não bate.

Substituir "Contexto" por três seções:

### Sintoma
O que acontece hoje, com a evidência: mensagem exata, print, valor errado, reclamação literal. Se o usuário não deu, dizer que falta: o primeiro critério de aceite passa a ser "evidência literal do sintoma coletada".

### Esperado
O que deveria acontecer. Uma frase.

### Reprodução
Como fazer o problema aparecer de novo. Se não existe reprodução, o primeiro critério de aceite é "existe uma forma de reproduzir".

Acrescentar:

### Hipóteses
Só as que o aterramento sustenta (um log, um commit recente, um padrão no sintoma), no máximo 3, da mais provável para a menos, cada uma com a evidência e **como descartar**. Sem evidência, omitir a seção: hipótese chutada ancora quem investiga, e o `/depurar` levanta as dele depois de reproduzir.

Regras fixas:
- Restrição obrigatória: "não corrigir sem antes reproduzir".
- Critério de aceite obrigatório: "o problema reproduzido antes não reproduz depois".
- Entrega esperada inclui a **causa raiz** em uma frase, não só o que mudou.
