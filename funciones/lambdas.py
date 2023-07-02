#las funciones son ciudadanos de primera clase
def centrigados_farheint(grados):
    return grados*1.8+32


#print(centrigados_farheint(10))
mi_function=centrigados_farheint
print(type(mi_function))
print(mi_function(10))

#funcion labmda
#expresada en una linea de codifgo y realizan tareas pequeña
#lambda <parametros>: cuerpo de la funcion 
funcion_grado=lambda grados: grados*1.8+32
print(funcion_grado(10))

""" 
sin parametros=lambda:True
parametros_default=lambda p1=10,p2=20,p3=30: p1+p2+p3
asteristo=lambda *args, **kwargs: len(args)+len(kwargs)
    """