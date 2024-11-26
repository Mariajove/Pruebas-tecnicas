"""
    Ejercicio 30:
    Crea una función que ordene y retorne una matriz de números.
    - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
    adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
    o de mayor a menor.
    - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
    automáticamente.
"""

def ordenar_matriz(lista, orden):
    if orden not in ["Asc", "Desc"]:
        return "El parámetro de orden debe ser 'Asc' o 'Desc'."
    matriz_ordenada = lista.copy()
    n = len(matriz_ordenada)
    for i in range(n):
        for j in range(0, n-i-1):
            if (orden == "Asc" and matriz_ordenada[j] > matriz_ordenada[j+1]) or (orden == "Desc" and matriz_ordenada[j] < matriz_ordenada[j+1]):
                matriz_ordenada[j], matriz_ordenada[j+1] = matriz_ordenada[j+1], matriz_ordenada[j]
    return matriz_ordenada

numeros = [2, 4, 6, 8, 9]
print("Original:", numeros)
print("Orden Ascendente:", ordenar_matriz(numeros, "Asc"))
print("Orden Descendente:", ordenar_matriz(numeros, "Desc"))
