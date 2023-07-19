def tabla_del(uno, dos):
    uno = []
    dos = []
    i=1
    for i in range(11):
         uno.append(uno * i)
         dos.append(dos * i)
    return uno, dos
 
uno,dos = tabla_del(1,2)
print(uno)
print(dos)