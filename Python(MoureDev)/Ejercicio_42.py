"""
  Ejercicio 42:
    Crea una función que calcule el valor del parámetro perdido
    correspondiente a la ley de Ohm.
    - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará
    el valor del tercero (redondeado a 2 decimales).
    - Si los parámetros son incorrectos o insuficientes, la función retornará
    la cadena de texto "Invalid values".
"""

def ohm(V=None, R=None, I=None):
    params = [V, R, I]
    num_params = sum(param is not None for param in params)
    if num_params != 2:
        return "Invalid values"

    if V is None:
        return round(I * R, 2)
    elif I is None:
        return round(V / R, 2)
    elif R is None:
        return round(V / I, 2)

#Ejemplos de funcionamiento correcto
print(ohm(V=4, R=2)) 
print(ohm(V=4, I=2))  
print(ohm(R=2, I=2))  
#Ejemplos de retorno "Invalid values"
print(ohm(4)) 
print(ohm(V=4, R=2, I=2))  
