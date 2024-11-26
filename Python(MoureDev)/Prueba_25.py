"""
    Ejercicio 25:
    Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
    ¿De cuántas maneras eres capaz de hacerlo?
    Crea el código para cada una de ellas.
"""

import numpy as np

for i in range(1,101):
    print(i)

j = list(range(1, 101))
print(j)

k=1
while k<=100:
    print(k)
    k+=1

m = [x for x in range(1, 101)]
print(m)

np.arange(1, 101)
