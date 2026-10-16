"""Cute Cat Cute Fox"""
n = int(input())
d = {}

for _ in range(n):
    line = input().strip()[1:-1]
    k, v = line.split(":")
    d[k.strip().strip('"')] = v.strip().strip('"')

if "Cat01" not in d.values() and "Garfield" not in d:
    d["Garfield"] = "Cat01"
if "Fox01" not in d.values() and "Fubuki" not in d:
    d["Fubuki"] = "Fox01"

cats = sorted((k for k, v in d.items() if v.startswith("Cat")), key=lambda k: int(d[k][3:]))
foxes = sorted((k for k, v in d.items() if v.startswith("Fox")), key=lambda k: int(d[k][3:]))

print("Cat :", len(cats))
print("Fox :", len(foxes))
for k in cats + foxes:
    print(k, ":", d[k])
