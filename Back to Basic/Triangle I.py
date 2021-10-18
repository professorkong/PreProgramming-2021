"""Triangle I"""
def main():
    """Tr"""
    cal1, cal2, cal3 = float(input()), float(input()), float(input())
    keep = (cal3**2)
    keep2 = (cal1**2+cal2**2)
    diff = abs(keep-keep2)
    if diff < 0.1:
        print("Yes")
    else:
        print("No")
main()
