"""
Ejercicio 10:
REVISAR
    Crea un programa que sea capaz de transformar texto natural a código
    morse y viceversa.
    - Debe detectar automáticamente de qué tipo se trata y realizar
    la conversión.
    - En morse se soporta raya "—", punto ".", un espacio " " entre letras
    o símbolos y dos espacios entre palabras "  ".
    - El alfabeto morse soportado será el mostrado en
    https://es.wikipedia.org/wiki/Código_morse.
"""
MORSE_CODE = {
    'A': '·-', 'B': '-···', 'C': '-·-·', 'D': '-··', 'E': '·', 'F': '··-·', 'G': '--·', 'H': '····', 'I': '··',
    'J': '·---', 'K': '-·-', 'L': '·-··', 'M': '--', 'N': '-·', 'O': '---', 'P': '·--·', 'Q': '--·-', 'R': '·-·',
    'S': '···', 'T': '-', 'U': '··-', 'V': '···-', 'W': '·--', 'X': '-··-', 'Y': '-·--', 'Z': '--··',
    '1': '·----', '2': '··---', '3': '···--', '4': '····-', '5': '·····', '6': '-····', '7': '--···', '8': '---··',
    '9': '----·', '0': '-----', ',': '--··--', '.': '·-·-·-', '?': '··--··', "'": '·----·', '!': '-·-·--', '/': '-··-·',
    '(': '-·--·', ')': '-·--·-', '&': '·-···', ':': '---···', ';': '-·-·-·', '=': '-···-', '+': '·-·-·', '-': '-····-',
    '_': '··--·-', '"': '·-··-·', '$': '···-··-', '@': '·--·-·', ' ': ' '
}

TEXT_CODE = {v: k for k, v in MORSE_CODE.items()}

def es_morse(texto):
    """Detecta si el texto es código morse (si contiene puntos y rayas)"""
    return all(c in ['·', '-', ' ', '—'] for c in texto)

def texto_a_morse(texto):
    """Convierte texto normal a código morse"""
    texto = texto.upper()  # Convertimos todo a mayúsculas
    morse = []
    
    for letra in texto:
        if letra in MORSE_CODE:
            morse.append(MORSE_CODE[letra])
    
    return ' '.join(morse)  # Un espacio entre letras, las palabras se separarán con más espacios automáticamente

def morse_a_texto(morse):
    """Convierte código morse a texto normal"""
    palabras = morse.split('  ')  # Doble espacio indica una separación de palabras
    texto = []
    
    for palabra in palabras:
        letras = palabra.split()  # Un espacio indica separación de letras
        palabra_traducida = ''.join([TEXT_CODE[letra] for letra in letras])
        texto.append(palabra_traducida)
    
    return ' '.join(texto)

def morse(texto):
    """Detecta y convierte de texto a morse o de morse a texto según el caso"""
    if es_morse(texto):
        return morse_a_texto(texto)
    else:
        return texto_a_morse(texto)

texto = input('¿Qué quieres traducir? ')
resultado = morse(texto)
print(resultado)

