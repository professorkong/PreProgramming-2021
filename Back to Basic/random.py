"""test"""
def main():
    """Test"""
    keep = int(input())
    while keep:
        tang = int(input("จะแทงจำนวนอะไรดี : "))
        print("คุณได้แทง : ",tang)
        if (tang > 5 and tang <= 10):
            ans = "คุณแทงสูง"
            print(ans)
        elif (tang >= 0 and tang <=5):
            ans = "คุณแทงต่ำ"
            print(ans)
        else:
            print("กรุณาพิมพ์เลข 0-10 เท่านั้น กรุณาพิมพ์ใหม่")
main()
