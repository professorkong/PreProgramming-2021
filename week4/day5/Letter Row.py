"""Letter Row"""
def main():
    """Doc"""
    num = int(input())
    keepstr = ""
    for _ in range(1, num+1):
        txt = input()
        for j in txt:
            if j.isalpha():
                keepstr = keepstr + j
    print(keepstr)
main()
