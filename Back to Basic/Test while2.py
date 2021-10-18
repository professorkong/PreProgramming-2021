"""Function Test"""
def main():
    """Docs"""
    a = int(input())
    b = int(input())
    while a>0:
        print(str(a)+"X"+str(b)+" = "+str(a*b))
        b = b + 1
        if b > 12:
            break
main()
