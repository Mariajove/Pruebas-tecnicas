"""
Ejercicio 6:
    Crea un programa que se encargue de calcular el aspect ratio de una
    imagen a partir de una url.
    - Url de ejemplo:
    https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
    - Por ratio hacemos referencia por ejemplo a los "16:9" de una
    imagen de 1920*1080px.
"""

#Se han usado las siguientes librerias para que lea la imagen de internet y me ayuden a hacer los calculos matemáticos
import urllib.request
from PIL import Image
from io import BytesIO
import math

#Hacemos una funcion para que calcule el aspect ratio (obtener los mayores comunes divisores)
def calcular_aspect_ratio(ancho, alto): 
    gcd = math.gcd(ancho, alto)
    return f"{ancho // gcd}:{alto // gcd}"

#Se lee la imagen de internet con ayuda de urllib.request
url = 'https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png' 
with urllib.request.urlopen(url) as imagen:
    img_data = imagen.read()

#Ahora se saca la imagen en pixeles con auida de Image o BytesIO
foto = Image.open(BytesIO(img_data))
ancho, alto = foto.size
aspect_ratio = calcular_aspect_ratio(ancho, alto)

print(f"Dimensiones de la imagen: {ancho}x{alto}")
print(f"Aspect ratio: {aspect_ratio}")
