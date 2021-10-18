"""MAX"""
def main():
    """Docstring"""
    num = int(input())
    lst = []
    for _ in range(num):
        lst.append(float(input()))
    lst.sort()
    print("%.2f"%lst[-1])
main()
