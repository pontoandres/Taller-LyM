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

def tokenizar(patron, codigo)-> list:
    tokens = re.findall(patron, codigo)
    return tokens



s=cargar_archivo()
print(s)

tokens = tokenizar(patron, s)
print(tokens)



def checkwalk (tokens):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "walk":
            try:
                p = int(tokens[i+1])
            except:
                p = None
            if p is not None:
                print("El walk esta bien")
            else:
                print("Error")            
    return None

def checkjump (tokens):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "jump":
            try:
                p = int(tokens[i+1])
                q = int(tokens[i+2])
            except:
                p = None
                q = None
            if (p is not None) and (q is not None):
                print("El jump está bien")
            else:
                print("Error")            
    return None


def check_defvar (tokens):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "defVar":
            if type(tokens[i+1]) == str:  
                try:  
                    p = int(tokens[i+2])
                except:
                    p = None
                if p is not None:
                    print("El defVar esta bien")
                else:
                    print("Error") 
    return None

def checkleap (tokens):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "leap":
            try:
                p = int(tokens[i+1])
            except:
                p = None
            if p is not None:
                print("El walk esta bien")
            else:
                print("Error")            
    return None


check_defvar(tokens)
