import random

salainen = random.randint(1,10)
while True:
    syote = input("Arvaa luku (1-10): ")

    #Tarkistetaan, että syöte on kokonaisluku

    try:
        arvaus = int(syote)
    except ValueError:
        print("Anna kokonaisluku.")
        continue

    if arvaus < salainen:
        print("Liian pieni arvaus.")
    elif arvaus > salainen:
        print("Liian suuri arvaus.")
    else:
        print("Oikein")
        break