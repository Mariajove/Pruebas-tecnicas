#Para decir los numeros pares de una lista
def pairnumbers(lista):
    pairs=[]
    for i in lista:
        if i % 2 ==0:
            pairs.append(i)
    return(pairs)

#Ejemplo
lista=[1,2,3,4,5,6,7,4,12]
print(pairnumbers(lista))
