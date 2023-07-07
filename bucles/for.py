#sintax
"""for var in iterable:
    # statements"""
#---------------ITERABLES--------------------------------------
for x in "hola":
  print(x) 
print("---------------------------")

#con listas 
nums = [4, 78, 9, 84]
for n in nums:
    print(n)

print("---------------------------") 
language = 'Python'
for letter in language:
    print(letter)
print("---------------------------")




#----------------------- range()----------------------------
#Para recorrer un conjunto de código un número específico de veces

""" El rango (inicio, fin, paso) toma tres parámetros: 
        1. Inicio, fin e incremento. (De forma predeterminada, comienza desde 0 y el incremento es 1)
        2. La secuencia de rango necesita al menos 1 argumento (fin). range(max)
        3. Devuelve un iterable cuyos valores van desde 0 hasta max - 1
"""



print("---------------------------")

for numb in range(1,11):
    print(numb)
    
print("---------------------------")
for num in range(0, 11, 2):
    print(num)
    
#-------------------------break -------------------------
print("---------------------------")
coleccion = [2, 4, 5, 7, 8, 9, 3, 4]
for e in coleccion:
    if e == 7:
        break
    print(e)


#-------------------------continue-------------------------
#¿que numeros imprime?
print("---------------------------")
numeros_p = [2, 4, 5, 7, 8, 9, 3, 4]
for y in numeros_p:
    if y % 2 != 0:
        continue
    print(y)
print("---------------------------")
#--------------------------for else ------------------------
"""
for e in iterable:
    # Tu código aquí
else:
    # Este código siempre se ejecuta si no
    # se ejecutó la sentencia break en el bloque for """

numeros = [1, 2, 4, 3,7, 5, 8, 6]
for n in numeros:
    if n == 3:
        print("el numero 3 se encuentra en la lista")
        break
else:
    print('No se encontró el número 3')
