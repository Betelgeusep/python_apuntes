class Coche:
    ''' Esta clase define el estado y comportamiento de un coche'''
    ruedas=4
    
    def __init__(self,color, aceleracion):
        self.color=color
        self.aceleracion=aceleracion
        self.velocidad=0
        
    def acelera(self):
        self.velocidad=self.velocidad+self.aceleracion
    def frena(self):
        v=self.velocidad-self.aceleracion
        if v<0:
            v=0
        self.velocidad=v
        
#instancia de la clase
c1 = Coche('rojo', 20)
print(c1.color)
print(c1.aceleracion)
print(c1.velocidad)



class CocheVolador(Coche):
    ruedas = 6
    def __init__(self, color, aceleracion, esta_volando=False):
        #llama a la clase padre o superclass
        #devuelve un objeto temporal de la superclase que permite invocar a los métodos definidos en la misma
        super().__init__(color, aceleracion)
        self.esta_volando = esta_volando
        
    def vuela(self):
        self.esta_volando = True
    def aterriza(self):
        self.esta_volando = False

cv1 = CocheVolador('rojo', 60, esta_volando=True)
print(cv1.esta_volando)
        
        
# isinstance(cv1, Coche)
# issubclass(CocheVolador, Coche)
        
