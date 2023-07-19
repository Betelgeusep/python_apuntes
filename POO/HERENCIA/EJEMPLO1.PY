class Dispositivo:
    
	def __init__(self,identificador,marca): #METODO CONSTRUCTOR
		self.identificador = identificador
		self.marca = marca

	def conectar(self):
		print("¡Conectado!")

# la clase base se indica entre paréntesis
class Teclado(Dispositivo):
	def __init__(self,identificador,marca,tipo):
     
		# llamada al constructor del padre
		Dispositivo.__init__(self,identificador,marca)
		self.tipo = tipo
  
	# metodo de la subclase
	def pulsar_tecla(self,tecla):
		print(tecla)

t1 = Teclado("0001", "Logitech", "AZERTY")
print(f"Id: {t1.identificador}, Marca: {t1.marca}, tipo: {t1.tipo}")
t1.conectar()
t1.pulsar_tecla("a")

