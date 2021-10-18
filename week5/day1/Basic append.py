"""EP1"""
def main():
    """Docstring"""
    keep = int(input())
    mylist = []
    for _ in range(keep):
        mylist.append(input())
    print(*mylist)
main()
