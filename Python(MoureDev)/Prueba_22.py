"""
    Ejercicio 22:
    Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
    resultado e imprímelo.
    - El .txt se corresponde con las entradas de una calculadora.
    - Cada línea tendrá un número o una operación representada por un
    símbolo (alternando ambos).
    - Soporta números enteros y decimales.
    - Soporta las operaciones suma "+", resta "-", multiplicación "*"
    y división "/".
    - El resultado se muestra al finalizar la lectura de la última
    línea (si el .txt es correcto).
    - Si el formato del .txt no es correcto, se indicará que no se han
    podido resolver las operaciones.
"""

def calcular_desde_archivo(archivo):
    try:
        with open(archivo, 'r') as f:
            lineas = f.readlines()

        resultado = None  
        operacion = None 

        for linea in lineas:
            linea = line.strip()  
            if linea in ('+', '-', '*', '/'):
                operacion = line 
            else:
                try:
                    numero = float(linea)  
                    if resultado is None:
                        resultado = numero  
                    else:
                        if operacion is not None:
                            if operacion == '+':
                                resultado += numero
                            elif operacion == '-':
                                resultado -= numero
                            elif operacion == '*':
                                resultado *= numero
                            elif operacion == '/':
                                if numero == 0:
                                    raise ValueError("División por cero.")
                                resultado /= numero
                        else:
                            raise ValueError("Operación no definida.")
                except ValueError:
                    print("Formato del archivo no correcto.")
                    return

        print(f"El resultado final es: {resultado}")

    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

calcular_desde_archivo("Challenge21.txt")

