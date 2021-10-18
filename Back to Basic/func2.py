"""func"""
def cal(para1, para2, para3):
    """หาค่าสูงสุดโดยใช้ฟังก์ชั่น"""
    return min(para1, para2, para3)
def main():
    """Doc"""
    keep1 = int(input())
    keep2 = int(input())
    keep3 = int(input())
    high = cal(keep1, keep2, keep3)
    print(high)
main()
