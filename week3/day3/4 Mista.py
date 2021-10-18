"""4 Mista"""
def my_top(one, two):
    """4 Mista"""
    if one.count("4") \
        or one.count("four") \
            or len(one)%4 == 0 \
                or one.count(two) == 4:\
        print("It's not safe four Mista....")
    else:
        print("MISTA, THIS ONE'S 4 U.")
my_top(input().lower(), (input().lower()))
