"""X-Burner"""
def main():
    """DOcstrings"""
    lst = []
    while True:
        keep = input().lower()
        if keep == "end":
            break
        else:
            ans = keep.split(",")
            lst.extend(ans)
    if "x-gloves" in lst and "leon's tail" in lst and "bullet" in lst and "contact lens" in lst \
    and "ring" in lst and "reborn" in lst and "tsuna" in lst:
        print("X-Burner is ready.")
    else:
        print("NO, I have to run!!!")
main()
