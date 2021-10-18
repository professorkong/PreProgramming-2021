"""magic"""
def main():
    """Docstring"""
    name = input()
    old = int(input())
    sex = input()
    high = float(input())
    
    if (old >= 13 and old <= 15) and sex == "Male" and high >= 160:
        print("Mr. %s Age: %d Height: %.2f"%(name, old, high))
        print("You can study in junior high school.")
    elif (old >= 13 and old <= 15) and sex == "Male" and high < 160:
        print("Mr. %s Age: %d Height: %.2f"%(name, old, high))
        print("You can not join this school.")
    elif (old >= 13 and old <= 15) and sex == "Female" and high >= 155:
        print("Miss %s Age: %d Height: %.2f"%(name, old, high))
        print("You can study in junior high school.")
    elif (old >= 13 and old <= 15) and sex == "Female" and high < 155:
        print("Miss %s Age: %d Height: %.2f"%(name, old, high))
        print("You can not join this school.")
    elif (old >= 16 and old <= 18) and sex == "Male" and high >= 170:
        print("Mr. %s Age: %d Height: %.2f"%(name, old, high))
        print("You can study in senior high school.")
    elif (old >= 16 and old <= 18) and sex == "Male" and high < 170:
        print("Mr. %s Age: %d Height: %.2f"%(name, old, high))
        print("You can not join this school.")
    elif (old >= 16 and old <= 18) and sex == "Female" and high >= 165:
        print("Miss %s Age: %d Height: %.2f"%(name, old, high))
        print("You can study in senior high school.")
    elif (old >= 16 and old <= 18) and sex == "Female" and high < 165:
        print("Miss %s Age: %d Height: %.2f"%(name, old, high))
        print("You can not join this school.")
    else:
        if sex == "Male":
            print("Mr. %s Age: %d Height: %.2f"%(name, old, high))
            print("You can not join this school.")
        elif sex == "Female":
            print("Miss %s Age: %d Height: %.2f"%(name, old, high))
            print("You can not join this school.")
main()
