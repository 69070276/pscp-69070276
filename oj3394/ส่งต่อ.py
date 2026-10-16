"""ส่งต่อ"""
n, s = map(int, input().split())
nxt = [0] + [int(input()) for _ in range(n)]

seen = set()
cur = s

while cur and cur not in seen:
    seen.add(cur)
    cur = nxt[cur]

print(len(seen))
