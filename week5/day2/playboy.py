"""playboy"""
def main():
    """playboy"""
    lst = []
    while True:
        keep = str(input()).capitalize()
        if keep == "Stop":
            break
        elif keep.isalpha():
            lst.append(keep)
    lst.sort()
    for i in lst:
        print(i)
main()
