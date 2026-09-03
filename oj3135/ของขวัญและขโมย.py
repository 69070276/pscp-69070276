"""ของขวัญและขโมย"""
import math

N, K, T = map(int, input().split())

count = N // math.gcd(N, K)
g = math.gcd(N, K)

if not (T - 1) % g:
    n = N // g
    k = K // g
    t = (T - 1) // g

    inv_k = pow(k, -1, n)
    position = (t * inv_k) % n

    print(position + 1)
else:
    print(count)
