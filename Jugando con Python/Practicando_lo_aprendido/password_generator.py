import random


def password_generator():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracteres = mayusculas + minusculas + simbolos + numeros
    
    contrasena = []
    
    for i in range(15):  # Se debe generar un password de 15 caracteres
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
        
    contrasena = ''.join(contrasena)  # los caracteres se pegan juntos para dar con un solo string
    return contrasena


def run():
    password = password_generator()
    print(f"Tu nueva contraseña es {password}")


if __name__ == "__main__":
    run()