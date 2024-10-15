#Para hacer una suma de digitos

def sumadigitos(digito):
    j=int(0)
    cadena=str(digito)
    vector=[]
    for caracter in cadena:
        vector.append(int(caracter))
    for i in vector:
        j=j+i
    return j

#Prueba
digito=3456

print(sumadigitos(digito))
