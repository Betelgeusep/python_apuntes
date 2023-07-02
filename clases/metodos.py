

class Usuario:
    def inicializar(self, username, password):
        #atr
        self.username =username
        self.password =password


user1 = Usuario()
user2 = Usuario()

user1.inicializar('user1','pass2')
user2.inicializar('user2', 'pass1')

print(user1.__dict__)
print(user2.__dict__)

#__init__
class Usuario1:
    #Object 
    
    def __init__(self,username='', password=''):
        
        self.username =username
        self.password =password


user1 = Usuario1('upaola','13213')
user2 = Usuario1('podas','sdada')

user4=Usuario1()

print(user1.__dict__)
print(user2.__dict__)
print(user4.__dict__)
