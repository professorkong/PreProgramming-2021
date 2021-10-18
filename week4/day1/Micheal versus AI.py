"""Function"""
def main():
    """Docstring"""
    dog = ("Chihuahua", "Yorkshire terrier", "Pug", "Dog")
    pig = ("Yorkshire", "Duroc", "Berkshire", "Pig")
    bread = ("Banana bread", "Baguette", "Breadstick", "Bread")
    keep1 = ""
    while True:
        keep = input().capitalize()
        keep1 += "Dog"*(keep in dog)+"Pig"*(keep in pig)+"Bread"*(keep in bread)
        if keep1.count("DogPigBread") == 1:
            print("Error!!!")
            break
        elif keep == "Take care micheal.":
            print("Attack Micheal!!")
            break
        elif keep1.count("DogDogDogDogDog") or keep1.count("PigPigPigPigPig") or\
            keep1.count("BreadBreadBreadBreadBread"):
            print("Stand By")
            break
main()
