#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path

HOOK = Path(__file__).with_name("check-commit.py")

CASES = [
    (0, 'git commit -m "Add conferir skill"', "message in the standard"),
    (0, 'ln -sfn x ~/.claude/skills/conferir && git commit -m "Add conferir skill"', "path containing claude outside the message"),
    (0, 'git status && cat ~/.claude/settings.json', "not a commit"),
    (0, 'git commit -m "Do not retry on 409"', "english word Do"),
    (0, 'git commit -m "Update homepage link" -m "Points to github.com"', "com inside a domain"),
    (0, 'gh pr create --title "Add tdd skill" --body "Adds the skill"', "clean PR"),
    (0, "python3 - <<'EOF'\ns = 'Claude Code'\nEOF\ngit commit -m \"Update docs\"", "heredoc not feeding the commit"),
    (2, 'git commit -m "feat: add skill"', "prefix"),
    (2, 'git commit -m "add skill"', "lowercase"),
    (2, 'git commit -m "Adiciona skill de brainstorming"', "portuguese"),
    (2, 'git commit -m "Add skill" -m "Co-Authored-By: Claude <x>"', "attribution in second -m"),
    (2, 'git commit -m "$(cat <<\'EOF\'\nAdd skill\n\nGenerated with Claude Code\nEOF\n)"', "attribution in heredoc message"),
    (2, "git commit -F - <<'EOF'\nAdd skill\n\nCo-Authored-By: someone\nEOF", "attribution in -F heredoc"),
    (2, 'gh pr create --title "Add tdd skill" --body "Generated with Claude Code"', "attribution in PR body"),
    (2, 'gh pr create --title "fix: broken link" --body "x"', "PR title with prefix"),
]


def run(command):
    payload = json.dumps({"tool_input": {"command": command}})
    result = subprocess.run([sys.executable, str(HOOK)], input=payload, capture_output=True, text=True)
    return result.returncode, result.stderr


def main():
    failures = 0
    for expected, command, label in CASES:
        code, stderr = run(command)
        status = "ok  " if code == expected else "FAIL"
        failures += code != expected
        print(f"{status} expected {expected} got {code}: {label}")
        if code != expected and stderr:
            print("     " + stderr.strip().replace("\n", "\n     "))
    print(f"\n{len(CASES) - failures}/{len(CASES)} passed")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
