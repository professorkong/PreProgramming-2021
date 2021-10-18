"""Func Thai"""
def main(calc1):
    """เก็บทรงไม่ค่อยอยู่"""
    kueb = calc1/(0.25)
    sok = calc1/(0.50)
    wadd = calc1/(2)
    sen = calc1/(40)
    yot = calc1/(16000)
    print("= %.03f kueb"%kueb)
    print("= %.03f sok"%sok)
    print("= %.03f wa"%wadd)
    print("= %.03f sen"%sen)
    print("= %.03f yot\n"%yot)
    return calc1
print("200 m")
main(200)
print("500 m")
main(500)
print("1 km")
main(1000)
print("2 km")
main(2000)
print("5 km")
main(5000)
