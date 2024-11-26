"""
  Ejercicio 54:
    Escribe un programa que reciba un texto y transforme lenguaje natural a
    "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
    se caracteriza por sustituir caracteres alfanuméricos.
    - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet)
    con el alfabeto y los números en "leet".
    (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""

def texto_a_leet(texto):
    leet_dict = {
        'a': '4', 'b': '8', 'c': '(', 'd': '[)', 'e': '3', 'f': '|=', 'g': '6', 
        'h': '#', 'i': '1', 'j': '_|', 'k': '|<', 'l': '1', 'm': r'|\/|', 
        'n': r'|\|', 'o': '0', 'p': '|*', 'q': '0_', 'r': '2', 's': '5', 
        't': '7', 'u': '(_)', 'v': r'\/', 'w': r'\/\/', 'x': '><', 'y': '`/', 'z': '2',
        '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', 
        '6': '6', '7': '7', '8': '8', '9': '9'
    }
    
    texto_leet = "".join(leet_dict.get(char.lower(), char) for char in texto)
    
    return texto_leet

#Ejemplo
texto = "¡Hola, este es un mensaje en leet!"
leet_texto = texto_a_leet(texto)
print(leet_texto) 
