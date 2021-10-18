def main():
    """Doc"""
    food = int(input())
    for i in range(0, food):
        for j in range(0, i+1):
            print("*", end=" ")
        print("")
        #print("")
    print("Close Program")
main()
