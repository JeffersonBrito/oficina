---
name: usar-oficina
description: Diz qual skill da oficina usar em cada situação e em que ordem. Injetada no início de toda sessão pelo hook do plugin. Use antes de responder a qualquer pedido, incluindo perguntas de esclarecimento, para decidir se um pedido passa por brainstorming, lapidar, depurar, tdd, conferir, entregar ou registrar.
---

# Usar a oficina

Antes de responder a qualquer pedido, decidir por qual skill ele passa. A decisão vem **antes** de perguntar, explorar arquivos ou começar a fazer. Se uma skill se aplica, invocar, anunciar em uma linha ("Usando lapidar para transformar esse pedido em task") e seguir o que ela diz. Se depois de ler a skill ela não servir, dizer isso em uma linha e seguir sem ela.

## Qual skill

| O pedido é... | Skill | Termina em |
|---------------|-------|-----------|
| Uma ideia ou dúvida ainda vaga: "quero um X", "não sei se A ou B", "como resolvo Y" | `brainstorming` | um comando `/lapidar` |
| Um pedido claro mas curto: "cria X", "escreve Y", "muda Z" | `lapidar` | uma task com critérios de aceite |
| Um sintoma: "dá erro", "tá quebrando", "valor errado", "flaky" | `lapidar` tipo `corrigir`, depois `depurar` | causa raiz explicada |
| Implementar código (feature, correção, mudança de comportamento) | `tdd` | código com relatório critério a critério |
| Qualquer entrega prestes a ser declarada pronta | `conferir` | PRONTO ou NÃO PRONTO |
| Fechar o trabalho em código: commit, push, PR | `entregar` | commit e PR no padrão da casa |
| Fim de uma task com algo não-óbvio aprendido | `registrar` | memória ou `CLAUDE.md` atualizado |

A cadeia inteira: **brainstorming → lapidar → (depurar) → tdd → conferir → entregar → registrar.** Entrar no ponto que o pedido pede; não forçar as etapas anteriores. Pedido claro não precisa de brainstorming. Entrega sem código não passa pelo tdd nem pelo entregar.

## Ordem quando mais de uma se aplica

Skills de processo primeiro, skills de domínio depois. "Cria o endpoint de cadastro" é `lapidar` → `tdd` → `conferir`; uma skill de NestJS ou de Python entra **dentro** do `tdd`, para dizer como escrever, não se escreve com teste.

## Quando não usar nenhuma

- Pergunta que se responde em uma ou duas frases, sem produzir nada.
- Comando direto e pequeno: "roda os testes", "mostra o diff", "abre o arquivo X".
- O usuário disse explicitamente "sem skill" ou "direto".

Na dúvida, usar. O custo de ler uma skill que não serve é uma linha; o custo de pular uma que servia é retrabalho.

## Sinais de que está pulando etapa

| Pensamento | Realidade |
|-----------|-----------|
| "É simples, vou direto" | Simples vira complexo no meio. `lapidar` de um pedido simples tem 15 linhas. |
| "Preciso entender o código antes de decidir a skill" | A skill diz como entender. Decidir primeiro. |
| "Já sei o que fazer" | Saber o que fazer não é ter critério de aceite. `lapidar`. |
| "Vou corrigir e depois vejo a causa" | Sintoma escondido. `depurar` antes. |
| "Os testes existem, está pronto" | Existir não é passar. `conferir`. |
| "Commito rápido para não perder" | Commit fora do padrão vai ser bloqueado. `entregar`. |
| "Isso eu lembro na próxima" | Não lembra. `registrar`. |
