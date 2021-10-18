"""Func One"""
def my_top():
    """Lucky One """
    keep_1, keep_2, keep_3 = int(input()), int(input()), int(input())
    if keep_1 == keep_2 and keep_1 == keep_3 and keep_2 == keep_3:
        print(0)
    elif keep_1 != keep_2 and keep_1 != keep_3 and keep_2 != keep_3:
        print(keep_1+keep_2+keep_3)
    elif keep_1 == keep_2:
        print(keep_3)
    elif keep_1 == keep_3:
        print(keep_2)
    elif keep_2 == keep_3:
        print(keep_1)
my_top()
