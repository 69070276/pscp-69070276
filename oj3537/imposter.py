"""Imposter"""
players = {}

while True:
    line = input().strip()
    if line.lower() == "start":
        break
    if not line:
        continue
    for pair in line.strip("{}").split(","):
        name, role = pair.split(":")
        players[name.strip().strip("'\"")] = role.strip().strip("'\"")

dead = {}

while True:
    name = input().strip()
    if name.lower() == "end":
        break
    if name in players:
        dead[name] = players.pop(name)

impostors = list(players.values()).count("Impostor")

print(f"{impostors} Impostor Remains")
print("***Alive***")
for name in sorted(players):
    print(f"{name} : {players[name]}")
print("***Dead***")
for name in sorted(dead):
    print(f"{name} : {dead[name]}")
