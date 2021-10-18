"""bat"""
def main():
    """calc"""
    bat = float(input()) #พื้นที่ทั้งหมด
    wide = float(input()) #พื้นที่ของแบตที่มี
    calc = int((bat/100) * wide) #หาพื้นที่แบต O
    batuse = int(wide - calc)  #แบตที่หมดไป _ เอา พื้นที่ทั้งหมด - พื้นที่ของเเบตที่มี
    print("("+(calc)*"O"+"_"*(batuse)+")"+(" %d%%"%(bat)))
main()
