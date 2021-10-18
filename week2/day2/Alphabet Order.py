"""Func Alphabet"""
def calc():
    """func main"""
    keep = input().upper()
    data = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    search = data.find(keep)+1
    print(search)
calc()
