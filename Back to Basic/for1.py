"""func"""
def main():
    """Doc"""
    keep = int(input())
    ans = 0
    cheaka = 0
    for i in range(1,keep+1):
        master = input()
        if master == "J":
            ans += 10
        elif master == "Q":
            ans += 10
        elif master == "K":
            ans += 10
        elif master.isnumeric():
            ans += int(master)
        if master == "A":
            cheaka += 1
            if ans > 10:
                ans += 1
            else:
                ans += 11
    if ans > 21:
        if cheaka >= 1:
            ans -= 10
    print(ans)
main()
