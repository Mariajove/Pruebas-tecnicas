#Maximo comun divisor

def comundivisor(a,b):
    #para el maximo comun divisor
    while b!=0:
        numero= a%b
        a=b
        b=numero
    return a

print(comundivisor(245,45))
