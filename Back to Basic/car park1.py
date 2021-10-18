"""DocString"""
def main():
    """DocString"""
    goin = int(input()) #วันที่ได้ทำการนำรถมาจอด
    timein = int(input()) #เวลาที่นำรถมาจอด
    goout = int(input()) #วันที่ได้ทำการนำรถออก
    timeout = int(input()) #เวลาที่นำรถออก
    if (goin > goout) or (timeout > 23) or (timein > 23) or \
        (goin > 365) or (goout >= 365 and timeout != 0) or (goin <= 0) or \
            ((goin == goout) and (timein > timeout)):
        print("error")
    #or = มีเงื่อนไขใดเป็นจริงจะเป็นจริง #and = ต้องเป็นจริงทั้ง 2 เงื่อนไขถึงเป็นจริง
    #วันที่
    else:
        if goin == goout:
            day = 0
            hour = timeout - timein
        elif timein <= timeout:
            day = goout - goin
            hour = timeout - timein
        elif timein > timeout:
            day = goout - goin - 1
            hour = 24 - timein + timeout
        if hour <= 2:
            price = day*200
        elif hour <= 12:
            price = (hour*15)+(day*200)
        elif hour > 12:
            price = (day+1)*200
        if day >= 7:
            price = price-((day//7)*300)
        if day >= 28:
            price = price-500
        print("%d day %d hour" %(day, hour))
        print("%d baht" %price)
main()
