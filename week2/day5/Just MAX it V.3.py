"""Func Max V3"""
def my_top():
    """Max V.3"""
    step1 = float(input())
    step2 = float(input())
    step3 = float(input())
    step4 = float(input())
    step5 = float(input())
    step6 = float(input())
    step7 = float(input())
    step8 = float(input())
    calc1 = (step1+step2)-min(step1, step2)
    calc2 = (step3+step4)-min(step3, step4)
    calc3 = (step5+step6)-min(step5, step6)
    calc4 = (step7+step8)-min(step7, step8)
    master1 = (calc1+calc2)-min(calc1, calc2)
    master2 = (calc3+calc4)-min(calc3, calc4)
    master3 = (master1+master2)-min(master1, master2)
    print("%.2f"%master3)
my_top()
