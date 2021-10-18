"""Box Daimon"""
def main():
    """calc"""
    keep = int(input())
    for i in range(keep):
        k = i+1
        for _ in range(keep-i-1):
            print(" ", end="  ")
        for _ in range(i+1):
            print(k, end=" ")
            k = k-1
        if i > 0:
            for _ in range(i-1):
                print(" ", end=" ")
            for _ in range(i+1):
                k = k+1
                print(k, end=" ")
        print()
    for i in range(1, keep):
        k = keep-i
        for _ in range(i):
            print(" ", end="  ")
        for _ in range(keep-i):
            print(k, end=" ")
            k = k-1
        if i < (keep-1):
            for _ in range(keep-i-2):
                print(" ", end=" ")
            for _ in range(keep-i):
                k = k+1
                print(k, end=" ")
        print()
main()
