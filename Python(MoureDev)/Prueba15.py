"""
Ejercicio 15:
    Escribe una función que calcule si un número dado es un número de Armstrong
    (o también llamado narcisista).
    Si no conoces qué es un número de Armstrong, debes buscar información
    al respecto.
    
    Numero de Armstrong: Numero que al separar sus dígitos, elevarlos a la cuarta a cada uno 
    y luego sumarlos dan el numero que eran loa dígitos juntos.
"""

numero=int(input('Dime el numero a verificar'))

# Convertir a cadena y usar map para convertir cada dígito a entero
digitos = list(map(int, str(numero)))

narci=0
potencia=len(digitos)
for i in digitos:
    narci+=i**potencia
if narci==numero:
    print('Es narcisista')
else:
    print('No es narcisista')
