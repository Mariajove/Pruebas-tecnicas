"""
    Ejercicio 36:
    Crea un programa que calcule el daño de un ataque durante
    una batalla Pokémon.
    - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
    - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
    - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
    (buscar su efectividad)
    - El programa recibe los siguientes parámetros:
    - Tipo del Pokémon atacante.
    - Tipo del Pokémon defensor.
    - Ataque: Entre 1 y 100.
    - Defensa: Entre 1 y 100.
"""

def calcular_danio(tipo_atacante, tipo_defensor, ataque, defensa):
    efectividades = {
        "Agua": {"Fuego": 2, "Agua": 1, "Planta": 0.5, "Eléctrico": 1},
        "Fuego": {"Planta": 2, "Agua": 0.5, "Fuego": 1, "Eléctrico": 1},
        "Planta": {"Agua": 2, "Fuego": 0.5, "Planta": 1, "Eléctrico": 1},
        "Eléctrico": {"Agua": 2, "Planta": 1, "Fuego": 1, "Eléctrico": 0.5},
    }
    if tipo_atacante not in efectividades or tipo_defensor not in efectividades[tipo_atacante]:
        raise ValueError("Tipo de Pokémon no válido.")
    if not (1 <= ataque <= 100) or not (1 <= defensa <= 100):
        raise ValueError("El ataque y la defensa deben estar entre 1 y 100.")

    efectividad = efectividades[tipo_atacante][tipo_defensor]

    danio = 50 * (ataque / defensa) * efectividad
    return danio

tipoat=input("Tipo del Pokémon atacante.")
tipodef=input("Tipo del Pokémon defensor.")
ataque=int(input("Ataque del Pokémon atacante."))
defensa=int(input("Defensa del Pokémon defensor."))

print(f"El daño es: {calcular_danio(tipoat, tipodef, ataque, defensa)}")

