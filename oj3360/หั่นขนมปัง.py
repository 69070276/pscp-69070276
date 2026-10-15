"""หั่นขนมปัง"""
w, h, m, n = map(int, input().split())
xs = [0] + list(map(int, input().split())) + [w]
ys = [0] + list(map(int, input().split())) + [h]

dx = sorted((xs[i + 1] - xs[i] for i in range(m + 1)), reverse=True)
dy = sorted((ys[i + 1] - ys[i] for i in range(n + 1)), reverse=True)

areas = [dx[0] * dy[0]]
if len(dy) > 1:
    areas.append(dx[0] * dy[1])
if len(dx) > 1:
    areas.append(dx[1] * dy[0])
if len(dx) > 1 and len(dy) > 1:
    areas.append(dx[1] * dy[1])

areas.sort(reverse=True)
print(areas[0], areas[1])
