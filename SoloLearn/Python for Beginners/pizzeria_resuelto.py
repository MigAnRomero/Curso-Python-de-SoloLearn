## Creaste tu propia pizzería y decidiste realizar tu propio menú interactivo para evitar 
# entregar físicamente cartillas con el menú como se hacía antes de la pandemia.
#  el menú debe mostrar 3 tipos de opciones de comida diferentes: Pizza, Panzerotti y Pasta. 
# Cada opción debe tener a su vez 3 posibles opciones (sabores) que el cliente debe porder elegir. 
# Cada vez que el cliente termine de elegir una opción debe mostrarse nuevamente el menú principal 
# con las opciones de los 3 tipos de comida, para cerrar el menú debe existir una cuarta opción que
#  se llame SALIR.

menu = input("¿Deseas ver el menú?\nSi\nNo\n")
menu = menu.upper()
acu_pizza = ""
acu_panzerotti = ""
acu_pasta = ""

while(menu == "SI"):
    print("-------------------------------------")
    seleccion = input("Pizza\nPanzerotti\nPasta\n")
    seleccion = seleccion.upper()
    print("-------------------------------------")
    if(seleccion == "PIZZA"):
        porciones_pizza = int(eval(input("1. Pizzeta\n2. 15 Porciones\n3. 30 Porciones\n")))
        print("-------------------------------------")
        sabor_pizza = input("Carnes\nHawaiana\nChunchullo\nBofe\nCriolla\n")
        print("-------------------------------------")
        if(porciones_pizza == 1):
            acu_pizza = acu_pizza + "Pizzeta de " + sabor_pizza + "\n"
        elif(porciones_pizza == 2):
            acu_pizza = acu_pizza + "15 porciones de " + sabor_pizza + "\n"
        elif(porciones_pizza == 3):
            acu_pizza += "30 porciones de " + sabor_pizza + "\n"
        else:
            print("Tamaño de pizza no existente")
            print("-------------------------------------")
    elif(seleccion == "PANZEROTTI"):
        cant_panzerotti = int(eval(input("¿Cuántos panzerottis deseas ordenar? ")))
        cont_panzerotti = 0
        print("-------------------------------------")
        while(cont_panzerotti < cant_panzerotti):
            sabor_panzerotti = input("Carnes\nHawaiano\nChunchullo\nBofe\nCriollo\n")
            print("-------------------------------------")
            acu_panzerotti += "Panzerotti " + sabor_panzerotti + "\n"
            cont_panzerotti += 1
    
    elif(seleccion == "PASTA"):
        sabor_pasta = input("Carbonara con bofe\nBolognesa con chunchullo\nNapolitana\nPuttanesca\n")
        acu_pasta = acu_pasta + "Pasta " + sabor_pasta + "\n"  


    print("-------------------------------------")
    error = input("¿Cometiste algún error en tu pedido?\nSi\nNo\n")
    error = error.upper()
    if(error == "SI"):
        acu_pizza = ""
        acu_panzerotti = ""
        acu_pasta = ""      
    print("-------------------------------------")
    menu = input("¿Deseas seguir ordenando comida?\nSi\nNo\n")
    menu = menu.upper()

print(f"\n-------------------------------------\n{acu_pizza}\n{acu_panzerotti}\n{acu_pasta}")