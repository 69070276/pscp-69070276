"""AB""" 
def main():
    """AB"""
    a = int(input())
    b = int(input())
    d = int(input())
    r = int(input())

    count = 0

    for i in range(a, b + 1):
        if i % d == r:
            count += 1
    print(count)
main()
