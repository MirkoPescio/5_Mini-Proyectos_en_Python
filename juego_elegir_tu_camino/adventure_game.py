print("Juego de elegir el camino")

name = input("Escriba su nombre: ")
print("Bienvenido " + name + " a esta aventura!!")

answer = input("Estás en una bifurcación. Tenés que elegir (izquierda/derecha): ")
answer.lower()

if (answer == "izquierda"):
    answer = input("Entraste a un río. Podés rodearlo o nadar. ¿Qué opción elegís? (rodear/nadar): ")
    answer.lower()

    if (answer == "rodear"):
        print("Caminaste muchos kilómetros y te deshidrataste")
    elif(answer == "nadar"):
        print("Elegiste nadar y fuiste comido por un caimán")
    else:
        print("No elegiste una opción válida. Perdiste")

elif (answer == "derecha"):
    answer = input("LLegaste a un puente. Se ve inestable. ¿Qué opción elegís? (cruzar/volver): ")
    answer.lower()

    if (answer == "cruzar"):
        print("Lograste cruzar y te encontraste con un sujeto")
        answer = input("¿Vas a hablar? (si/no): ").lower()
        if (answer == "si"):
            print("Al hablar con el sujeto te regaló ORO. Ganaste!!")
        elif (answer == "no"):
            print("El sujeto se ofendió y te robó la cantimplora. Perdiste")
        else:
            print("No elegiste una opción válida. Perdiste")
    elif (answer == "volver"):
        print("Volviste al principio del camino. Perdiste")
    else:
        print("No elegiste una opción válida. Perdiste")

else:
    print("No elegiste una opción válida. Perdiste")

print("Gracias por probar esta demo", name)
