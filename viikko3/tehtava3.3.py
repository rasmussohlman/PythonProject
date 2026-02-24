sukupuoli = input("Anna biologinen sukupuolesi (mies/nainen):")
hb = int(input("Anna hemoglobiiniarvo (g/l):"))
if sukupuoli == "nainen":
    if hb < 117:
        print("Hemoglobiiniarvo alhainen.")
    elif hb <= 175:
        print("Hemoglobiiniarvo normaali.")
    else:
        print("Hemoglobiiniarvo korkea,")

elif sukupuoli == "mies":
    if hb < 134:
        print("Hemoglobiiniarvo alhainen.")
    elif hb <= 195:
        print("Hemoglobiiniarvo normaali.")
    else:
        print("Hemoglobiiniarvo korkea,")
