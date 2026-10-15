"""Point Sorting"""
t = int(input())

for _ in range(t):
    n = int(input())
    pts = [tuple(map(int, input().split())) for _ in range(n)]
    pts.sort(key=lambda p: (p[0] + p[1], -p[1]))
    for x, y in pts:
        print(x, y)
