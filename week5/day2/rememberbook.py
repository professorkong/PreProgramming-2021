"""rebook"""
def main():
    """rebook"""
    keep = int(input())
    lst = []
    lst2 = []
    lst3 = []
    for _ in range(keep):
        book = str(input())
        lst.append(book)
    remember = int(input())
    for _ in range(remember):
        book2 = str(input())
        lst2.append(book2)
    for k in lst:
        if k not in lst2 and k not in lst3:
            lst3.append(k)
    print(len(lst3))
    for calc in lst3:
        print(calc)
main()
