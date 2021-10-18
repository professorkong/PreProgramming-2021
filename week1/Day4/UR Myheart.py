"""UR Heart"""
def main():
    """ur"""
    heart = int(input())
    bonus = int(input())
    print("My Heart " + "%s"%(heart) + " Heart |" + ("<3" * heart) + ("<3"* bonus) + "\
    " + ("_" * (10 - (heart + bonus))) + "|" + "\nMy Bonus "+"%s"%(bonus)+" Heart")
main()
