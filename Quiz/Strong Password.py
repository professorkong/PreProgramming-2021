"""Strong Password"""
def calc(keepstr):
    """def"""
    score = 0
    if keepstr.isnumeric():
        score += 50
    elif keepstr.isalpha():
        score += 30
        if keepstr.islower():
            score += 100
        elif keepstr.isupper():
            score += 85
        else:
            score += 175
    elif keepstr.isalnum():
        score += 75
    chec = 0
    for i in keepstr:
        if i == keepstr[0]:
            chec += 1
    chec -= 1
    score -= max((chec - 3), 0)*15
    score += max(len(keepstr)-10, 0)*10
    score += ord(keepstr[-1])
    return score
def main():
    """calc"""
    keepstr = input()
    if len(keepstr) < 6:
        print("try again")
        keepstr2 = input()
        if len(keepstr2) < 6:
            print("process terminated")
        else:
            score = calc(keepstr2)
            print("Password : %s"%(len(keepstr2)*"*"))
            print("Security score : %d"%(score))
            if score < 150:
                print("Security level : poor")
            elif score < 300:
                print("Security level : acceptable")
            else:
                print("Security level : secure")
    else:
        score = calc(keepstr)
        print("Password : %s"%(len(keepstr)*"*"))
        print("Security score : %d"%(score))
        if score < 150:
            print("Security level : poor")
        elif score < 300:
            print("Security level : acceptable")
        else:
            print("Security level : secure")
main()
