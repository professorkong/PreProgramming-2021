"""mathone"""
def main():
    """math"""
    keep = int(input())
    lst = []
    lst2 = []
    for _ in range(keep):
        number = int(input())
        lst.append(number)
    multipul = float(input())
    for j in lst:
        lst2.append("%.2f"%(multipul * j))
    print(lst2)
main()
