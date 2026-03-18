luvut = []

while True:
    syote = input("Anna luku(tyhjä lopettaa): ")
    if syote == "":
        break
    try:
        luku = float(syote)
        luvut.append(luku)
    except ValueError:
        print("Syötä vain numeroita.")

luvut.sort(reverse=True)

print("Viisi suurinta lukua:")
for luku in luvut[:5]:
    print(luku)