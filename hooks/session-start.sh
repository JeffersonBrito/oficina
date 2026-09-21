#!/usr/bin/env bash
set -euo pipefail
root="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
echo "<oficina-padroes>"
cat "$root/docs/padroes.md"
echo "</oficina-padroes>"
