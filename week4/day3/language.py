"""LANG"""
def fac(class):
    """Docstring"""
    calc_1 = 1
    if class == 0:
        return 1
    else:
        for i in range(1, class + 1):
            calc_1 = calc_1*i
        return calc_1
def main():
    """calc"""
    keep1 = int(input())
    keep2 = int(input())
    keep3 = int(input())
    keep4 = int(input())
main()
