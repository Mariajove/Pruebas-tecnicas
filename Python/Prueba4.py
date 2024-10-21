"""
Ejercicio 4:
    Escribe un programa que se encargue de comprobar si un número es o no primo.
    Hecho esto, imprime los números primos entre 1 y 100.
"""

def esprimo(n):
    if n==1:
        return False #1 no es un numero primo porque su unico factor es el mismo
    elif n==2:
        return True #2 si lo es porque sus factores es 1 y el mismo
    else:
        for i in range(2,n): #Se comprueba si un numero tiene mas factores que el mismo
            if n%i==0:
                return False
    return True

for i in range(1,101): #Se muestran los numeros primos por pantalla
    if esprimo(i)==True:
        print(i)
