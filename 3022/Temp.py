"""Temp"""
def main():
    """Temp"""
    value = float(input())
    from_unit = input()
    to_unit = input()

    if from_unit == "C":
        celsius = value
    elif from_unit == "K":
        celsius = value - 273.15
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value * 5 / 9 - 273.15

    if to_unit == "C":
        result = celsius
    elif to_unit == "K":
        result = celsius + 273.15
    elif to_unit == "F":
        result = celsius * 9 / 5 + 32
    else:  # R
        result = (celsius + 273.15) * 9 / 5

    print(f"{result:.2f}")
main()
