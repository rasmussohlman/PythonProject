import math

while True:
    luku = int(input("Anna kokonaisluku"))

    if luku == 0:
        break

    if luku < 0:
        print("Virheellinen numero")
    else:
        print("Luvun neliöjuuri on", math.sqrt(luku))

