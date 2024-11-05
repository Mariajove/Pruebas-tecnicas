"""
    Ejercicio 24:
    Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
    que calcule el mínimo común múltiplo (mcm) de dos números enteros.
    - No se pueden utilizar operaciones del lenguaje que
    lo resuelvan directamente.
"""
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mcm(numero1, numero2):
    return abs(numero1 * numero2) // mcd(numero1, numero2)

print(mcm(12, 21)) 
print(mcd(12,21))
