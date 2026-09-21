#!/usr/bin/env bash
set -euo pipefail
root="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"

strip_frontmatter() {
  awk 'NR == 1 && $0 == "---" { skipping = 1; next } skipping && $0 == "---" { skipping = 0; next } !skipping' "$1"
}

echo "<oficina-usar>"
strip_frontmatter "$root/skills/usar-oficina/SKILL.md"
echo "</oficina-usar>"
echo
echo "<oficina-padroes>"
cat "$root/docs/padroes.md"
echo "</oficina-padroes>"
