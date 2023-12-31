import re
# Jose Miguel Alvear - 202010602
# Ponto Andres Moreno - 202224525

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
    
    errores = 0
    
    errores = check_defvar(tokens ,errores)
    errores = checkwalk(tokens, errores)
    errores = checkjump(tokens, errores)
    errores = checkleap(tokens, errores)
    errores = checkturn(tokens, errores)
    errores = checkturnto(tokens, errores)
    errores = checkdrop(tokens, errores)
    errores = checkget(tokens, errores)
    errores = checkgrab(tokens, errores)
    errores = checkletGo(tokens, errores)
    errores = checkfacing(tokens, errores)
    
    print("EL numero de errores encontrados es: ", errores)
    
    

def checkwalk (tokens, errores):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "walk":
            try:
                p = int(tokens[i+2])
            except:
                p = None
            if (p is None):
                print("Error")
                errores += 1  
            if tokens[i+1] is not ("("):
                print("Falta '('")
                errores += 1
            if tokens[i+3] is not (")"):
                if tokens[i+3] is not ("north" or "south" or "east" or "west" or "left" or "right" or "front" or "back"):
                    print("error de direccion")
                    errores += 1
    return errores
                





def checkjump (tokens, errores):
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
                errores += 1
            if tokens[i+1] is not ("("):
                print("Falta '('")
                errores += 1
            if tokens[i+4] is not (")"):
                print("Falta ')'")
                errores += 1
    return errores





def check_defvar (tokens, errores):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "defVar":
            if type(tokens[i+1]) == str:  
                try:  
                    p = int(tokens[i+2])
                except:
                    p = None
                if p is None:
                    print("Error") 
                    errores += 1
    return errores

def checkleap (tokens, errores):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "leap":
            try:
                p = int(tokens[i+2])
            except:
                p = None
            if (p is None):
                print("Error")  
                errores += 1
            if tokens[i+1] is not ("("):
                print("Falta '('")
                errores += 1
            if tokens[i+3] is not (")"):
                if tokens[i+3] is not ("north" or "south" or "east" or "west" or "left" or "right" or "front" or "back"):
                    print("error de direccion")
                    errores += 1
    return errores

def checkturn (tokens, errores):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "turn":
            if  tokens[i+2] is not ("left" or "right" or "around"):
                print("Error de direccion") 
                errores += 1
            if tokens[i+1] is not ("("):
                print("Falta '('")
                errores += 1
            if tokens[i+3] is not (")"):
                print("Falta ')'")
                errores += 1
    return errores

def checkturnto (tokens, errores):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "turnto":
            if  tokens[i+2] is not ("north" or "south" or "east" or "west"):
                print("Error de direccion") 
                errores += 1
            if tokens[i+1] is not ("("):
                print("Falta '('")
                errores += 1
            if tokens[i+3] is not (")"):
                print("Falta ')'")
                errores += 1
    return errores


def checkdrop (tokens, errores):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "drop":
            try:
                p = int(tokens[i+2])
            except:
                p = None
            if (p is None):
                print("Error")
                errores += 1  
            if tokens[i+1] is not ("("):
                print("Falta '('")
                errores += 1
            if tokens[i+3] is not (")"):
                print("Falta ')'")
                errores += 1
    return errores

def checkget (tokens, errores):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "get":
            try:
                p = int(tokens[i+2])
            except:
                p = None
            if (p is None):
                print("Error")  
                errores += 1
            if tokens[i+1] is not ("("):
                print("Falta '('")
                errores += 1
            if tokens[i+3] is not (")"):
                print("Falta ')'")
                errores += 1
    return errores

def checkgrab (tokens, errores):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "grab":
            try:
                p = int(tokens[i+2])
            except:
                p = None
            if (p is None):
                print("Error")  
                errores += 1
            if tokens[i+1] is not ("("):
                print("Falta '('")
                errores += 1
            if tokens[i+3] is not (")"):
                print("Falta ')'")
                errores += 1
    return errores

def checkletGo (tokens, errores):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "letGo":
            try:
                p = int(tokens[i+2])
            except:
                p = None
            if (p is None):
                print("Error")  
                errores += 1
            if tokens[i+1] is not ("("):
                print("Falta '('")
                errores += 1
            if tokens[i+3] is not (")"):
                print("Falta ')'")
                errores += 1
    return errores

def checkfacing (tokens, errores):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "facing":
            if  tokens[i+2] is not ("north" or "south" or "east" or "west"):
                print("Error de direccion") 
                errores += 1
            if tokens[i+1] is not ("("):
                print("Falta '('")
                errores += 1
            if tokens[i+3] is not (")"):
                print("Falta ')'")
                errores += 1
    return errores

checksyntax(tokens)
