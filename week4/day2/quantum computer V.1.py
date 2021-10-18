"""quantum computer V.1"""
def main():
    """Docstring"""
    number = int(input()) + 1
    keep = 0
    for _ in range(1, number):
        sass = input().upper()
        if sass == "INC":
            keep = keep + 1
        elif sass == "DEC":
            keep = keep - 1
        elif sass == "DUBL":
            keep = keep * 2
        elif sass == "HALF":
            keep = keep / 2
    print("%.2f"%keep)
main()
