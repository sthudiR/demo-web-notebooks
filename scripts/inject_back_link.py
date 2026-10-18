"""Add a floating 'back' pill to every JupyterLite HTML entry page (lab, repl, tree, notebooks)."""
import pathlib, sys

PILL = (
    '<style>'
    '#dw-back{position:fixed;top:0;left:0;right:0;height:32px;z-index:100000;display:flex;align-items:center;'
    'gap:6px;padding:0 12px;background:#0f1419;border-bottom:2px solid #e0a458;font:500 13px system-ui,sans-serif}'
    '#dw-back a{color:#e6edf3;text-decoration:none;padding:3px 10px;border-radius:6px}'
    '#dw-back a:hover{background:#e0a458;color:#0f1419}'
    '#dw-back a.cur{background:#e0a458;color:#0f1419;font-weight:700}'
    '#dw-back .sep{color:#8b98a5}'
    'body{position:absolute!important;top:32px!important;left:0;right:0;bottom:0;height:auto!important}'
    '</style>'
    '<nav id="dw-back" aria-label="Site navigation">'
    '<a href="https://sthudir.github.io/demo-web-hub/">&larr; Back to hub</a><span class="sep">/</span>'
    '<a href="/demo-web-notebooks/">Sourdough Lab</a><span class="sep">/</span>'
    '<a class="cur" href="#" aria-current="page" onclick="return false">Notebook</a></nav>'
    '<script>if(window.top!==window.self){document.getElementById("dw-back").remove();'
    'document.body.style.cssText="top:0!important"}</script>'
)

for page in pathlib.Path(sys.argv[1]).rglob("index.html"):
    if page.parts[-2] not in {"lab", "repl", "tree", "notebooks", "edit", "consoles"}:
        continue
    html = page.read_text()
    if "dw-back" not in html and "</body>" in html:
        page.write_text(html.replace("</body>", PILL + "</body>", 1))
        print("patched", page)
