"""Giraffe"""
n = int(input())
h = [int(input()) for _ in range(n)]

count = 0
for i in range(n):
    left = not i or h[i] > h[i - 1]
    right = i == n - 1 or h[i] > h[i + 1]
    if left and right:
        count += 1
print(count)
