"""Windy"""
def main():
    """Doc"""
    berker = ""
    stock = True
    material = ("cheese", "egg", "ketchup", "mayonnaise", "beef steak", "chicken steak", \
    "fish steak", "bacon", "sausage", "french fries", "bun")
    while True:
        keep = input().lower()
        if keep not in material and keep != "end":
            stock = False
        if "vegetables" in keep:
            print("We have to cancel your order! Get out!!")
            break
        if keep != "end":
            berker = berker + keep + " "
        else:
            if berker.count("bun") >= 2 and berker.count("bun end") == 1:
                if stock:
                    print("This is your burger, have a good meal.")
                else:
                    print("I'm not sure if it is a Windy Burger.")
            else:
                print("I'm not sure if it is a Windy Burger.")
            break
main()
