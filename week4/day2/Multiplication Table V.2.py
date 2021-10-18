"""Multiplication Table V.2"""
def main():
    """Docstring"""
    #number = int(input())
    #print("-----------------")
    for sing in range(2, 12+1):
        print("-------------")
        for song in range(1, 13):
            print("%2d x%3d = %3d"%(sing, song, sing*song))
    print("-------------")
main()
