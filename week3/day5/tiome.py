"""Late_Meeting"""
def main():
    """Function Late_Meeting"""
    hour = int(input())
    minute = int(input())
    second = int(input())
    time = input()
    fminute = int(input())
    fsecond = int(input())
    f_sec = (second + fsecond)%60
    minplus = (second + fsecond)//60
    f_min = (minute + fminute + minplus)%60
    hourplus = (minute + fminute + minplus)//60
    f_hour = hour + hourplus
    if (fminute == 0) and (fsecond == 0):
        print("%.02d:%.02d:%.02d %s" %(f_hour, f_min, f_sec, time))
    else:
        if time == 'pm':
            f_hour = f_hour + 12
        total_time = ((f_hour%24)*3600) + (f_min*60) + f_sec
        if (hour == 12) and ((fminute + minute) < 720):
            if time == 'am':
                time = 'am'
            else:
                time = 'pm'
        elif (hour == 12) and ((fminute + minute) >= 720):
            if time == 'am':
                time = 'pm'
            else:
                time = 'am'
        else:
            if 0 <= total_time <= 43199:
                time = 'am'
            elif 43200 <= total_time < 86400:
                time = 'pm'
        f_hour = f_hour%12
        if f_hour == 0:
            f_hour = 12
        print("%.02d:%.02d:%.02d %s" %(f_hour, f_min, f_sec, time))
main()
