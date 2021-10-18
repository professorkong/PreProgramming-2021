"""the world"""
def main():
    """Docstring"""
    keep1 = int(input())
    keep2 = int(input())
    calc = int(input()) + 1
    distance = 0
    for _ in range(1, calc):
        chronos = int(input())
        chronos_2 = int(input())
        calc2 = (((keep1 - chronos)**2) + ((keep2 - chronos_2)** 2))**0.5
        if 500 - calc2 > 0:
            distance = distance + 1
    if distance > 1:
        print("You got %d enemies in your area."%(distance))
    elif distance == 1:
        print("You got 1 enemy in your area.")
    else:
        print("Muda Muda Muda.")
main()
