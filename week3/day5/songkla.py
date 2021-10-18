"""songkla"""
def main():
    """Doc"""
    sui = input().lower()
    phung = input().lower()
    calc = calculate(sui, phung)
    print(calc)
def calculate(sui, phung):
    """ด๊อกสตริง"""
    psuiwin = (sui == "bird" and phung == "water") * "Sui"
    psuiwina = (sui == "stone" and phung == "bird") * "Sui"
    psuiwinb = (sui == "water" and phung == "stone") * "Sui"
    pphungwin = (sui == "water" and phung == "bird") * "Numphung"
    pphungwina = (sui == "stone" and phung == "water") * "Numphung"
    pphungwinb = (sui == "bird" and phung == "stone") * "Numphung"
    draw = (sui == phung) * "Draw"
    return psuiwin+psuiwina+psuiwinb+pphungwin+pphungwina+pphungwinb+draw
main()
