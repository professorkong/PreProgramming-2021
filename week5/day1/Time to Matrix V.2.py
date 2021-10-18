"""Matrix V.2"""
def main(empty):
    """Docstring"""
    row, col = input().split()
    lst1 = [[int(i) for i in input().split()] for _ in range(int(row))]
    lst2 = [[int(i) for i in input().split()] for _ in range(int(row))]
    for j in range(int(row)):
        for k in range(int(col)):
            empty.append(lst1[j][k] + lst2[j][k])
        print(str(empty).replace(",", ""))
        empty = []
main(empty=[])
