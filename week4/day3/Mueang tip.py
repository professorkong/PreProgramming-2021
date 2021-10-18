"""ภาษาเมืองทิพย์"""
def roby(calc1, calc2):
    """ภาษาเมืองทิพย์"""
    return kids(calc1) // (kids(calc2) * (kids(calc1 - calc2)))
def kids(calc):
    """ภาษาเมืองทิพย์"""
    keep1 = 1
    for i in range(1, abs(calc)+1):
        keep1 = keep1 * i
    return keep1
def main():
    """ภาษาเมืองทิพย์"""
    endland = int(input())
    germany = int(input())
    spain = int(input())
    italian = int(input())
    if endland < germany:
        germany = endland
    if spain < italian:
        italian = spain
    print("%d Alphabet"%(germany + italian))
    rprprp = roby(endland, germany) * roby(spain, italian) * kids(germany + italian)
    if germany + italian == 0:
        rprprp = 0
    print("%d Word"%(rprprp))
main()
