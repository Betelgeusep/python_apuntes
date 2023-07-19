#almacenan informacion en pares de datos
#llave y valor (un elemento que corresponde a la llave)
#las llaves por lo general son texto y son unicas
#los valores pueden ser cualquiera no tienen restriccion
#es de un solo sentido 
#en otros lenguajes de programacion son conocidos como 
# hashmap o json



#sintaxis

lenguage={"nombre": "python", "creador":"Guido van Rossum"}
print("\n el diccionario es: ")
print(lenguage)

lenguage={
            "nombre": "python", 
            "creador":"Guido van Rossum",
            "x":"y"
            }
 
#
# Creando un diccionario

# con llaves diferentes
Dic = {'Nombre': 'maria', 1: [1, 2, 3, 4]}
print("\nDiccionario con diferentes llves: ")
print(Dic)


#diccionario vacio 
vacio={}
print("\n el diccionario vacio: ")
print(vacio)


# Creando diccionario
# con el metodo dict() 
Dict = dict({1: 'uno', 2: 'dos', 3: 'tres'})
print("\nDicccionario con el uso del metodo dict(): ")
print(Dict)


print("\n-----acceder al diccionario------")
#no podemos usar indices para ir a los elementos 
#tenemos que usar las llaves para acceder a sus valores
#        si una clave es una cadena, se tiene que especificar como 
#         una cadena;
#        las claves son sensibles a las mayúsculas y minúsculas: 
#         'Nombre' sería diferente a 'nombre'. 
#        No se puede utilizar una clave que no exista
print("\nAccediendo a la llave nombre: ")
print(lenguage["nombre"])
print(Dic[1])





#-------------buscar si estan las llaves ------------------
#lenguage={"nombre": "python", "creador":"Guido van Rossum"}
print("\n---------------------------------")

words = ['name', 'last_name', 'creador']
 
for word in words:
    if word in lenguage:
        print(word, "->", lenguage[word])
    else:
        print(word, "no está en el diccionario")
print("\n---------------------------------")


# lenguage={"nombre": "python", "creador":"Guido van Rossum"}

print("\n-----añadir elementos----")

#Las llaves son unicas no se pueden repetir 
lenguage["año_lanzamiento"]=1991
print(lenguage)
#actualizar los datos
lenguage["año_lanzamiento"]=1999
print(lenguage)

#agregando listas a los valores de llaves
print("\n------agregar listas a los valores de llaves----")
lenguage["caracteristicas"]=["sencillo","facil","genial"]
print(lenguage)

# Añadiendo llaves y valores aninado a un diccionarioKey value to Dictionary

#Dict = dict({1: 'uno', 2: 'dos', 3: 'tres'})
Dict[5] = {'python': {'1': 'facil', '2': 'alto_nivel'}}
print("\ndiccionarios aninados en llave: ")
print(Dict)



print("\n-----metodo update------")
lenguage.update({"tipo":"alto_nivel"})
print(lenguage)

print()



# elimimando elementos 
#los valores no existen si no estan sus claves

print("----------------eliminar llaves-----------")
del lenguage['tipo']
print (lenguage)

print()
lenguage.update({"tipo":"alto_nivel"})
print (lenguage)

#eliminar el ultimo elemento de la lista
lenguage.popitem()
print(lenguage)

# lenguage.pop('tipo')

#eliminar todos los elementos
#   lenguage.clear()
print()
#funciones y metodos en diccionarios 

#se recomienda una tupla para que sea solo leer

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

#get 

usuario={
    'name':'eduardo ismael',
    'age':26,
    'job':'codigo facilito'
}

calificaciones=usuario.get('calificaciones','la llave no existe')

if calificaciones:
    for calificacion in calificaciones:
        print(calificacion)

usuarios=['eduardo', 'fernando', 'uriel', 'rafael']
diccionario={ usuario:position+1
             for position, usuario in enumerate(usuarios)}

print(diccionario)

#set default
#si la llave no existe empieza a añadir 

valor=diccionario.setdefault('e',5)
print(valor)
print(diccionario)

def suma_pares(numero_1 = 10, numero_2 = 20):
    return numero_1 + numero_2
def suma_pares(numero_1=10, numero_2=20):
    return numero_1 + numero_2