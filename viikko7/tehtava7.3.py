lentoasemat = {}

while True:
    print("\n1. Syötä uusi lentoasema")
    print("2. Hae lentoaseman tiedot")
    print("3. Lopeta")

    valinta = input("Valitse toiminto (1-3): ")

    if valinta == "1":
        icao = input("Syötä ICAO-koodi: ").upper()
        nimi = input("Syötä lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print(f"Lentoasema {nimi} ({icao}) tallennettu.")

    elif valinta == "2":
        icao = input("Syötä ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(f"Lentoasema: {lentoasemat[icao]}")
        else:
            print("Lentoasemaa ei löydy.")

    elif valinta == "3":
        print("Ohjelma päättyy.")
        break

    else:
        print("Virheellinen valinta, yritä uudelleen.")