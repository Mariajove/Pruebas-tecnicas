"""
    Ejercicio 38:
    ¡Han anunciado un nuevo "The Legend of Zelda"!
    Se llamará "Tears of the Kingdom" y se lanzará el 12 de mayo de 2023.
    Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos
    "The Legend of Zelda" de la historia?
    Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda
    que tú selecciones.
    - Debes buscar cada uno de los títulos y su día de lanzamiento 
    (si no encuentras el día exacto puedes usar el mes, o incluso inventártelo)
"""

from datetime import datetime

def calcular_diferencia(fecha1, fecha2):
    fecha1 = datetime.strptime(fecha1, "%d-%m-%Y")
    fecha2 = datetime.strptime(fecha2, "%d-%m-%Y")

    if fecha1 > fecha2:
        fecha1, fecha2 = fecha2, fecha1

    diferencia = fecha2 - fecha1
    años = diferencia.days // 365
    días = diferencia.days % 365
    
    return años, días

fecha_zelda_1986 = "21-02-1986"
fecha_zelda_1998 = "21-11-1998"

años, días = calcular_diferencia(fecha_zelda_1986, fecha_zelda_1998)
print(f"Entre 'The Legend of Zelda' (1986) y 'Ocarina of Time' (1998) han pasado {años} años y {días} días.")
