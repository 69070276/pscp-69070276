"""isPrime_large"""
n = int(input())

is_prime = True
if n < 2:
    is_prime = False
else:
    for d in range(2, int(n ** 0.5) + 1):
        if not n % d:
            is_prime = False
            break

if is_prime:
    print("YES")
else:
    print("NO")
