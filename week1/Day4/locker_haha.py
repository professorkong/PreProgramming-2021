"""locker"""
def main():
    """calc locker"""
    all_lock = int(input())
    all_use = int(input())
    print((all_use*"X")+("O"*(all_lock-all_use))+" (available: %s"%(all_lock-all_use)+")")
main()
