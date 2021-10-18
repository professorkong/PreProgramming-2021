"""mod is broken"""
def calc():
    """func main"""
    keep_a = int(input())
    keep_b = int(input())
    keep_c = int(input())
    keep_d = int(input())
    keep_x = int(input())
    keep_y = int(input())
    keep_data = float((((keep_b/((keep_a**2)/keep_d))+(keep_x*(keep_b/keep_a)))\
    *keep_y)/(keep_y*keep_c))
    print("%.2f"%keep_data)
calc()
