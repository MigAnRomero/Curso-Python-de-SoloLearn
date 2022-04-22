# Para generar el rango como una lista, debemos convertirlo explícitamente 
# en una lista, usando la función list().
numbers = list(range(10))
print(numbers) 

# Otro ejemplo:
print("||---Segundo Ejemplo---||")
nums = list(range(5))
print(nums)
print(nums[4])

# Si se llama a range con un argumento, producirá un objeto con valores desde 0 
# hasta ese argumento. 
# Si se llama con dos argumentos, producirá valores del primero al segundo. 
# Por ejemplo:
print("||---Range con dos armumentos---||")
numbers = list(range(3, 8))
print(numbers) 

# También hay un tercer argumento que puedes usar con range() , y es realmente útil. 
# Se llama Paso y determina el intervalo de la secuencia producida. Echar un vistazo:
print("||---Range con tres armumentos---||\nEl tercer argumento determina el intervalo de la secuencia.")
numbers = list(range(5, 20, 2))
print(numbers)

print("||---Segundo Ejemplo con Range de tres argumentos---||")
nums = list(range(3, 15, 3))
print(nums)
print(nums[2])

# ¿Quieres ir hacia atrás? ¡No hay problema! También podemos crear una lista de 
# números decrecientes, usando un número negativo como tercer argumento. 
# Por ejemplo:
print("||---Retroceso en la lista con el tercer argumento---||")
x = list(range(7, 3, -1))
print(x)

print("||---||")
numbers = list(range(5, 10, 2))
print(numbers)