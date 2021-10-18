"""How many in this ads"""
def main():
    """Docstring"""
    number = 0
    trim_low = 0
    trim_up = 0
    keep = input()
    for idonknow in keep:
        if idonknow.islower():
            trim_low = trim_low + 1
        elif idonknow.isdigit():
            number = number + 1
        elif idonknow.isupper():
            trim_up = trim_up + 1
    print("%d number(s)\n%d uppercase letter(s)\n%d lowercase letter(s)"\
    %(number, trim_up, trim_low))
main()
