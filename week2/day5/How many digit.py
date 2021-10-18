"""How many digit"""
def my_top():
    """digit"""
    step1 = input().replace(".", "")
    keep = str(int(step1))
    step2 = int(((keep)).count("0"))
    step3 = int(((keep)).count("1"))
    step4 = int(((keep)).count("2"))
    step5 = int(((keep)).count("3"))
    step6 = int(((keep)).count("4"))
    step7 = int(((keep)).count("5"))
    step8 = int(((keep)).count("6"))
    step9 = int(((keep)).count("7"))
    step10 = int(((keep)).count("8"))
    step11 = int(((keep)).count("9"))
    calc = (step2+step3+step4+step5+step6+step7+step8+step9+step10+step11)
    print(calc)
my_top()