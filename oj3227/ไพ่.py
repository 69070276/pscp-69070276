"""44"""
card = input().strip().upper()

value = card[:-1]
suit = card[-1]

value_name = {
    "A": "ace",
    "J": "jack",
    "Q": "queen",
    "K": "king"
}

suit_name = {
    "D": "diamonds",
    "H": "hearts",
    "S": "spades",
    "C": "clubs"
}

value = value_name.get(value, value)

print(value, "of", suit_name[suit])
