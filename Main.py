import janken

def menu():
    while True:
        print("--BENVINGUT AL MINI ARCADE--")
        print("Jugar a Pedra, Paper, Tisora")
        print("Jugar a Endivinar el Número")
        print("S: Sortir")

        eleccio = int(input("Tria una opcio"))
        match eleccio:
            case 1:
                janken()
            case 2:

            case 3:
                print("Sortint")
                break
            case _:
                print("Opcio no valida")
                continue
menu()

