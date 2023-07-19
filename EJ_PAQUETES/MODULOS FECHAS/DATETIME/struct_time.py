'''
time.struct_time:
    0 tm_year   # Especifica el año.
    1 tm_mon    # Especifica el mes (valor de 1 a 12)
    2 tm_mday   # Especifica el día del mes (value from 1 to 31)
    3 tm_hour   # Especifica la hora (valor de 0 a 23)
    4 tm_min    # Especifica el minuto (valor de 0 a 59)
    5 tm_sec    # Especifica el segundo (valor de 0 a 61)
    6 tm_wday    # Especifica el día de la semana (valor de 0 a 6)
    7 tm_yday   # Especifica el día del año (valor de 1 a 366)
    8 tm_isdst  # Especifica si se aplica el horario de verano (1: sí, 0: no, -1: no se sabe)
    9 tm_zone   # Especifica el nombre de la zona horaria (valor en forma abreviada)
    10 tm_gmtoff # Especifica el desplazamiento al este del UTC (valor en segundos)
 
'''

import time

timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp))

timestamp1 = 1572879180
st = time.gmtime(timestamp)

print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))
    