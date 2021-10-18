"""Catching Gokaijerry"""
def main():
    """Docstring"""
    police = int(input())
    aj_tin = 0
    while True:
        keep = input()
        if keep == "The trap is set.":
            aj_tin = 1
        if keep == "No trap here":
            aj_tin = 0
        if keep == "Boom!!!":
            if aj_tin == 0:
                police -= 1
                aj_tin = 1
        if keep == "Boom!!!":
            if aj_tin == 1:
                police = police
        if keep == "Catch the Gokaijerry":
            print("%d police is catching Gokaijerry."%(police))
            break
        if police == 0:
            print("Gokaijerry is alive.")
            break
main()
