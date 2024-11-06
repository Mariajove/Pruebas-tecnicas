"""
    Ejercicio 35:
    Dado un array de enteros ordenado y sin repetidos,
    crea una función que calcule y retorne todos los que faltan entre
    el mayor y el menor.
    - Lanza un error si el array de entrada no es correcto.
"""

def rellenar(vector):
    if sorted(vector) != vector or len(vector) != len(set(vector)):
        print("Error, no está ordenado.")

    menor, mayor = vector[0], vector[-1]
    completo = list(range(menor, mayor + 1))
    faltantes = [num for num in completo if num not in vector]
    return faltantes

vector = [2, 3, 5, 8, 9]
print(rellenar(vector)) 
