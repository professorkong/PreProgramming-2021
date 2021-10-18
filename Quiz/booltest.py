"""calc"""
def calc(down, top):
    """calc"""
    down = down * bool(down >= top)
    top = top * bool(top >= down)
    keep = down + top
    return keep
def main():
    cal1 = float(input())
    cal2 = calc(cal1, float(input()))
    cal3 = calc(cal2, float(input()))
    cal4 = calc(cal3, float(input()))
    cal5 = calc(cal4, float(input()))
    cal6 = calc(cal5, float(input()))
    cal7 = calc(cal6, float(input()))
    cal8 = calc(cal7, float(input()))
    print("%d"%cal8)
main()
