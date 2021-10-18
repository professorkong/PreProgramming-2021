"""MorLam V.1"""
def main():
    """Docstring"""
    football = input()
    hed = 0
    while True:
        press = input().lower()
        if press == "stop":
            print("ball in cup %s"%football)
            print("shuffle %d time "%hed)
            break
        if press == "1":
            if football == "A":
                football = "B"
            elif football == "B":
                football = "A"
        elif press == "2":
            if football == "B":
                football = "C"
            elif football == "C":
                football = "B"
        elif press == "3":
            if football == "A":
                football = "C"
            elif football == "C":
                football = "A"
        hed = hed + 1
main()
