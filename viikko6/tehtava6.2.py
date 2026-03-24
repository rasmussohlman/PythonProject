import random

def heita_noppaa():
    return random.randint(1,6)

def main():
    while True:
        silmaluku = heita_noppaa()
        print("Heitto:", silmaluku)
        if silmaluku == 6:
            break

main()

import random

def heita_noppaa(tahkot):
    return random.randint(1,tahkot)
def main():
    tahkot = int(input("Anna nopan tahkojen määrä:"))
    print(f"Heitetään {tahkot}-tahkoista noppaa kunnes tulee {tahkot}.")

    while True:
        silmaluku = heita_noppaa(tahkot)
        print("Heitto:", silmaluku)
        if silmaluku == tahkot:
            break
main()
