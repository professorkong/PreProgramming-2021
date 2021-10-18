"""Basic While"""
def main():    
    keep1 = int(input())
    keep2 = int(input())
    keep3 = int(input())
    if keep1 < keep2 and keep2 < keep3 or keep2 > keep1:
        print("Pass")
    else:
        print("Not Pass")
main()
