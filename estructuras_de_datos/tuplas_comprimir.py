lista=[1,2,3,4,5]

tupla=(10,20,30,40,50)

lista2=[100,200,300,400]

resultado=zip(tupla,lista,lista2) # -> zip

#a partir del objeto zip generamos otra tupla

resultado=tuple(resultado)
print(resultado)
