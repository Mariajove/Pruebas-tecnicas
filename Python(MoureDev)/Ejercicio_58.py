"""
  Ejercicio 58:
    Crea un programa que calcule quien gana más partidas al piedra,
    papel, tijera, lagarto, spock.
    - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
    - La función recibe un listado que contiene pares, representando cada jugada.
    - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
    "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
    - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
    - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
"""

def calcular_ganador(juegos):
    # Definimos las reglas de victoria
    reglas = {
        "🗿": ["✂️", "🦎"],   # Piedra vence a tijera y lagarto
        "📄": ["🗿", "🖖"],   # Papel vence a piedra y Spock
        "✂️": ["📄", "🦎"],   # Tijera vence a papel y lagarto
        "🦎": ["📄", "🖖"],   # Lagarto vence a papel y Spock
        "🖖": ["🗿", "✂️"],   # Spock vence a piedra y tijera
    }

    jugador1 = 0
    jugador2 = 0

    for juego in juegos:
        j1, j2 = juego  # Separar las jugadas de cada jugador
        if j2 in reglas[j1]:  # Jugador 1 gana si la jugada de Jugador 2 está en la lista de vencidos por Jugador 1
            jugador1 += 1
        elif j1 in reglas[j2]:  # Jugador 2 gana si la jugada de Jugador 1 está en la lista de vencidos por Jugador 2
            jugador2 += 1

    # Determinar el resultado final
    if jugador1 > jugador2:
        return "Player 1"
    elif jugador2 > jugador1:
        return "Player 2"
    else:
        return "Tie"

# Ejemplo de uso
entrada = [("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️")]
print(calcular_ganador(entrada))  # Salida esperada: "Player 2"
