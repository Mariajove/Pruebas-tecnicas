"""
    Ejercicio 33:
    Dado un listado de números, encuentra el SEGUNDO más grande
"""

numeros = [2, 3, 4, 5, 6, 7, 8, 9]

mayor = segundo = -10000
for i in numeros:
    if i > mayor:
        segundo = mayor 
        mayor = i             
    elif i > segundo and i < mayor:
        segundo = i

print("El segundo número más grande es:", segundo)
