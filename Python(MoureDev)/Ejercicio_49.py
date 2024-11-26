"""
  Ejercicio 49:
    ¿Conoces el calendario de adviento de la comunidad (https://adviento.dev)?
    24 días, 24 regalos sorpresa relacionados con desarrollo de software,
    ciencia y tecnología desde el 1 de diciembre.

    Enunciado: Crea una función que reciba un objeto de tipo "Date" y retorne
    lo siguiente:
    - Si la fecha coincide con el calendario de aDEViento 2022: Retornará el regalo
    de ese día (a tu elección) y cuánto queda para que finalice el sorteo de ese día.
    - Si la fecha es anterior: Cuánto queda para que comience el calendario.
    - Si la fecha es posterior: Cuánto tiempo ha pasado desde que ha finalizado.

    Notas:
    - Tenemos en cuenta que cada día del calendario comienza a medianoche 00:00:00
    y finaliza a las 23:59:59.
    - Debemos trabajar con fechas que tengan año, mes, día, horas, minutos
    y segundos.
"""

from datetime import datetime, timedelta

def calendario(fecha_str):
    regalos_adviento = {
        1: "Introducción a Git y GitHub",
        2: "Desarrollo de aplicaciones móviles",
        3: "Algoritmos de ordenamiento",
        4: "Bases de datos SQL y NoSQL",
        5: "Programación funcional en Python",
        6: "Machine Learning básico",
        7: "Introducción a la ciencia de datos",
        8: "Herramientas de DevOps",
        9: "Análisis de rendimiento en aplicaciones web",
        10: "APIs REST y GraphQL",
        11: "Arquitectura de microservicios",
        12: "Introducción a Blockchain",
        13: "Construcción de interfaces de usuario",
        14: "Automatización de tareas con Python",
        15: "Control de versiones avanzado",
        16: "Testing en desarrollo de software",
        17: "Estructuras de datos en JavaScript",
        18: "Inteligencia artificial aplicada",
        19: "Introducción a la ciberseguridad",
        20: "Desarrollo de videojuegos básicos",
        21: "Introducción a la robótica",
        22: "Uso de contenedores con Docker",
        23: "Redes neuronales y aprendizaje profundo",
        24: "Resumen y recursos avanzados"
    }

    fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
    inicio_calendario = datetime(fecha.year, 12, 1)
    fin_calendario = datetime(fecha.year, 12, 24, 23, 59, 59)
    if fecha < inicio_calendario:
        tiempo_restante = inicio_calendario - fecha
        return f"Faltan {tiempo_restante.days} días para que comience el calendario de adviento."
    elif inicio_calendario <= fecha <= fin_calendario:
        dia = fecha.day
        regalo = regalos_adviento.get(dia, "No hay regalo definido para este día.")
        fin_dia = datetime(fecha.year, 12, dia, 23, 59, 59)
        tiempo_para_fin_dia = fin_dia - fecha
        return f"Regalo del día {dia}: {regalo}. Tiempo para el final del día: {tiempo_para_fin_dia}."
    else:
        tiempo_desde_final = fecha - fin_calendario
        return f"Han pasado {tiempo_desde_final.days} días desde que finalizó el calendario de adviento."

# Ejemplo 
print(calendario("11/12/2024"))  
