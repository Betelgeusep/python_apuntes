# inicializamos la clase
class Alumno:
    # inicializamos los atributos
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
 
 
    # función para imprimir los datos
    def imprimir(self):
               print("Nombre: ",self.nombre)
               print("Nota: ",self.nota)
               if self.nota < 5:
                              print("El alumno ha suspendido")
               else:
                              print("El alumno ha aprobado")
 
    # función para obtener el resultado

               
 
 
 
# bloque principal
# creamos los nuevos objetos
alumno1=Alumno("ivan",8)
alumno2=Alumno("juan",4)
 

 
# imprimimos los datos y resultados de cada alumno
alumno1.imprimir()
alumno2.imprimir()
