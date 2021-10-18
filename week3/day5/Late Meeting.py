"""Late Meeting"""
def main():
    """Doc"""
    hrr = int(input())
    minn = int(input())
    secc = int(input())
    am_or_pm = input()
    end_min = int(input())
    end_sec = int(input())
    if hrr == 12:
        hrr = 0
    if am_or_pm == "pm":
        hrr = hrr + 12
    secc = secc + end_sec
    minn = minn + (secc//60) + end_min
    secc = secc % 60
    hrr = hrr + (minn//60)
    minn = minn % 60
    hrr = hrr % 24
    if hrr >= 12:
        am_or_pm = "pm"
    else:
        am_or_pm = "am"
    hrr = hrr%12
    if hrr == 0:
        hrr = 12
    print("%02d:%02d:%02d %s"%(hrr, minn, secc, am_or_pm))
main()
