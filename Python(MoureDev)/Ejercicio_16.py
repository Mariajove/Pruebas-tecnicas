"""
Ejercicio 16:
    Crea una función que calcule y retorne cuántos días hay entre dos cadenas
    de texto que representen fechas.
    - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
    - La función recibirá dos String y retornará un Int.
    - La diferencia en días será absoluta (no importa el orden de las fechas).
    - Si una de las dos cadenas de texto no representa una fecha correcta se
    lanzará una excepción.
"""

#La librería datetime está muy bien para cosas de fechas
from datetime import datetime

fecha_inicio= input('Introduce la fecha de inicio (dd/mm/aaaa): ')
fecha_fin= input('Introduce la fecha de fin (dd/mm/aaaa): ')
fecha_inicio = datetime.strptime(fecha_inicio, '%d/%m/%Y')
fecha_fin = datetime.strptime(fecha_fin, '%d/%m/%Y')

diferencia = fecha_fin - fecha_inicio
valor=diferencia.days

print(f'{valor} días')
