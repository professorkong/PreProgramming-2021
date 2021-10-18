"""Prime Number"""
def checkprime(num):
    """Docstring"""
    keep = 0
    if num > 1:
        for i in range(2, num, 1):
            if (num % i) == 0:
                keep = 1
                break
    else:
        keep = 1
    if keep == 0:
        return True
    elif keep == 1:
        return False
def main():
    """Docstring"""
    num1 = int(input())
    num2 = int(input())
    ans = 0
    keep = ""
    for i in range(num1, num2+1, 1):
        if checkprime(i):
            keep = keep + str(i)+" "
            ans = ans + i
    if keep == "":
        print("not found prime number")
    else:
        print(keep)
        print("sum of prime = %d"%ans)
main()
