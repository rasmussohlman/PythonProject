while True:
    print("Valitse toiminto:")
    print("1) Yhteenlasku")
    print("2) Vähennyslasku")
    print("3) Kertolasku")
    print("4) Jakolasku")
    print("0) Lopeta")

    valinta = input("Anna valinta: ")

    if valinta == "0":
        print("Lopetetaan ohjelma.")
        break

    if valinta in ["1", "2", "3", "4"]:
        luku1 = float(input("Anna ensimmäinen luku: "))
        luku2 = float(input("Anna toinen luku: "))

        if valinta == "1":
            print("Tulos:", luku1 + luku2)
        elif valinta == "2":
            print("Tulos:", luku1 - luku2)
        elif valinta == "3":
            print("Tulos:", luku1 * luku2)
        elif valinta == "4":
            if luku2 == 0:
                print("Nollalla ei voi jakaa.")
            else:
                print("Tulos:", luku1 / luku2)
    else:
        print("Virheellinen valinta.")

    print()