"""Stairs V.1"""
def main():
    """calc"""
    keep = (input())
    calc = len(keep)
    for i in range(0, calc):
        for j in range(0, calc):
            if i == j or j == calc -1-i:
                print(keep[j], end=" ")
            else:
                print(" ", end=" ")
        print()
main()
