"""Concurrent"""
def calc():
    """func main"""
    time = float(input())
    date = time // (24 * 3600) #time//(24hr*3600sec)
    time = time % (24 * 3600) #24hr*3600sec
    hour = time // 3600 #hour//(sec3600)
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    print("%02d:%02d:%02d:%02d"%(date, hour, minutes, seconds))
calc()
