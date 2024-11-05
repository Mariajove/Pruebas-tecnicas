"""
    Ejercicio 26:
    Crea un programa que calcule quien gana más partidas al piedra,
    papel, tijera.
    - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
    - La función recibe un listado que contiene pares, representando cada jugada.
    - El par puede contener combinaciones de "R" (piedra), "P" (papel)
    o "S" (tijera).
    * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
"""

def piedrapapel(juegos):
    jugador1 = 0
    jugador2 = 0
    
    for juego in juegos:
        if juego == ("R", "S") or juego == ("S", "P") or juego == ("P", "R"):
            jugador1 += 1
        elif juego == ("S", "R") or juego == ("P", "S") or juego == ("R", "P"):
            jugador2 += 1

    if jugador1 > jugador2:
        return "Player 1"
    elif jugador2 > jugador1:
        return "Player 2"
    else:
        return "Tie"

entrada = [("R", "S"), ("S", "R"), ("P", "S")]
print(piedrapapel(entrada))  

