"""
    Ejercicio 28:
    Crea un programa que determine si dos vectores son ortogonales.
    - Los dos array deben tener la misma longitud.
    - Cada vector se podría representar como un array. Ejemplo: [1, -2]
"""

def ortogonales(vec1,vec2):
    if len(vec1)!=len(vec2):
        return "No son ortogonales"
    else:
        proesc=0
        for i in range(len(vec1)):
            proesc+=vec1[i]*vec2[i]
        if proesc==0:
            return "Son ortogonales"
        else:
            return "No son ortogonales"

print(ortogonales([1, 2], [-2, 1]))  
print(ortogonales([1, 1], [1, -1]))  
print(ortogonales([1, 2], [1, 2]))   
print(ortogonales([1, 2], [3]))     
