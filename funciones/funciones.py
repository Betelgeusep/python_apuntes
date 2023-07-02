def sum(n1, n2):
    #resultador=numero_dos+numero_uno
    #return resultador
    return n1+ n2 , 'suma' #retorna una tupla 
    
    
 
numero_uno=int(input('ingresa un numero: '))
numero_dos=int(input('ingresa otro numero: '))   
sum(numero_uno,numero_dos)

resultado=sum(numero_uno,numero_dos)
print(resultado)

#parametros adicionales 
def area_circulo(radio,pi=3.14):
    return pi*(radio**2)

resultado1 = area_circulo(10,3.14)
print(resultado1)