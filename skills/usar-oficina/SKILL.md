---
name: usar-oficina
description: Diz qual skill da oficina usar em cada situação e em que ordem. Injetada em toda sessão pelo hook. Use antes de responder a qualquer pedido.
---

# Usar a oficina

Antes de responder a qualquer pedido, inclusive antes de perguntar ou explorar arquivos, decidir por qual skill ele passa. Se uma se aplica: invocar, anunciar em uma linha ("Usando lapidar para transformar esse pedido em task") e seguir. Se depois de ler ela não servir, dizer em uma linha e seguir sem ela.

| O pedido é... | Skill | Termina em |
|---------------|-------|-----------|
| ideia ou dúvida vaga: "quero um X", "não sei se A ou B" | `brainstorming` | um `/lapidar` |
| pedido claro mas curto: "cria X", "escreve Y" | `lapidar` | task com critérios de aceite |
| sintoma: "dá erro", "valor errado", "flaky" | `lapidar` tipo `corrigir`, depois `depurar` | causa raiz |
| implementar código | `tdd` | código com relatório |
| entrega prestes a ser dada como pronta | `conferir` | PRONTO ou NÃO PRONTO |
| commit, push, PR | `entregar` | commit e PR no padrão |
| fim de task com algo não-óbvio | `registrar` | memória ou `CLAUDE.md` |

Cadeia: **brainstorming → lapidar → (depurar) → tdd → conferir → entregar → registrar.** Entrar no ponto que o pedido pede, sem forçar etapas anteriores. Skills de processo primeiro; uma skill de NestJS ou Python entra dentro do `tdd`, para dizer como escrever.

**Nenhuma skill** quando: pergunta que se responde em uma ou duas frases; comando direto e pequeno ("roda os testes", "mostra o diff"); o usuário disse "sem skill". Na dúvida, usar: ler uma que não serve custa uma linha; pular uma que servia custa retrabalho.

| Pensamento | Realidade |
|-----------|-----------|
| "É simples, vou direto" | `lapidar` de pedido simples tem 15 linhas. |
| "Já sei o que fazer" | Saber não é ter critério de aceite. |
| "Corrijo e depois vejo a causa" | `depurar` antes. |
| "Os testes existem, está pronto" | Existir não é passar. `conferir`. |
