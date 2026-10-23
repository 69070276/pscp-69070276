"""B - Fully pair?"""
s = input().strip()

count = {}
for ch in s:
    count[ch] = count.get(ch, 0) + 1

RESULT = "".join(ch for ch, n in count.items() if n % 2)

if not RESULT:
    print("fully paired")
else:
    print(RESULT)
