"""Duplicate"""
m = int(input())
n = int(input())

a = {input().strip() for _ in range(m)}
b = {input().strip() for _ in range(n)}

both = sorted(a & b, reverse=True)

if both:
    for x in both:
        print(x)
else:
    print("Nope")
