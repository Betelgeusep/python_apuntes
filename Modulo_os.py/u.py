'''
version - almacena la versión del sistema operativo.
machine - almacena el identificador de hardware, por ejemplo, x86_64.
'''
import os
print(os.listdir())

#creando directorios
#os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.listdir())
    
#donde estoy ahora 
print(os.getcwd())

#eliminando direcotrios 
#os.mkdir("my_second_directory")
print(os.listdir())

#Para eliminar un directorio y sus subdirectorios
os.makedirs("my_first_directory/my_second_directory")
os.removedirs("my_first_directory/my_second_directory")
print(os.listdir())
 