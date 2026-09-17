"""แปลงดอกไม้"""
L, N = map(int, input().split())

total = 0
k = 0
while total < N:
    k += 1
    a = (k - 1) * L + 1
    b = k * L
    s = (a + b) * L // 2
    total += s
print(k)
