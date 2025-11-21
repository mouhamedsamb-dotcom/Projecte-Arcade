import random
resultat = marcador 
marcador = {"Jugador": resultat, "Màquina": 0}
def print_marcador(marcador):
    print("------------------")
    print("  Marcador Jenken ")
    print("------------------")
    jugadors = list
print("------------------")
print("  Jugador:", marcador["Jugador"])
print("  Màquina:", marcador["Màquina"])
print("------------------")
    
def janken():
    
    while True:
        opcions = ["paper", "tisora", "pedra"]
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
            print("Has guanyat!")
            marcador[Jugador] += 1
            print_marcador(marcador)
        else:
            print("Has perdut!")
            marcador 
            print_marcador(marcador)




janken()