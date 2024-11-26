"""
    Ejercicio 31:
    Crea una función que reciba un texto y muestre cada palabra en una línea,
    formando un marco rectangular de asteriscos.
    - ¿Qué te parece el reto? Se vería así:
    **********
    * ¿Qué   *
    * te     *
    * parece *
    * el     *
    * reto?  *
    **********
"""

def mostrar_marco(frase):
    palabras = frase.split()  
    longitud_max = max(len(palabra) for palabra in palabras) 
    print('*' * (longitud_max + 4))

    for palabra in palabras:
        print(f"* {palabra.ljust(longitud_max)} *")

    print('*' * (longitud_max + 4))

frase = input("Dime la frase: ")
mostrar_marco(frase)
