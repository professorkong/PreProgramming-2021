"""Phasmophobian"""
def func(text1, text2):
    """Doc"""
    keep = ""
    if text1 == "spirit box" or text2 == "spirit box":
        if text2 == "freezing temperature" or text1 == "freezing temperature":
            keep = ("I think %s is the answer!!!."%("Wraith"))
        elif text2 == "fingerprints" or text1 == "fingerprints":
            keep = ("I think %s is the answer!!!."%("Hantu"))
        elif text2 == "no evidence" or text1 == "no evidence" and text2 == \
        "spirit box" or text1 == "spirit box":
            keep = ("I think %s and %s, so one of them is the answer!!!."%("Wraith", "Hantu"))
    if text1 == "ghost writing" or text2 == "ghost writing":
        if text2 == "ghost orb" or text1 == "ghost orb":
            keep = ("I think %s is the answer!!!."%("Yurei"))
        elif text2 == "fingerprints" or text1 == "fingerprints":
            keep = ("I think %s is the answer!!!."%("Revenant"))
        elif text2 == "no evidence" or text1 == "no evidence" and text2 == \
        "ghost writing" or text1 == "ghost writing":
            keep = ("I think %s and %s, so one of them is the answer!!!."%("Yurei", "Revenant"))
    if text1 == "emf level 5" or text2 == "emf level 5":
        if text2 == "ghost orb" or text1 == "ghost orb":
            keep = ("I think %s is the answer!!!."%("Phantom"))
        elif text2 == "freezing temperature" or text1 == "freezing temperature":
            keep = ("I think %s is the answer!!!."%("Banshee"))
        elif text2 == "no evidence" or text1 == "no evidence" and text2 == \
        "emf level 5" or text1 == "emf level 5":
            keep = ("I think %s and %s, so one of them is the answer!!!."%("Phantom", "Banshee"))
    return keep
def func2(text1, text2):
    """Doc"""
    keep = str()
    if text1 == "fingerprints" or text2 == "fingerprints":
        if text2 == "ghost writing" or text1 == "ghost writing":
            keep = ("I think %s is the answer!!!."%("Revenant"))
        elif text2 == "spirit box" or text1 == "spirit box":
            keep = ("I think %s is the answer!!!."%("Hantu"))
        elif text2 == "no evidence" or text1 == "no evidence" and text2 == \
        "fingerprints" or text1 == "fingerprints":
            keep = ("I think %s and %s, so one of them is the answer!!!."%("Revenant", "Hantu"))
    if text1 == "freezing temperature" or text2 == "freezing temperature":
        if text2 == "spirit box" or text1 == "spirit box":
            keep = ("I think %s is the answer!!!."%("Wraith"))
        elif text2 == "emf level 5" or text1 == "emf level 5":
            keep = ("I think %s is the answer!!!."%("Banshee"))
        elif text2 == "no evidence" or text1 == "no evidence" and text2 == \
        "freezing temperature" or text1 == "freezing temperature":
            keep = ("I think %s and %s, so one of them is the answer!!!."%("Wraith", "Banshee"))
    if text1 == "ghost orb" or text2 == "ghost orb":
        if text2 == "emf level 5" or text1 == "emf level 5":
            keep = ("I think %s is the answer!!!."%("Phantom"))
        elif text2 == "ghost writing" or text1 == "ghost writing":
            keep = ("I think %s is the answer!!!."%("Yurei"))
        elif text2 == "no evidence" or text1 == "no evidence" and text2 == \
        "ghost orb" or text1 == "ghost orb":
            keep = ("I think %s and %s, so one of them is the answer!!!."%("Phantom", "Yurei"))
    return keep
def main():
    """Doc"""
    text1 = input().lower()
    text2 = input().lower()
    if text1 == "no evidence" and text2 == "no evidence":
        print("I think %s, %s, %s, %s, %s and %s, so one of them is the answer!!!." \
            %("Wraith", "Phantom", "Yurei", "Banshee", "Revenant", "Hantu"))
    else:
        if func2(text1, text2) == "":
            print(func(text1, text2))
        else:
            print(func2(text1, text2))
main()
