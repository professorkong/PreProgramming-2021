"""Func fire"""
def main():
    """top"""
    your = input().upper()
    pas = len(your)
    pas2 = pas+4
    pas3 = pas2*"-"
    print("|%s|"%pas3)
    print("|  %s  |"%your)
    print("|%s|"%pas3)
main()