"""
  Ejercicio 48:
    Crea un función que reciba un texto y retorne la vocal que
    más veces se repita.
    - Ten cuidado con algunos casos especiales.
    - Si no hay vocales podrá devolver vacío.
"""

def vocal_mas_repetida(texto):
    vocales = "aeiou"
    conteo = {vocal: 0 for vocal in vocales} 
    for letra in texto.lower(): 
        if letra in conteo:
            conteo[letra] += 1
    mas_vocal = max(conteo, key=conteo.get)
    
    return mas_vocal if conteo[mas_vocal] > 0 else ""


print(vocal_mas_repetida("Hola, esto es una prueba")) 
