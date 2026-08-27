"""สงครามส่งด่วน"""
origin, destination = input().split()
weight = float(input())

routes = {
    ("BKK", "CNX"): (10, 30),
    ("CNX", "UBP"): (15, 40),
    ("UBP", "BKK"): (20, 40),
    ("BKK", "PKT"): (25, 50),
    ("PKT", "CNX"): (30, 60),
    ("UBP", "PKT"): (40, 70),
}

key = (origin, destination)

if key in routes:
    base, rate = routes[key]
    fee = base + rate * weight
    print(f"{fee:.2f}")
else:
    print("Error")
