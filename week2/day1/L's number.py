"""Problem Number"""
def calc():
    """func main"""
    number_1 = int(input())//10000%10
    number_2 = int(input())//10000%10
    number_3 = int(input())//10000%10
    number_4 = int(input())
    number_5 = (number_4)//10000%10
    number_6 = (number_4)//1000%10
    number_7 = (number_4)//100%10
    number_8 = (number_4)//10%10
    costall = number_1+number_2+number_3+number_5+number_6+number_7+number_8
    print(costall)
calc()
