"""Basic While"""
def main():    
    """Doc"""
    keep = int(input())
    for i in range(1,keep+1):
        for j in range(1,i+1):
            print("*", end="2")
        print()
main()
