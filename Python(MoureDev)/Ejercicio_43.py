"""
  Ejercicio 43:
    Crea una función que transforme grados Celsius en Fahrenheit
    y viceversa.

    - Para que un dato de entrada sea correcto debe poseer un símbolo "°"
    y su unidad ("C" o "F").
    - En caso contrario retornará un error.
"""

def grados(grado):
    if "º" in grado and (grado.endswith("F") or grado.endswith("C")):
        if "F" in grado:
            fahrenheit = float(grado.replace("ºF", ""))
            celsius = (fahrenheit - 32) * 5 / 9
            return round(celsius, 2)
        elif "C" in grado:
            celsius = float(grado.replace("ºC", ""))
            fahrenheit = (celsius * 9 / 5) + 32
            return round(fahrenheit, 2)
    else:
        return "Error"

print(grados("32ºF")) 
print(grados("0ºC")) 
print(grados("100"))    
print(grados("25ºK"))  
