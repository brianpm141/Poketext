import shutil
import os
import re


def separar_texto(archivo_entrada, archivo_salida):
    separadores = [" ", "=", "<", ">", "/",
                   "*", '"', ";"]  # Lista de separadores
    try:
        with open(archivo_entrada, 'r') as f_input:
            texto = f_input.read()
        with open(archivo_salida, 'w') as f_output:
            for separador in separadores:
                # Usar expresión regular para dividir el texto en palabras y separadores
                texto = re.sub(f'({re.escape(separador)})', r'\n\1\n', texto)
            f_output.write(texto)
        print("Texto separado correctamente.")
    except FileNotFoundError:
        print("No se pudo encontrar el archivo de entrada.")


# elimina los espacios vacios de la salida
def eliminaespacios(archivo_salida):
    with open(archivo_salida, 'r') as file:
        lines = file.readlines()
    lines = [line for line in lines if line.strip()]
    with open(archivo_salida, 'w') as file:
        file.writelines(lines)


separar_texto("entrada.txt", "salida.txt")
eliminaespacios("salida.txt")
