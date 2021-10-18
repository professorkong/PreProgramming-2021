"""Basic While"""
def cal(kids1, kids2):
    if kids1 > kids2:
        return kids1
    else:
        return kids2
def main():    
    """Docs"""
    keep1 = int(input())
    kid = cal(keep1, int(input()))
    kid = cal(kid, int(input()))
    kid = cal(kid, int(input()))
    kid = cal(kid, int(input()))
    kid = cal(kid, int(input()))
    kid = cal(kid, int(input()))
    kid = cal(kid, int(input()))
    print(kid)
main()
