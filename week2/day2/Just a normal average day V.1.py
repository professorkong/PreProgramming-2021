"""Func AVG"""
def calc():
    """func main"""
    keep_1 = float(input())
    keep_2 = float(input())
    keep_3 = float(input())
    keep_4 = float(input())
    keep_5 = float(input())
    keep_6 = float(input())
    print("max : %.02f"%max(keep_1, keep_2, keep_3, keep_4, keep_5, keep_6))
    print("min : %.02f"%min(keep_1, keep_2, keep_3, keep_4, keep_5, keep_6))
    print("sum : %.02f"%sum((keep_1, keep_2, keep_3, keep_4, keep_5, keep_6)))
    print("avg : %.04f"%sum((keep_1/6, keep_2/6, keep_3/6, keep_4/6, keep_5/6, keep_6/6)))
calc()
