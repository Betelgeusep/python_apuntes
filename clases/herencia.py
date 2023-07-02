class Animal():
    def comer(self):
        print('el animal come.')
        
    def dormit(self):
        print('el animal duerme.')


class mascota(Animal):#clase padre
    #sobreescribir
    def comer(self):
        print('el animal come')
    
class perro(mascota):#clase hija
    pass

class felino:
    
    def cazar(self):
        print('el felino caza')
    
class gato(mascota,felino): #herencia multiple
    def __init__(self,nombre):
        self.nombre=nombre
        

duke=perro()
duke.comer()
duke.dormit()

patricio=gato()
patricio.comer()
patricio.dormit()
patricio.cazar()


duke=gato('duke')
duke.comer()
duke.dormit()
