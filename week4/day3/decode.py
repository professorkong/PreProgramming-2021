"""change data"""
def fac():
    """Docstring"""
    keep = int(input())
    password = ""
    test = ""
    y_y = 0
    for _ in range(keep):
        kids = input()
        password += kids
    while True:
        kids2 = input()
        test += kids2
        y_y += 1
        if test.count(password):
            print("Finally, We found this treasure.\n%d"%y_y)
            break
fac()
