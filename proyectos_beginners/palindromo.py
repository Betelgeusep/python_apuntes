text = input("Ingresa un texto: ")

# Quitar todos los espacios...
text = text.replace(' ','')

# ... y revisar si la palabra es igual en ambos sentidos
if len(text) > 1 and text.upper() == text[::-1].upper():
	print("Es un palíndromo")
else:
	print("No es un palíndromo")