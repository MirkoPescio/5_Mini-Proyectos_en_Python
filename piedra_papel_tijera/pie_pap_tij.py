import random

user_wins = 0
computer_wins = 0
lista_de_opciones = ["piedra", "papel", "tijera"]

while True:
    user_input = input("Elija [piedra, papel o tijera] o q para salir: ")
    user_input.lower()
    if (user_input == "q"):
        break

    if (user_input not in lista_de_opciones):
        continue
    
    random_number = random.randint(0, 2)
    # piedra: 0; papel: 1, tijera: 2
    PC_input = lista_de_opciones[random_number]

    # Procediendo a las condiciones de puntaje:
    if (user_input == "piedra" and PC_input == "tijera"):
        print("Ganaste!")
        print("La PC eligió: ", PC_input)
        user_wins += 1
        continue
    elif (user_input == "papel" and PC_input == "piedra"):
        print("Ganaste!")
        print("La PC eligió: ", PC_input)
        user_wins += 1
        continue
    elif (user_input == "tijera" and PC_input == "papel"):
        print("Ganaste!")
        print("La PC eligió: ", PC_input)
        user_wins += 1
        continue
    else:
        print("Perdiste")
        print("La PC eligió: ", PC_input)
        computer_wins += 1
        continue

print("El juego terminó con un puntaje de " + str(user_wins) + " puntos para el jugador y " + str(computer_wins) + " puntos para la PC")

