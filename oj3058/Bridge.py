"""Bridge"""
def main():
    """Bridge"""
    a = int(input())
    b = int(input())
    goal = int(input())

    big = min(b, goal // 5)
    remain = goal - big * 5

    if remain <= a:
        print(remain)
    else:
        print(-1)
main()
