"""
    Ejercicio 21:
    Crea una función que sume 2 números y retorne su resultado pasados
    unos segundos.
    - Recibirá por parámetros los 2 números a sumar y los segundos que
    debe tardar en finalizar su ejecución.
    - Si el lenguaje lo soporta, deberá retornar el resultado de forma
    asíncrona, es decir, sin detener la ejecución del programa principal.
    Se podría ejecutar varias veces al mismo tiempo.
"""

import threading
import time

def async_sum(number_one, number_two, seconds, callback):
    def run():
        time.sleep(seconds)
        callback(number_one + number_two)
    
    thread = threading.Thread(target=run)
    thread.start()

def main():
    async_sum(5, 2, 10, lambda result: print(result))
    async_sum(1, 3, 5, lambda result: print(result))

if __name__ == "__main__":
    main()
