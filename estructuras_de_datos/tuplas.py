#SINTAXIS 

# cada elemento de una tupla puede ser de distinto tipo (punto flotante, entero, cadena, o cualquier otro tipo de dato)

#Primera forma 


lenguage=("python", "c","c++")
print(lenguage)


#tambien puede declararse sin parentesis
lenguages="python","cobol","c"
print(lenguages)


#una tupla vacia 
mi_tupla=()
print(mi_tupla)

#una tupla de un solo elemento 
un_elemento=(1,)
print(un_elemento)
un_elemento1=1,
print(un_elemento1)

print("-----------------------")

#acceder a los elementos es igula que con las listas
nombre='paola','maria','ale','diego'
print(nombre)

print("-----------------------")
print(nombre[0])
print(nombre[-1])
print(nombre[1:])
print(nombre[:-2])
print(nombre[:])
print("-----------for-----------")
for elem in nombre:
    print(elem)
#las tuplas no son mutables por lo tanto no se modifican 

"""¿Qué más pueden hacer las tuplas?

la función len() acepta tuplas, y regresa el número de elementos contenidos dentro;
el operador + puede unir tuplas (ya se ha mostrado esto antes)
el operador * puede multiplicar las tuplas, así como las listas;
los operadores in y not in funcionan de la misma manera que en las listas.
    """
    
#---------------------funcion len ------------------------
edad = (1, 10, 15,20,34)

edad_nombres = edad + ('paola','maria','mateo','miriam')
edad3 = edad * 3
edad_nombres

print(len(edad3))
print(edad_nombres)
print(edad3)
print(10 in edad)
print(-10 not in edad)