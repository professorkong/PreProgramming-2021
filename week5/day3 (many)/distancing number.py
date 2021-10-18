"""DS"""
def main():
    """Doc"""
    keep1 = input()
    calc = keep1.split() #รับข้อความมาใช้ spirt เพื่อแยกช่องว่างของตัวเลขแต่ละตัว
    lst = []
    for i in range(0, len(calc)-1): #วนเลขตั้งแต่ 0 ถึงตำแหน่งก่อนสุดท้าย #len(calc) คือหาขนาด list
        keep2 = int(calc[i+1]) - int(calc[i]) #หาระยะห่างระหว่างค่าแต่ละตำแหน่ง
        lst.append(abs(keep2))
    print(min(lst))
main()
