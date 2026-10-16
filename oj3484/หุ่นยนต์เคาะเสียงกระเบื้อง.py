"""หุ่นยนต์เคาะเสียงกระเบื้อง"""
n, p = input().split()
n = int(n)
p = float(p)

g = [list(map(int, input().split())) for _ in range(n)]

for row in g:
    bad = sum(1 for x in row if x)
    print(*row, bad, sum(row))

col_tiles = [sum(1 for i in range(n) if g[i][j]) for j in range(n)]
col_pts = [sum(g[i][j] for i in range(n)) for j in range(n)]

print(*col_tiles)
print(*col_pts)

total_tiles = sum(col_tiles)
total_pts = sum(col_pts)
print(total_tiles, total_pts, f"{total_pts * p:.2f}")
