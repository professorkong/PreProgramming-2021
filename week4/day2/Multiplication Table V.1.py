"""Multiplication Table V.1"""
def main():
    """Docstring"""
    number = int(input())
    print("-----------------")
    for sing in range(number+1):
        for song in range(1, 13):
            print("%3d x%4d = %5d"%(sing, song, sing*song))
    print("-----------------")
main()
