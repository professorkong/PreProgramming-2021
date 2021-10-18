"""Kira"""
def main():
    """calc"""
    keepnum = input()
    ans = 0
    for i in range(len(keepnum)):
        ans = ans + int(keepnum[i])
    ans = ans**3
    keep = keepnum[0:5]
    ans = ans + int(keep)
    if len(str(ans)) < 5:
        print("%.05d"%ans)
    elif len(str(ans)) > 5:
        num = str(ans)[0:5]
        print(num)
    else:
        print(ans)
main()
