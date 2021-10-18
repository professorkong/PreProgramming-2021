"""Pyramid"""
def main():
    """calc"""
    keep = int(input())
    for i in range(1, keep+1):
        print(" "*(keep-i)+"*"*(2*i-1))
    for i in range(keep, 0, -1):
        if i != keep:
            print(" "*(keep-i)+"*"*(2*i-1))
main()
