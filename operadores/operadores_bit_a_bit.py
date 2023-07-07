x = 2   
y = 7
print("el binario de 2: ",bin(2)) #010
print("el binario de 7: ",bin(7)) #111

#010
#111
#------
#010
#421

print("-----&------")#and
resultado=x & y 

#010
#111
#-----
#111


print(resultado)
print("-----|------")#or

resultado=x | y
print(resultado)

#010
#111
#------
#101
#401
print("-----^------")
resultado=x ^ y
print(resultado)


#010 x
#-----
#101
print("-----~------")
resultado= ~x
print(resultado)

#010
#100
#         1000
x = 2   #1000 
y = 7   #011
print("-----<<------")
resultado=x << 2
print('<<',resultado)

print("----->>------")
resultado=y >> 1
print(resultado)

