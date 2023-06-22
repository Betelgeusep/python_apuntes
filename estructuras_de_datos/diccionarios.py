#almacenan informacion en pares de datos
#llave y valor (un elemento que corresponde a la llave)
#las llaves por lo general son texto
#los valores no pueden ser cualquiera no tienen restriccion

#en otros lenguajes de programacion son conocidos como hashmap o json

#sintaxis

lenguage={"nombre": "python", "creador":"Guido van Rossum"}
print(lenguage)



print("-----acceder al diccionario")
#no podemos usar indices para ir a los elementos 
#tenemos que usar las llaves para acceder a sus valores

print(lenguage["nombre"])


print("-----añadir elementos----")
#Las llaves son unicas no se pueden repetir 
lenguage["año_lanzamiento"]=1991
print(lenguage)
#actualizar los datos
lenguage["año_lanzamiento"]=1991
print(lenguage)

print("------agregar listas a los valores de llaves----")
lenguage["caracteristicas"]=["sencillo","facil","genial"]
print(lenguage)

#funciones y metodos en diccionarios 

print("------metodo item---")
#retorna una lista de tuplas donde cada tupla es la combinacion de cada llava con su respectivo valor
print(lenguage.items())


print("------metodo keys ---")
#retorna una lista con las llaves del diccionario 
print(lenguage.keys())


print("------metodo values ---")
#retorna una lista con los valores del diccionario 
print(lenguage.values())


for elemento in lenguage.keys():
    print(elemento)

for elemento in lenguage.values():
    print(elemento)
    
for llave, valor in lenguage.items():
    print(llave, valor)

#imprime como una tupla
for elemento in lenguage.items():
    print(elemento)