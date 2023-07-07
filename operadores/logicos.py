#comparar valores boleanos
#and , or y not

# and 
#todos tienen que ser verdadero para que sea true 
resultado=True and True
print(resultado) #true
resultado=True and True and False
print(resultado)#false 


#or 
# por lo menos una tiene que ser true para que el resultado sea true
resultado=True or True
print(resultado) #true

resultado=True or False or False
print(resultado)#true


resultado=False and False
print(resultado) #false


resultado=True and (False or 5>10)
#          true and(false or False)
#          true and false
#          false
print('operacion: ',resultado) #false


#not
#negar un valor booleano
resultado=not True
print(resultado) #false
resultado=not False
print(resultado) #false


