"""change data"""
def fac():
    """Docstring"""
    calc_1 = input()
    for i in calc_1:
        if i.isalpha():
            if i.isupper():
                print(chr((((ord(i)-65)+5)%26)+65), end="")
            elif i.islower():
                print(chr((((ord(i)-97)+5)%26)+97), end="")
        elif i.isdigit():
            i = (int(i)+5)%10
            print(i, end="")
        else:
            print(i, end="")
fac()
