#unicode

'''ord()'''
#Esta función recibe un carácter y devuelve su 
# representación en código unicode.
letras = "ABCDE123@abcde"
for letra in letras:
    print("El valor de {} es {}".format(letra, ord(letra)))
    


'''chr()'''
#Esto recibe un número y 
# devuelve su representación como carácter. 
numeros = [65, 200, 66, 97, 98]
for numero in numeros:
    print("El carácter que representa a {} es {}".format(numero, chr(numero)))