"""Func Max V.4"""
def high(down, top):
    """Docstring"""
    down = down * bool(down >= top)
    top = top * bool(top > down)
    return down + top
def main():
    """output"""
    cal1 = float(input())
    cal2 = high(cal1, float(input()))
    cal3 = high(cal2, float(input()))
    cal4 = high(cal3, float(input()))
    cal5 = high(cal4, float(input()))
    cal6 = high(cal5, float(input()))
    cal7 = high(cal6, float(input()))
    cal8 = high(cal7, float(input()))
    cal9 = high(cal8, float(input()))
    cal10 = high(cal9, float(input()))
    print("%.2f"%cal10)
main()
