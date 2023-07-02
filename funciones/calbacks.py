# funciones como argumentos para otras
#funciones 

#son funcionales modularizabeles
#promedio de cualquier listado

promedio=lambda *args: sum(args)/len(args)
#print(promedio(10,20,30,2,4,4))

#si un alumno ha aprobado la mateira
aprobar=lambda calificacion: calificacion>=7
#print(aprobar(10))

def es_aprobatorio(calidficacion):
    return calidficacion>=90


def mostrar_mensaje(fun_promedio,fun_aprobar,*args):
    promedio=fun_promedio(*args)
    if fun_aprobar(promedio):
        print('felicidades ,aprobaste la matera')
    else:
        print('no aprobaste la matera')

mostrar_mensaje(promedio, aprobar,10,20,32,41,3)
