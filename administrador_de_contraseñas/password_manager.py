# Módulo de Python para encriptar contraseñas
from cryptography.fernet import Fernet


"""
def write_key():
    key = Fernet.generate_key()
    with open("./administrador_de_contraseñas/key.key", 'wb') as key_file:
        key_file.write(key)

"""

def load_key():
    file = open("./administrador_de_contraseñas/key.key", 'rb')
    key = file.read()
    file.close()
    return key

master_pwd = input("¿Cuál es la contraseña principal?: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open("./administrador_de_contraseñas/contraseñas.txt", 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print("Usuario:", user, "| Contraseña:", fer.decrypt(passw.encode()).decode())

def add():
    username = input("Ingrese su nombre de usuario: ")
    pwd = input("Ingrese su contraseña: ")

    with open("./administrador_de_contraseñas/contraseñas.txt", 'a') as file:
        file.write(username + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("¿Quiere agregar una nueva contraseña o ver alguna de las existentes? (ver/agregar) (q para terminar la ejecución): ")
    if (mode.lower() == "q"):
        break
    elif (mode.lower() == "ver"):
        view()
    elif (mode.lower() == "agregar"):
        add()
    else:
        print("Comando no reconocido")




