"""arithmetic sequence"""
def main():
    """Docstring"""
    first = int(input())
    second = int(input())
    third = int(input())
    if third > 0:
        second = second + 1
    else:
        second = second - 1
    for _ in range(first, second, third):
        print(_)
main()
