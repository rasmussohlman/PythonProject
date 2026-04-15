import random

nimet = set()

while True:
    nimi = input("Syötä nimi (tai tyhjä lopettaaksesi): ")

    if nimi == "":
        break

    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

print("\nSyötetyt nimet satunnaisessa järjestyksessä:")
satunnainen = list(nimet)
random.shuffle(satunnainen)
for nimi in satunnainen:
    print(nimi)