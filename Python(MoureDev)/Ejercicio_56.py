"""
  Ejercicio 56:
    Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
    Podrás configurar generar contraseñas con los siguientes parámetros:
    - Longitud: Entre 8 y 16.
    - Con o sin letras mayúsculas.
    - Con o sin números.
    - Con o sin símbolos.
    (Pudiendo combinar todos estos parámetros entre ellos)
"""

import random
import string

def generar_contrasena(longitud=12, mayusculas=True, numeros=True, simbolos=True):

    if longitud < 8 or longitud > 16:
        raise ValueError("La longitud debe estar entre 8 y 16 caracteres.")
    caracteres = list(string.ascii_lowercase)
    caracteres.extend(string.ascii_uppercase)
    if numeros:
        caracteres.extend(string.digits)
    if simbolos:
        caracteres.extend(string.punctuation)
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    return contrasena

print(generar_contrasena(longitud=12, mayusculas=True, numeros=True, simbolos=True))
