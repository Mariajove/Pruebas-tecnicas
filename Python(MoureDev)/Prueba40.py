"""
    Ejercicio 40:
    Implementa uno de los algoritmos de ordenación más famosos:
    el "Quick Sort", creado por C.A.R. Hoare.
    - Entender el funcionamiento de los algoritmos más utilizados de la historia
    Nos ayuda a mejorar nuestro conocimiento sobre ingeniería de software.
    Dedícale tiempo a entenderlo, no únicamente a copiar su implementación.
    - Esta es una nueva serie de retos llamada "TOP ALGORITMOS",
    donde trabajaremos y entenderemos los más famosos de la historia.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    #Primero se escoge el ultimo elemento para que sea nuestra referencia
    pivote = arr[-1] 
    #Posteriormente se ordenan los numeros en funcion de si son mayores o menores a la referencia
    menores = [x for x in arr[:-1] if x <= pivote]
    mayores = [x for x in arr[:-1] if x > pivote]
    #Se llama finalmente de forma recursiva a la funcion para que los acabe ordenando
    return quick_sort(menores) + [pivote] + quick_sort(mayores)

# Ejemplo de uso
arr = [9, 7, 5, 11, 12, 2, 14, 3, 10, 4]
print("Arreglo original:", arr)
arr_ordenado = quick_sort(arr)
print("Arreglo ordenado:", arr_ordenado)
