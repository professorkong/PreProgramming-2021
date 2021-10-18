"""test"""
def calc(widht, hight):
    """Docs"""
    keep = widht + hight
    return keep
def main():
    """calc"""
    num1 = int(input())
    num2 = int(input())
    cal = calc(num1, num2)
    cal2 = calc(cal, num1)
    print(cal2)
main()

