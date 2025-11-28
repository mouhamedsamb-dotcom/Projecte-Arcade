import janken, nana
# Arcade amb dos jocs: Pedra, Paper, Tisora i Endivinar el Número
def menu():
    while True:
        print("--BENVINGUT AL MINI ARCADE--")
        print("1, Jugar a Pedra, Paper, Tisora")
        print("2, Jugar a Endivinar el Número")
        print("S: Sortir")
#Demanem una elecció a l'usuari i cridem a la funció corresponent
        eleccio = input("Tria una opcio")
        match eleccio:
            case "1":
                janken()
            case "2":
                nana()
            case "S" | "s":
                print("Sortint")
                return
            case _:
                print("Opció no vàlida")
                return
menu()

