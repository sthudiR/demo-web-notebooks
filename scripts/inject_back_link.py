"""Add a floating 'back' pill to every JupyterLite HTML entry page (lab, repl, tree, notebooks)."""
import pathlib, sys

PILL = (
    '<div id="dw-back" style="position:fixed;left:12px;bottom:12px;z-index:100000;'
    'display:flex;gap:6px;font:600 13px system-ui,sans-serif">'
    '<a href="/demo-web-notebooks/" style="background:#e0a458;color:#0f1419;padding:6px 12px;'
    'border-radius:999px;text-decoration:none">&larr; Sourdough Lab</a>'
    '<a href="https://sthudir.github.io/demo-web-hub/" style="background:#0f1419;color:#e6edf3;'
    'padding:6px 12px;border-radius:999px;text-decoration:none">demo-web hub</a></div>'
)

for page in pathlib.Path(sys.argv[1]).rglob("index.html"):
    if page.parts[-2] not in {"lab", "repl", "tree", "notebooks", "edit", "consoles"}:
        continue
    html = page.read_text()
    if "dw-back" not in html and "</body>" in html:
        page.write_text(html.replace("</body>", PILL + "</body>", 1))
        print("patched", page)
