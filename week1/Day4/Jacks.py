"""calcJacks"""
def main():
    """timetosleep"""
    yourtime = float(input())
    yourmin = int(yourtime)*60
    yoursec = (float("%.2f"%(yourtime%1)))*100
    print(int(yourmin+yoursec))
main()
