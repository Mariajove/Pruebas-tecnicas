#La sucesion de fibonachi se puede hacer de dos formas: de forma recursiva o sin usar una funcion recursiva
#Primera forma: funcion sin ser recursiva
def fibo(n):
    a,b=0,1
    for _ in range(n):
        a=b
        b=a+b
    return a

# Solicitar la posición de Fibonacci al usuario
n = int(input("Introduce la posición de Fibonacci que deseas calcular: "))

# Imprimir el resultado
print(f"El número de Fibonacci en la posición {n} es {fibonacci(n)}")

#Segunda forma: Funcion recursiva
def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)

# Solicitar la posición de Fibonacci al usuario
number = int(input("Introduce la posición de Fibonacci que deseas calcular: "))

# Imprimir el resultado
print(f"El número de Fibonacci en la posición {number} es {fibonachi()}")
