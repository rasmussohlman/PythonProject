import random

maara = int(input("Kuinka montaa arpakuutiota heitetään?"))

summa = 0

for i in range(maara):
    heitto = random.randint(1,6)
    summa += heitto

print("Silmälukujen summa on: " , summa)


    