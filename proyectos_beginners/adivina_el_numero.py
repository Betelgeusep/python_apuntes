#ADIVINA EL NUMERO 

#EL USUARIO TIENE QUE ADIVINAR UN NUMERO GENERADO ALEATORIO
from random import randint


def adivina_el_numero(x):
    print("====================")
    print("Bienvenida al juego!")
    print("====================")
    print("tu meta es adivinar el numero generado por la computadora")
    
    numero_aleatorio=randint(1,x)
    
    prediccion=0
    while prediccion!=numero_aleatorio:
        prediccion=int(input(f'adivina el numero entre 1 y {x}: '))
        
        if prediccion<numero_aleatorio:
            print("intenta otra vez. este numero es muy pequeño")
        elif prediccion>numero_aleatorio:
            print("intenta otra vez. este numero es muy grande")
    print(f"felicitaciones adivinaste el numero  {numero_aleatorio} correctamente")


xy=int(input('ingresa un numero'))
print(prediccion)adivina_el_numero(xy)
