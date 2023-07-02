#scope

#variables diferentes y alcances diferentes
animal='leon' #variable global

def imprimir_animal():
    global animal
    animal='ballena'
    # animal='ballena'#variable local
    print(animal)
    print(id(animal))
    
imprimir_animal()
print(animal)
print(id(animal))