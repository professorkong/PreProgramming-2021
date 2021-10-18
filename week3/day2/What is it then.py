"""WIIT"""
def my_top():
    """wiit"""
    keep1 = input()
    if keep1.isalpha():
        print("\'%s\' is an alphabet."%keep1)
    elif keep1.isnumeric():
        print("\'%s\' is numeric."%keep1)
    else:
        print("\'%s\' is not both an alphabet and numeric."%keep1)
my_top()
