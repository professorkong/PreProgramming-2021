"""Empire"""
def main():
    """Docstring"""
    lst = []
    while True:
        keepfl = input()
        if keepfl == "-":
            break
        lst.append(int(keepfl))
    lst.sort()
    if lst[0] == 0:
        print("Error! Not have this floor.")
    else:
        print("OK! Wait please.")
        print("-----")
        print("Lift is arriving!")
        for i in lst:
            print("-----")
            print("Lift is going up!")
            if i == 1:
                print("-----")
                print("Lift has reached the %dst floor!"%(i))
            if i == 2:
                print("-----")
                print("Lift has reached the %dnd floor!"%(i))
            if i == 3:
                print("-----")
                print("Lift has reached the %drd floor!"%(i))
            if i == 4:
                print("-----")
                print("Lift has reached the %dth floor!"%(i))
            if i == 5:
                print("-----")
                print("Lift has reached the %dth floor!"%(i))
main()
