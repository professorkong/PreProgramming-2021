"""JAI 1"""
def main():
    """Docstring"""
    lst = []
    while True:
        keep = input().capitalize() #รับอินพุทมาเป็นตัวอักษรแรกพิมพ์ใหญ่
        if keep == "Stop": #ถ้าพิมพ์ stop ให้เบรค
            break
        elif keep.isalpha(): #แล้วถ้า keep ที่รับมาเป็น isalpha(ตัวอักษร)
            if keep not in lst: #กรณีแรก ถ้า keep ไม่อยู่ใน lst
                lst.append(keep) #ให้เพิ่มข้อมูลที่รับมาจาก keep ลงใน lst
    name = input().capitalize() 
    if name.isalpha():
        if name in lst:
            print(lst.index(name)+1)
        else:
            print("Not found")
    elif name.isnumeric():
        if int(name) > len(lst):
            print("Not found")
        else:
            print(lst[int(name)-1])
    else:
        print("Not found")
main()
