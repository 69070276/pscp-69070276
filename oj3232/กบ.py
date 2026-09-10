"""กบกระโดด"""
X, Y = map(int, input().split())

total = 0
jumps = 0
distance = X

while distance > 0:
    total += distance
    jumps += 1

    if total >= Y:
        print(jumps)
        break

    distance -= 2
else:
    print(-1)
