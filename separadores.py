def separarCaracteres(entrada):

    igual = ['=', '<', '>']
    menque = ['=', '>']
    signo = None
    with open(entrada, 'r') as input_file:
        data = input_file.read()

    with open('salida.txt', 'w') as output_file:
        concat = False
        cad = False
        coment = False
        comentaux = False
        fincom = False
        caracter = False
        maque = False
        for char in data:
            if (char == "=" or signo == "=") and (not coment and not cad and not caracter):
                if concat:
                    if char in igual:
                        output_file.write(char)
                    else:
                        output_file.write('\n')
                        output_file.write(char + '\n')
                    signo = None
                    concat = False
                else:
                    output_file.write(char)
                    concat = True
                    signo = "="

            elif (char == "<" or signo == "<") and (not coment and not cad and not caracter):
                if concat:
                    if char in menque:
                        output_file.write(char)
                    else:
                        output_file.write('\n')
                        output_file.write(char + '\n')
                    signo = None
                    concat = False
                else:
                    output_file.write(char)
                    concat = True
                    signo = "<"

            elif (char == '>' or maque) and (not coment and not cad and not caracter):
                if maque:
                    if char == '=':
                        output_file.write(char + '\n')
                        maque = False
                    else:
                        output_file.write('\n')
                        output_file.write(char + '\n')
                        maque = False
                else:
                    output_file.write(char)
                    maque = True

            elif (char == '*' or signo == '*') and (not coment and not cad and not caracter):
                if signo == '*':
                    if char == '*':
                        output_file.write(char + '\n')
                        signo = None
                    else:
                        output_file.write('\n')
                        output_file.write(char + '\n')
                        signo = None
                else:
                    output_file.write(char + '\n')
                    signo = '*'

            elif (char == '"' or cad) and (not coment and not caracter):
                if cad:
                    if char == '\n' or char == '"':
                        output_file.write(char + '\n')
                        cad = False
                    else:
                        output_file.write(char)
                else:
                    output_file.write(char)
                    cad = True

            elif (char == '/' or coment) and (not cad and not caracter):
                if char == '\n':
                    output_file.write(char + '\n')
                    coment = False
                    comentaux = False
                    fincom = False
                elif coment:
                    if fincom:
                        if char == '/':
                            output_file.write(char + '\n')
                            coment = False
                            comentaux = False
                            fincom = False
                    else:
                        if comentaux:
                            if char == '*':
                                output_file.write(char)
                                fincom = True
                            else:
                                output_file.write(char)
                        else:
                            if char == '*':
                                output_file.write(char)
                                comentaux = True
                            else:
                                output_file.write(char + '\n')
                                coment = False
                                comentaux = False
                                fincom = False
                else:
                    output_file.write(char)
                    coment = True

            elif (char == "'" or caracter) and (not coment and not cad):
                if caracter:
                    if char == "'" or char == '\n':
                        output_file.write(char + '\n')
                        caracter = False
                    else:
                        output_file.write(char)
                else:
                    output_file.write(char)
                    caracter = True

            elif (char == '\n' or char == ' ') and (not coment and not cad and not caracter):
                output_file.write('\n')

            else:
                output_file.write(char)


def eliminaespacios(archivo_salida):
    with open(archivo_salida, 'r') as file:
        lines = file.readlines()
    lines = [line for line in lines if line.strip()]
    with open(archivo_salida, 'w') as file:
        file.writelines(lines)


separarCaracteres("entrada.txt")
eliminaespacios("salida.txt")
