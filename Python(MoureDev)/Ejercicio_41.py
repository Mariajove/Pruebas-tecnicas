"""
  Ejercicio 41:
    Crea una función que sea capaz de dibujar el "Triángulo de Pascal"
    indicándole únicamente el tamaño del lado.

    - Aquí puedes ver rápidamente cómo se calcula el triángulo:
    https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif
"""

def generar_triangulo_pascal(n):
    triangulo = [[1]]
    for i in range(1, n):
        fila = [1]
        for j in range(1, i):
            fila.append(triangulo[i - 1][j - 1] + triangulo[i - 1][j])
        fila.append(1)
        triangulo.append(fila)
    return triangulo
n = 10
triangulo_pascal = generar_triangulo_pascal(n)

# Imprimir el triángulo
for fila in triangulo_pascal:
    print(fila)
