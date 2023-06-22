import random


def adivina_el_numero_pc(x):
    print("====================")
    print("Bienvenida al juego!")
    print("====================")
    print("tu meta es que la computadora adivine tu numero")
    print()
    print(f'selecciona un numero entre 1 y {x} para que la computadora intente adivinarlo')
    print()
    
    limite_inferior=1
    limite_superir=x
    
    respuesta=''
    while respuesta!='c':
        #generar una prediccion 
        if limite_inferior != limite_superir:
            prediccion=random.randint(limite_inferior,limite_superir)
        else:
            prediccion=limite_inferior
            
        #obtener la respuesta del usuario
        respuesta=input(f'mi prediccion es {prediccion}. si es muy alta ingresa A si es muy baja ingresa B , si es correcta ingresa C: ').lower()
        print()
        if respuesta=='a':
            limite_superir=prediccion-1
        elif respuesta=='b':
            limite_inferior=prediccion+1
    print(f'si la computadora adivino tu numero correctamenta {x}')
    

adivina_el_numero_pc(10)
        
        