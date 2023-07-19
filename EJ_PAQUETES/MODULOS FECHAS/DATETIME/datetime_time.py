#El módulo datetime también tiene una clase que te permite presentar la hora TIME
#time(hour, minute, second, microsecond, tzinfo, fold)
from datetime import time
t = time(14, 53, 20, 1)

print("Tiempo:", t)
print("Hora:", t.hour)
print("Minutos:", t.minute)
print("Segundos:", t.second)
print("Microsegundo:", t.microsecond)