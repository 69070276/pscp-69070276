"""Ink"""
import math
def main():
    """ink"""
    PI = 3.1416

    S, N = map(int, input().split())

    for _ in range(N):
        x, y = map(int, input().split())
        t = PI * (x * x + y * y) / S
        print(math.ceil(t))
main()
