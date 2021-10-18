"""AP"""
def my_top(level):
    """APP"""
    apexpex = 0
    if level > 1:
        if level < 21:
            apexpex += (level%21) - 1
        else:
            apexpex += 19
    if level > 21:
        if level < 301:
            apexpex += (level - 20)//2
        else:
            apexpex += 139 + 1
    if level > 301:
        apexpex += ((level % 501)-300)//5
    if level >= 500:
        apexpex = 199
    print("%d Packs opened \n%d Packs more"%(apexpex, 500-apexpex))
my_top(int(input()))
