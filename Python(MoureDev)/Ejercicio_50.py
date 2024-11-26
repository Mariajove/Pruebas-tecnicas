"""
  Ejercicio 50:
    Crea una función que sea capaz de detectar y retornar todos los
    handles de un texto usando solamente Expresiones Regulares.
    Debes crear una expresión regular para cada caso:
    - Handle usuario: Los que comienzan por "@"
    - Handle hashtag: Los que comienzan por "#"
    - Handle web: Los que comienzan por "www.", "http://", "https://"
    y finalizan con un dominio (.com, .es...)
"""

import re

def detectar_handles(texto):
    handle_usuario = r'@\w+'                 
    handle_hashtag = r'#\w+'            
    handle_web = r'(https?://\S+|www\.\S+)'   
    
    usuarios = re.findall(handle_usuario, texto)
    hashtags = re.findall(handle_hashtag, texto)
    webs = re.findall(handle_web, texto)
    
    return {
        "usuarios": usuarios,
        "hashtags": hashtags,
        "webs": webs
    }

texto = "Aquí tienes algunos ejemplos: @usuario1, #desarrollo, https://ejemplo.com, www.test.es, y otro @usuario2."
print(detectar_handles(texto))
