"""Way"""
def my_top():
    """Way"""
    rain_or_sun = input()
    imporant = input()
    keep = float(input())
    if rain_or_sun == "rainy" and imporant == "not important":
        print("Not go")
    else:
        if keep < 0:
            print("Error")
        elif keep < 1:
            print("Walk")
        elif keep < 20:
            print("Motorcycle")
        elif keep < 300:
            print("Car")
        else:
            print("Private jet")
my_top()
