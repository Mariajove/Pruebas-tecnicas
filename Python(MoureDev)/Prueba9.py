"""
Ejercicio 9:
    Crea un programa se encargue de transformar un número
    decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""
#Primero se registra el numero que se quiere convertir y se inicializa el vector donde se guarde el binario
decimal=int(input('Dime un numero que convierta a binario'))
modulos=[]

while decimal!=0:
    resto=decimal%2 #Primero se obtiene el resto del numero entre 2 (para ver si ponemos 1 o 0 en el modulo)
    cociente=decimal//2 #Posteriormente conseguimos el cociente para que se sustituya en la siguiente iteracion
    modulos.append(resto) #Se añade el resto para ir obteniendo el numero en binario
    decimal=cociente #Se repite hasta que no tengamos mas cociente para dividir

print(modulos)
