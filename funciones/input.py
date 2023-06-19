val = input("Ingresa un numero: ")
print(val)
print()

name = input('cual es tu nombre \n')     # \n ---> newline  ---> It causes a line break
print(name)

print()

""" LA FUNCION INPUT SIEMPRE ES UNA CADENA """
#------------- saber que tipo de input---------------
# Program to check input
# type in Python
 
num = input ("numero :")
print(num)
name1 = input("nombre: ")
print(name1)
 
# Printing type of input value
print ("type of de numero", type(num))
print ("type of de nombre", type(name1))
print()

#-----------convertir string a entero o flotante-----
#int(entrada())
#float (entrada ())
num = int(input("Ingresa un numero : "))
print(num, " ", type(num))
 
           
floatNum = float(input("Ingresa un numero decimal: "))
print(floatNum, " ", type(floatNum))

#¿que pasa aquí ?, ¿como lo soluciono?
print("correcion")
anything = int(input("Ingresa un número para correcgit:"))
something = anything ** 2.0
print(anything, "al cuadrado es", something)



#------operadores aritméticos: + y *.------------
#El signo de + (más), al ser aplicado a dos cadenas, se convierte en un operador de concatenación:
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")

#El signo de * (asterisco), cuando es aplicado a una 
# cadena y a un número (o a un número y cadena) se convierte en un operador de replicación:
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

print('paola'*5+10*"*")

#-------multiples entradas- ----------------------
# funcion.split()
"""Esta función ayuda a obtener múltiples entradas de los usuarios. 
Rompe la entrada dada por el separador especificado. 
i no se proporciona un separador, cualquier espacio en blanco es un separador"""
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)