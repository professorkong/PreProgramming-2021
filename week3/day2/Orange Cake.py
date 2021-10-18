"""Orange Cake"""
def my_top():
    """Cake"""
    keep1 = int(input())
    keep2 = int(input())
    calc2 = keep1-(keep2*(keep1//keep2))
    if keep1 < keep2:
        print("Not enough money;(")
        print("Money left: %d"%keep1)
    elif keep1 >= keep2:
        print("Orange Cake: %d"%(keep1//keep2))
        print("Money left: %d"%calc2)
my_top()
