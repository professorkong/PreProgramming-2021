"""Centerr"""
def doing():
    """call"""
    raka = int(input())
    minn = int(input())
    second = int(input())
    calc = 0
    if second > 30:
        minn = minn + 1
    if minn > 2 and raka > 0:
        if minn < 15:
            calc = 15 * raka
        else:
            calc = minn * raka
        print(calc)
    else:
        print("free")
doing()
