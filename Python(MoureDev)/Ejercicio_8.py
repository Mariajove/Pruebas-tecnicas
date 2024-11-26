"""
Ejercicio 8:
    Crea un programa que cuente cuantas veces se repite cada palabra
    y que muestre el recuento final de todas ellas.
    - Los signos de puntuación no forman parte de la palabra.
    - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
    - No se pueden utilizar funciones propias del lenguaje que
    lo resuelvan automáticamente.
"""
#Se importa la libreria para que ayude a quitar signos para que se conteen mejor las palabras
import string

#Se define una funcion para que contee las palabras
def conteo(texto):
    texto = texto.lower() #Se pone en minusculas para evitar errores
    contador_palabras = {} #Se crea un diccionario (mirar por favor esto que es importante)
    signos=string.punctuation+"¿¡" #En string no estan interrogaciones y exclamaciones en el listado de puntuaciones
    texto = texto.translate(str.maketrans('', '', signos)) #Se quitan los signos de puntuación
    palabras = texto.split() #Con la funcion split ya se consigue un diccionario con las palabras que hay en el texto

    for palabra in palabras:
        if palabra in contador_palabras:
            contador_palabras[palabra] += 1 #Se hace conteos y se añade al diccionario
        else:
            contador_palabras[palabra] = 1 #La palabra solo ha aparecido una vez y se añade al diccionario
    
    return contador_palabras

#Ejemplo
texto = "Hola, hola! ¿Cómo estás? Estoy bien, bien bien."
recuento = conteo(texto)
#Se muestra en pantalla (observando los elementos del diccionario, 
#cada definición (palabra) tiene asignado un valor (cantidad))
for palabra, cantidad in recuento.items():
    print(f'La palabra "{palabra}" aparece {cantidad} veces.')
