"""
  Ejercicio 60:
    Crea un programa que simule el comportamiento del sombrero selccionador del
    universo mágico de Harry Potter.
    - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
    - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
    - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
    coloque al alumno en una de las 4 casas de Hogwarts:
    (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
    - Ten en cuenta los rasgos de cada casa para hacer las preguntas
    y crear el algoritmo seleccionador:
    Por ejemplo, en Slytherin se premia la ambición y la astucia.
"""

preguntas_y_casas = {
    1: {
        1: "Hufflepuff",
        2: "Ravenclaw",
        3: "Gryffindor",
        4: "Slytherin"
    },
    2: {
        1: "Hufflepuff",
        2: "Ravenclaw",
        3: "Gryffindor",
        4: "Slytherin"
    },
    3: {
        1: "Hufflepuff",
        2: "Ravenclaw",
        3: "Gryffindor",
        4: "Slytherin"
    },
    4: {
        1: "Hufflepuff",
        2: "Ravenclaw",
        3: "Gryffindor",
        4: "Slytherin"
    },
    5: {
        1: "Hufflepuff",
        2: "Ravenclaw",
        3: "Gryffindor",
        4: "Slytherin"
    }
}

preguntas = [
    "¿Qué valoras más en una amistad?\n1. Lealtad\n2. Inteligencia\n3. Valentía\n4. Ambición",
    "¿Qué preferirías hacer en tu tiempo libre?\n1. Ayudar a un amigo en apuros\n2. Resolver un acertijo complicado\n3. Explorar un lugar misterioso\n4. Planear cómo lograr tus metas personales",
    "¿Qué cualidad consideras más importante en un líder?\n1. Justicia\n2. Sabiduría\n3. Coraje\n4. Persuasión",
    "¿Qué camino tomarías si te pierdes en el bosque?\n1. El que parezca más seguro y claro\n2. El que tenga símbolos o pistas interesantes\n3. El más oscuro y desafiante\n4. El que probablemente lleve a algo valioso",
    "¿Qué animal te representa mejor?\n1. Tejón\n2. Águila\n3. León\n4. Serpiente"
]

puntos_casas = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}

print("¡Bienvenido al Sombrero Seleccionador de Hogwarts!\nResponde las siguientes preguntas:")
for i, pregunta in enumerate(preguntas, start=1):
    print(f"\nPregunta {i}:")
    print(pregunta)
    while True:
        try:
            respuesta = int(input("Selecciona una opción (1-4): "))
            if respuesta in [1, 2, 3, 4]:
                casa = preguntas_y_casas[i][respuesta]
                puntos_casas[casa] += 1
                break
            else:
                print("Por favor, selecciona una opción válida (1-4).")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número del 1 al 4.")

casa_asignada = max(puntos_casas, key=puntos_casas.get)

print("\n¡Gracias por responder! Según tus respuestas, el Sombrero Seleccionador te ha asignado a:")
print(f"🏠 {casa_asignada} 🏠")
