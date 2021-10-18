"""Data Spike"""
def calcma1(cal1, cal2, cal3, cal4, cal5, cal6, cal7, cal8):
    """Docs"""
    if cal1 > cal2 and cal1 > cal3 and cal1 > cal4 and cal1 > cal5 and cal1 > cal6\
        and cal1 > cal7 and cal1 > cal8:
        print(cal1)
    elif cal1 < cal2 and cal2 > cal3 and cal2 > cal4 and cal2 > cal5 and cal2 > cal6\
        and cal2 > cal7 and cal2 > cal8:
        print(cal2)
    elif cal1 < cal3 and cal2 < cal3 and cal4 < cal3 and cal5 < cal3 and cal6 < cal3\
        and cal7 < cal3 and cal8 < cal3:
        print(cal3)
    elif cal1 < cal4 and cal2 < cal4 and cal3 < cal4 and cal5 < cal4 and cal6 < cal4\
        and cal7 < cal4 and cal8 < cal4:
        print(cal4)
def calcma2(cal1, cal2, cal3, cal4, cal5, cal6, cal7, cal8):
    if cal1 < cal5 and cal2 < cal5 and cal3 < cal5 and cal4 < cal5 and cal6 < cal5\
        and cal7 < cal5 and cal8 < cal5:
        print(cal5)
    elif cal1 < cal6 and cal2 < cal6 and cal3 < cal6 and cal4 < cal6 and cal5 < cal6\
        and cal7 < cal6 and cal8 < cal6:
        print(cal6)
    elif cal1 < cal7 and cal2 < cal7 and cal3 < cal7 and cal4 < cal7 and cal5 < cal7\
        and cal6 < cal7 and cal7 > cal8:
        print(cal7)
    elif cal1 < cal8 and cal2 < cal8 and cal3 < cal8 and cal4 < cal8 and cal5 < cal8\
        and cal6 < cal8 and cal7 < cal8:
        print(cal8)
def main():
    """Docs"""
    keep1 = int(input())
    keep2 = int(input())
    keep3 = int(input())
    keep4 = int(input())
    keep5 = int(input())
    keep6 = int(input())
    keep7 = int(input())
    keep8 = int(input())
    calcma1(keep1, keep2, keep3, keep4, keep5, keep6, keep7, keep8)
    calcma2(keep1, keep2, keep3, keep4, keep5, keep6, keep7, keep8)
main()
