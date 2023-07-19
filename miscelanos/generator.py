def pares():
    for x in range(0, 102, 2):
        yield x  #suspenderemos, de forma momentánea, la ejecución de la función; esto para retornar un objeto. Una vez el objeto haya sido retornado la función podrá reaundarsé en el punto donde se detuvo.
        
''''if __name__ == '__main__':
    print('Listado de todos los números pares del 1 al 100')

    for par in pares():
        print(par)'''

'''numeros = pares()
par = next(numeros)
print(par)
par = next(numeros)
print(par)
par = next(numeros)
print(par)
par = next(numeros)
print(par)
par = next(numeros)
print(par)
par = next(numeros)
print(par)'''


'''if __name__ == '__main__':
    numeros = pares()

    while True:
        try:
            par = next(numeros)
            print(par)
        except StopIteration:
            print('Sin más valores en el generador')
            break'''
    
    
generador = ( number for number in range(0, 102, 2))
print(generador)
print('Listado de números pares')
for par in generador:
    print(par)
    
    
    