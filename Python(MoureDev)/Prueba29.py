"""
    Ejercicio 29:
    Simula el funcionamiento de una máquina expendedora creando una operación
    que reciba dinero (array de monedas) y un número que indique la selección
    del producto.
    - El programa retornará el nombre del producto y un array con el dinero
    de vuelta (con el menor número de monedas).
    - Si el dinero es insuficiente o el número de producto no existe,
    deberá indicarse con un mensaje y retornar todas las monedas.
    - Si no hay dinero de vuelta, el array se retornará vacío.
    - Para que resulte más simple, trabajaremos en céntimos con monedas
    de 5, 10, 50, 100 y 200.
    - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
"""

articulos = {
    1: ("Agua Mineral", 100),     
    2: ("Refresco", 150),          
    3: ("Café", 200),             
    4: ("Chocolate", 120),       
    5: ("Galletas", 80),           
    6: ("Chicles", 50),           
    7: ("Frutos Secos", 250),    
    8: ("Bocadillo de Jamón", 300),
    9: ("Barra de Energía", 150),  
    10: ("Cerveza", 200),          
    11: ("Té Helado", 160),        
    12: ("Snickers", 100),         
    13: ("Patatas Fritas", 90),    
    14: ("Zumos Naturales", 130),  
    15: ("Caramelos", 40)          
}

monedas_disponibles = [5, 10, 20, 50, 100, 200]  

def devolver_cambio(cambio, monedas_disponibles):
    resultado = []
    for moneda in sorted(monedas_disponibles, reverse=True):
        while cambio >= moneda:
            resultado.append(moneda)
            cambio -= moneda
    return resultado

def maquina_expendedora(monedas, numero_producto):
    for moneda in monedas:
        if moneda not in monedas_disponibles:
            return "Una o más monedas no son válidas. Monedas aceptadas: 5, 10, 50, 100, 200 céntimos."
    total_dinero = sum(monedas)
    if numero_producto not in articulos:
        return "El número de producto no existe. Por favor, elija un número de producto válido."
    nombre_articulo, precio_articulo = articulos[numero_producto]
    if total_dinero < precio_articulo:
        return f"Dinero insuficiente. Te devuelvo: {monedas}"
    cambio = total_dinero - precio_articulo
    monedas_de_vuelta = devolver_cambio(cambio, monedas_disponibles)
    return f"Has comprado: {nombre_articulo}. Cambio devuelto: {monedas_de_vuelta}"

if __name__ == "__main__":
    accion = False
    while not accion:
        try:
            monedas_input = input("Inserte las monedas (separadas por comas, por ejemplo: 100,50,20): ")
            monedas = list(map(int, monedas_input.split(",")))
            if sum(monedas) == 0:
                print("No me has dado monedas.")
                continue
            numero_producto = int(input("Inserte el número del artículo (1-15): "))
            resultado = maquina_expendedora(monedas, numero_producto)
            print(resultado)
            continuar = input("¿Desea realizar otra compra? (s/n): ")
            if continuar.lower() != 's':
                accion = True
        except ValueError:
            print("Error: Introduzca un valor numérico válido.")
