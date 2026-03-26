numero = int(input("Anna numero väliltä 1-10:"))
if numero < 1 or numero > 10:
    print("Luvun täytyy olla väliltä 1-10")
else:
    print(f"Kertotaulu luvulle {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {i*numero}")


