sanat = ["kanariisi", "talo", "pöytä", "kissa", "aurinko", "rantaloma"]

laskuri = 0

for sana in sanat:
    if len(sana) > 5:
        laskuri += 1

print(f"Listassa on {laskuri} sanaa, joissa on yli 5 kirjainta.")