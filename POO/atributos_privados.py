'''
 he definido el atributo username y el método private_method como privados. 
 Es decir, un atributo y un método que solo pueden ser utilizados dentro 
 de la clase donde fueron creados.
'''

class Usuario:

    def __init__(self, nombreUsuario):
        self.__username = nombreUsuario


    def __private_method(self):
        print('Este es un método privado')
        
        
    def public_method(self):
        print(self.__username)
        self.__private_method()
        
#si tratamos de acceder

py = Usuario('Paola') # creamos un objeto
#print(py.__username)   # obtendremos un erros

py.public_method()

print(py.__dict__)

print(py._Usuario__username)

py._Usuario__private_method()

#cambiar estos metodos privados

py._Usuario__username = 'Cambio de username'
print(py._Usuario__username )
