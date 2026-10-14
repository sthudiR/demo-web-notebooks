import json, sys
def nb(path, cells):
    out=[]
    for kind,src in cells:
        c={"cell_type":kind,"metadata":{},"source":src.strip("\n").splitlines(True)}
        if kind=="code": c.update(execution_count=None,outputs=[])
        out.append(c)
    json.dump({"cells":out,"metadata":{"kernelspec":{"name":"python","display_name":"Python (Pyodide)","language":"python"},"language_info":{"name":"python"}},"nbformat":4,"nbformat_minor":5},open(path,"w"),indent=1)

nb("notebooks/hydration.ipynb",[
("markdown","# Hydration and baker's percentages\nEdit any number and re-run the cell (Shift+Enter)."),
("code","""flour = 500      # grams
water = 365
salt = 10
starter = 100    # 100% hydration starter

# starter is half flour, half water
total_flour = flour + starter / 2
total_water = water + starter / 2
print(f"Total hydration: {total_water / total_flour:.1%}")
print(f"Salt: {salt / total_flour:.1%}")"""),
("code","""def recipe(total_flour, hydration, salt_pct=0.02, starter_pct=0.20):
    return {
        "flour": total_flour,
        "water": round(total_flour * hydration),
        "salt": round(total_flour * salt_pct, 1),
        "starter": round(total_flour * starter_pct),
    }

for h in (0.65, 0.70, 0.75, 0.80):
    print(f"{h:.0%}", recipe(800, h))"""),
])
nb("notebooks/fermentation.ipynb",[
("markdown","# Fermentation timing with the Q10 rule\nWarmer dough ferments faster. With Q10 = 2, every 10 C rise roughly halves the time."),
("code","""def ferment_hours(temp_c, ref_temp=24, ref_hours=5, q10=2.0):
    return ref_hours * q10 ** ((ref_temp - temp_c) / 10)

for t in (18, 21, 24, 27, 30):
    h = ferment_hours(t)
    print(f"{t} C -> {h:.1f} h ({int(h)} h {round((h % 1) * 60)} min)")"""),
("code","""# Fridge retard: how long at 4 C?
print(round(ferment_hours(4), 1), "hours at 4 C (rough model)")

# Try your own kitchen:
kitchen = 22
print("Bulk ferment at", kitchen, "C:", round(ferment_hours(kitchen, q10=2.2), 1), "h")"""),
])
