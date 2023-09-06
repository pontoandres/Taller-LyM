import re


def cargar_archivo()-> str:
    codigo = ""
    
    nombre = "codigo.txt"
    
    archivo = open(nombre, "r")
    linea = archivo.readline()
    for linea in archivo:
        codigo += linea
    return codigo


patron = r'[\w]+|[(){}]'

def tokenizar(patron, codigo)-> list:
    tokens = re.findall(patron, codigo)
    return tokens



s=cargar_archivo()
print(s)

tokens = tokenizar(patron, s)
print(tokens)

def checksyntax(tokens):
    
    check_defvar(tokens)
    checkwalk(tokens)
    checkjump(tokens)
    checkleap(tokens)
    checkturn(tokens)
    checkturnto(tokens)
    checkdrop(tokens)
    checkget(tokens)
    checkgrab(tokens)
    checkletGo(tokens)
    checkfacing(tokens)
    
    

def checkwalk (tokens):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "walk":
            try:
                p = int(tokens[i+2])
            except:
                p = None
            if (p is None):
                print("Error")  
            if tokens[i+1] is not ("("):
                print("Falta '('")
            if tokens[i+3] is not (")"):
                if tokens[i+3] is not ("north" or "south" or "east" or "west" or "left" or "right" or "front" or "back"):
                    print("error de direccion")
                





def checkjump (tokens):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "jump":
            try:
                p = int(tokens[i+2])
                q = int(tokens[i+3])
            except:
                p = None
                q = None
            if (p is None) and (q is None):
                print("Error")  
            if tokens[i+1] is not ("("):
                print("Falta '('")
            if tokens[i+4] is not (")"):
                print("Falta ')'")


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
                p = int(tokens[i+2])
            except:
                p = None
            if (p is None):
                print("Error")  
            if tokens[i+1] is not ("("):
                print("Falta '('")
            if tokens[i+3] is not (")"):
                if tokens[i+3] is not ("north" or "south" or "east" or "west" or "left" or "right" or "front" or "back"):
                    print("error de direccion")

def checkturn (tokens):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "turn":
            if  tokens[i+2] is not ("left" or "right" or "around"):
                print("Error de direccion") 
            if tokens[i+1] is not ("("):
                print("Falta '('")
            if tokens[i+3] is not (")"):
                print("Falta ')'")

def checkturnto (tokens):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "turnto":
            if  tokens[i+2] is not ("north" or "south" or "east" or "west"):
                print("Error de direccion") 
            if tokens[i+1] is not ("("):
                print("Falta '('")
            if tokens[i+3] is not (")"):
                print("Falta ')'")


def checkdrop (tokens):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "drop":
            try:
                p = int(tokens[i+2])
            except:
                p = None
            if (p is None):
                print("Error")  
            if tokens[i+1] is not ("("):
                print("Falta '('")
            if tokens[i+3] is not (")"):
                print("Falta ')'")

def checkget (tokens):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "get":
            try:
                p = int(tokens[i+2])
            except:
                p = None
            if (p is None):
                print("Error")  
            if tokens[i+1] is not ("("):
                print("Falta '('")
            if tokens[i+3] is not (")"):
                print("Falta ')'")

def checkgrab (tokens):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "grab":
            try:
                p = int(tokens[i+2])
            except:
                p = None
            if (p is None):
                print("Error")  
            if tokens[i+1] is not ("("):
                print("Falta '('")
            if tokens[i+3] is not (")"):
                print("Falta ')'")

def checkletGo (tokens):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "letGo":
            try:
                p = int(tokens[i+2])
            except:
                p = None
            if (p is None):
                print("Error")  
            if tokens[i+1] is not ("("):
                print("Falta '('")
            if tokens[i+3] is not (")"):
                print("Falta ')'")

def checkfacing (tokens):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "facing":
            if  tokens[i+2] is not ("north" or "south" or "east" or "west"):
                print("Error de direccion") 
            if tokens[i+1] is not ("("):
                print("Falta '('")
            if tokens[i+3] is not (")"):
                print("Falta ')'")

checksyntax(tokens)
