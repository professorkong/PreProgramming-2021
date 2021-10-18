"""magic"""
def main():
    """Docstring"""
    name = input()
    old = int(input())
    sex = input()
    high = float(input())
    if sex == "Male":
        print("Mr. %s Age: %d Height: %.2f"%(name, old, high))
    elif sex == "Female":
        print("Miss %s Age: %d Height: %.2f"%(name, old, high))
    if old >= 13 and old <= 15:
        if sex == "Male" and high >= 160:
            print("You can study in junior high school.")
        elif sex == "Female" and high >= 155:
            print("You can study in junior high school.")
        elif sex == "Male" and high < 160:
            print("You can not join this school.")
        elif sex == "Female" and high < 155:
            print("You can not join this school.")
    elif old >= 16 and old <= 18:
        if sex == "Male" and high >= 170:
            print("You can study in senior high school.")
        elif sex == "Female" and high >= 165:
            print("You can study in senior high school.")
        elif sex == "Male" and high < 170:
            print("You can not join this school.")
        elif sex == "Female" and high < 165:
            print("You can not join this school.")
    else:
        print("You can not join this school.")
main()
