#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
skills_dir="${HOME}/.agents/skills"
agents_file="${HOME}/.codex/AGENTS.md"
start="<!-- oficina:start -->"
end="<!-- oficina:end -->"

strip_frontmatter() {
  awk 'NR == 1 && $0 == "---" { skipping = 1; next } skipping && $0 == "---" { skipping = 0; next } !skipping' "$1"
}

link_skills() {
  mkdir -p "$skills_dir"
  for skill in "$root"/skills/*/; do
    name="$(basename "$skill")"
    ln -sfn "${skill%/}" "$skills_dir/$name"
    echo "  \$$name -> $skills_dir/$name"
  done
}

oficina_block() {
  echo "$start"
  echo "Bloco gerado por oficina/codex/install.sh. Não editar à mão; rode o script de novo para atualizar."
  echo
  strip_frontmatter "$root/skills/usar-oficina/SKILL.md" | sed -E 's#`/([a-z-]+)`#`$\1`#g; s#/(brainstorming|lapidar|depurar|tdd|conferir|entregar|registrar)\b#$\1#g'
  echo
  cat "$root/docs/padroes.md"
  echo "$end"
}

write_agents() {
  mkdir -p "$(dirname "$agents_file")"
  touch "$agents_file"
  if grep -qF "$start" "$agents_file"; then
    awk -v s="$start" -v e="$end" '$0 == s { skipping = 1 } !skipping { print } $0 == e { skipping = 0 }' "$agents_file" > "$agents_file.tmp"
  else
    cp "$agents_file" "$agents_file.tmp"
  fi
  { cat "$agents_file.tmp"; [ -s "$agents_file.tmp" ] && echo; oficina_block; } > "$agents_file"
  rm "$agents_file.tmp"
  echo "  $agents_file atualizado"
}

echo "Skills:"
link_skills
echo "AGENTS.md:"
write_agents
echo
echo "Pronto. Reinicie o Codex. Invoque com \$lapidar, \$tdd, \$conferir..."
