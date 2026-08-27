"""Arcade"""
first_line = input().split()
num = int(first_line[0])
check = int(first_line[1])

starts = []
stops = []

for i in range(num):
    line = input().split()
    starts.append(int(line[0]))
    stops.append(int(line[1]))

times = input().split()

results = []

for i in range(check):
    t = int(times[i])
    count = 0
    for j in range(num):
        if starts[j] <= t < stops[j]:
            count += 1
    results.append(str(count))

print(" ".join(results))
