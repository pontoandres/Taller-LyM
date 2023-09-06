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
    
    

def checkwalk (tokens):
    direcciones = ["front", "right", "left", "back"]
    cardinales = ["north", "south", "west", "east"]
    l = len(tokens)
    i = 0
    while i <l :       
        if tokens[i] == "walk":
            if tokens[i+1] is not "(":
                error = True
                print("Falta '('")
                #print(tokens[i] + tokens[i+1] + str(tokens[i+2]) + tokens[i+3] + tokens[i+4])
                i += 1
            else:
                a = i
                #a = posicion de (
                try:
                    p = int(tokens[i+2])
                except:
                    p = None
                if p is None:
                    error = True
                    print("Error de numero") 
                    #print(tokens[i] + tokens[i+1] + str(tokens[i+2]) + tokens[i+3] + tokens[i+4])
                    i += 1                                  
                if tokens[i+3] is not ")":
                    if  (tokens[i+3] not in direcciones) or (tokens[i+3] not in cardinales):
                        error = True
                        print("direccion")
                        print(tokens[i] + tokens[i+1] + str(tokens[i+2]) + tokens[i+3] + tokens[i+4])
                        i += 1
                    if tokens[i+4] is not ")":
                        error = True
                        print(")")
                        #print(tokens[i] + tokens[i+1] + str(tokens[i+2]) + tokens[i+3] + tokens[i+4])
                        i += 1
                    else:
                        i += 1  # Avanzar al siguiente conjunto de tokens
                else:
                    i += 1  # Avanzar al siguiente conjunto de tokens
        else:
            i += 1  # Avanzar al siguiente token si no es "walk"
                





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
            if (p is not None) and (q is not None):
                print("El jump está bien")
            else:
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
                p = int(tokens[i+1])
            except:
                p = None
            if p is not None:
                print("El walk esta bien")
            else:
                print("Error")            
    return None

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
        if tokens[i] == "jump":
            try:
                p = int(tokens[i+2])
            except:
                p = None
            if (p is not None):
                print("El drop está bien")
            else:
                print("Error")  
            if tokens[i+1] is not ("("):
                print("Falta '('")
            if tokens[i+3] is not (")"):
                print("Falta ')'")
                
def checkdrop (tokens):
    l = len(tokens)
    for i in range(0, l):
        if tokens[i] == "jump":
            try:
                p = int(tokens[i+2])
            except:
                p = None
            if (p is not None):
                print("El drop está bien")
            else:
                print("Error")  
            if tokens[i+1] is not ("("):
                print("Falta '('")
            if tokens[i+3] is not (")"):
                print("Falta ')'")

check_defvar(tokens)
checkwalk(tokens)
