"""
  Ejercicio 57:
    Escribe un programa que, dado un número, compruebe y muestre si es primo,
    fibonacci y par.
    Ejemplos:
    - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
    - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""

import math

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def es_fibonacci(n):
    # Un número es de Fibonacci si y solo si 5*n^2 + 4 o 5*n^2 - 4 es un cuadrado perfecto
    return (math.isqrt(5 * n * n + 4) ** 2 == 5 * n * n + 4) or (math.isqrt(5 * n * n - 4) ** 2 == 5 * n * n - 4)

def es_par(n):
    return n % 2 == 0

def analizar_numero(n):
    resultado = f"{n} "
    resultado += "es primo, " if es_primo(n) else "no es primo, "
    resultado += "es fibonacci, " if es_fibonacci(n) else "no es fibonacci, "
    resultado += "es par" if es_par(n) else "es impar"
    return resultado

# Ejemplos de uso
print(analizar_numero(2))  # Salida: 2 es primo, es fibonacci y es par
print(analizar_numero(7))  # Salida: 7 es primo, no es fibonacci y es impar
