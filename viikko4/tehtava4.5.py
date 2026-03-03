oikea_kaytt = "python"
oikea_sala = "rules"

yritykset = 0

while yritykset < 5:
    user = input("Käyttäjätunnus:")
    salasana = input("Salasana:")

    if user == oikea_kaytt and salasana == oikea_sala:
        print("Tervetuloa")
        break
    else:
        print("Väärä tunnus tai salasana.")
        yritykset += 1
if yritykset == 5:
    print("Pääsy evätty")


