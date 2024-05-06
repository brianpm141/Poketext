def separar_texto(texto, separadores):
    separadores = set(separadores)
    resultado = []
    palabra_actual = ""
    for caracter in texto:
        if caracter in separadores:
            if palabra_actual:
                resultado.append(palabra_actual)
                palabra_actual = ""
            resultado.append(caracter)
            if caracter not in ["=", "<", ">"]:  # Excepciones
                # Agregar salto de línea después del separador
                resultado.append("\n")
        else:
            palabra_actual += caracter
    if palabra_actual:
        resultado.append(palabra_actual)
    return resultado


def procesar_texto(entrada):
    separadores = [" ", "=", "<", ">", "/", "*", '"', ";"]
    texto_procesado = separar_texto(entrada, separadores)
    salida = []
    i = 0
    while i < len(texto_procesado):
        token = texto_procesado[i]
        if token == "/":
            if i + 1 < len(texto_procesado) and texto_procesado[i + 1] == "*":
                i += 2
                while i < len(texto_procesado):
                    if texto_procesado[i] == "*" and i + 1 < len(texto_procesado) and texto_procesado[i + 1] == "/":
                        break
                    i += 1
            else:
                salida.append(token)
                i += 1
        elif token == "*":
            if i + 1 < len(texto_procesado) and texto_procesado[i + 1] == "/":
                i += 2
            else:
                salida.append(token)
                i += 1
        else:
            salida.append(token)
            i += 1
    return salida


def concatenar_tokens(tokens):
    resultado = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == "=":
            if i - 1 >= 0 and tokens[i - 1] not in ["<", ">"]:
                resultado[-1] += token
                i += 1
            else:
                resultado.append(token)
                i += 1
        elif token == "<" or token == ">":
            if i + 1 < len(tokens) and tokens[i + 1] == "=":
                resultado[-1] += token + "="
                i += 2
            else:
                resultado.append(token)
                i += 1
        else:
            resultado.append(token)
            i += 1
    return resultado


with open("entrada.txt", "r") as archivo_entrada:
    texto = archivo_entrada.read()

texto_procesado = procesar_texto(texto)
texto_concatenado = concatenar_tokens(texto_procesado)

with open("salida.txt", "w") as archivo_salida:
    archivo_salida.write("".join(texto_concatenado))


def eliminaespacios(archivo_salida):
    with open(archivo_salida, 'r') as file:
        lines = file.readlines()
    lines = [line for line in lines if line.strip()]
    with open(archivo_salida, 'w') as file:
        file.writelines(lines)


eliminaespacios("salida.txt")
