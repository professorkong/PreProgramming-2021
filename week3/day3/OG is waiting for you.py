"""OG"""
def my_top():
    """OG"""
    age = int(input())
    def keep1():
        """Doc"""
    if age < 17:
        print("May be next time.")
    if age >= 17 and age < 20:
        dek = input().upper()
        if dek == "Y":
            keep = int(input())
            if keep >= 12:
                ucan = input().upper()
                if ucan == "Y":
                    print("You can be in OG!")
                else:
                    print("May be next time.")
            else:
                print("May be next time.")
        else:
            print("May be next time.")
    def keep2():
        """Doc"""
        if age >= 20 and age <= 23:
            keepdata = int(input())
            if keepdata >= 12:
                ucan = input().upper()
                if ucan == "Y":
                    print("You can be in OG!")
                else:
                    print("May be next time.")
            else:
                print("May be next time.")
        if age > 23:
            print("May be next time.")
    keep1()
    keep2()
my_top()
