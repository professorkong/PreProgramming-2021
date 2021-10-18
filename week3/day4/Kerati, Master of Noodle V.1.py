"""Noodle"""
def my_top():
    """Noodle"""
    brand = input().lower()
    savor = input().lower()
    many = int(input())
    chot = 280
    maw = chot * (85/100)
    nis = chot+(((chot/8)**(1/2))*3)
    yum = chot-(chot%100)/16
    if brand == "chotipat":
        print((calc(chot, savor)*many))
    elif brand == "mawai":
        print((calc(maw, savor)*many))
    elif brand == "nisjung":
        print((calc(nis, savor)*many))
    elif brand == "yummayro":
        print((calc(yum, savor)*many))
    else:
        print("No Data !!")
def calc(calc1, calc2):
    #คำนวณ
    """Calc"""
    if "pork" in calc2:
        return int(calc1)
    else:
    #จะมีจำนวนเส้นมากกว่าจำนวนเส้นของรสหมู อยู่ 10%
        return int(calc1*(110/100))
my_top()
