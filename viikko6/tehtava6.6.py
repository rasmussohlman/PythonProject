import math

def pizzan_yksikkohinta(halkaisija_cm, hinta_euro):
    # halkaisija → säde
    sade_m = (halkaisija_cm / 2) / 100
    pinta_ala = math.pi * (sade_m ** 2)
    return hinta_euro / pinta_ala

def main():
    print("Anna ensimmäisen pizzan tiedot:")
    d1 = float(input("Halkaisija (cm): "))
    h1 = float(input("Hinta (€): "))

    print("\nAnna toisen pizzan tiedot:")
    d2 = float(input("Halkaisija (cm): "))
    h2 = float(input("Hinta (€): "))

    y1 = pizzan_yksikkohinta(d1, h1)
    y2 = pizzan_yksikkohinta(d2, h2)

    print(f"\nPizzan 1 yksikköhinta: {y1:.2f} €/m²")
    print(f"Pizzan 2 yksikköhinta: {y2:.2f} €/m²")

    if y1 < y2:
        print("\nPizza 1 antaa paremman vastineen rahalle.")
    elif y2 < y1:
        print("\nPizza 2 antaa paremman vastineen rahalle.")
    else:
        print("\nPizzat ovat täsmälleen yhtä edullisia.")

main()