"""Matrix V.1"""
def main():
    """Docstring"""
    row, col = input().split("x")
    keep1, keep2 = input().split(",")
    make = []
    makelst = []
    for _ in range(int(row)):
        for _ in range(int(col)):
            make.append(int(input()))
        makelst.append(make)
        make = []
    print("result =", makelst[int(keep1)-1][int(keep2)-1])
    for i in makelst:
        print(str(i).replace(",", ""))
main()
