"""3star"""
def doing():
    """Car park 3 star"""
    day = int(input())
    time = int(input())
    day1 = int(input())
    time1 = int(input())
    dayx = (day1 - day)*(time1 >= time)+(day1 - day - 1)*(time1 < time)
    timea = (time1 - time)*(time1 >= time) + ((24-time)+time1) * (time1 < time)
    keeptime = (timea)*(timea <= 12)*(timea > 2)
    keepday = 1*(timea > 12)
    if 0 < day <= 365 and 0 < day1 <= 365 and 0 <= time < 24 and 0 <= time1 < 24 and not \
(day > day1) and not ((day == day1) and (time > time1)):
        if (dayx) < 7:
            print("%d day %d hour\n%d baht"%(dayx, timea, 200*dayx + 200*keepday + 15*keeptime))
        elif 28 > (dayx):
            print("%d day %d hour\n%d baht"%(dayx, timea, 200*dayx + 200*keepday + 15*keeptime \
-(300*((dayx)//7))))
        elif (dayx) >= 28:
            print("%d day %d hour\n%d baht"%(dayx, timea, 200*dayx + 200*keepday +\
15*keeptime -500-(300*((dayx)//7))))
    else:
        print("error")
doing()
