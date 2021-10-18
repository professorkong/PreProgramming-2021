"""Func I'don know"""
def my_top():
    """สูตรการแปลงอุณหภูมิเคลวิน"""
    cels = float(input())
    fahren = (cels*(9/5)+32)
    kelvin = (cels+273.15)
    rankine = ((cels+273.15)*(9/5))
    reaumer = ((cels)*(4/5))
    print("Celsius    = %.4f"%cels)
    print("Fahrenheit = %.4f"%fahren)
    print("Kelvin     = %.4f"%kelvin)
    print("Rankine    = %.4f"%rankine)
    print("Reaumer    = %.4f"%reaumer)
my_top()
