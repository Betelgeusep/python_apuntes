''' 
 Esta declaración toma como entrada una condición booleana,
 que cuando devuelve verdadero no hace nada y continúa el 
 flujo normal de ejecución, pero si se calcula que es falso, genera un 
 AssertionError junto con el mensaje opcional provisto. 


# inicializar variables
a = 4
b = 0
 
# usando assert 
print("The value of a / b is : ")
assert b != 0,"Zero Division Error"
print(a / b)'''


'''
La declaración de afirmación se usa dentro de una función en este ejemplo 
para verificar que la longitud y el ancho de un rectángulo sean positivos 
antes de calcular su área. La aserción genera un AssertionError con el mensaje 
"La longitud y el ancho deben ser positivos" si es falso. 
Si la afirmación es verdadera, la función devuelve el área del rectángulo; 
si es falso, sale con un error. Para mostrar cómo utilizar la afirmación en varias situaciones, 
la función se llama dos veces, una vez con entradas positivas y otra vez con entradas negativas.
'''

# Funcion para calcular el area de un triangulo
def calculate_rectangle_area(length, width):
    # Assertion para verificar la longitud y el ancho sean positivos 
    assert length > 0 and width > 0, "Length y width"+ \
                " deberian ser positivos"
    # Calcular el area
    area = length * width
    return area
 
 
# llamado a la funcion positivos 
area1 = calculate_rectangle_area(5, 6)
print("el Area del rectangulo con altura 5 y ancho 6: ", area1)
 
# llamado a la funcion positivos 
area2 = calculate_rectangle_area(-5, 6)
print("el Area del rectangulo con altura -5 y ancho 6: ", area2)