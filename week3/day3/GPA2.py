"""GPA"""
def my_top():
    """GPA"""
    score = float(input())
    print("4.0" * (score >= 80) or ("3.5" * (score >= 75) or ("3.0" * (score >= 70)\
        or ("2.5" * (score >= 65) or ("2.0" * (score >= 60) or ("1.5" * (score >= 55)\
            or ("1.0" * (score >= 50) or ("0.0" * (score < 50)))))))))
my_top()
