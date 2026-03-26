def suurin_arvo(a, b, c):
    return max(a, b, c)

luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))

tulos = suurin_arvo(luku1, luku2, luku3)
print(f"Suurin arvo on: {tulos}")