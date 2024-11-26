"""
  Ejercicio 51:
    Crea una función que sea capaz de encriptar y desencriptar texto
    utilizando el algoritmo de encriptación de Karaca
    (debes buscar información sobre él).
"""

def encriptar_karaca(texto):
    texto_invertido = texto[::-1]
    reemplazos = {"a": "0", "e": "1", "i": "2", "o": "3", "u": "4"}
    texto_encriptado = "".join(reemplazos.get(char, char) for char in texto_invertido)
    texto_encriptado += "aca"
    return texto_encriptado

def desencriptar_karaca(texto_encriptado):
    if texto_encriptado.endswith("aca"):
        texto_encriptado = texto_encriptado[:-3]
    else:
        return "Formato de encriptación no válido"
    reemplazos_inversos = {"0": "a", "1": "e", "2": "i", "3": "o", "4": "u"}
    texto_revertido = "".join(reemplazos_inversos.get(char, char) for char in texto_encriptado)
    texto_desencriptado = texto_revertido[::-1]
    return texto_desencriptado

texto = "hola"
encriptado = encriptar_karaca(texto)
print("Texto encriptado:", encriptado) 

desencriptado = desencriptar_karaca(encriptado)
print("Texto desencriptado:", desencriptado) 
