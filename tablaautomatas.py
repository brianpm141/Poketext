import ventanas
matriz = []  # matriz que contiene la tabla
aceptacion = [1, 2, 4, 6, 8, 11, 13, 17]  # estados que son de aceptacion
s = 0
# tabla del automata
matriz.append([1, 2, 6, 5, 5, 7, 9, 12, 14, '', '', ''])
matriz.append([1, 1, 1, '', '', '', '', '', '', '', '', ''])
matriz.append([2, 2, 2, '', 3, '', '', '', '', '', '', ''])
matriz.append([4, 4, 4, '', '', '', '', '', '', '', '', ''])
matriz.append([4, 4, 4, '', '', '', '', '', '', '', '', ''])
matriz.append(['', '', 6, '', '', 7, '', '', '', '', '', ''])
matriz.append(['', '', 6, '', '', 7, '', '', '', '', '', ''])
matriz.append(['', '', 8, '', '', '', '', '', '', '', '', ''])
matriz.append(['', '', 10, '', '', '', 11, '', '', '', 10, 10])
matriz.append(['', '', '', '', '', '', 11, '', '', '', '', ''])
matriz.append(['', '', '', '', '', '', '', '', '', '', '', ''])
matriz.append(['', '', 12, '', '', '', '', 13, '', '', 12, 12])
matriz.append(['', '', '', '', '', '', '', '', '', '', '', ''])
matriz.append(['', '', '', '', '', '', '', '', '', 15, '', ''])
matriz.append(['', '', 15, '', '', '', '', '', '', 16, 15, 15])
matriz.append(['', '', '', '', '', '', '', '', 17, '', '', ''])
matriz.append(['', '', '', '', '', '', '', '', '', '', '', ''])


def test_aut():
    return "hola mundo"


# sañida de que automata es
def salida(s):
    if s == 1:
        return "variable"
    elif s == 2:
        return "metodo"
    elif s == 4:
        return "paquete"
    elif s == 6:
        return "numero entero"
    elif s == 8:
        return "numero real"
    elif s == 11:
        return "caracter"
    elif s == 13:
        return "cadena"
    elif s == 17:
        return "comentario"


# obtiene la pos del estado
def valor(caracter):
    if caracter.islower():
        return 0
    elif caracter.isupper():
        return 1
    elif caracter.isdigit():
        return 2
    elif caracter == '+':
        return 3
    elif caracter == '-':
        return 4
    elif caracter == '.':
        return 5
    elif caracter == "'":
        return 6
    elif caracter == '"':
        return 7
    elif caracter == '/':
        return 8
    elif caracter == '*':
        return 9
    elif caracter.isalpha():
        return 10
    elif not caracter.isalnum():
        return 11


# Recorre la cadena comprobando si existe cada uno de los caracteres y si termina en estado de aceptacion
def comprobar_cadena(cadena):
    s = 0
    fila_caracteres = ""
    for caracter in cadena:  # coloca los caracteres en una fila
        fila_caracteres += caracter
    for caracter in fila_caracteres:  # comprueba los caracteres
        pos = valor(caracter)  # se obtiene el valor de s
        if pos != '':  # comprueba si el salto es a otro estado
            s = matriz[s][pos]  # cambia s por el nuevo estado
        else:
            ventanas.ventana_texto("error", "caracter no valido")
            exit()
    if s in aceptacion:  # retorno de la cadena
        return True
    else:
        return False
