"""Just Max V.3"""
def change(num1):
    """change"""
    keepa = float(input())
    if num1 > keepa:
        keepb = num1
    elif keepa >= num1:
        keepb = keepa
    return float(keepb)
def my_top():
    """V.3"""
    num1 = float(input())
    num1 = change(num1)
    num1 = change(num1)
    num1 = change(num1)
    num1 = change(num1)
    num1 = change(num1)
    num1 = change(num1)
    num1 = change(num1)
    num1 = change(num1)
    num1 = change(num1)
    num1 = change(num1)
    num1 = change(num1)
    num1 = change(num1)
    num1 = change(num1)
    num1 = change(num1)
    print("%.2f"%num1)
my_top()
