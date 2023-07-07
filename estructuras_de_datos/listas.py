#primera forma
#lista=list()
vocales = list('aeiou')
print(vocales)

#segunda forma
#lista=[]

#indice   0      1   2   3
#lista=['string',10,15.6,True]

#crear listas que almacenen un tipo de dato
#cada uno de los valores les corresponde una posicion y empieza en 0
#                0         1       2       3     4   
#                -5       -4      -3      -2    -1
lista_cursos=['python','django','flack','ruby','java']
cuarto_elemento=lista_cursos[3]
print(cuarto_elemento)
primer_curso=lista_cursos[0]
print(primer_curso)
primer_curso=lista_cursos[-5]
print(primer_curso)

print("----------------------------")
segundo_curso=lista_cursos[1]
print(segundo_curso)

print("----------------------------")
ultimo_curso=lista_cursos[-1]
print(ultimo_curso)


#si intentamos obtener un elemento que no exista obtendremos un errror


#LISTA ES DINAMICA 
print("----------------------------")
# --------------------ACTUALIZAR DATOS------------------------------------
lista_cursos=['python','django','flack','ruby','java']

lista_cursos[0]='html'
print(lista_cursos)



print("----------------------------")
#--------------------funcion len()---------------------------------------

print("la cantidad de curso es: ",len(lista_cursos))





print("----------------------------")
#-----------------------LISTAS COMPUESTAS---------------------
lista = [1, ['a', 'e', 'i', 'o', 'u'], 8.9, 'hola']
print("la cantidad de curso es: ",len(lista))




#---------------------SUBLISTAS------------------------------
lista_cursos=['python','django','flack','ruby','java']
#list1=lista_cursos si hacemos esto estamos reemplazando los nombres 

# queremos crear una sublista a partir del indice 0 al 3 
# [start:end]
print("----------------indice inicio y (fin-1) -----------------")
sub_lista=lista_cursos[0:3]
print(sub_lista)

#con indices que no se encuentren en la lista no hay error
print("----------------indices que no se encuentran en la lista-----------------")
sub_lista=lista_cursos[1:100]
print(sub_lista)

#obtener los ultimos elementos de la lista a partir del indice inicial
# [start:]
print("----------------ultimos elementos de la lista-----------------")
sub_lista=lista_cursos[2:]
print(sub_lista) 

print("----------------primeros elementos-----------------")
#obtener los primeros elementos de la lista a partir del indice final
# [:end]
sub_lista=lista_cursos[:3]
print(sub_lista)

print("----------------sublista con saltos----------------")
#sublita a partir de saltos 
# lista_cursos=['python','django','flack','ruby','java']
# [start:end:saltos]
sub_lista=lista_cursos[1:4:2]
print(sub_lista)


print("----------------sublista con todos elementos de la lista original-----------------")
#sublista con todos lo elementos de la lista original
# [:]
sub_lista=lista_cursos[:]
print(sub_lista)



print("----------------modificar listas-----------------")
#-------------------modificar listas ----------------------
lista_cursos=['python','django','flack','ruby','java']
#añadir nuevos elementos al final de nuestra lista
print("----append-------")

lista_cursos.append('css')
lista_cursos.append('c++')
print(lista_cursos)
print(len(lista_cursos))

# para añadir varios elementos al final de la lista
print("----extend-------")
lista_cursos.extend(['js','cobol'])
print(lista_cursos)
print(len(lista_cursos))

print("-----insert-------")
#añadir un elemento a la lista en un indice en particular la lista se rcorre
#.insert(indice, elemento)
#los demas elementos se desplazan 
lista_cursos.insert(1, 'rails')
print(lista_cursos)
print(len(lista_cursos))

#extender una lista a partir de otra

lista_cursos2=['c','c++','docker']

lista_cursos.extend(lista_cursos2)

print(len(lista_cursos))


#----------------------Eliminar elementos de listas------------------------------------------------------------
print("-------del --------")
#del
# Elimina el elemento del índice 1
vocales = ['a', 'e', 'i', 'o', 'u']
del vocales[1]
print(vocales)


# Elimina los elementos con índices 2 y 3
vocales = ['a', 'e', 'i', 'o', 'u']
del vocales[2:4]
print(vocales)


# Elimina todos los elementos
vocales = ['a', 'e', 'i', 'o', 'u']
del vocales[:]
print(vocales)

#puedes especificar de donde a donde quieres borrar [inicio:fin-1]

print("-------remove--------")
#-------metodo remove
letras = ['a', 'b', 'k', 'a', 'v']

# Elimina la primera ocurrencia del carácter a
letras.remove('a')
print(letras)


print("-------pop-------")
# Obtiene y elimina el último elemento
letras.pop()
print(letras)

print("-------clear-------")
#borra todos los elementos de una lista 
letras = ['a', 'b', 'c']
letras.clear()
print(letras)



#------------------------------------------------------------------------------------------

#------------------------------insertar por consola elementos a la lista-------------------

mi_lista = []

numero_elementos = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(numero_elementos):
    elementos = int(input("Ingresa un elemento de la lista: "))
    mi_lista.append(elementos)
print(mi_lista)

#------------------------------------------------------------------------------------------

#----------------------------------ordenar listas con metodos------------------------------

lista=[8,90,1,5,44,132,600,3,4]

#ordenar nuestra lista  de forma ascendente
lista.sort()
print(lista)
#descendente reverse
lista.sort(reverse=True)
print("-----------------------")
#numero mayor o menor en la lista
lista.sort()
print(lista[0]) #menor
print(lista[-1])#mayor
print("-----------------------")
#funcion max y min 
print(min(lista))
print(max(lista))

# invertir una lista 
print("-----------------------")
lst = [5, 3, 1, 2, 4]
print(lst)
 
lst.reverse()
print(lst)
print("-----------------------")
#------------------------------------------------------------------------------------------
#saber que un elemento esta en la lista

print(10 in lista) #el resultado es booleano 
print(11 not in lista)

#------------------------------------------------------------------------------------------
print("-----------------------")
#llenar la potencia elevado a dos de x numero 
squares = [x ** 2 for x in range(10)]
print(squares)

#------------------------------------------------------------------------------------------
