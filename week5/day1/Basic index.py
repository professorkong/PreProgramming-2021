"""EP2"""
def main(text):
    """Docstring"""
    while True:
        keep = input()
        check = keep.lower()
        if check == "end":
            break
        text.append(keep)
    calc = int(input())
    if calc >= len(text):
        print("Index Not Found")
    else:
        print('List[%d] = "%s" '%(calc, text[calc]))
main([])
