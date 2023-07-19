# La función filter() filtra una lista de elementos para los que una función devuelve True.

#  filter(una_funcion, una_lista)

# Imagina que quieres filtrar una lista de números para obtener solo los valores pares.
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = []
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
print(pares)


valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = list(filter(lambda x : x % 2 == 0, valores))
print(pares)