"""
Ejercicio 20:
    Crea una función que reciba días, horas, minutos y segundos (como enteros)
    y retorne su resultado en milisegundos.
"""

dias=int(input('Dime los dias'))
horas=int(input('Dime las horas'))
minutos=int(input('Dime los minutos'))
segundos=int(input('Dime los segundos'))

milisegundos=1000*(segundos+minutos*60+horas*3600+dias*86400)

print('En milisegundos es', milisegundos)
