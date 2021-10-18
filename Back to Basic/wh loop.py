"""test"""
def main():
    """calc"""
    num1 = 0
    while True:
        num2 = int(input())
        if num2 >= 0:
            num1 = num1 + num2
        else:
            break
    print(num1)
main()
# """test"""
# def main():
#     """calc"""
#     num1 = 0
#     num2 = int(input())
#     while num2 >= 0:
#         num1 = num1 + num2
#         num2 = int(input())
#         if num2 < 0:
#             break
#     print(num1)
# main()
