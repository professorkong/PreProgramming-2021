"""firework"""
def main():
    """calc"""
    keep = int(input())
    for i in range(-keep, keep, 1):
        for j in range(-keep, keep, 1):
            if abs(i) == abs(j): #or j == 0:
                print(keep(i), end=" ")
            elif i == 0:
                 print(keep(j), end=" ")
            else:
                 print(" ", end=" ")
        print()
main()
