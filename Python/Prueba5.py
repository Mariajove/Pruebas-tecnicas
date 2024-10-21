"""
Ejercicio 5:
    Crea una única función (importante que sólo sea una) que sea capaz
    de calcular y retornar el área de un polígono.
    - La función recibirá por parámetro sólo UN polígono a la vez.
    - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
    - Imprime el cálculo del área de un polígono de cada tipo.
"""

def calculo_area(tipo, base=None, altura=None, lado=None):
    try: #Vamos a hacerlo con try para que se pueda ejecutar si no tenemos ciertos datos (por ejemplo que no necesitemos lado)
        if tipo == "triangulo":
            return base * altura * 0.5
        elif tipo == "cuadrado":
            return lado ** 2
        elif tipo == "rectangulo":
            return base * altura
        else:
            return "Tipo de polígono no soportado"
    except TypeError:
        return "Error, faltan datos o los valores no son correctos"

a = input('Dime el tipo de polígono (triangulo, cuadrado, rectangulo): ').lower() #Para convertir todo en minusculas y pueda leerlo la funcion

if a == "triangulo" or a == "rectangulo": #Que pida solo lo necesario para calcular cada poligono
    try:
        b = float(input('Dime la base: '))  
        c = float(input('Dime la altura: ')) 
        print(f"El área del {a} es:", calculo_area(a, base=b, altura=c))
    except ValueError:
        print("Error: Di los valores de nuevo.")

elif a == "cuadrado":
    try:
        d = float(input('Dime el lado: ')) 
        print("El área del cuadrado es:", calculo_area(a, lado=d))
    except ValueError:
        print("Error: Di los valores de nuevo.")

else:
    print("Tipo de polígono no válido")
