'''
verificamos si un número entero es par o impar. 
si el entero es impar, se genera una excepción. 
entonces 
si es un entero impar, entonces se genera un error.



a = 5
  
if a % 2 != 0:
    raise Exception("deberia ser un numero par")'''

#GENERAR UN TIPO ERROR ESPECIFICO

s = 'hola'
  
try:
    num = int(s)
except ValueError:
    raise ValueError("la cadena string debe ser cambiado a un entero")
#raise