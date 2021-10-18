"""Stairs V.1"""
def main():
    """calc"""
    keep = int(input())
    for row in range(1, keep+1, 1):
        for coloum in range(1,row+1,1):
            print("*", end="")
        print()
main()
