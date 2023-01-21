#Las preguntas que te irá haciendo la esfinge corresponden a los print de esta plantilla
#Por favor completa cada reto

#Clase 1 Proyecto: Definidendo la aventura

#Reto 1 - Pon tu respuesta después del print
print("Define el equipamiento para una aventura de trekking y su valor en trekjuls (moneda del juego):")

mapa = 70.67
botas = 120.23
bateria = 11.69
linterna = 28
agua = 73
botella = 20.5
snacks = 8.8
brujula = 60.99
reloj = 83.75
lentes_sol = 53.28

#Reto 2 - Pon tu respuesta después de cada print
print("\nLista tres objetos del equipamiento: Nombre y valor", "\nBotella:", botella, "\nAgua:", agua, "\nSnacks:", snacks)

print("¿Puedes combinar elementos de tu equipo para prepararte mejor?")

agua_en_botella = agua + botella
linterna_funcional = linterna + bateria
mi_ubicacion = mapa + brujula

print(f"\nAgua en botella: {agua_en_botella}", f"\nLinterna funcional: {linterna_funcional}", f"\nMi ubicación: {mi_ubicacion}")

print("\n¿El precio del agua en botella es menor al de la linterna funcional?")
print(f"¿El precio del agua en botella < al de la linterna funcional?: {agua_en_botella < linterna_funcional}")

print("\n¿Cuanto valdría comprar unos snacks y una brujula?")
print(f"Precio de una snack más una brújula: {snacks + brujula}")

print("\n¿Si tienes 100 puntos, te alcanza para comprar unas botas?")
print(f"Respuesta: {botas <= 100} porque las botas tienen {botas} puntos.")

#Clase 2 Proyecto: Tomando decisiones

#Reto 3 - Pon tu respuesta después del print
print("\nLa esfinge te dice: No debes colocar más de 5 objetos en tu mochila, y tampoco pasarte de 200 trekjuls: ¿Cuales elementos colocarías?")

mochila = 0

# No se elige el mapa si uno puede orientarse con una brújula
opcion_uno = agua_en_botella + linterna_funcional + brujula + reloj + snacks
opcion_dos = agua_en_botella + linterna_funcional + brujula + reloj
opcion_tres = agua_en_botella + linterna_funcional + brujula

if (opcion_uno <= 200):
    mochila = opcion_uno
    print("El valor de los elementos es menor a 200: ", mochila)

elif (opcion_dos <= 200):
    mochila = opcion_dos
    print("El valor de los elementos es menor a 200", mochila)

elif (opcion_tres <= 200):
    mochila = opcion_tres
    print("El valor de los elementos es menor a 200. Total compra: ", mochila)

else:
    print("Ups! Ninguna de tus intentos fue exitoso")

print("Valores de la opciones elegidas", f"\nOpción uno: {opcion_uno}", f"\nOpción dos: {opcion_dos}", f"\nOpción tres: {opcion_tres}")

#Reto 4 - Pon tu respuesta después del print
print ("\nEs tu dia de suerte! Te voy a dar otra mochila, pero solo puedes agregarle agua en botella")
mochila_dos = 0

while (mochila_dos <= 200):
    mochila_dos += agua_en_botella
    print(f"Mochila dos: {mochila_dos}")

mochila_dos -= agua_en_botella
print(f"Nos pasamos, vamos a restar una botella de agua, ahora tenemos: {mochila_dos}")

#Clase 3 Proyecto: Almacenando equipamimento

#Reto 4 - Pon tu respuesta después del segundo print
print("\nLe hice una actualización a tu mochila te dice la esfinge, porque solo podias conocer el valor de los objetos que tenias")
print("Ahora sabras el objeto que tienes, la cantidad y su valor unitario, pero tu debes volverla a llenarla")

mochila_actualizada = {
    "agua_en_botella" : {"cantidad": 1, "valor_unitario": agua_en_botella},
    "linterna_funcional" : {"cantidad": 1, "valor_unitario": linterna_funcional},
    "brujula" : {"cantidad": 1, "valor_unitario": brujula}
}

print("\nMostrar mochila_actualizada: ", mochila_actualizada)

mochila_dos_actualizada = {
    "agua_en_botella" : {"cantidad": 2, "valor_unitario": agua_en_botella}
}

print("\nMostrar mochila_dos_actualizada: ", mochila_dos_actualizada)

#Reto 5 - Pon tu respuesta después del print
print("\nAhora, en esta aventura te van a acompañar 8 integrantes más, y te voy a pedir que les armes una mochila igual a la tuya y la coloques en el compartimiento de tu vehiculo")

vehiculo = [{}] * 7

for compartimiento in range(7):
    vehiculo[compartimiento] = {
        "agua_en_botella" : {"cantidad": 1, "valor_unitario": agua_en_botella},
        "linterna_funcional" : {"cantidad": 1, "valor_unitario": linterna_funcional},
        "brujula" : {"cantidad": 1, "valor_unitario": brujula}
    }
    print("Acabas de armar la mochila para el compartimiento: ", compartimiento + 1)

print("")

numero_compartimiento = 0

for mochila in vehiculo:
    numero_compartimiento += 1
    print(f"Numero de compartimiento {numero_compartimiento} para la mochila: ", mochila, "\n")


#Clase 4 Proyecto: Organizandonos un poco

#Reto 6 - Pon tu respuesta después del segundo print
print("\nTe pido que para cuatro integrantes recolectes 3 elementos sin importar las cantidades que quieras adicionarles, y te da las siguientes opciones: brujula, linterna_funcional, snacks y agua_en_botella")
print("Pero necesito que calcules el total de elementos que hay en tu equipo")

def agregar_elementos_a_mochilas():  # La función que llama a las otras cuando se usa
    for compartimiento in range(3):
        vehiculo[compartimiento] = {
            "agua_en_botella" : {"cantidad": 1, "valor_unitario": agua_en_botella},
            "linterna_funcional" : {"cantidad": 2, "valor_unitario": linterna_funcional},
            "brujula" : {"cantidad": 3, "valor_unitario": brujula},
            "snacks" : {"cantidad": 2, "valor_unitario": snacks},
        }
    imprimir(vehiculo)
    calcular_total_elementos_en_mochilas(vehiculo)

def calcular_total_elementos_en_mochilas(vehiculo):
    total_elementos_mochilas = {}
    
    print("Calculo elementos en mochila")
    for mochila in vehiculo: 
        for elemento, detalle in mochila.items(): 
            if elemento in total_elementos_mochilas:
                total_elementos_mochilas[elemento] += detalle["cantidad"]
            else:
                total_elementos_mochilas[elemento] = detalle["cantidad"]

    print(total_elementos_mochilas)

def imprimir(estructura):
    for objeto in estructura:
        print(objeto, "\n")

agregar_elementos_a_mochilas()