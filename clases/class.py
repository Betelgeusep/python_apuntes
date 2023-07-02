#nomenclatura camelcase

#atributos de clase -> pertenecen a una clase
#atributos de instancia -> pertencen a un objeto

class Usuario:
    username ='username por default'
    email =''

cody = Usuario()
print(cody)

#atributos de clase
print(Usuario.username)
Usuario.username='user1'
print(Usuario.username)

#atributos de instancia 
#__dict__

user1=Usuario()
# 1.- primero verifica si el atrivuto existe dentro del objeto
#2.- verifica si el atrr existe dentro de la clase ->lectura
# 3.- lanzar un error 
print(user1.username)
print(id(user1.username))
print(id(Usuario.username))
print(user1.__dict__)

user1.username='cody' #añadimos el atributo al objeto
user1.password='123'
print(user1.username) #atributo de instanci
print(id(user1.username))
print(id(Usuario.username))