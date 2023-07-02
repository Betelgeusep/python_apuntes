#codigo mas legible

"""
a-> funcion proncipal (decorador)
b-> funcion a decorar
c-> funcion decorada

a(b)->c

"""


def funcion_a(funcion_b):
    def funcion_c(*args, **kwargs):
        print('antes del llamado')
        resultado= funcion_b(*args,**kwargs)
        print('depsues del llamado')
        return resultado
    return funcion_c

@funcion_a
def saludar():
    print('hola nos encontramos en una funcion')
 
saludar()   

@funcion_a
def suma(num_1,num_2):
    return num_1+num_2
result=suma(10,20)

print(result)
