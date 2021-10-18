"""ไม่บอกหรอกเกรดไปคำนวณเอาหยิ่ง"""
def main():
    """Function ไม่บอกหรอกเกรดไปคำนวณเอาหยิ่ง"""
    score = int(input())
    print("4.0" * (score >= 80) + "3.5" * (score < 80 and score >= 75) \
+ "3.0" * (score < 75 and score >= 70) + "2.5" * (score < 70 and score >= 65) \
+ "2.0" * (score < 65 and score >= 60) + "1.5" * (score < 60 and score >= 55) \
+ "1.0" * (score < 55 and score >= 50) + "0.0" * (score < 50))
main()
