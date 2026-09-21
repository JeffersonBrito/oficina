---
name: nome-da-skill
description: Uma frase dizendo o que a skill faz + quando usar, com as palavras que o usuário provavelmente vai dizer ("estruturar", "expandir", "/nome-da-skill"). Essa descrição é o único critério que o Claude usa para decidir se carrega a skill, então ela precisa ser específica.
---

# Nome da skill

Uma ou duas frases: o que entra, o que sai.

## Princípio

A ideia central em um parágrafo. O que faz esta skill ser diferente de simplesmente pedir ao modelo.

## Fluxo

### 1. <Primeira etapa>
O que fazer, com critério de parada.

### 2. <Segunda etapa>
...

## Formato da saída

O formato exato, em um bloco de código, para o resultado ser previsível.

## Checklist de qualidade

- [ ] Item binário: dá para dizer "passou" ou "não passou".
- [ ] ...

## O que esta skill NÃO faz

- Limites explícitos evitam que ela invada o território de outra skill.

## Referências

| Arquivo | Quando ler |
|---------|-----------|
| `references/x.md` | Só quando ... (progressive disclosure: o SKILL.md fica curto, o detalhe vai para cá) |
