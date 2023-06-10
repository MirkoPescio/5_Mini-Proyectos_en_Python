import random

print("Bienvenido al juego: ADIVINAR EL NUMERO")
top_of_range = input("Ingrese el número tope: ")

intentos = input("Ingrese el número de intentos disponibles para el jugador: ")

if (intentos.isdigit()):
    intentos = int(intentos)

    if (intentos <= 0):
        print("Ingrese un número mayor a 0 la próxima vez")
        quit()
else:
    print("Ingrese un número la próxima vez")
    quit()

if (top_of_range.isdigit()):
    top_of_range = int(top_of_range)

    if (top_of_range <= 0):
        print("Ingrese un número mayor a 0 la próxima vez")
        quit()
else:
    print("Ingrese un número la próxima vez")
    quit()

random_number = random.randint(0, top_of_range)

while (intentos > 0):
    print("Ahora adivine el número...")
    print("Intentos disponibles: " + str(intentos))
    user_guess = input("Ingrese un número: ")

    if (user_guess.isdigit()):
        user_guess = int(user_guess)
    else:
        print("Ingrese un número la próxima vez")
        continue

    if (user_guess == random_number):
        print("¡ADIVINASTE!")
        break
    else:
        intentos -= 1
        print("No es el número")
        
if (intentos == 0):
    print("El número pensado por la PC era: " + str(random_number))

