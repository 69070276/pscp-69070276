"""Surprising"""
def main():
    """Surprising"""
    total_score = float(input())
    max_score = float(input())

    remaining = total_score - 2 * max_score

    if remaining > 0:
        min_possible = remaining
    else:
        min_possible = 0

    gap = max_score - min_possible

    if gap > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
