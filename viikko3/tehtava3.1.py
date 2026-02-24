pituus = int(input("Anna kuhan pituus (cm): "))
alamitta = 37
if pituus < alamitta:
    puuttuu = alamitta - pituus
    print(f"Kuha on alamittainen. Laske se takaisin järveen! Se on {puuttuu} cm vajaa.")
else: print("Kuha on oikean mittainen.")
