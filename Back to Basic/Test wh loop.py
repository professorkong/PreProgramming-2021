"""While"""
def main():
    """Test"""
    while True:
        indx = float(input())
        if indx == 0:
            print("จำนวนที่ต้องการ = %d"%(indx))
            break
        else:
            if indx > 0:
                print("ระบุจำนวน 0 เท่านั้น, จำนวนที่คุณระบุคือ %.3f"%(indx))
            elif indx < 0:
                print("ระบุจำนวน 0 หรือ มากกว่า 0, จำนวนที่คุณระบุคือ %.3f"%(indx))
main()
