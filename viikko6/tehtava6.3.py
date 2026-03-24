def gallonat_litroiksi (gallonat):
    return gallonat * 3.785

def main():
    while True:
        try:
            gallonat = float(input("Anna bensiinin määrä (gallonoina, negatiivinen lopettaa):"))
        except ValueError:
            print("Syötä numero")
            continue

        if gallonat < 0:
            print("Ohjelma päättyy.")
            break

        litrat = gallonat_litroiksi(gallonat)
        print(f"{gallonat} galloonaa =  {litrat:.2f} litraa")
main()


