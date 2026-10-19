#!/usr/bin/env bash
# Builds MyST html with base path, builds JupyterLite into lite/, assembles site/
set -euo pipefail
cd "$(dirname "$0")/.."

rm -rf site _build/html _build/lite
BASE_URL=/demo-web-notebooks npx myst build --html
mkdir -p site
cp -r _build/html/. site/
cp public/site.json public/thumbnail.svg public/preview.webm public/preview.mp4 site/
# GoatCounter analytics on the MyST pages
find site -name '*.html' -not -path 'site/lite/*' -exec sed -i 's|</head>|<script data-goatcounter="https://demo-web.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script></head>|' {} +
.venv/bin/jupyter lite build --contents notebooks --output-dir site/lite --lite-dir _build/litedir --base-url /demo-web-notebooks/lite/
python3 scripts/inject_back_link.py site/lite
touch site/.nojekyll
