#almacenan informacion en pares de datos
#llave y valor (un elemento que corresponde a la llave)
#las llaves por lo general son texto y son unicas
#los valores pueden ser cualquiera no tienen restriccion
#es de un solo sentido 
#en otros lenguajes de programacion son conocidos como hashmap o json

#sintaxis

lenguage={"nombre": "python", "creador":"Guido van Rossum"}
print(lenguage)

# tambien puede escribirse 
"""lenguage={"nombre": "python", 
            "creador":"Guido van Rossum"
            }
    """
#diccionario vacio 
vacio={}

print()

print("-----acceder al diccionario")
#no podemos usar indices para ir a los elementos 
#tenemos que usar las llaves para acceder a sus valores
#        si una clave es una cadena, se tiene que especificar como 
#         una cadena;
#        las claves son sensibles a las mayúsculas y minúsculas: 
#         'Nombre' sería diferente a 'nombre'. 
#        No se puede utilizar una clave que no exista

print(lenguage["nombre"])



#-------------buscar si estan las llaves ------------------
print()
print("---------------------------------")

words = ['name', 'last_name', 'creador']
 
for word in words:
    if word in lenguage:
        print(word, "->", lenguage[word])
    else:
        print(word, "no está en el diccionario")
print("---------------------------------")
print()



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


print()
print("-----metodo update")
lenguage.update({"tipo":"alto_nivel"})
print(lenguage)

print()



# elimimando llaves 
#los valores no existen si no estan sus claves
print("----------------eliminar llaves-----------")
del lenguage['tipo']
print (lenguage)

print()
lenguage.update({"tipo":"alto_nivel"})

#eliminar el ultimo elemento de la lista
lenguage.popitem()
print(lenguage)

print()
#funciones y metodos en diccionarios 

print("-----------------metodo item----------------------------")
#retorna una lista de tuplas donde cada tupla es la combinacion de cada llava con su respectivo valor
print(lenguage.items())

print()

print("-----------------metodo keys----------------------------")
#retorna una lista con las llaves del diccionario 
print(lenguage.keys())
print()

print("----------------metodo values--------------------------")
#retorna una lista con los valores del diccionario 
print(lenguage.values())
print()

print("----------------recorrer diccionarios gracias a los metodos---------")
for elemento in lenguage.keys():
    print(elemento)
    
print()
for elemento in lenguage.values():
    print(elemento)
    
print()   
for llave, valor in lenguage.items():
    print(llave, valor)
    
print()
#imprime como una tupla
for elemento in lenguage.items():
    print(elemento)
    
print()