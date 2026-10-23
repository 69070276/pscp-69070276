"""Bill"""
def main():
    """Bill"""
    price = float(input())

    service = price * 0.10
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000

    a = price + service
    vat = a * 0.07
    b = a + vat

    print(f"{b:.2f}")
main()
