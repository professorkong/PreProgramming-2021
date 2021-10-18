"""Func I'don know"""
def calc():
    """func main"""
    bank = int(input())
    test = (bank//1000)
    bank = (bank%1000)
    test_2 = (bank//500)
    bank = (bank%500)
    test_3 = (bank//100)
    bank = (bank%100)
    test_4 = (bank//50)
    bank = (bank%50)
    test_5 = (bank//20)
    bank = (bank%20)
    print(test, test_2, test_3, test_4, test_5, sep="\n")
calc()
