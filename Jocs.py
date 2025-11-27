import random 
marcador = {"Jugador": 0, "Màquina": 0}
def print_marcador(marcador):
    print("------------------")
    print("  Marcador Jenken ")
    print("------------------")
    print("  Jugador:", marcador["Jugador"])
    print("  Màquina:", marcador["Màquina"])
    print("------------------")   
def janken():
    opcions = ["paper", "tisora", "pedra"]
    while marcador["Jugador"] < 2 and marcador["Màquina"] < 2: 
        print("Opcions: paper, tisora, pedra")
        opcio = input("Tria una opcio (o 's' per sortir): ")
        if opcio == 's':
            print("Sortint del joc.")
            break
        if opcio not in opcions:
            print("Opció no vàlida.")
            break

        maquina = random.choice(opcions)
        print("La màquina tria:", maquina)

        if opcio == maquina:
            print("Empat!")
        elif (opcio == "paper" and maquina == "pedra") or \
            (opcio == "tisora" and maquina == "paper") or \
            (opcio == "pedra" and maquina == "tisora"):
            print("Has guanyat aquesta ronda!")
            marcador["Jugador"] += 1
        else:
            print("Has perdut aquesta ronda!")
            marcador["Màquina"] += 1 
        print_marcador(marcador)
    
    if marcador["Jugador"] == 2:
        print("Has guanyat la partida!")
    elif marcador["Màquina"] == 2:
        print("La màquina ha guanyat la partida!")
janken()
def nana():