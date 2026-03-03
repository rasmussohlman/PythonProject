tuuma = int(input("Anna tuumat (negatiivinen lopettaa): "))

while tuuma >= 0:
    cm = tuuma * 2,54
    print(tuuma, "tuumaa =" , cm, "cm")
    tuuma = float(input("Anna tuumat (negatiivinen lopettaa): "))
print("Toiminta lopetettu.")
