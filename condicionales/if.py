#---------------------If -------------------------
"""
if condicion:
   # sentencias que se van a ejecutar si cumple la condicion
"""
print("calcularemos un numero si es mayor a 15")
i = int(input("ingrese un numero: "))
  
if (i > 15):
    print(i,"es mayor a 15")
print(i," es menor a 15")
print()
#---------------------if abreviada-------------------------  
#if condicion: sentencia 
i = 10
if i < 15: print(i, "es menor que 15")


#---------------------If else -------------------------
"""if (condicion):
    # sentencias que se van a ejecutar si cumple la condicion
else:
    # sentencias que se van a ejecutar si no cumple la condicion
"""
n = int(input("ingrese un numero: "))
if (n < 15):
    print(n,"es menor que 15")
    print("sentencia if")
else:
    print(n,"es mayor a 15")
    print("sentencia else")
print("no estoy en if ni en else")
print()

#-----------------------if else abreviada--------------------------
#sentencia cuando es verdara if condicion else sentencia cuando es falsa
i = 10
print(True) if i < 15 else print(False)

#---------------------If else aninadas -------------------------

"""if (condition1):
   # Executes when condition1 is true
   if (condition2): 
      # Executes when condition2 is true
   # if Block is end here
# if Block is end here
    """
print(" aninadas")
m = int(input("ingrese un numerov: "))
if (m == 10):
    #  sentencia verdarea 
    if (m < 15):
        print(m,"es menor a 15")
    if (m < 12):
        print(m,"es menor a 12")
    else:
        print(m,"es mayor a 15")
print()

#---------------------elif o else if -------------------------
"""
if (condicion):
    sentencia
elif (condicion):
    sentencia
.
.
else:
    sentencia
"""
print("si un numero es igual a los de las lista")
i = int(input("ingrese un numerov: "))
if (i == 10):
    print(i,"es igual a 10")
elif (i == 15):
    print(i,"es igual a 15")
elif (i == 20):
    print(i,"es igual a 20")
else:
    print(i,"no esta en la lista")
    
