"""songkla"""
def main():
    """Doc"""
    gan_x = int(input())
    gan_y = int(input())
    car_ax = int(input())
    car_ay = int(input())
    car_bx = int(input())
    car_by = int(input())
    calc_a = (((gan_x - car_ax)**2)+(gan_y - car_ay)**2)**0.5
    calc_b = (((gan_x - car_bx)**2)+(gan_y - car_by)**2)**0.5
    if calc_a < calc_b:
        print("A")
    elif calc_a > calc_b:
        print("B")
    elif calc_a == calc_b:
        if car_ay < car_by:
            print("B")
        elif car_ay > car_by:
            print("A")
        elif car_ay == car_by:
            if car_ax < car_bx: 
                print("A")
            elif car_ax > car_bx:
                print("B")
            elif car_ax == car_bx:
                print("A")
main()
