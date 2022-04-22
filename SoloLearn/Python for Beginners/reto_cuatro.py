# Reto 4
# Crea una función para crear listas aleatorias con el IMC de personas
# Crea una función que clasifique los IMC en Bajo peso, Peso Normal, Sobrepeso u obeso
# Muestra cuantas personas entran en cada categoría según su IMC
# Crea otra función que genere grupos de personas para acondicionamiento físico:
# Los grupos de bajo peso están conformados por 10 personas
# Los grupos de peso normal están conformados por 30 personas
# Los grupos de sobrepeso están conformados por 15 personas 
# Los grupos de obeso están conformados por 5 personas
def lista_aleatoria(n1,n2,longitud):
    import random
    from random import randint
    lista_vacia = []
    for element in range(longitud):
        lista_vacia.append(random.randint(n1,n2))
    return lista_vacia
lista_imc = lista_aleatoria(15,35,100)
def grupos(cant_bp,cant_n,cant_sp,cant_o):
    grupos_bp = int(cant_bp/10)
    grupos_n = int(cant_n/30)
    grupos_sp = int(cant_sp/15)
    grupos_o = int(cant_o/5)
    resultado = (f"Personas con Bajo Peso: {cant_bp}, Grupos de personas con Bajo Peso: {grupos_bp}\n"
                 +f"Personas con Peso Normal: {cant_n}, Grupos de personas con Peso Normal: {grupos_n}\n"
                 +f"Personas con Sobrepeso: {cant_sp}, Grupos de personas con Sobrepeso: {grupos_sp}\n"
                 +f"Personas con Obesidad: {cant_o}, Grupos de personas con Obesidad: {grupos_o}")
    return resultado

def clas_imc(lista):
    bajo_peso = 0
    normal = 0
    sobrepeso = 0
    obeso = 0
    for imc in lista:
        if(imc < 18.5):
            bajo_peso += 1
        elif(imc >= 18.5 and imc < 25):
            normal += 1
        elif(imc >= 25 and imc < 30):
            sobrepeso += 1
        else:
            obeso += 1
    resultados_totales = grupos(bajo_peso,normal,sobrepeso,obeso)
    return resultados_totales
print(clas_imc(lista_imc))