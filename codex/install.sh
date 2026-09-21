#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
plugins_dir="${HOME}/plugins"
marketplace="${HOME}/.agents/plugins/marketplace.json"

mkdir -p "$plugins_dir" "$(dirname "$marketplace")"
ln -sfn "$root" "$plugins_dir/oficina"
echo "  $plugins_dir/oficina -> $root"

python3 - "$marketplace" <<'PY'
import json
import sys
from pathlib import Path

path = Path(sys.argv[1])
market = json.loads(path.read_text()) if path.exists() and path.read_text().strip() else {}
market.setdefault("name", "local")
market.setdefault("interface", {"displayName": "Local Plugins"})
plugins = [p for p in market.get("plugins", []) if p.get("name") != "oficina"]
plugins.append({
    "name": "oficina",
    "source": {"source": "local", "path": "./plugins/oficina"},
    "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
    "category": "Developer Tools",
})
market["plugins"] = plugins
path.write_text(json.dumps(market, indent=2, ensure_ascii=False) + "\n")
print(f"  {path} atualizado")
PY

echo
echo "Pronto. Reinicie o Codex, abra /plugins, aba do marketplace local, e instale a oficina."
echo "Skills ficam disponíveis como \$lapidar, \$tdd, \$conferir... e os hooks passam a valer."
