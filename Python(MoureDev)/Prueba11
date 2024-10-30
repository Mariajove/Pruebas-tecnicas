"""
Ejercicio 11:
    Crea un programa que comprueba si los paréntesis, llaves y corchetes
    de una expresión están equilibrados.
    - Equilibrado significa que estos delimitadores se abren y cieran
    en orden y de forma correcta.
    - Paréntesis, llaves y corchetes son igual de prioritarios.
    No hay uno más importante que otro.
    - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
    - Expresión no balanceada: { a * ( c + d ) ] - 5 }
"""

expresion = '{ [a * ( c + d ) ] - 5 }'
pares = {'(': ')', '[': ']', '{': '}'} #Se define el diccionario donde observaremos donde 
validacion = []

for char in expresion:
    if char in '([{':  # Si es un delimitador de apertura
        validacion.append(char)  # Lo agregamos a la pila
    elif char in ')]}':  # Si es un delimitador de cierre
        if not validacion or pares[validacion[-1]] != char:
            # Si no coincide o la pila está vacía, no está balanceada
            print('No está equilibrada')
            break
        validacion.pop()  # Sacamos el último delimitador de la pila si coincide

# Verificar si la pila está vacía al final
else:  # El else del for se ejecuta si no hubo ningún break
    if len(validacion) == 0:
        print('Está equilibrada')
    else:
        print('No está equilibrada')

