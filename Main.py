from jocs import janken 


def menu():
    print("--BENVINGUT AL MINI ARCADE--")
    print("Jugar a Pedra, Paper, Tisora")
    print("Jugar a Endivinar el Número")
    print("S: Sortir")
while True:
    eleccio = int(input("Tria una opcio"))
    match eleccio:
        case 