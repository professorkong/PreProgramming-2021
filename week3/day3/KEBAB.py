"""AP"""
def my_top():
    """Doc"""
    keep1 = int(input())
    keep2 = int(input())
    feedback = input()
    if feedback == "This kebab is very good":
        keep1 = keep1-(keep1 * (30/100))
    elif feedback == "This is not good not bad":
        keep1 = keep1-(keep1 * (5/100))
    elif feedback == "This is not kebab":
        keep1 = keep1+(keep1 * (16/100))
    else:
        keep1 = keep1*0
    keep1 = keep1*keep2
    print("%.2f"%keep1)
my_top()
