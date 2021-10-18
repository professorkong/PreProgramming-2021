"""quantum computer V.2"""
def main():
    """Docstring"""
    keep = 0
    count = 0
    start = 0
    cool = 0
    while True:
        sass = input().upper()
        if cool == 0 and count >= 1000:
            print("ERROR: NonAbsoluteZeroLimitExceeded (QCP002)")
            break
        if sass == "BOOT":
            start = 1
            count += 1
        if sass == "FRZ":
            cool = 1
            count += 1
        if sass == "INC" and start == 1:
            keep = keep + 1
            count += 1
        if sass == "DEC" and start == 1:
            keep = keep - 1
            count += 1
        if sass == "DUBL" and start == 1:
            keep = keep * 2
            count += 1
        if sass == "HALF" and start == 1:
            keep = keep / 2
            count += 1
        if sass == "END":
            break
    if cool == 0 and start == 1 and count < 1000:
        print("WARN: AbsoluteZero (QCP001)")
    elif start == 0 and keep == 0 and count < 1000:
        print("WARN: MissingBootInstruction (QCP003)")
    print("%.6f"%keep)
main()
