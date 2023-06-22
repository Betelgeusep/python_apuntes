#tuplas
#permite guardar elementos unicos 
#los elementos pueden ser de diferentes tipos


#sintaxis 
set1={1,2,3}
print(set1)

#si imprimimos valores repetidos 
set2={1,1,1,2,2,3}
print(set2)

#no son estructuras ordenadas
#no podemos acceder a ellas como las listas o tuplas 
#no podemos acceder mediante indices

set3={1,2.0,"texto"}


print("-------insertar elementos-----")
#set son mutables podemos alterar el contenido del set pero no las variables que contiene

set1.add(4)
print(set1)

set1.update([4,5,6])
print(set1)

print(len(set1))


print("-------borrar  elementos-----")
#eliminar un elemento
set1.discard(2)
print(set1)

#eliminar elemento
#si tratamos de eliminar un elemento que no existe python retorna error

set1.remove(3)
print(set1)

#borrar todos los elementos 
set1.clear()
print(set1)
