import time

class Student:
    def take_nap(self, seconds):
        print("Estoy muy cansado. Tengo que tomar una siesta. Hasta luego.")
        time.sleep(seconds)
        print("¡Dormí bien! ¡Me siento genial!")

#student = Student()
#student.take_nap(60)

# La función ctime devuelve una cadena para la marca de tiempo pasada.
timestamp = 1572879180
print(time.ctime(timestamp))
print(time.ctime())