"""
Definamos una función que calcula el Índice de Masa Corporal (IMC).

Como puedes observar, la formula ocupa dos valores:

peso (originalmente en kilogramos)
altura (originalmente en metros)

"""

def indice_imc(weight, height):
    
    return weight / height ** 2
 
 
print(indice_imc(52.5, 1.65))

#-----------libras a kilogramos-----------
#1 lb = 0.45359237 kg

def lb_to_kg(lb):
    return lb * 0.45359237
 
 
print(lb_to_kg(2))


#-----------pies y pulgadas a metros-----------
#1 ft = 0.3048 m, y 1 in = 2.54 cm = 0.0254 m.
def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254
 
 
print(ft_and_inch_to_m(1, 1))