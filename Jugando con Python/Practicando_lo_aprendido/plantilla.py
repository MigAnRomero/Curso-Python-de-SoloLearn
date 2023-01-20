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
print("Lista tres objetos del equipamiento: Nombre y valor", "\nBotella:", botella, "\nAgua:", agua, "\nSnacks:", snacks)

print("¿Puedes combinar elementos de tu equipo para prepararte mejor?")

agua_en_botella = agua + botella
linterna_funcional = linterna + bateria
mi_ubicacion = mapa + brujula

print(f"Agua en botella: {agua_en_botella}", f"\nLinterna funcional: {linterna_funcional}", f"\nMi ubicación: {mi_ubicacion}")

print("¿El precio del agua en botella es menor al de la linterna funcional?")
print(f"¿El precio del agua en botella < al de la linterna funcional?: {agua_en_botella < linterna_funcional}")

print("¿Cuanto valdría comprar unos snacks y una brujula?")
print(f"Precio de una snack más una brújula: {snacks + brujula}")

print("¿Si tienes 100 puntos, te alcanza para comprar unas botas?")
print(f"Respuesta: {botas <= 100} porque las botas tienen {botas} puntos.")

#Clase 2 Proyecto: Tomando decisiones

#Reto 3 - Pon tu respuesta después del print
print("La esfinge te dice: No debes colocar más de 5 objetos en tu mochila, y tampoco pasarte de 200 trekjuls: ¿Cuales elementos colocarías?")

mochila = 0

# No se elige el mapa si uno puede orientarse con una brújula

if ((agua_en_botella + linterna_funcional + brujula + reloj + snacks) <= 200):
    mochila = agua_en_botella + linterna_funcional + brujula + reloj + snacks
    print("El valor de los elementos es menor a 200: ", mochila)

elif ((agua_en_botella + linterna_funcional + brujula + reloj) <= 200):
    mochila = agua_en_botella + linterna_funcional + brujula + reloj
    print("El valor de los elementos es menor a 200", mochila)

elif ((agua_en_botella + linterna_funcional + brujula) <= 200):
    mochila = agua_en_botella + linterna_funcional + brujula
    print("El valor de los elementos es menor a 200. Total compra: ", mochila)

else:
    print("Ups! Ninguna de tus intentos fue exitoso")

#Reto 4 - Pon tu respuesta después del print
print ("Es tu dia de suerte! Te voy a dar otra mochila, pero solo puedes agregarle agua en botella")






#Clase 3 Proyecto: Almacenando equipamimento

#Reto 4 - Pon tu respuesta después del segundo print
print("Le hice una actualización a tu mochila te dice la esfinge, porque solo podias conocer el valor de los objetos que tenias")
print("Ahora sabras el objeto que tienes, la cantidad y su valor unitario, pero tu debes volverla a llenarla")









#Reto 5 - Pon tu respuesta después del print
print("Ahora, en esta aventura te van a acompañar 8 integrantes más, y te voy a pedir que les armes una mochila igual a la tuya y la coloques en el compartimiento de tu vehiculo")











#Clase 4 Proyecto: Organizandonos un poco

#Reto 6 - Pon tu respuesta después del segundo print
print("Te pido que para cuatro integrantes recolectes 3 elementos sin importar las cantidades que quieras adicionarles, y te da las siguientes opciones: brujula, linterna_funcional, snacks y agua_en_botella")
print("Pero necesito que calcules el total de elementos que hay en tu equipo")

