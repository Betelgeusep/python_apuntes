#El método today devuelve un objeto del tipo date que representa la fecha local actual.
from datetime import date, datetime,time

today = date.today()

print("Hoy:", today)
print("Año:", today.year)
print("Mes:", today.month)
print("Día:", today.day)

# crear un objeto date
my_date = date(2019, 11, 4)
print(my_date)


#La clase date nos da la capacidad de crear un objeto del tipo fecha a partir de una marca de tiempo.
import time

timestamp = time.time()
print("Marca de tiempo:", timestamp)

d = date.fromtimestamp(timestamp)
print("Fecha:", d)

#el método fromisoformat, que toma una fecha en el formato AAAA-MM-DD compatible con el estándar ISO 8601

todays_Date = datetime.now()
 
date_in_ISOFormat = todays_Date.isoformat()
 
# Printing Today's date in ISO format
print("Today's date in ISO Format: " , date_in_ISOFormat)


#El método replace()
d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)

#weekday. Devuelve el día de la semana como un número entero, donde 0 es el lunes y 6 es el domingo.
d = date(2023, 7, 19)
print(d.weekday())
    

#isoweekday, que también devuelve el día de la semana como un número entero, pero 1 es lunes y 7 es domingo:

d = date(2023, 7, 19)
print(d.isoweekday())


    
