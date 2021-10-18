"""หมอลำซิ่ง"""
def fac():
    """Docstring"""
    calc_1 = 0
    calc_2 = 0
    keep = input()
    for i in keep:
        if i == "1":
            calc_1 = calc_1 + 1
        elif i == "0":
            calc_1 = 0
        if calc_1 >= calc_2:
            calc_2 = calc_1
    if calc_2 <= 1:
        print("Rank D")
    elif calc_2 == 2:
        print("Rank C")
    elif calc_2 == 3:
        print("Rank B")
    elif calc_2 == 4:
        print("Rank A")
    elif calc_2 == 5:
        print("Rank S")
    elif calc_2 >= 6:
        print("Rank SSS")
fac()
