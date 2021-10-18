"""JM"""
def main():
    """Doc"""
    keep1 = int(input())
    keep2 = int(input())
    kong = ""
    for i in range(0, keep1+1):
        kong += str(i) #เก็บเลขที่วนไว้ใน kong
    keep = kong.count(str(keep2))#หาจำนวนในตัวแปร kong โดย count จำนวนที่ต้องการจะหาว่ามีจำนวนกี่ตัว
    print(keep)
main()
