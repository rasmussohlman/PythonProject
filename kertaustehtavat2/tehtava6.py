def summa(a, b):
    return a + b

def erotus(a, b):
    return a - b

def tulo(a, b):
    return a * b

def osamaara(a, b):
    if b == 0:
        return "Virhe: nollalla ei voi jakaa!"
    return a / b


print("Valitse laskutoimitus:")
print("1) Summa")
print("2) Erotus")
print("3) Tulo")
print("4) Osamäärä")

valinta = input("Anna valinta (1-4): ")

luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))

if valinta == "1":
    print("Tulos:", summa(luku1, luku2))
elif valinta == "2":
    print("Tulos:", erotus(luku1, luku2))
elif valinta == "3":
    print("Tulos:", tulo(luku1, luku2))
elif valinta == "4":
    print("Tulos:", osamaara(luku1, luku2))
else:
    print("Virheellinen valinta.")