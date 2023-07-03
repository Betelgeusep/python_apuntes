class User:
    nombre=''
    
    def __init__(self,nombre):#metodo constructor -> inicalializar el objeto
        #retorna un nuevo objeto a la clase
        self.nombre = nombre
        
        print('hola, mi nombres '+self.nombre)
    
    def saludar(self, saludo):
        print(saludo+self.nombre)
        
        
class Empleado(User):#clase hijo
    salario = 0
    
    def Modificar_salario(self, salario):
        self.salario = salario
        
    def ver_salario(self):
        print(self.salario)
        
    def saludar(self):
        print("mi nombre es: "+self.nombre+"y gano: "+str(self.salario))


#instancias 
paola = User('paola')#objeto de instancia
paola.nombre='paola'
paola.saludar('heloo ')


#herencia -> herede los objetos del padre  como jerarquia 
"""sucede entre clases 

        """

empleado=Empleado('uriel')
empleado.saludar('hola me llamo')
empleado.Modificar_salario(1000)
empleado.ver_salario()
    

