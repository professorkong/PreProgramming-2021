"""Password"""
def main():
    """Docstring"""
    name_1 = input()
    name_2 = input()
    name_3 = input()
    mylist = input()
    keeplist = []
    keeplist.append(name_1)
    keeplist.append(name_2)
    keeplist.append(name_3)
    keepsprit = mylist.split(",")
    for i in keepsprit:
        check0 = 0
        check1 = 0
        check2 = 0
        check3 = 0
        check4 = 0
        check5 = 0
        for j in i:
            if j.isupper():
                check0 += 1
            if j.islower():
                check1 += 1
            if j.isnumeric():
                check2 += 1
            if j == ("#") or j == ("$") or j == ("@"):
                check3 += 1
            if i.count(" ") == 0:
                check4 += 1
            if len(i) >= 6 and len(i) <= 12:
                check5 += 1
        if check0 >= 1 and check1 >= 1 and check2 >= 1 and check3 >= 1 and check4 >= 1 and \
        check5 >= 1:
            print("%s (%s)"%(i, keeplist[keepsprit.index(i)]))
main()
