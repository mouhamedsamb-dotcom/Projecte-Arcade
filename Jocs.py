from Robot import random

opcions = ["paper", "tisora", "pedra"]

def janken():
    print("Paper")
    print("Tisora")
    print("Pedra")

    opcio = input("Tria una opcio: ").lower()
    maquina = random.choice(opcions)

    print("La màquina tria:", maquina)

    if opcio == maquina:
        print("Empat!")
    elif (opcio == "paper" and maquina == "pedra") or \
         (opcio == "tisora" and maquina == "paper") or \
         (opcio == "pedra" and maquina == "tisora"):
        print("Has guanyat!")
    else:
        print("Has perdut!")

janken()