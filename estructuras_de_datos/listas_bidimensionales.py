#-----------------------------------tablas en python con listas -------------------------------------
nombre_de_la_tabla = []

# También puedes iniciar la listas en el interior
nombre_de_la_tabla = [[], []]

mi_tabla = [['Juan', 'Laura'], [21, 32]]

print("------------------------------------------------")
# Muestra Juan (la primera posición es la 0, 0)
print(mi_tabla[0][0])

print("------------------------------------------------")
# Muestra 32 (última fila, segunda columna)
print(mi_tabla[-1][1])
print("------------------------------------------------")
# Muestra 21
print(mi_tabla[1][0])
print("------------------------------------------------")
# Muestra Laura
print(mi_tabla[0][1])
print("------------------------------------------------")
# Muestra la lista con nombres
print(mi_tabla[0])
print("------------------------------------------------")
#---------------------------------------------------------------------
mi_tabla = [['Juan', 'Laura'], [21, 32]]

# Recorriendo los elementos

# Accedemos a cada fila (que es una lista)
for fila in mi_tabla:
    # Accedemos a cada columna dentro de la fila
    for columna in fila:
        print(columna)
print("------------------------------------------------")
# Recorriendo los índices
# i serían las filas
for i in range(len(mi_tabla)):
    for j in range(len(mi_tabla[i])):
        print(mi_tabla[i][j])

# Con while y los índices
fila = 0

while fila < len(mi_tabla):
    columna = 0
    while columna < len(mi_tabla[fila]):
        print(mi_tabla[fila][columna])
        columna += 1
    fila += 1
    
#---------------------------------------------------------------------
board = []
 
for i in range(8):
    row = [8 for i in range(8)]
    board.append(row)
print(board)

board = [[8 for i in range(8)] for j in range(8)]
print(board)