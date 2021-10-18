"""MorLam V.2"""
def main():
    """Docstring"""
    number = int(input()) + 1
    keep1 = 0
    keep2 = 0
    for _ in range(1, number):
        part1 = int(input())
        part2 = int(input())
        if part1 == part2:
            keep2 = keep2 + 1
        else:
            keep1 = keep1 - 1
            keep2 = 0
        keep1 = keep1 + keep2
    print(str(keep1)+" Point")
main()
