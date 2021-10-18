"""Do you Know"""
def my_top():
    """ปีอธิกสุรทิน"""
    keep1 = int(input())
    if keep1 %400 == 0 or keep1 %4 == 0 and keep1 %100 != 0:
        print("%s is a leap year."%keep1)
    else:
        print("%s is not a leap year."%keep1)
my_top()
