#!/usr/bin/env bash
# Builds MyST html with base path, builds JupyterLite into lite/, assembles site/
set -euo pipefail
cd "$(dirname "$0")/.."

rm -rf site _build/html _build/lite
BASE_URL=/demo-web-notebooks npx myst build --html
mkdir -p site
cp -r _build/html/. site/
cp public/site.json public/thumbnail.svg site/
.venv/bin/jupyter lite build --contents notebooks --output-dir site/lite --lite-dir _build/litedir --base-url /demo-web-notebooks/lite/
python3 scripts/inject_back_link.py site/lite
touch site/.nojekyll
