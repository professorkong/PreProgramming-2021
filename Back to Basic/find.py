"""Function Test"""
def main():
    text = "Today at Sunday. I stay at home and keep at coding. "
    word = "at"
    caltext = 0
    text2 = text[text.find(word, caltext)+len(word)+1:] #หาคำใน text โดยใช้ find + len(คำที่จะหา)+1:
    next_world = text2[: text2.find(" ")] #หาคำไปจนเจอ speckbar แล้วจึงหยุด
    print(next_world)
    caltext = text2.find(" ") + 1
    text2 = text[text.find(word, caltext)+len(word)+1:] #หาคำใน text โดยใช้ find + len(คำที่จะหา)+1:
    next_world = text2[: text2.find(" ")] #หาคำไปจนเจอ speckbar แล้วจึงหยุด
    print(next_world)
    caltext = text2.find(" ") + 1
    text2 = text[text.find(word, caltext)+len(word)+1:] #หาคำใน text โดยใช้ find + len(คำที่จะหา)+1:
    next_world = text2[: text2.find(" ")] #หาคำไปจนเจอ speckbar แล้วจึงหยุด
    print(next_world)
main()
