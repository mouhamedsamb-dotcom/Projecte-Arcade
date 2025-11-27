import random 
marcador = {"Jugador": 0, "Màquina": 0}
def print_marcador(marcador):
    print("------------------")
    print("  Marcador  ")
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
numero_secret = random.randint(1, 100)
intents = 0
def nana():
    while True:
        print("Endevina el número entre 1 i 100.")
        if not intent.isdigit():
            print("Si us plau, introdueix un número vàlid.")
            continue
        intent = int(intent)
        intents += 1
        if intent < 1 or intent > 100:
            print("El número ha d'estar entre 1 i 100.")
            continue
        if intent < numero_secret:
            print("Es mes alt!")
        elif intent > numero_secret:
            print("Es mes baix!")
        else:
            print(f"Has endevinat el número {numero_secret} en {intents} intents.")
            break

