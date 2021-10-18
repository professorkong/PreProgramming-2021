"""Herb"""
def my_top():
    """HHH"""
    keep1, keep2, keep3, keep4, keep5, keep6, keep7, keep8, keep9, keep10 = int(input()), \
    int(input()), int(input()), int(input()), int(input()), int(input()), \
    int(input()), int(input()), int(input()), int(input())
    if keep1 > 100:
        keep1 = 0
    if keep2 > 100:
        keep2 = 0
    if keep3 > 100:
        keep3 = 0
    if keep4 > 100:
        keep4 = 0
    if keep5 > 100:
        keep5 = 0
    if keep6 > 100:
        keep6 = 0
    if keep7 > 100:
        keep7 = 0
    if keep8 > 100:
        keep8 = 0
    if keep9 > 100:
        keep9 = 0
    if keep10 > 100:
        keep10 = 0
    calc = keep1+keep2+keep3+keep4+keep5+keep6+keep7+keep8+keep9+keep10
    if calc == 420:
        print("herb")
    else:
        print(calc)
my_top()
