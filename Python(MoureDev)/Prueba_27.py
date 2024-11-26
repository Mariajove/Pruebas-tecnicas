"""
    Ejercicio 27:
    Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
    - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
    - EXTRA: ¿Eres capaz de dibujar más figuras?
"""

def dibujar_cuadrado(tamano):
    for i in range(tamano):
        print('*' * tamano)

def dibujar_triangulo(tamano):
    for i in range(1, tamano + 1):
        print('*' * i)

def dibujar_rectangulo(base, altura):
    for i in range(altura):
        print('*' * base)

def dibujar_rombo(tamano):
    # Parte superior
    for i in range(tamano):
        print(' ' * (tamano - i - 1) + '*' * (2 * i + 1))
    # Parte inferior
    for i in range(tamano - 2, -1, -1):
        print(' ' * (tamano - i - 1) + '*' * (2 * i + 1))

def dibujar_figura(figura, tamano, altura=None):
    if figura == "cuadrado":
        dibujar_cuadrado(tamano)
    elif figura == "triangulo":
        dibujar_triangulo(tamano)
    elif figura == "rectangulo":
        if altura is None:
            print("Por favor, proporciona la altura del rectángulo.")
        else:
            dibujar_rectangulo(tamano, altura)
    elif figura == "rombo":
        dibujar_rombo(tamano)
    else:
        print("Figura no reconocida. Por favor, elige 'cuadrado', 'triangulo', 'rectangulo' o 'rombo'.")

figura = input("¿Qué figura deseas dibujar (cuadrado, triangulo, rectangulo, rombo)? ").strip().lower()
tamano = int(input("Introduce el tamaño del lado (o base para el rectángulo): "))

if figura == "rectangulo":
    altura = int(input("Introduce la altura del rectángulo: "))
    dibujar_figura(figura, tamano, altura)
else:
    dibujar_figura(figura, tamano)
