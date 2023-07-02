# CLOSURE
# funcion que puede generar a otra funcion pueden acceder a varibales local 

def saludar(username):
    mensaje=f'hola {username}' #variable local
    
    def mostrar_mensaje(): #anidada
        print(mensaje)
        
    return mostrar_mensaje

username='cody'
respuesta=saludar(username)

respuesta()