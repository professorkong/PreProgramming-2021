"""Stairs V.2"""
def main():
    """calc"""
    keep = int(input())
    for i in range(1, keep+1):
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(2, i + 1):
            print(i - j + 1, end="")
        print()
main()
