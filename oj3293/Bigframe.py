"""Big Frame"""
lines = [input().rstrip() for _ in range(5)]

max_len = max(len(line) for line in lines)

border = "*" * (max_len + 4)

print(border)

for line in lines:
    print("* " + line.ljust(max_len) + " *")

print(border)
