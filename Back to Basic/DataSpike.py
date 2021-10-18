"""Data Spike"""
def calcmax1(cal1 , cal2, cal3, cal4, cal5, cal6):
    if cal1 > cal2 and cal1 > cal3 and cal1 > cal4 and cal1 > cal5 and cal1 > cal6:
        return cal1
    elif cal1 < cal2 and cal2 > cal3 and cal2 > cal4 and cal2 > cal5 and cal2 > cal6:
        return cal2
    elif cal1 < cal3 and cal2 < cal3 and cal4 < cal3 and cal5 < cal3 and cal6 < cal3:
        return cal3
    elif cal1 < cal4 and cal2 < cal4 and cal3 < cal4 and cal5 < cal4 and cal6 < cal4:
        return cal4
    elif cal1 < cal5 and cal2 < cal5 and cal3 < cal5 and cal4 < cal5 and cal6 < cal5:
        return cal5
    elif cal1 < cal6 and cal2 < cal6 and cal3 < cal6 and cal4 < cal6 and cal5 < cal6:
        return cal6
def main():    
    """Docs"""
    keep1 = int(input())
    keep2 = int(input())
    keep3 = int(input())
    keep4 = int(input())
    keep5 = int(input())
    keep6 = int(input())
    calc = calcmax1(keep1, keep2, keep3, keep4, keep5, keep6)
    print(calc)
main()
