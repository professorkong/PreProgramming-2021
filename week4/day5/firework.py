"""firework"""
def main():
    """calc"""
    keep = input().upper()
    calc = len(keep)
    for i in range(-calc+1, calc, 1):
        for j in range(-calc+1, calc, 1):
            if abs(i) == abs(j) or j == 0:
                print(keep[abs(i)], end=" ")
            elif i == 0:
                 print(keep[abs(j)], end=" ")
            else:
                 print(" ", end=" ")
        print()
main()
