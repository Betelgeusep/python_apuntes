
#definicion de una funcion 

#entre los parentesis escribimos los parametros que requiere la funcion
#si no requiere parametros se deja vacio


""" 
def <nombre_funcion>():
    <instruccion>

"""
#llamar la Funcion 

"""
    <nombre_funcion>()
"""
#VARIABLES GLOBALES
#generalmente se escriben en la primera seccion del archivo
#se escriben en mayusculas
#se utilizan en cualquier parte del codigo

APELLIDO='pinto'

def funcion():
    print("mi primera funcion")
    nombre="ana" #variables locales (solo sirve dentro de la funcion)
    print(nombre,APELLIDO)
    
funcion()#llamado a la funcion 
print(APELLIDO)

#PARAMETROS
#Son los valores que una funcion puede recibir
#se definen dentro de los parentesis de la funcion

def perimetro_cuadrado(lado, unidades):
    perimetro=lado*4
    print(f'el perimetro es: {perimetro} {unidades}')

perimetro_cuadrado(4, 'metros')

perimetro_cuadrado(lado=4, unidades='metros')
perimetro_cuadrado(unidades='metros',lado=4)


print("------return ----------")
#---------------------------------------------------------
#funcion RETURN
# retorna o devuelve el valor 
def perimetro_square(lado):
    perimetro=lado*4
    return perimetro

def area_cuadrado(lado):
    area=lado*lado
    return area

#el valor de return puede ser guardado en una varibale
perimetro=perimetro_square(lado=5)
area=area_cuadrado(lado=5)

print(f'area :{area}, perimetro: {perimetro} ')


#---------------------------------------------------------

print("----calcular cuadrado----------")
def calcular_cuadrado(lado):
    perimetro=lado*4
    area=lado*lado
    return area, perimetro

area1, perimetro1=calcular_cuadrado(lado=8)
print(f'area :{area1}, perimetro: {perimetro1} ')


print("----capturar los dos valores en una sola variable----------")
resultado=calcular_cuadrado(lado=8)
print(resultado)#el resultado es un dupla



#-------documentacion de funciones-----
# __doc__ (modulos, clases,metodos y funciones)
#descripcion corta
def area_triangulo(b,h):
    """ calcular el area de un triangulo"""
    area=(b*h)/2
    return area

area_triangulo(5,4)

#descripcion larga

def area_triangulo2(b,h):
    """ calcular el area de un triangulo
    
    Esta funcion recibe el valor b que es la base y h la altura de un triangulo
    y a partir de este retorna su su area
    
    Args:
        b(int): medida de la base de un triangulo
        h(int): medida de la altura de un triangulo
        
    Returns:
        area(float): el area del triangulo
    
    TODO:
        *
    """
    area=(b*h)/2
    return area

area_triangulo2(5,4)

print(area_triangulo2.__doc__)
print(help(area_triangulo2))
#-------------------------none------------------------------

def saludo(nombre):
    print(f'Hola {nombre}')
    
print(saludo('j2logo'))





def introduction(first_name, last_name="Smith"):
     print("Hola, mi nombre es", first_name, last_name)
introduction("Jorge", "Pérez")
introduction("Enrique")

#-------------funciones con listas----
def tabla_del(numero):
    resultados = []
    for i in range(11):
         resultados.append(numero * i)
    return resultados
 
res = tabla_del(3)
print(res)
 