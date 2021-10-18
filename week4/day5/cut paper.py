"""countdown"""
def main():
    """Doc"""
    keep = input()
    num = int(input())
    keep_num_chars = keep[:num+1]
    print(keep_num_chars)
    out = keep[num:len(keep)]
    print(out)
main()
