def kuusi(koko):
    print("Tämä on kuusi!")

    # Kuusen latvus (kaikki rivit paitsi viimeinen leveä)
    for i in range(koko - 1):
        tahdet = 2 * i + 1
        valit = (koko - 1) - i
        print(" " * valit + "*" * tahdet)

    # Viimeinen leveä rivi (sama leveys kuin edellisellä)
    viimeiset_tahdet = 2 * (koko - 2) + 1
    print("*" * viimeiset_tahdet)

    # Runko
    print(" " * (koko - 1) + "*")


# Testikutsu
kuusi(5)