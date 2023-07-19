
# declarando la clase
class GfG:
    nombre = "Python"
    edad = 10
 
 
# inicializar objeto
obj = GfG()
 
# usando hasattr para ver si nombre existe
print("Nombre existe ? " + str(hasattr(obj, 'nombre')))
 
# 
print("Name existe? " + str(hasattr(obj, 'name')))