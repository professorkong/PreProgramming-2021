"""Basic While"""
def main():
    """Doc"""
    master = 0
    number = 1
    while number >= 0:
        number = int(input())
        if number >= 0:
            master = master + number
    print(master)
main()
