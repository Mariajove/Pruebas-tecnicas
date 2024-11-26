"""
  Ejercicio 44:
    Este es un reto especial por Halloween.
    Deberemos crear un programa al que le indiquemos si queremos realizar "Truco
    o Trato" y un listado (array) de personas con las siguientes propiedades:
    - Nombre de la niña o niño
    - Edad
    - Altura en centímetros

    Si las personas han pedido truco, el programa retornará sustos (aleatorios)
    siguiendo estos criterios:
    - Un susto por cada 2 letras del nombre por persona
    - Dos sustos por cada edad que sea un número par
    - Tres sustos por cada 100 cm de altura entre todas las personas
    - Sustos: 🎃 👻 💀 🕷 🕸 🦇

    Si las personas han pedido trato, el programa retornará dulces (aleatorios)
    siguiendo estos criterios:
    - Un dulce por cada letra de nombre
    - Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
    - Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
    - Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩
    - En caso contrario retornará un error.
"""

import random

def trucotrato(opcion, array):
    if opcion == "Truco":
        emotruco = ["🎃", "👻", "💀", "🕷", "🕸", "🦇"]
        totalletras = sum(len(fila["nombre"]) for fila in array) // 2
        emote1 = random.choices(emotruco, k=totalletras)
        
        totaledad = 0
        for fila in array:
            if fila["edad"] % 2 == 0:
                totaledad += 2
        emote2 = random.choices(emotruco, k=totaledad)
        
        totalalturas = sum(fila["altura"] // 100 for fila in array)
        emote3 = random.choices(emotruco, k=totalalturas)
        
        trucofinal = emote1 + emote2 + emote3
        return trucofinal

    elif opcion == "Trato":
        emotetrato = ["🍰", "🍬", "🍡", "🍭", "🍪", "🍫", "🧁", "🍩"]
        totalletras = sum(len(fila["nombre"]) for fila in array)
        emote1 = random.choices(emotetrato, k=totalletras)
        
        totaledad = 0
        for fila in array:
            if fila["edad"] >= 10:
                totaledad += 3
            else:
                totaledad += fila["edad"] // 3
        emote2 = random.choices(emotetrato, k=totaledad)
        
        totalalturas = 0
        for fila in array:
            totalalturas += min(fila["altura"] // 50, 3)
        emote3 = random.choices(emotetrato, k=totalalturas)
        
        tratofinal = emote1 + emote2 + emote3
        return tratofinal

    else:
        return "Error, no se ha puesto ni truco ni trato"


#Ejemplo
opcion = "Trato"
array = [
    {"nombre": "Pedro", "edad": 10, "altura": 160},
    {"nombre": "Juan", "edad": 8, "altura": 135},
    {"nombre": "Carlos", "edad": 6, "altura": 110}
]

print(trucotrato(opcion, array))
