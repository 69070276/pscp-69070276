"""Padthai"""
need = {
    "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp", "Bean Sprouts",
    "Noodle", "Chives", "Lime", "Egg", "Oil", "Peanuts",
}
taste_need = {"Sweet", "Sour", "Salty"}

ing = set()
while True:
    line = input().strip()
    if line == "Cook":
        break
    ing.add(line)

taste = set()
while True:
    line = input().strip()
    if line == "End":
        break
    taste.add(line)

if not ing <= need:
    print("This is not Pad Thai!!!")
elif ing != need:
    print("This is bad!")
elif taste != taste_need:
    print("Not Bad...")
else:
    print("Delicious!")
