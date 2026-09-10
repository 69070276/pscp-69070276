"""สลากกินแบ่ง"""
win_letter, win_number = input().split()
my_letter, my_number = input().split()

if my_letter == win_letter and my_number == win_number:
    print(1000000)
elif my_number == win_number:
    print(100000)
elif my_letter == win_letter and my_number[-3:] == win_number[-3:]:
    print(2000)
elif my_letter == win_letter and my_number[-2:] == win_number[-2:]:
    print(1000)
elif my_number[-3:] == win_number[-3:]:
    print(200)
elif my_number[-2:] == win_number[-2:]:
    print(100)
elif my_letter == win_letter:
    print(20)
else:
    print(0)
