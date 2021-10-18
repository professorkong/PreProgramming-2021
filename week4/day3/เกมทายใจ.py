"""เกมทายใจ"""
def main():
    """Docstring"""
    keep1 = int(input())
    keep2 = int(input())
    for _ in range(keep2):
        keep3 = int(input())
        if keep3 == keep1:
            print("Yes! It is %d." %keep1)
            break
        else:
            continue
    if keep3 != keep1:
        print("No more chances. You lose.")
main()
