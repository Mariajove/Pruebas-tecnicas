"""
    Ejercicio 37:
    ¡La Tierra Media está en guerra! En ella lucharán razas leales
    a Sauron contra otras bondadosas que no quieren que el mal reine
    sobre sus tierras.
    Cada raza tiene asociado un "valor" entre 1 y 5:
    - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3),
    Númenóreanos (4), Elfos (5)
    - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2),
    Huargos (3), Trolls (5)
    Crea un programa que calcule el resultado de la batalla entre
    los 2 tipos de ejércitos:
    - El resultado puede ser que gane el bien, el mal, o exista un empate.
    Dependiendo de la suma del valor del ejército y el número de integrantes.
    - Cada ejército puede estar compuesto por un número de integrantes variable
    de cada raza.
    - Tienes total libertad para modelar los datos del ejercicio.
    Ej: 1 Peloso pierde contra 1 Orco
    2 Pelosos empatan contra 1 Orco
    3 Pelosos ganan a 1 Orco
"""

def calcular_fuerza(ejercito):
    razas = {
        "Peloso": 1,
        "Sureños buenos": 2,
        "Enanos": 3,
        "Númenóreanos": 4,
        "Elfos": 5,
        "Sureños malos": 2,
        "Orcos": 2,
        "Goblins": 2,
        "Huargos": 3,
        "Trolls": 5
    }
    fuerza_total = 0

    for raza, integrantes in ejercito.items():
        if raza in razas:
            fuerza_total += razas[raza] * integrantes
        else:
            raise ValueError(f"La raza {raza} no es válida.")
    
    return fuerza_total

def batalla(bien, mal):
    fuerza_bien = calcular_fuerza(bien)
    fuerza_mal = calcular_fuerza(mal)
    
    if fuerza_bien > fuerza_mal:
        return "¡El bien gana!"
    elif fuerza_bien < fuerza_mal:
        return "¡El mal gana!"
    else:
        return "¡Empate!"

# Ejemplo de uso
ejercito_bien = {
    "Peloso": 3,
    "Enanos": 2,
    "Elfos": 1
}

ejercito_mal = {
    "Orcos": 4,
    "Trolls": 1
}

print(batalla(ejercito_bien, ejercito_mal)) 
