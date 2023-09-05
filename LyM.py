import re


def cargar_archivo()-> str:
    codigo = ""
    
    nombre = "codigo.txt"
    
    archivo = open(nombre, "r")
    linea = archivo.readline()
    for linea in archivo:
        codigo += linea
    return codigo


patron = r'\b\w+\b'

def tokenizar(codigo)-> list:
    tokens = re.findall(patron, codigo)
    return tokens



s=cargar_archivo()
print(s)
