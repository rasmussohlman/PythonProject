def poista_parittomat(numerot):
    return [luku for luku in numerot if luku % 2 == 0]

def main():
    alkuperainen = [3, 8, 11, 4, 7, 10, 13, 2, 21, 76, 85, 67, 22]
    karsittu = poista_parittomat(alkuperainen)

    print("Alkuperäinen lista:", alkuperainen)
    print("Parittomat poistettu:", karsittu)

main()