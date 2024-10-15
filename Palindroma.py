#Para saber si una palabra es o no palindroma

def espalindroma(palabra):
    palabra=palabra.lower()
    if palabra==palabra[::-1]:
        return "Es palindroma"
    else:
        return "No es palindroma" 

palabra1="Ana"
print(espalindroma(palabra1))
palabra2="Casa"
print(espalindroma(palabra2))
