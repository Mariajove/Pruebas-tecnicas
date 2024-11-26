"""
Ejercicio 14:
    Escribe una función que calcule y retorne el factorial de un número dado
    de forma recursiva.
"""
numero=int(input('Dime el nuumero'))
factorial = 1
i=1
while (i <= numero):
    factorial = factorial * i
    i = i + 1
print (factorial)
