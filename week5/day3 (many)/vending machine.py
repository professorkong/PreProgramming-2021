"""vending machine"""
def main():
    """Docstring"""
    money = 0
    count = 0
    while True:
        data = input()
        if data == "END":
            break
        elif int(data) // 1 >= 0:
            money += int(data)
        elif int(data) // 1 < 0:
            ans = money + int(data)
            if ans >= 0:
                money += int(data)
                count = count+ 1
            elif ans < 0:
                print("ERROR: Not enough money for this item.")
    print("Items: %s"%count)
    print("Change: %s THB"%money)
main()
