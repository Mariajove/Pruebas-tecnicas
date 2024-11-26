"""
  Ejercicio 46:
    Dado un array de números enteros positivos, donde cada uno
    representa unidades de bloques apilados, debemos calcular cuantas unidades
    de agua quedarán atrapadas entre ellos.

    - Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].

                ⏹
                ⏹
        ⏹💧💧⏹
        ⏹💧⏹⏹💧⏹
        ⏹💧⏹⏹💧⏹
        ⏹💧⏹⏹⏹⏹

    Representando bloque con ⏹︎ y agua con 💧, quedarán atrapadas 7 unidades
    de agua. Suponemos que existe un suelo impermeable en la parte inferior
    que retiene el agua.
"""

def agua(array):
    if not array:
        return 0
    n = len(array)
    left_max = [0] * n  
    right_max = [0] * n 
    water = 0
    left_max[0] = array[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], array[i])
    right_max[n-1] = array[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], array[i])
    for i in range(n):
        water += max(0, min(left_max[i], right_max[i]) - array[i])
    return water

# Ejemplo
array = [4, 0, 3, 6, 1, 3]
print(agua(array))
