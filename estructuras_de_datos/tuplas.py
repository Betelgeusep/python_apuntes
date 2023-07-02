#SINTAXIS 

#Primera forma 


lenguage=("python", "c","c++",3)
print("\nEsta es un tupla: ")
print(lenguage)


#tambien puede declararse sin parentesis
lenguages="python","cobol","c"
print("\nEsta tambien es una tupla sin parentesis: ")
print(lenguages)


#una tupla vacia 
mi_tupla=()
print("\nTupla vacia: ")
print(mi_tupla)
# cada elemento de una tupla puede ser de distinto tipo 
# (punto flotante, entero, cadena, o cualquier otro tipo de dato)

# Creating a Tuple
# with Mixed Datatype
Tupla1 = (5, 'python', 7, 'py')
print("\nTupla con diferentes datos: ")
print(Tupla1)



#una tupla de un solo elemento 
un_elemento=(1,)
print("\nTupla un solo elemento parentesis: ")
print(un_elemento)
print(type(un_elemento))


un_elemento1=1,
print("\nTupla un solo elemento sin parentesis: ")
print(un_elemento1)




# empaquetados de tuplas
nombre='paola','maria','ale','diego'
print("\nTuplas empaquetados: ")
print(nombre)

#acceder a los elementos es igula que con las listas
print("\nacceder al elemento 0: ")
print(nombre[0])
print("\nacceder al ultimo elemento: ")
print(nombre[-1])
print("\nacceder desdel el primer elemento hasta el ultimo: ")
print(nombre[1:])
print("\nacceder al desde el elemento 0 al penultimo: ")
print(nombre[:-2])
print("\nacceder a todos los elementos: ")
print(nombre[:])

print("\nrevertir la tupla: ")
print(nombre[::-1])


# Tambien se puede desempaquetar 
# los valores de las tuplas
a, b, c, d = nombre
print("\nValores despues de desempaquetar: ")
print("a es igual ",a)
print("b es igual ",b)
print("c es igual ",c)
print("d es igual ",d)

#si las variables no alcanzan podemos

numero=(1,23,5,3,2,3,4,2)
#se almacenaran en una lista * los restantes
#* -> lista
uno,dos,tres,*resto_valores=numero

#si no deseamos trabajar con los restantes valores
#_ -> omitir valor
uno,dos,tres,*_=numero

#omitir elementos con un rango 
uno,dos,tres,*_ , nueve, diez=numero

#omitir un elementos especificos
uno,_,tres,*_ , nueve, diez=numero

print("-----------for-----------")
for elem in nombre:
    print(elem)
    
#las tuplas no son mutables por lo tanto no se modifican 

print("-----------------------")

# Creando tuplas 
# con el uso de listas
list1 = [1, 2, 4, 5, 6]
print("\nTupla utilizando listas: ")
print(tuple(list1))




# Creando tuplas
# con el uso de funciones incorporadas tuple()
Tuple1 = tuple('python')
print("\nTuplas con el uso de funciones incor..: ")
print(Tuple1)


print("-----------------------")
"""¿Qué más pueden hacer las tuplas?"""

#el operador + puede unir tuplas (ya se ha mostrado esto antes)
edad = (1, 10, 15,20,34)
edad_nombres = edad + ('paola','maria','mateo','miriam')
print("\nTuplas concatenadas: ")
print(edad_nombres)


#el operador * puede multiplicar las tuplas, así como las listas;

# Creando una tupla
# con repeticion
rep = ('python',) * 3
print("\nTupla con repeticion: ")
print(rep)

# la función len() acepta tuplas, y regresa el número de elementos contenidos dentro;

print("\nLa longitud de la tupla rep es: ")
print(len(rep))


#los operadores in y not in funcionan de la misma manera que en las listas.
print("\n 10 esta en la lista edad?  ")
print(10 in edad)
print("\n 10 no esta en la lista edad?  ")
print(-10 not in edad)



""" COMO ELIMINAR LAS TUPLAS """
# eliminando tuplas
 
numeros = (0, 1, 2, 3, 4)
del numeros
 
print(numeros)