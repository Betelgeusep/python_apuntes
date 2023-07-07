x='hola'.encode('utf-8')
print(x)

y='café'.encode('utf-8')
print(y)

print('ª'.encode('utf-8'))
print(b'\xc2\xaa'.decode('utf-8'))