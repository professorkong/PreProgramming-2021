"""Func One"""
def my_top():
    """kon puan pee"""
    keep = int(input())
    secret_1 = int(keep//10000)%10
    secret_2 = int(keep//1000)%10
    secret_3 = int(keep//100)%10
    secret_4 = int(keep//10)%10
    secret_5 = int(keep)%10
    calc = secret_1+secret_2+secret_3+secret_4+secret_5
    if calc %2 == 0 and calc %4 == 0:
        print("ผีตานี")
    elif calc %2 == 0 and calc %4 != 0:
        print("ผีกระหัง")
    elif calc %2 != 0 and calc %5 == 0:
        print("ผีกระสือ")
    elif calc %2 != 0 and calc %5 != 0:
        print("ผีปอบ")
my_top()
