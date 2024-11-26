""""
Ejercicio 2:
    Escribe una función que reciba dos palabras (String) y retorne
    verdadero o falso (Bool) según sean o no anagramas.
    - Un Anagrama consiste en formar una palabra reordenando TODAS
    las letras de otra palabra inicial.
    - NO hace falta comprobar que ambas palabras existan.
    - Dos palabras exactamente iguales no son anagrama.
"""

import numpy as np
a=input("Dime una palabra") #Como no se indica que sea int, input ya guarda como una cadena
b=input("Dime otra palabra")

if sorted(a)==sorted(b) and a!=b: #Sorted pilla una palabra y ordena las letras en un vector
    print(True)
if a==b:
    print(False)
else:
    print(False)

