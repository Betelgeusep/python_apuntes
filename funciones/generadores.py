# un tipo especial de funcion que retorna objetos que podemos iterar
def pares(): #generador -> lazy iterator
    for num in range(0,100,2):
        yield num #la funcion suspende su ejecucion
        
#for par in pares():
#   print(par)
generador=pares()
"""
print(next(generador))
print(next(generador))"""

#ahorra memoriar
#cuando trabajemos con miles de registros

while True:
    try:
        par=next(generador)
        print(par)
    except StopIteration:
        print('finalizo la iteracion')