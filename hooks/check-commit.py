#!/usr/bin/env python3
import json
import re
import sys

PREFIX = re.compile(r"^(feat|fix|chore|docs|refactor|test|style|perf|ci|build|revert)(\([^)]*\))?!?:", re.I)
ATTRIBUTION = re.compile(r"co-authored-by|generated with|claude|anthropic", re.I)
PORTUGUESE = re.compile(
    r"[áàâãéêíóôõúç]|\b(adiciona|adicionar|corrige|corrigir|atualiza|atualizar|ajusta|ajustar|cria|criar"
    r"|melhora|melhorar|refatora|refatorar|altera|alterar|muda|mudar|da|das|dos|para|sem|nova|novo)\b",
    re.I,
)
QUOTED = r"(?:\"([^\"]*)\"|'([^']*)'|(\S+))"
MESSAGE_FLAG = re.compile(r"(?:-m|--message)(?:=|\s+)" + QUOTED, re.S)
TITLE_FLAG = re.compile(r"(?:-t|--title)(?:=|\s+)" + QUOTED, re.S)
BODY_FLAG = re.compile(r"(?:-b|--body)(?:=|\s+)" + QUOTED, re.S)
FED_HEREDOC = re.compile(
    r"(?:-m|--message|-b|--body|-F|--file|--body-file)(?:=|\s+)(?:\"?\$\(cat\s+|-\s+)?<<-?\s*['\"]?(\w+)['\"]?\n(.*?)\n\s*\1\b",
    re.S,
)


def read_command():
    try:
        payload = json.load(sys.stdin)
    except ValueError:
        return ""
    return payload.get("tool_input", {}).get("command", "") or ""


def is_commit(command):
    return re.search(r"\bgit\s+commit\b", command) is not None


def is_pr(command):
    return re.search(r"\bgh\s+pr\s+(create|edit)\b", command) is not None


def values(pattern, text):
    return [next(g for g in m.groups() if g is not None) for m in pattern.finditer(text)]


def message_texts(command):
    texts = values(MESSAGE_FLAG, command) + values(TITLE_FLAG, command) + values(BODY_FLAG, command)
    texts += [body for _, body in FED_HEREDOC.findall(command)]
    return texts


def title_of(command):
    pattern = MESSAGE_FLAG if is_commit(command) else TITLE_FLAG
    found = values(pattern, command)
    if found:
        return found[0]
    heredocs = FED_HEREDOC.findall(command)
    return heredocs[0][1] if heredocs else None


def title_problems(title):
    problems = []
    first_line = title.strip().splitlines()[0] if title.strip() else ""
    if not first_line:
        return problems
    if PREFIX.match(first_line):
        problems.append(f'prefixo proibido em "{first_line}": use uma frase, sem "tipo:"')
    if first_line[0].islower():
        problems.append(f'"{first_line}" precisa começar com maiúscula')
    if len(first_line) > 72:
        problems.append(f"título com {len(first_line)} caracteres; máximo 72")
    if PORTUGUESE.search(first_line):
        problems.append(f'"{first_line}" parece português; commits e PRs são em inglês')
    return problems


def main():
    command = read_command()
    if not (is_commit(command) or is_pr(command)):
        return
    problems = []
    if any(ATTRIBUTION.search(text) for text in message_texts(command)):
        problems.append("rodapé de atribuição (Co-Authored-By, Generated with, Claude) é proibido")
    title = title_of(command)
    if title:
        problems.extend(title_problems(title))
    if not problems:
        return
    kind = "commit" if is_commit(command) else "PR"
    sys.stderr.write(f"oficina bloqueou o {kind}. Padrão: frase curta em inglês, capitalizada, sem prefixo, sem atribuição.\n")
    for problem in problems:
        sys.stderr.write(f"- {problem}\n")
    sys.exit(2)


if __name__ == "__main__":
    main()
