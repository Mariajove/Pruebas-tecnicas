"""
  Ejercicio 45:
    Crea una función que retorne el número total de bumeranes de
    un array de números enteros e imprima cada uno de ellos.
    - Un bumerán (búmeran, boomerang) es una secuencia formada por 3 números
    seguidos, en el que el primero y el último son iguales, y el segundo
    es diferente. Por ejemplo [2, 1, 2].
    - En el array [2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes ([2, 1, 2]
    y [4, 2, 4]).
"""

def bumeranes(vector):
    bumeran=[]
    for i in range(1, len(vector) - 1):
        if vector[i-1]==vector[i+1] and vector[i]!=vector[i+1]:
            bumeran.append([vector[i - 1], vector[i], vector[i + 1]])
    return bumeran

#Ejemplo
vec=[2, 1, 2, 3, 3, 4, 2, 4]
print(bumeranes(vec))
