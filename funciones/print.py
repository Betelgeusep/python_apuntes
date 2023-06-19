# funcion print(argumento)
#el argumento puede ser Cadenas, números, caracteres, valores lógicos, objetos

#----uso de las comillas---
print('comillas simples')
print("comillas doble")
# hola como estas sabias que "x" persona esta de viaje

print('hola como estas sabias que "x" persona esta de viaje')

print('dobles uso de "comillas"')
print("dobles uso de 'comillas'")

print("caracter especial ")
#\' o \"
# hola como estas sabias que "x" persona esta de viaje
print("hola como estas sabias que \"x\" persona esta de viaje")
print("caracter \"especial\" ")


# triple_quotes.py

print('''hi there.
how are you?''')



#----nueva linea---------- 
#\n 
print("nueva linea \n otra linea")
#
print("hola mundo")
print()
print("hello")



#-----multiples argumentos-------------
print("primer argumento", "segundo argumento","variable", sep="*")



#-------Argumentos de palabra clave-------------

# end=
# termina con un espacio 
print("hola ", end="   ")
print("siguiente argumento")

#sep=""
#para separar los argumentos y termina después del último argumento.
print('PA','0', sep='-', end=' ')
print('LA')

#\n provides new line after printing the year
print('7','06','2012', sep='-', )
print (" FECHA")
  
print('Red','Green','usuario', sep=',', end='@')
print('gmail.com')


#----------variables ----------------

nombre = 'paola'
edad = 22
print("Mi nombre es", nombre, "y yo tengo",edad , "años", end=" ")
print("Un gusto conocerte!.")