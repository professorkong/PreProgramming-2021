"""secret code"""
def main():
    """calc secret"""
    keep = int(input())
    secret_1 = int(keep//100000000)%10
    secret_2 = int(keep//1000000)%10
    secret_3 = int(keep//10000)%10
    secret_4 = int(keep//100)%10
    secret_5 = int(keep)%10
    print(secret_1, secret_2, secret_3, secret_4, secret_5, sep="")
main()
