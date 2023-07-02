

lenguajes='python ruby java rust c c++'

#crear una lista a partir de un string
 # cada espacio denota un nuevo elemento para dividir
listado_lenguajes=lenguajes.split()
print(listado_lenguajes)

lenguajes='python-ruby-java-rust-c-c++'
listado_lenguajes=lenguajes.split('-')
print(listado_lenguajes)

#diviendo con un parametro
lenguajes='python-ruby-java-rust-c-c++'
listado_lenguajes=lenguajes.split('-',2)
print(listado_lenguajes)


#metodo join 

#nos permite generar un string a partir de una lista
lenguajes=['python', 'ruby', 'java', 'rust', 'c', 'c++']
strin_lenguajes=' '.join(lenguajes)
print(strin_lenguajes)

strin_lenguajes='/ '.join(lenguajes)
print(strin_lenguajes)


#busqueda 
#metodo count para contar cuantas frases o palabras existen en un string
titulo_curso='curso profesional de python, donde aprenderemos python'
contador=titulo_curso.count('python')

print(contador)
contador=titulo_curso.count('o')
print(contador)

#verifica si esta en el texto 
#sensible a mayusculas o minisculas
print('python' in titulo_curso.lower())
print('python' not in titulo_curso.lower())

#si empieza con ?
print(titulo_curso.startswith('curso'))

#si finaliza con?
print(titulo_curso.endswith('curso'))


#justificar texto 

mensaje='hola'

#ljust -> justificar a la izquierda
#rjust -> justificar a la derecha
# center ->center

#se genera un nuevo string

mensaje1=mensaje.ljust(20)
print(mensaje1)
mensaje2=mensaje.rjust(20)
print(mensaje2)
mensaje3=mensaje.center(20)
print(mensaje3)
