# syntax
"""
while condicion:
    sentencia
"""
"""Aquí, condición puede ser un literal, 
el valor de una variable, 
el resultado de una expresión 
o el valor devuelto por una función."""
print("while ")
i = 1
while i < 6:
  print(i)
  i += 1
  
print("------------------")

count = 0
while (count < 3):
    count += 1
    print("Hola",count)
    
    

print("------------------")
#¿que hace esta algoritmo?
numero = 0
print('')
while numero <= 10:
    print(f'fda{numero * 3}')
    numero += 1
print('Fin')
print()
print("------------------")


# encontrar un numero en una lista -----------------

valores = [4, 1, 9, 2, 7, 4]
encontrado = False
indice = 0
longitud = len(valores)
while not encontrado and indice < longitud:
    valor = valores[indice]
    if valor == 5:
        encontrado = True
    else:
        indice += 1
if encontrado:
    print(f'El número 5 ha sido encontrado en el índice {indice}')
else:
    print('El número 5 no se encuentra en la lista de valores')


#---------sentencia break---------------
"""Con la instrucción break podemos detener el bucle incluso 
si la condición while es verdadera:"""
print("------------------")

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
print("------------------")

valores = [5, 1, 9, 2, 7, 4]

encontrado = False
indice = 0
longitud = len(valores)
while indice < longitud:
    valor = valores[indice]
    if valor == 2:
        encontrado = True
        break
    else:
        indice += 1
if encontrado:
    print(f'El elemento 2 ha sido encontrado en el índice {indice}')
else:
    print('El elemento 2 no se encuentra en la lista de valores')

print("------------------")
#---------sentencia continue ---------------
"""Con la instrucción continue podemos detener la 
iteración actual y continuar con la siguiente
    """
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

print("------------------")

#---------while else ---------------
"""Con la declaración else podemos ejecutar un bloque 
de código una vez cuando la condición ya no sea verdadera:"""
i = 1
while i <= 6:
  print(i)
  i += 1
else:
  print("i no es mas grande que 6")
  
  
print("------------------")
 
valores = [5, 1, 9, 2, 7, 4]

indice = 0
longitud = len(valores)
while indice < longitud:
    valor = valores[indice]
    if valor == 2:
        print(f'El elemento 2 ha sido encontrado en el índice {indice}')
        break
    else:
        indice += 1
else:
    print('El elemento 2 no se encuentra en la lista de valores')
  

print("------------------")
  
#Escriba un programa que pregunte una y otra vez si desea continuar con el programa
print("DIGA si PARA CONTINUAR")
respuesta = input("¿Desea continuar el programa?: ")

while respuesta=="si":
  respuesta=input("desea continuar con el programa?: ")
else:
  print("hasta luego")

print("------------------")
  
#Escriba un programa que solicite una contraseña limite 3 intentos

print("verificacion de contraseña")
contraseña = input("Ingrese la contraseña: ")
i=1
while contraseña!='abc'and i<=3:
  print(f"tu contraseña es incorrecta, te quedan {3-i} intentos ")
  contraseña = input("Ingrese la contraseña: ")
  i+=1
if contraseña=='abc':
  print("la contraseña es correcta")
elif i==3:
  print("se acabaron tus intentos porque tu contraseña es incorrecta")
    