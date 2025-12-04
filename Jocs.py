#Importem el fitxer robot.py per a utilitzar la funció robot()
import robot
import random
#Cream la funció triar_mode per a seleccionar el mode de joc
def triar_mode():
    print("Benvingut a Janken!")
    print("Tria el mode de joc:")
    print("1 - Primer que arribe a 3 victòries")
    print("2 - Millor de 5 rondes")
#Ara utilitzarem un condicional per a que l'usuari puga triar el mode de joc i el que ensenyarem en pantalla.
    mode = input("Opció: ")
    print("Mode seleccionat:", "Primer que arribe a 3" if mode == "1" else "Al millor de 5")
    return mode

#Crearem una altra funcio per a ensenyar el marcador
def print_marcador(marcador):
    print("------------------")
    print("  Marcador  ")
    print("------------------")
    print("  Jugador:", marcador["Jugador"])
    print("  Màquina:", marcador["Màquina"])
    print("------------------")   

#Ara anem a crear la funcio principal on esta el joc.
def janken():
    opcions = ["paper", "tisora", "pedra"]
    marcador = {"Jugador": 0, "Màquina": 0}

    mode = triar_mode()
# Aqui posarem el nombre de rondes per al mode 5 i per al mode 3 victòries que seran 100000 per a que no afecte al joc.
    rondes = 5 if mode == "2" else 100000 

    ronda_actual = 0
#Ara fem un bucle while per a que el joc continue fins que un dels jugadors guanye.
    while True:
        #L'opcio 1 es al millor de 3 acaba quan un dels jugaors arriba al marcador de 3  
        if mode == "1" and (marcador["Jugador"] == 3 or marcador["Màquina"] == 3):
            break
        #L'opcio 2 es al millor de 5 acaba quan s'arriba al nombre de rondes.
        if mode == "2" and ronda_actual == rondes:
            break

        print("Opcions: paper, tisora, pedra")
        opcio = input("Tria una opcio (o 's' per sortir): ")

        if opcio == 's':
            print("Sortint del joc.")
            return

        if opcio not in opcions:
            print("Opció no vàlida.")
            continue
#Ara cridem a la funcio robot per a que trieu la opcio de la maquina
        maquina = random.choice(opcions)
        print("La màquina tria:", maquina)
#Ara fem les condicions per a veure qui guanya cada ronda
        if opcio == maquina:
            print("Empat!")
        elif (opcio == "paper" and maquina == "pedra") or \
             (opcio == "tisora" and maquina == "paper") or \
             (opcio == "pedra" and maquina == "tisora"):
            print("Has guanyat aquesta ronda!")
# Actualitzem el marcador
            marcador["Jugador"] += 1
        else:
            print("Has perdut aquesta ronda!")
            marcador["Màquina"] += 1
#Incrementem la ronda actual i mostrem el marcador
        ronda_actual += 1
        print_marcador(marcador)
# Despres de que acabe el joc mostrem el resultat final
    if marcador["Jugador"] > marcador["Màquina"]:
        print("Has guanyat la partida!")
    elif marcador["Jugador"] < marcador["Màquina"]:
        print("La màquina ha guanyat la partida!")
    else:
        print("Empat final!")
janken()
#Ara crearem una altra funcio per al joc de endevinar el numero
def nana():
# Importem el fitxer robot.py per a utilitzar la funció robot()
    import robot
    numero_secret = random.randint(1, 100)
    intents = 0
    while True:
    # Fem que l'usuari introduisca un número
        intent = input("Introdueix un número 1-100 (o 's' per sortir): ").strip()
        if intent == 's':
            print("Sortint del joc.")
            return
     
        if not intent.isdigit():
            print("Introdueix un número vàlid.")
            continue
# Convertim l'entrada a enter i sumem els intents
        intent = int(intent)
        intents += 1
#Donem pistes a l'usuari utilitzant condicions.
        if intent < 1 or intent > 100:
            print("El número ha de ser entre 1 i 100.")
            continue
        if intent < numero_secret:
            print("Es més baix")
        elif intent > numero_secret:
            print("És més alt!")
        else:
            print(f"Has endevinat el número {numero_secret} en {intents} intents.")
            return
        import random
nana()