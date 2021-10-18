"""teacher"""
def main():
    """Docstring"""
    keep1 = input()
    keep2 = input()
    score = 10
    calc = 0
    wonleb = ""
    for i in range(1, len(keep2) + 1):
        if keep1[i - 1:i].lower() == keep2[i - 1:i].lower():
            wonleb += keep2[i - 1:i]
        else:
            wonleb += "("+keep2[i-1:i]+")"
            calc = calc + 1
    wonleb = wonleb.replace(")(", "")
    print(wonleb, end="")
    score -= calc
    if calc > score:
        score = 0
    print("\n%d/10 (-%d)" %(score, abs(calc)))
main()
