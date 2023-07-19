

class Persona:
 
    # metodo init o constructor
    def __init__(self, nombre):
        self.nombre = nombre
 
    # ejemplo de metodo
    def hola(self):
        print('Hola mi nombre es: ', self.nombre)
 
 
p = Persona('Paola')
p.hola()

p2 = Persona('maria')
p3 = Persona('pedro')

p2.hola()
p3.hola()