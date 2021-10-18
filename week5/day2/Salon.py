"""Salon"""
def main():
    """Docstrings"""
    name = input()
    nation = input().lower()
    input()
    confirm = input().upper()
    lst2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    lst = []
    lst3 = ["wash the hair", "wash-cut-dry", "haircut", "perm", "snip", "hair straightening",\
        "hair dye", "eyebrow tattoo", "lip tattoo", "make up"]
    if confirm == "Y":
        money = int(input())
    for _ in range(3):
        keep = input().lower()
        if keep == "-":
            pass
        else:
            lst2[calc(keep)] += 1
            if keep not in lst:
                lst.append(keep)
    keep2 = lst2[0]*120+lst2[1]*170+lst2[2]*50+lst2[3]*300+lst2[4]*350+lst2[5]*250\
        +lst2[6]*400+lst2[7]*700+lst2[8]*800+lst2[9]*1000
    if nation == "malaysian":
        keep2 *= 2
    elif nation == "thai":
        keep2 = keep2
    if confirm == "Y":
        keep2 = keep2 - money
    if keep2 < 0:
        keep2 = 0
    for j in lst:
        print(j.title(), lst2[lst3.index(j)])
    print("%s %d Baht"%(name, keep2))
def calc(keep):
    """Doc"""
    cal = 0
    if keep == "wash the hair":
        cal = 0
    elif keep == "wash-cut-dry":
        cal = 1
    elif keep == "haircut":
        cal = 2
    elif keep == "perm":
        cal = 3
    elif keep == "snip":
        cal = 4
    elif keep == "hair straightening":
        cal = 5
    elif keep == "hair dye":
        cal = 6
    elif keep == "eyebrow tattoo":
        cal = 7
    elif keep == "lip tattoo":
        cal = 8
    elif keep == "make up":
        cal = 9
    return cal
main()
