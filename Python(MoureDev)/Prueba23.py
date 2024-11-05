"""
    Ejercicio 23:
    Crea una función que reciba dos array, un booleano y retorne un array.
    - Si el booleano es verdadero buscará y retornará los elementos comunes
    de los dos array.
    - Si el booleano es falso buscará y retornará los elementos no comunes
    de los dos array.
    - No se pueden utilizar operaciones del lenguaje que
    lo resuelvan directamente.
"""

def recibe(array1, array2, booleano):
    if booleano: 
        comunes = []
        for elemento in array1:
            if elemento in array2 and elemento not in comunes:
                comunes.append(elemento)
        return comunes
    else: 
        no_comunes = []
        
        for elemento in array1:
            if elemento not in array2:
                no_comunes.append(elemento)
        
        for elemento in array2:
            if elemento not in array1 and elemento not in no_comunes:
                no_comunes.append(elemento)
        
        return no_comunes

array1 = ["manzana", "pera", "banana", "naranja"]
array2 = ["banana", "kiwi", "naranja", "sandía"]

resultado_comunes = recibe(array1, array2, True)
print("Elementos comunes:", resultado_comunes)  

resultado_no_comunes = recibe(array1, array2, False)
print("Elementos no comunes:", resultado_no_comunes)  
