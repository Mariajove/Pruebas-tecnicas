"""
Ejercicio 3:
    Escribe un programa que imprima los 50 primeros números de la sucesión
    de Fibonacci empezando en 0. 
    - La serie Fibonacci se compone por una sucesión de números en
    la que el siguiente siempre es la suma de los dos anteriores.
    0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonachi(n): #Se puede hacer de dos formas, he escogido hacer la forma de funcion recursiva
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonachi(n-1) + fibonachi(n-2)
    
sucesion=[] #Aqui se guardarán los numeros de la sucesion de fibonachi
for i in range(0,31): #Puedo hacer 50 pero se me peta el ordenador
    sucesion.append(fibonachi(i))
print(sucesion)
