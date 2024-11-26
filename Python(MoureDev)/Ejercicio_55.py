"""
  Ejercicio 55:
    Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
    El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
    gane cada punto del juego.

    - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
    - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
    15 - Love
    30 - Love
    30 - 15
    30 - 30
    40 - 30
    Deuce
    Ventaja P1
    Ha ganado el P1
    - Si quieres, puedes controlar errores en la entrada de datos.
    - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
"""


def juego_tenis(partida):
    puntajes = {0: "Love", 1: "15", 2: "30", 3: "40"}
    puntos_p1 = 0
    puntos_p2 = 0
    ventaja = None  # Indica si un jugador tiene ventaja

    for i in partida:
        if i == "P1":
            puntos_p1 += 1
        elif i == "P2":
            puntos_p2 += 1
        else:
            print("Entrada inválida.")
            continue

        if puntos_p1 >= 3 and puntos_p2 >= 3:
            if puntos_p1 == puntos_p2:
                print("Deuce")
                ventaja = None
            elif puntos_p1 == puntos_p2 + 1:
                print("Ventaja P1")
                ventaja = "P1"
            elif puntos_p2 == puntos_p1 + 1:
                print("Ventaja P2")
                ventaja = "P2"
            elif puntos_p1 >= puntos_p2 + 2:
                print("Ha ganado P1")
                return
            elif puntos_p2 >= puntos_p1 + 2:
                print("Ha ganado P2")
                return
        else:
            marcador_p1 = puntajes.get(puntos_p1, "40")
            marcador_p2 = puntajes.get(puntos_p2, "40")
            print(f"{marcador_p1} - {marcador_p2}")

        if puntos_p1 == 4 and puntos_p2 < 3:
            print("Ha ganado P1")
            return
        elif puntos_p2 == 4 and puntos_p1 < 3:
            print("Ha ganado P2")
            return

partida = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
juego_tenis(partida)
