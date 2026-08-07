"""log"""
def main():
    """log"""
    N = int(input())
    listn = []
    for x in range(N, -1, -1):
        if not x %10 :
            listn.append(x)
        else:
            continue

    print(*listn)
main()
