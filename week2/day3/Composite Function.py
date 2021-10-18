"""Func Composite Function"""
def ref():
    """Composite Function"""
    #กำหนดค่าและแสดงผล
    anst = float(input())
    print("%.4f"%(fog1(gof1(anst))))
    print("%.4f"%(gof1(fog1(anst))))
def fog1(anst):
    """fogx"""
    #ฟังก์ชั่น f(x)
    fogx = (15+anst-(anst**3))/(((anst**2)/3+11))
    return fogx
def gof1(anst):
    """gof"""
    #ฟังก์ชั่น g(x)
    gofx = ((anst**3 )+(4*(anst)-1))
    return gofx
ref()
