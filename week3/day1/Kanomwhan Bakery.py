"""Kanomwhan"""
def my_top():
    """ขนมหวานสุดแสนจะอร่อย แต่แพงไปหน่อยเท่านั้นเอง"""
    kon = int(input())
    price = float(input())
    delete = int(input())
    calc_1 = (kon * price)-((delete/100)*(kon*price))
    calc_2 = ((((kon//4)*3)+(kon%4))*price)
    if kon < 3:
        print("Promotion 1 %.3f Baht"%(kon*price))
        print("Purchase successfully !")
        print("Have a good meal with \"Kanomwhan\"")
    elif calc_1 <= calc_2:
        print("Promotion 1 %.3f Baht"%calc_1)
        print("Purchase successfully !")
        print("Have a good meal with \"Kanomwhan\"")
    elif calc_1 > calc_2:
        print("Promotion 2 %.3f Baht"%calc_2)
        print("Purchase successfully !")
        print("Have a good meal with \"Kanomwhan\"")
my_top()
