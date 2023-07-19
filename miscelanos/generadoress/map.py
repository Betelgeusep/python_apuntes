# map(function, list)
# map(una_funcion, una_lista)


list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))# map junto con la primer lambda para crear una nueva lista en la que todos los elementos han sido evaluados como 2 elevado a la potencia tomada del elemento correspondiente de list_1.
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()
    
    
#Imagina que tienes una lista de enteros y quieres obtener una nueva lista con el cuadrado de cada uno de ellos.
enteros = [1, 2, 4, 7]
cuadrados = []
for e in enteros:
    cuadrados.append(e ** 2)
     
print(cuadrados)

enteros = [1, 2, 4, 7]
cuadrados = list(map(lambda x : x ** 2, enteros))
print(cuadrados)