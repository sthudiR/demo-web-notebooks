#!/usr/bin/env bash
# Serves the built site/ under /demo-web-notebooks/ exactly like GitHub Pages (lite/ only exists in a full build).
set -euo pipefail
cd "$(dirname "$0")/.."
[ -d site/lite ] || bash scripts/build.sh
rm -rf .preview && mkdir -p .preview && ln -s ../site .preview/demo-web-notebooks
echo "Open http://localhost:3001/demo-web-notebooks/"
python3 -m http.server 3001 --directory .preview
