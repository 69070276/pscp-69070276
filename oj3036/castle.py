"""ปราสาท"""
import math

def main():
    """ปราสาท"""
    n = int(input())

    if n == 1:
        print(0)
        return

    r = math.isqrt(n - 1) + 1
    p = n - (r - 1) ** 2

    cost = 2 * (r - 1)
    if not p % 2:
        cost -= 1
    print(cost)
main()
