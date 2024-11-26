"""
Ejercicio 19:
REVISAR
    Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
    y retorne lo siguiente:
    - "X" si han ganado las "X"
    - "O" si han ganado los "O"
    - "Empate" si ha habido un empate
    - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
    O si han ganado los 2.
    Nota: La matriz puede no estar totalmente cubierta.
    Se podría representar con un vacío "", por ejemplo.
"""

import numpy as np

def gana(matriz):
    x_count = np.count_nonzero(matriz == 'X')
    o_count = np.count_nonzero(matriz == 'O')
    total_count = x_count + o_count
    
    if total_count > 9 or x_count > 5 or o_count > 5 or (x_count + o_count < 3 and total_count < 3):
        return "Nulo"

    for i in range(3):
        if np.all(matriz[i, :] == 'X'):
            return "X" 
        if np.all(matriz[i, :] == 'O'):
            return "O" 
        if np.all(matriz[:, i] == 'X'):
            return "X"  
        if np.all(matriz[:, i] == 'O'):
            return "O" 

    if np.all(np.diag(matriz) == 'X') or np.all(np.diag(np.fliplr(matriz)) == 'X'):
        return "X"  
    if np.all(np.diag(matriz) == 'O') or np.all(np.diag(np.fliplr(matriz)) == 'O'):
        return "O" 

    if total_count == 9:
        return "Empate"
    return "Nulo"

matriz = np.array([
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    [' ', ' ', 'X']
])

resultado = gana(matriz)
print(f'Resultado del juego: {resultado}')
