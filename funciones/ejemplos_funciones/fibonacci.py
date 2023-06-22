"""
    Son una secuencia de números enteros los cuales siguen una regla sencilla:

el primer elemento de la secuencia es igual a uno (Fib1 = 1)
el segundo elemento también es igual a uno (Fib2 = 1)
cada número después de ellos son la suman de los dos números anteriores (Fibi = Fibi-1 + Fibi-2)
Aquí están algunos de los primeros números en la serie Fibonacci:

fib_1 = 1 fib_2 = 1 fib_3 = 1 + 1 = 2 fib_4 = 1 + 2 = 3 fib_5 = 2 + 3 = 5 fib_6 = 3 + 5 = 8 fib_7 = 5 + 8 = 13
    """
    
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):  # probando
    print(n, "->", fib(n))

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)