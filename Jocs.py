import random 
def triar_mode():
    print("Benvingut a Janken!")
    print("Tria el mode de joc:")
    print("1 - Primer que arribe a 3 victòries")
    print("2 - Millor de 5 rondes")

    mode = input("Opció: ")
    print("Mode seleccionat:", "Primer a 3" if mode == "1" else "Millor de 5")

def print_marcador(marcador):
    marcador = {"Jugador": 0, "Màquina": 0}
    print("------------------")
    print("  Marcador  ")
    print("------------------")
    print("  Jugador:", marcador["Jugador"])
    print("  Màquina:", marcador["Màquina"])
    print("------------------")   
def janken():
    opcions = ["paper", "tisora", "pedra"]
    while marcador["Jugador"] < 3 and marcador["Màquina"] < 3: 
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
    triar_mode()
    
    if mode == '1' and marcador["Jugador"] == 3:
        print("Has guanyat la partida!")
    elif mode == '1' and marcador["Màquina"] == 3:
        print("La màquina ha guanyat la partida!")
        print("Fi del joc!")
    elif mode == '2' and marcador["Jugador"] > marcador["Màquina"]:
        print("Has guanyat la partida!")
    elif mode == '2' and marcador["Jugador"] < marcador["Màquina"]:
        print("La màquina ha guanyat la partida!")
janken()

def nana():
    numero_secret = random.randint(1, 100)
    intents = 0
    while True:
        intent = input("Introdueix un número 1-100 (o 's' per sortir): ").strip()
        if intent == 's':
            print("Sortint del joc.")
            return
        if not intent.isdigit():
            print("Introdueix un número vàlid.")
            continue
        intent = int(intent)
        intents += 1
        if intent < numero_secret:
            print("És més alt!")
        elif intent > numero_secret:
            print("És més baix!")
        else:
            print(f"Has endevinat el número {numero_secret} en {intents} intents.")
            return