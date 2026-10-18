# demo-web-notebooks - Sourdough Lab

Jupyter Book 2 (MyST, `mystmd`) site with JupyterLite (Pyodide kernel) so the notebooks run in the browser with no server.
Topic: hydration, baker's percentages and Q10 fermentation timing as editable Python.

Live: https://sthudir.github.io/demo-web-notebooks/ (JupyterLite at `/lite/`)

## Run locally
```bash
npm ci
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
bash scripts/build.sh                      # outputs ./site
mkdir -p /tmp/x && ln -sfn "$PWD/site" /tmp/x/demo-web-notebooks
cd /tmp/x && python3 -m http.server 8000   # open http://localhost:8000/demo-web-notebooks/
```
For live MyST authoring only: `BASE_URL= npx myst start` (the lite/ part is not included).

## Build
`bash scripts/build.sh` runs `BASE_URL=/demo-web-notebooks myst build --html`, copies `_build/html` into `site/`,
adds `site.json` + `thumbnail.svg`, and runs `jupyter lite build --contents notebooks --base-url /demo-web-notebooks/lite/ --output-dir site/lite`.
Notebooks live in `notebooks/` (regenerate with `python scripts/mknb.py` or edit directly).
Pyodide itself is fetched at runtime from the jsDelivr CDN (v0.26.4) by the kernel extension.

## Deploy
`.github/workflows/deploy.yml` builds and deploys `site/` to GitHub Pages on push to main. Optional secret
`HUB_DISPATCH_TOKEN` triggers a `site-updated` dispatch to sthudiR/demo-web-hub.

## Video
`content/lab.md` embeds the YouTube privacy-enhanced iframe (`youtube-nocookie.com/embed/aqz-KE-bpKQ`) in a 16:9 `.video-wrap` with `loading="lazy"`. Change the ID there.

## Base path
Everything assumes `/demo-web-notebooks/`: `BASE_URL` for MyST, `--base-url` for JupyterLite. Content links are relative (`../lite/...`). Rename the repo => update both.
Design tokens (`--dw-*`) are in `tokens.css`.

## Licence
Public domain (CC0). Everything here is made up for a demo; use and share it freely. See `LICENSE`.
