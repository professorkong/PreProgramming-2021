"""test"""
def main():
    """calc"""
    summm = 0
    while True :
        ans1 = int(input())
        summm = summm + ans1
        if ans1 < 0:
            break
    print(summm)
main()
