---
title: Sourdough Lab
---

# Sourdough Lab

Bread is chemistry you can eat. This little lab turns three baking ideas into **Python you can edit and run right here in your browser** - no install, no server. A Pyodide kernel (via JupyterLite) does the work.

<a class="btn-accent" href="lite/lab/index.html?path=hydration.ipynb">Open the hydration notebook</a>
<a class="btn-accent" href="lite/lab/index.html?path=fermentation.ipynb">Open the timing notebook</a>

> **Try this:** open the hydration notebook, change the flour weight, and press Shift+Enter to see every percentage update.

## What's inside

- **[Hydration and baker's percentages](content/hydration.md)** - why every ingredient is a percent of the flour.
- **[Fermentation timing](content/timing.md)** - the Q10 rule: warmer dough rises faster.
- **[The lab](content/lab.md)** - a live Python prompt, plus a video to watch while your dough rests.

:::{note}
The first time you launch a notebook, the browser downloads the Python runtime (a few MB). After that it is cached.
:::

:::{admonition} Behind this page
:class: dropdown

| | |
|---|---|
| **Built with** | Jupyter Book 2 (MyST) for the pages, JupyterLite with Pyodide for the Python |
| **The numbers** | 1.9 MB to load · pages ready in about 0.3 s (Python loads when you open a notebook) · builds in 44 s · 144 lines of source · you write Markdown and Python |
| **Good for** | Books with code readers can edit and run in the browser |
| **Not for** | Small, fast sites: the Python lab is 82 MB |
| **More** | [Source on GitHub](https://github.com/sthudiR/demo-web-notebooks) · [Pick your tool](https://sthudir.github.io/demo-web-hub/which/) · [Back to hub](https://sthudir.github.io/demo-web-hub/) |

Ready time: median of 5 cold loads on one home connection, 23 Oct 2026. Size is what a first visit downloads. Build time is the median of the last 5 GitHub Actions builds and includes installing the tools.
:::
