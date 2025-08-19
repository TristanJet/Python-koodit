tal = float(input("Enter talents: "))
pnd = float(input("Enter pounds: "))
lot = float(input("Enter lots: "))

ltg = 13.3
ptl = 32
ttp = 20

g = lot * ltg
g += pnd * ptl * ltg
g += tal * ttp * ptl * ltg

print(f"Total weight in grams: {g}")
kg, grams = divmod(g, 1000)
# kg = g // 1000
# grams = g % 1000
print(f"In modern units:\n{kg} kilograms and {round(grams, 2)} grams")
