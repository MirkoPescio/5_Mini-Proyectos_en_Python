print("Bienvenido a mi juego de preguntas!!")

playing = input("Vas a empezar a jugar? (Si/No): ")

if playing.capitalize() != "Si":
    quit() # Función útil para cortar la ejecución de un programa

print("Empieza el juego...")
puntaje = 0 # Es el contador. Por cada acierto se va a sumar en 1
preguntasTotales = 4


answer1 = input("¿Qué significa las siglas de CPU?: ")
if (answer1.lower() == "central processing unit"):
    puntaje += 1
    print("Correcto!!")
else:
    print("Incorrecto. Significa: central processing unit")

answer2 = input("¿Qué significa las siglas de GPU?: ")
if (answer2.lower() == "graphics processing unit"):
    puntaje += 1
    print("Correcto!!")
else:
    print("Incorrecto. Significa: graphics proccessing unit")

answer3 = input("¿Qué significa las siglas de RAM?: ")
if (answer3.lower() == "random access memory"):
    puntaje += 1
    print("Correcto!!")
else:
    print("Incorrecto. Significa: random access memory")

answer4 = input("¿Qué significa las siglas de PSU?: ")
if (answer4.lower() == "power supply"):
    puntaje += 1
    print("Correcto!!")
else:
    print("Incorrecto. Significa: power supply")


print("Acertaste " + str(puntaje) + " preguntas")
print("Tu porcentaje de respuestas correctas es del: " + str((puntaje / preguntasTotales) * 100) + " %")
