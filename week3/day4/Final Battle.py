"""Final Battle"""
def my_top():
    """Final Battle"""
    ben = int(input())
    gwen = int(input())
    gwen_control = int(input())
    zun = int(input())
    calc1 = ((gwen*(gwen_control/100))+zun)
    if calc1 > ben:
        print("The world is save!")
    elif calc1 == ben:
        print("The world is save but we lost our hero.")
    elif calc1 < ben:
        print("Ben 99 is going to ruin the world.")
my_top()
