"""การหารธรรมดา"""
def main():    
    """Docs"""
    v = int(input())
    if v == 1800:
        print("Not a Leap Year")
    elif v%4==0:
        print("Leap Year")
    else:
        print("Not a Leap Year")
main()
