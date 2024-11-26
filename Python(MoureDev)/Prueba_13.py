"""
Ejercicio 13:
    Escribe una función que reciba un texto y retorne verdadero o
    falso (Boolean) según sean o no palíndromos.
    Un Palíndromo es una palabra o expresión que es igual si se lee
    de izquierda a derecha que de derecha a izquierda.
    NO se tienen en cuenta los espacios, signos de puntuación y tildes.
    Ejemplo: Ana lleva al oso la avellana.
"""

palabra=input('Dime la palabra').lower()

def espalindroma(palabra):
    if palabra==palabra[::-1]:
        return True
    else:
        return False

print(espalindroma(palabra))
