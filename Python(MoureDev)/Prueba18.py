"""
Ejercicio 18:
    Crea una función que evalúe si un/a atleta ha superado correctamente una
    carrera de obstáculos.
    - La función recibirá dos parámetros:
        - Un array que sólo puede contener String con las palabras
        "run" o "jump"
        - Un String que represente la pista y sólo puede contener "_" (suelo)
        o "|" (valla)
    - La función imprimirá cómo ha finalizado la carrera:
        - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
        será correcto y no variará el símbolo de esa parte de la pista.
        - Si hace "jump" en "_" (suelo), se variará la pista por "x".
        - Si hace "run" en "|" (valla), se variará la pista por "/".
    - La función retornará un Boolean que indique si ha superado la carrera.
    Para ello tiene que realizar la opción correcta en cada tramo de la pista.
"""
def evaluar_carrera(acciones, pista):
    superado = True  
    
    for i in range(len(acciones)):
        if acciones[i] == "run":
            if pista_lista[i] == "|":  
                pista_lista[i] = "/" 
                superado = False 
        elif acciones[i] == "jump":
            if pista_lista[i] == "_": 
                pista_lista[i] = "x"  
                superado = False  
              
    return superado 

acciones = ["run","run","jump"]
pista_lista = ["_","_","|"]
resultado = evaluar_carrera(acciones, pista)
print(resultado)
