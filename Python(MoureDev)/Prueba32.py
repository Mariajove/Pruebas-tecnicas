"""
    Ejercicio 32:
    Crea una función que imprima los 30 próximos años bisiestos
    siguientes a uno dado.
    - Utiliza el menor número de líneas para resolver el ejercicio.
"""

conteo=0
anio=int(input("Dime el año actual: "))
while conteo<30:
    anio+=1
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print(anio)
        conteo+=1
