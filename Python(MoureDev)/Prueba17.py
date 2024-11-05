"""
Ejercicio 17:
    Crea una función que reciba un String de cualquier tipo y se encargue de
    poner en mayúscula la primera letra de cada palabra.
    - No se pueden utilizar operaciones del lenguaje que
    lo resuelvan directamente.
"""

def capitalizar_palabras(frase):
    resultado = ""
    en_espacio = True 

    for char in frase:
        if en_espacio and char.isalpha():  
            resultado += char.upper() 
            en_espacio = False 
        else:
            resultado += char  
            if char == ' ': 
                en_espacio = True

    return resultado

frase = input('Dime una frase: ')
resultado = capitalizar_palabras(frase)
print(resultado)
