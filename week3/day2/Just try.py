"""AVG V.2"""
def ref():
    """V2"""
    anst1 = int(input())
    anst2 = int(input())
    anst3 = int(input())
    anst4 = int(input())
    anst5 = int(input())
    name1(anst1)
    name1(anst2)
    name1(anst3)
    name1(anst4)
    name1(anst5)
def name1(anst1):
    """Docsting"""
    if anst1 < 7:
        print("CHILD")
    elif anst1 < 25:
        print("TEENAGER")
    elif anst1 < 59:
        print("ADULT")
    elif anst1 >= 59:
        print("ELDER")
ref()
