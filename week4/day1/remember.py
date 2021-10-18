"""remember"""
def main():
    """Docstring"""
    keep = str()
    while True:
        keep2 = input().lower()
        if keep2.isalpha() and keep2 != "end":
            keep = keep2 + keep + " "
        if keep2 == "end":
            keep3 = keep.count(input().lower())
            print(keep3)
            break
main()
