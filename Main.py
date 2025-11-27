import janken, nana

def menu():
    while True:
        print("--BENVINGUT AL MINI ARCADE--")
        print("1, Jugar a Pedra, Paper, Tisora")
        print("2, Jugar a Endivinar el Número")
        print("S: Sortir")

        eleccio = input("Tria una opcio")
        match eleccio:
            case "1":
                janken()
            case "2":
                nana()
            case "S" | "s":
                print("Sortint")
                break
            
menu()

