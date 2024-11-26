"""
    Ejercicio 39:
    Crea un programa se encargue de transformar un número binario
    a decimal sin utilizar funciones propias del lenguaje que
    lo hagan directamente.
"""

def binario_a_decimal(binario):
    decimal = 0
    longitud = len(binario)
    for i in range(longitud):
        bit = binario[i]
        decimal += bit * (2 ** (longitud - 1 - i))
    return decimal

entrada = input("Dime el número binario que quieres convertir a decimal: ")
binario = [int(digito) for digito in entrada]
decimal = binario_a_decimal(binario)

print(f"El número binario {entrada} es igual a {decimal} en decimal.")

