---
title: Hydration and baker's percentages
---

# Hydration and baker's percentages

Bakers describe a recipe relative to the flour. Flour is always **100%**; everything else is a percentage of it.

$$\text{hydration} = \frac{\text{water}}{\text{flour}}$$

A loaf with 500 g flour and 350 g water is **70% hydration**. Higher hydration gives a more open, glossy crumb but a stickier dough.

| Ingredient | Grams | Baker's % |
|---|---|---|
| Flour | 500 | 100% |
| Water | 350 | 70% |
| Salt | 10 | 2% |
| Starter | 100 | 20% |

## Don't forget the starter

A 100% hydration starter is half flour and half water, so 100 g of it adds 50 g of each to your totals. Try it, editing the numbers freely:

```{code-block} python
flour, water, starter = 500, 350, 100
total_flour = flour + starter / 2
total_water = water + starter / 2
print(f"{total_water / total_flour:.1%}")
```

<a class="btn-accent" href="../lite/lab/index.html?path=hydration.ipynb">Run it in the notebook</a>
