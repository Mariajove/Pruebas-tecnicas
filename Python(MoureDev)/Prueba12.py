"""
Ejercicio 12:
    Crea una función que reciba dos cadenas como parámetro (str1, str2)
    e imprima otras dos cadenas como salida (out1, out2).
    - out1 contendrá todos los caracteres presentes en la str1 pero NO
    estén presentes en str2.
    - out2 contendrá todos los caracteres presentes en la str2 pero NO
    estén presentes en str1.
"""
import string

# Palabras de entrada
frase1 = input('Dime la primera cadena: ').lower()
frase2 = input('Dime la segunda cadena: ').lower()
#Se quitan los signos de puntuacion
signos = string.punctuation + "¿¡"
frase1 = frase1.translate(str.maketrans('', '', signos))
frase2 = frase2.translate(str.maketrans('', '', signos))
#Se separan las palabras de la frase
palabras1 = frase1.split()
palabras2 = frase2.split()

# Listas para palabras que no se repiten
norepe1 = []
norepe2 = []
# Encontrar palabras no repetidas en frase1 y frase2
for palabra1 in palabras1:
    if palabra1 not in palabras2 and palabra1 not in norepe1:
        norepe1.append(palabra1)
for palabra2 in palabras2:
    if palabra2 not in palabras1 and palabra2 not in norepe2:
        norepe2.append(palabra2)

# Imprimir resultados
print("Palabras en la primera frase que no están en la segunda:", norepe1)
print("Palabras en la segunda frase que no están en la primera:", norepe2)
