import ventanas
matriz = []  # matriz que contiene la tabla
aceptacion = [1, 2, 4, 6, 8, 11, 13, 17]  # estados que son de aceptacion
s = 0
# tabla del automata
matriz.append([1, 2, 6, 5, 5, 7, 9, '', '', 12, 14, ''])
matriz.append([1, 1, 1, '', '', '', '', '', '', '', '', ''])
matriz.append([2, 2, 2, '', 3, '', '', '', '', '', '', ''])
matriz.append([4, 4, 4, '', '', '', '', '', '', '', '', ''])
matriz.append([4, 4, 4, '', '', '', '', '', '', '', '', ''])
matriz.append(['', '', 6, '', '', 7, '', '', '', '', '', ''])
matriz.append(['', '', 6, '', '', 7, '', '', '', '', '', ''])
matriz.append(['', '', 8, '', '', '', '', '', '', '', '', ''])
matriz.append(['', '', 8, '', '', '', '', '', '', '', '', ''])
matriz.append(['', '', 10, '', '', '', 11, 10, 10, '', '', ''])
matriz.append(['', '', '', '', '', '', 11, '', '', '', '', ''])
matriz.append(['', '', '', '', '', '', '', '', '', '', '', ''])
matriz.append(['', '', 12, '', '', '', '', 12, 12, 13, '', ''])
matriz.append(['', '', '', '', '', '', '', '', '', '', '', ''])
matriz.append(['', '', '', '', '', '', '', '', '', '', '', 15])
matriz.append(['', '', 15, '', '', '', '', 15, 15, '', '', 16])
matriz.append(['', '', '', '', '', '', '', '', '', '', 17, ''])
matriz.append(['', '', '', '', '', '', '', '', '', '', '', ''])


# sañida de que automata es
def salida(s):
    if s == 1:
        return 35
    elif s == 2:
        return 36
    elif s == 4:
        return 37
    elif s == 6:
        return 38
    elif s == 8:
        return 39
    elif s == 11:
        return 40
    elif s == 13:
        return 41
    elif s == 17:
        return 42
    else:
        return 0

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
        return 9
    elif caracter == '/':
        return 10
    elif caracter == '*':
        return 11
    elif caracter.isalpha():
        return 7
    elif not caracter.isalnum():
        return 8


# Recorre la cadena comprobando si existe cada uno de los caracteres y si termina en estado de aceptacion
def comprobar_cadena(cadena):
    s = 0
    for caracter in cadena:  # itera sobre los caracteres de la cadena
        pos = valor(caracter)  # se obtiene el valor de s
        if isinstance(s, int) and isinstance(pos, int):
            s = matriz[s][pos]

    resultado = salida(s)
    return resultado
