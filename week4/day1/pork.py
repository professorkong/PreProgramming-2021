"""Pork"""
def main():
    """Doc"""
    keep = 0
    stone = ""
    #keep1 = ""
    while True:
        num = input().lower()
        if num == "end":
            break
        else:
            papaya = ("mh", "ph", "sh", "wh", "gh")
            if num in papaya:
                stone = stone + num + " "
                if num == "gh":
                    keep_mh = stone.count("mh")
                    keep_ph = stone.count("ph")
                    keep_sh = stone.count("sh")
                    keep_wh = stone.count("wh")
                    if keep_mh and keep_sh and keep_ph and keep_wh:
                        keep = keep + 1
                        stone = ""
            else:
                print("ERROR")
                stone = ""
    print(keep)
main()
