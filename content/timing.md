---
title: Fermentation timing
---

# Fermentation timing

Yeast and bacteria are temperature-sensitive. The **Q10 rule** says that for every 10 C increase, activity multiplies by about Q10 (roughly 2 for sourdough).

$$t = t_{ref} \cdot Q_{10}^{(T_{ref} - T)/10}$$

If bulk fermentation takes 5 hours at 24 C, then at 30 C it takes about 3.3 hours, and at 18 C about 7.6 hours.

```{code-block} python
def ferment_hours(temp_c, ref_temp=24, ref_hours=5, q10=2.0):
    return ref_hours * q10 ** ((ref_temp - temp_c) / 10)

print(round(ferment_hours(30), 1))
```

:::{warning}
This is a rule of thumb. Flour, starter strength and hydration all shift the numbers - always judge by the dough (risen about 50%, jiggly, domed), not the clock.
:::

<a class="btn-accent" href="lite/lab/index.html?path=fermentation.ipynb">Run it in the notebook</a>
