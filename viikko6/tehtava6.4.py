def laske_summa(numerot):
    return sum(numerot)

def main():
    luvut = [3, 7, 12, -4, 9]
    summa = laske_summa(luvut)
    print(f"Listan {luvut} summa on {summa}")

main()