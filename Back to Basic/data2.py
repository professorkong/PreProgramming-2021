"""Dataspike"""
def main(num1, num2):
    """dataspike"""
    if num1 > num2:
        return num1
    else:
        return num2
def justm():
    """dataspike"""
    num = int(input())
    ans = main(num, int(input()))
    ans = main(ans, int(input()))
    ans = main(ans, int(input()))
    ans = main(ans, int(input()))
    ans = main(ans, int(input()))
    ans = main(ans, int(input()))
    ans = main(ans, int(input()))
    print(ans)
justm()
