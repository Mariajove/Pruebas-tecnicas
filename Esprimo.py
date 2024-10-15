#Numero primo

def esprimo(numero):
    numero=abs(numero)
    if numero<=2:
        return "Es primo"
    if numero > 2:
        for i in range(2,numero):
            resto=numero%i
            if resto==0:
                return "No es primo"
    return "Es primo"

#Para probar
print(esprimo(23))
