x = 2   
y = 7
print("el binario de: ",bin(2)) #010
print("el binario de: ",bin(7)) #111

#010
#111

#010

print("-----&------")
resultado=x & y 

#010
#111

#111


print(resultado)
print("-----|------")

resultado=x | y
print(resultado)

#010
#111
#101
print("-----^------")
resultado=x ^ y
print(resultado)


#010
#101
print("-----~------")
resultado= ~x
print(resultado)

#010
#100

print("-----<<------")
resultado=x << 2
print(resultado)

print("----->>------")
resultado=y >> 1
print(resultado)

