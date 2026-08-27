"""สหกรณ์โรงเรียน"""
member = input()
n = int(input())

total = 0
for _ in range(n):
    price = float(input())
    total = total + price

if member == "Y":
    total = total * 0.95
else:
    if total >= 500:
        total = total * 0.97

ROUNDED = int(total * 100 + 0.5 + 1e-9)
total = ROUNDED / 100

print(f"{total:.2f}")
